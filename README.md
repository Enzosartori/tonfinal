# Como utilizar a API REST

Passo a passo para utilização da API REST criada para solucionar o case "Desafio 2", utilizando o Windows como sistema operacional.


## Pré-requisitos

Primeiramente, deve-se ter o Python instalado, dando preferência a versão 3.8.5, mesma utilizada na criação da API.
Disponível para download no endereço : https://www.python.org/downloads/ . Ao instalar, aceitar a instalação do "pip", para possibilitar o download
das libs que serão utilizadas de forma mais fácil.

Em seguida, deve-se instalar o Flask e algumas libs:

Para o Flask, digitar no cmd o seguinte comando:
```sh
pip install flask
```

Para a lib Jsonify, digitar no cmd o seguinte comando:
```sh
pip install flask-jsonpify
```

Para a lib Restful, digitar no cmd o seguinte comando:
```sh
pip install flask-restful
```

Para a lib SQLAlchemy, digitar no cmd o seguinte comando:
```sh
pip install flask-sqlalchemy
```


Para o banco de dados, utilizei o SQLite, por ser open source e não necessitar de um servidor para funcionar. Para criar o arquivo base .db utilizei o SQLiteStudio,
que pode ser baixado pela url: https://sqlitestudio.pl/ .


## Utilização da API:

Os seguintes métodos foram implementados:


GET - Lê o banco de dados e "printa" os valores no operador

POST - Insere um novo valor ao banco de dados

PUT - Atualiza um valor no banco de dados

DELETE - Apaga um valor no banco de dados

### GET:

Entra na url: 	https://tonfinal.herokuapp.com/users para visualizar toda a base de dados
		https://tonfinal.herokuapp.com/users/id , substituindo "id" pelo id do usuário você terá apenas as informações daquele usuário


### POST:

Abrir o cmd e digitar: 

```sh
curl -i -X POST -H "Content-Type:application/json" -d "{\"nome\": \"nomedesejado\", \"cargo\": \"cargodesejado\", \"idade\": númerodesejado }" https://tonfinal.herokuapp.com/users
```

substituir nomedesejado pelo nome do usuário, cargodesejado pelo cargo do usuário e númerodesejado pelo valor da idade em número.

Ex:
```sh
curl -i -X POST -H "Content-Type:application/json" -d "{\"nome\": \"Enzo\", \"cargo\": \"Estagiario\", \"idade\": 28 }" https://tonfinal.herokuapp.com/users
```

### PUT:

Abrir o cmd e digitar:

```sh
curl -i -X PUT -H "Content-Type:application/json" -d "{\"id\": 1, \"nome\": \"Enzo\", \"cargo\": \"Estagiario\", \"idade\": 228 }" https://tonfinal.herokuapp.com/users
```

Onde podem ser alterados os valores Enzo, Estagiario e 228 pelo novo valor desejado. O id não é modificável.


### DELETE:

```sh
curl -i -X DELETE -H "Content-Type:application/json" -d "{\"id\": 6 }" https://tonfinal.herokuapp.com/users 
```

Pode-se alterar o valor 6. Deletará os dados do usuário referente ao id 6, nesse caso.



Também é possível utilizar o Postman para mandar os comandos de GET, POST, PUT e DELETE.
