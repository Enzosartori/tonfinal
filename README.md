# Como utilizar a API REST

Passo a passo para utilização da API REST criada para solucionar o case "Desafio 2".



Os seguintes métodos foram implementados:


GET - Lê o banco de dados e "printa" os valores no operador

POST - Insere um novo valor ao banco de dados

PUT - Atualiza um valor no banco de dados

DELETE - Apaga um valor no banco de dados

### GET:

Entrar na url: 	https://basefuncton.herokuapp.com/users para visualizar toda a base de dados e 
		https://basefuncton.herokuapp.com/users/id , substituindo "id" pelo id do usuário,para informações daquele usuário


### POST:

Abrir o cmd e digitar: 

```sh
curl -i -X POST -H "Content-Type:application/json" -d "{\"nome\": \"nomedesejado\", \"cargo\": \"cargodesejado\", \"idade\": númerodesejado }" https://basefuncton.herokuapp.com/users
```

substituir nomedesejado pelo nome do usuário, cargodesejado pelo cargo do usuário e númerodesejado pelo valor da idade em número.

Ex:
```sh
curl -i -X POST -H "Content-Type:application/json" -d "{\"nome\": \"Enzo\", \"cargo\": \"Estagiario\", \"idade\": 28 }" https://basefuncton.herokuapp.com/users
```

Ao executar o comando um log da ação será gerado na própria cmd, como : {"status": "success"}

### PUT:

Abrir o cmd e digitar:

```sh
curl -i -X PUT -H "Content-Type:application/json" -d "{\"id\": 1, \"nome\": \"Enzo\", \"cargo\": \"Estagiario\", \"idade\": 228 }" https://basefuncton.herokuapp.com/users
```

Onde podem ser alterados os valores Enzo, Estagiario e 228 pelo novo valor desejado. O id não é modificável.

Ao executar o comando um log da ação será gerado na própria cmd, como : {"status": "success"}

### DELETE:

```sh
curl -i -X DELETE -H "Content-Type:application/json" -d "{\"id\": 6 }" https://basefuncton.herokuapp.com/users 
```

Pode-se alterar o valor 6. Deletará os dados do usuário referente ao id 6, nesse caso.

Ao executar o comando um log da ação será gerado na própria cmd, como : {"status": "success"}



#### Também é possível utilizar o Postman para mandar os comandos de GET, POST, PUT e DELETE.
