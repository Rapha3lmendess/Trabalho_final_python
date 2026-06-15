import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="senac",
        database="biblioteca"
    )
    return conexao