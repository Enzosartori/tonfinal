from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///dados.db')
app = Flask(__name__)
api = Api(app)

def getApp():
    return app

class Users(Resource):
    
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select * from user")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        nome = request.json['nome']
        cargo = request.json['cargo']
        idade = request.json['idade']
        
        conn.execute(
            "insert into user values(null, '{0}','{1}' ,'{2}')".format(nome, cargo, idade))

        query = conn.execute('select * from user order by id desc limit 1')
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def put(self):
        conn = db_connect.connect()
        id = request.json['id']
        nome = request.json['nome']
        cargo = request.json['cargo']
        idade = request.json['idade']

        conn.execute("update user set nome ='{0}', cargo ='{1}' , idade = '{2}'  where id = '{3}' ".format(nome, cargo, idade, id ))

       
        query = conn.execute("select * from user where id={0} ".format(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def delete(self): 
        conn = db_connect.connect()
        id = request.json['id']
        conn.execute("delete from user where id={0} ".format(id))
        return {"status": "success"}

class UserById(Resource):
    
    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("select * from user where id = {0} ".format(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


api.add_resource(Users, '/users') 
api.add_resource(UserById, '/users/<id>')



if __name__ == '__main__':
    app.run()
