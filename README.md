Config pylint: pylint --generate-rcfile > .pylintrc

### ESTRUTURA
* server: registro das blueprints da aplicação
* routes: recebem as requisições http e preparam a tipagem de requisição e da resposta. Os modelos ficam na pasta views
* views: são acionadas pelas rotas. Invocam os serviços dos controller
* controllers: realizada toda lógica de negócio. Caso necessite de alguma biblioteca externma (de terceiros) invocam os serviços presentes na pasta drivers
* drivers: implementa serviços de bibliotecas externas (de terceiros)