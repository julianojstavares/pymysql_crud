from config import conecta
from queries import sql_insert, sql_select, sql_update, sql_delete


# CRUD - CREATE, READ, UPDATE, DELETE

tablename = 'clientes'

# C = Create = SQL INSERT
def create():
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            columns = '(nome, sobrenome, idade, peso)'
            values = "('Fulano', 'de Tal', 20, 60)"
            sql = sql_insert(tablename, columns, values)
            cursor.execute(sql)
            conexao.commit()

# R = Read = SQL SELECT
def read():
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            sql = sql_select(tablename)
            cursor.execute(sql)
            resultado = cursor.fetchall()
            for linha in resultado:
                print(linha)

def update():
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            column = 'nome'
            value = " 'Beltrano' "
            idNumber = 8
            sql = sql_update(tablename, column, value, idNumber)
            cursor.execute(sql)
            conexao.commit()

def delete():
    with conecta() as conexao:
        with conexao.cursor() as cursor:
            idNumber = 1
            sql = sql_delete(tablename, idNumber)
            cursor.execute(sql)
            conexao.commit()


if __name__ == "__main__":
    
    pass
    #create()
    #read()
    #update()
    #delete()