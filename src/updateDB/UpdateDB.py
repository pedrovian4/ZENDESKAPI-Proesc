import psycopg2 as pg
from dotenv import load_dotenv
from os import environ as env

load_dotenv('../../.env')

def conectaBanco():
    conexao = pg.connect(user=env['user'],password=env['password'],
                                  host=env['host'],
                                  port=env['port'],
                                  database=env['database'])
    return conexao

def fazQuery(sql):
    conexao = conectaBanco()
    cursor = conexao.cursor()
    cursor.execute(sql)
    commit =  conexao.commit() 
    conexao.close()
    return commit
