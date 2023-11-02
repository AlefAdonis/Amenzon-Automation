# Amenzon-Automation

> Este é um repositório destinado as soluções do Workshop: "Do Manual ao Automático: Transformando o Trabalho Através de Automações', realizado no dia 24/10/2023


### Situação
Uma empresa de transportes de carga, chamada Amenzon, possui um sistema que detecta automaticamente a saída e entrada de caminhões no seu galpão. Esse sistema armazena os dados do caminhão em um banco de dados, com apenas as informações do motorista, do caminhão e da rota dele. Devido a alguns problemas nas cidades em que os galpões estão instalados, algumas mercadorias estão sendo tomadas do motorista, e como a empresa não tem um registro financeiro do que os motoristas levam, a Amenzon não sabe quanto de prejuízo ela está tendo e em quais rotas isso acontece.

Tendo isso em mente, o CTO Zezo Beijos decidiu fazer uma linha de processo para contabilizar os produtos de cada caminhão, afim de fazer um balanço financeiro e uma investigação de qual a melhor rota para os motoristas. Sendo assim, ele delegou para a equipe de Logística que fizesse esse monitoramento, que por não conhecer as maravilhas da automação, implementou tudo manualmente, da seguinte forma:

1. Primeiro, um funcionário, anota todas as placas dos carros que estão saindo, e coloca em um excel.
2. Após isso, ele relaciona os dados da placa com uma planilha de controle (que possui  informações dos lotes enviados) que a área de logística possui e é atualizada a cada 30 minutos.
3. Em seguida, ele relaciona com uma tabela de preços para cada produtos dos lotes (fixa)
4. Após isso,  ele gera um balanço financeiro para cada caminhão que saiu.

Zezo Beijos percebendo que ter um funcionário para fazer apenas esse processo todos os dias, para cada galpão, era uma perda de dinheiro muito grande. Por isso, ele decidiu montar uma equipe de desenvolvedores para automatizar esse processo e você foi designado como Tech Lead desse grupo. O seu propósito é diminuir o FTE para, no mínimo, 95% em todos os galpões da Amenzon. Agora, vamos automatizar!!!

### Diagrama de Fluxo
![amenzon-automation](https://github.com/AlefAdonis/Amenzon-Automation/assets/62490971/d8fe6922-0b07-495d-b253-a1faedfb4519)


### OBS

Execute o comando `pip install pandas openpyxl` antes de iniciar o desenvolvimento

