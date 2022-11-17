import logging
import mysql.connector

cnx = mysql.connector.connect(user='root', password='mysql',
                              host='127.0.0.1',
                              port = 3306, 
                              database='bancoteste')
cnx.close()