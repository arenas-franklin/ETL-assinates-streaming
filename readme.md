# ETL com Python - Como Manipular Grandes Massas de dados com python

## Descrição Técnica Detalhada do Projeto ETL com Planilhas Excel e Python

**Introdução:**

Este documento apresenta uma descrição técnica detalhada de um projeto ETL (Extração, Transformação e Carregamento) que utilizei planilhas Excel como fonte de dados e Python para o tratamento e integração dos dados. O objetivo é fornecer uma visão abrangente das etapas envolvidas no projeto, ferramentas e técnicas utilizadas, desafios encontrados e soluções implementadas.

**1. Fonte de Dados:**

* O projeto utilizou como fonte de dados  **planilhas Excel** .
* As planilhas continham dados  fictícios de registro de assinatura de serviço de strimeaming.
* As colunas apresentadas são: sale_date, customer, amount, utml_link, age.
* Os dados estavam em formatos xlsx com e registro de paises diferentes.
* A qualidade dos dados era considerada boa.

**2. Extração:**

* A etapa de extração foi realizada utilizando o modulo nativo do python glob e os.
* O pandas facilitou a leitura das planilhas Excel, convertendo-as em estruturas de dados Python (DataFrames).
* Cada planilha foi lida em um DataFrame separado, preservando a formatação original.
* Metadados das planilhas, como location, campaign também foram extraídos.

**3. Transformação:**

* A etapa de transformação envolve operações como :
  * extração de  nome de aquivos
  * extraão de nome de registros linkados

**4. Carregamento:**

* A etapa de carregamento envolveu a integração das informações em base de dados e um arquivo unico xlsx(excel) .

**5. Ferramentas e Bibliotecas:**

* **Linguagem de programação:** Python 3.8
* **Bibliotecas:**
  * pandas: Manipulação e análise de dados em formato tabular.
  * os : Módulo Python para gerenciar arquivos, pastas, comandos e informações do sistema
  * glob: Módulo Python para localizar arquivos e pastas .
* **Ambiente de desenvolvimento:**  IDE Python ( Visual Studio Code)

**6. Desafios e Soluções:**

* **Desafios:**
  * extrair a informação  do país que o serviço de strimign foi assinado do nome do arquivo
  * extrair o tipo de campanha da url que o cliente assinou
* **Soluções:**
  * usado  modulos os e glob para localizar e estrair o nome dos aquivos
  * usado regex regex (expressão regular), para extrair  tipo da campanha da url
  * pandas utlizado para leitura do excel, ajuntar os Dataframes e  conversão.

**7. Considerações Finais:**

* O projeto ETL foi concluído com sucesso, resultando em um conjunto de dados limpo, consistente e integrado a uma base de dados xslx(arquivo excel).
* O Python e suas bibliotecas, como pandas e os modulos os glob, se mostraram ferramentas valiosas para o tratamento e integração de dados e manipulaçã ode arquivos e diretorios.
* A documentação detalhada das etapas do projeto, código e decisões tomadas facilitou a compreensão e replicabilidade do processo.
* O projeto demonstra a viabilidade de utilizar o Python para realizar tarefas complexas de ETL em projetos de médio a grande porte, que consiste uma grande base de arquivos para leitura.
* Automaização do processo para novas tabelas serem lidas.

**8. Melhorias Futuras:**

* Realizar  um realatório Análise Exploratória de Dados(EDA) em arquivo jupyter notebook.
* Criação de Dashbord dashboard (Streamlit, Dash, D3.js )
