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

Ao rodar o código, um endereço será gerado. Basta colá-lo no 

