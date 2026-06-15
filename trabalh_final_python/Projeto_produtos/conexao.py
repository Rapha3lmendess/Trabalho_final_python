import mysql.connector

def conectar():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="senac",
        database="controle_estoque"
    )