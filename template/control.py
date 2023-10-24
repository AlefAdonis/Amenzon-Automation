import json
import sys

import pandas as pd
import os
import datetime
from utils.tools import create_logger


global log
# TODO File Setup
# Setup do que a automação irá consumir
INPUT_DIR = "../data/"
PRICE_FILE = "precos.xlsx"
LOGIST_FILE = "logistica.xlsx"
CONTROL_FILE = "controle-veiculos.json"

# Setup do que a automação irá produzir
OUTPUT_DIR = "../product/"
PRODUCT_FILE = "balanco_financeiro"
RUNNIG_FILE = "running.robot"

# TODO Robot Initializer
def robot_initializer():
    global log
    log = create_logger(os.getcwd())

    log.info("Initiating automation!")


# TODO Robot Finisher
def robot_finisher(success: bool):

    os.remove(OUTPUT_DIR+RUNNIG_FILE)

    if not success:
        try:
            with open(OUTPUT_DIR + "error.robot", 'a') as f:
                f.close()
                pass
            log.info("Created the error File")
        except OSError as error:
            log.error(f'Failed creating the file: {error}')

    log.info("Finishing Automation!")
    sys.exit(os.EX_OK)


if __name__ == "__main__":
    robot_initializer()

    # Primeiras Verificações dos arquivos
    try:
        if not os.path.isdir(OUTPUT_DIR):
            log.info(f"Creating output dir in the path: {OUTPUT_DIR}")
            os.mkdir(OUTPUT_DIR)
    except OSError as error:
        log.error(f"Error while creating the output dir: {error}")

    if os.path.isfile(OUTPUT_DIR+RUNNIG_FILE):
        log.info("Another process is already runnig!")
        sys.exit(os.EX_SOFTWARE)

    try:
        with open(OUTPUT_DIR + RUNNIG_FILE, 'a') as f:
            f.close()
            pass
        log.info("Created the Running File")
    except OSError as error:
        log.error(f'Failed creating the file: {error}')
        sys.exit(os.EX_SOFTWARE)

    if (not os.path.isfile(INPUT_DIR+LOGIST_FILE) or not os.path.isfile(INPUT_DIR+PRICE_FILE) or
            not os.path.isfile(INPUT_DIR+CONTROL_FILE)):
        log.error("There is input data missing!")
        robot_finisher(False)

    # Fazendo o "GET" do controle de veículos
    log.info("Getting the transportion control Data")
    with open(INPUT_DIR+CONTROL_FILE) as control_f:
        control_dict = json.load(control_f)
        control_f.close()
    control_df = pd.DataFrame.from_dict(control_dict["controle"])

    # Extraindo os dados do arquivos de Input
    log.info("Getting the Logistic input file")
    logist_df = pd.read_excel(INPUT_DIR+LOGIST_FILE, sheet_name='Folha1')

    log.info("Getting the Price input file")
    price_df = pd.read_excel(INPUT_DIR + PRICE_FILE, sheet_name='Folha1')

    log.info("Merging the dataframes of the Logistics Data and Control Data")
    logist_df.rename({"Transporter": "placa_caminhão"}, axis=1, inplace=True)
    info_transportation_df = control_df.merge(logist_df, how="left", on="placa_caminhão")

    log.info("Merging the dataframes of the Info Transportation Data and Price Data")
    info_transportation_df.rename({"nome": "motorista"})
    consolidated_df = info_transportation_df.merge(price_df, how="left", on=["Name", "Source"])

    log.info("Calculating the total Price of the Products")
    consolidated_df["Total_Price"] = (consolidated_df["QTD_Kg"] / consolidated_df["Unit_Kg"]) * \
                                     consolidated_df["Unit_Price"] * consolidated_df["QTD_Packages"]

    for galpao in consolidated_df["galpao"].unique():
        galpao_consolidated_df = consolidated_df.loc[consolidated_df["galpao"] == galpao].copy()

        log.info(f"Filtering the data for the {galpao}.")
        galpao_consolidated_df.drop(["nome", "idade", "galpao", "marca_caminhão", "Expiration", "ID"], axis=1, inplace=True)
        galpao_consolidated_df.rename({"rota": "Route", "cpf": "Drivers_Document", "placa_caminhão": "Vehicle_Plate"}, axis=1, inplace=True)

        columns = ['Drivers_Document', 'Vehicle_Plate', 'Route', 'SKU',  'Name', 'Source','Post_Date', 'Expiration_Date',
                   'QTD_Packages', 'QTD_Kg', 'Unit_Kg', 'Unit_Price',  'Total_Price']

        galpao_consolidated_df = galpao_consolidated_df[columns].sort_values(by="Total_Price", ascending=False)

        log.info("Exporting the  the output to an excel file")
        galpao_consolidated_df.to_excel(OUTPUT_DIR+PRODUCT_FILE + f" {galpao}.xlsx", index=False)

    robot_finisher(True)
