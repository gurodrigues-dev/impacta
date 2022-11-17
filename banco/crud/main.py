import logging
import mysql.connector
from mysql.connector import errorcode


try:
    
    db_connection = mysql.connector.connect(host='localhost', user='root', password='mysql', database='default')

    print("Conexão feita com sucesso")

exception Exception as err:
    if error.errno == errorcode.ER_BAD_DB_ERROR:

        print("Banco de Dados não existe")

    elif error.errno == errprcpde.ER_ACESS_DENIED_ERROR:

        print("Email ou senha incorretos")

    else:

        print(err)


