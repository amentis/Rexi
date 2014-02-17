__author__ = 'amentis'

from mysql import connector


def database_connect():
    connection = connector.connect(user='rexi', password='U4rx8Pfcx5', host='127.0.0.1', database='rexi')

    connection.close()

#TODO: continue writing that