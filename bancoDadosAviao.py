import sqlite3

def conexao():
    try:
        conn = sqlite3.connect("dataBaseAviao.db")
        return conn
    except:
        print('Erro ao conectar ao banco de dados')

def create_table():
    try:
        connection = conexao()
        cursor = connection.cursor()
        cursor.execute('''
                        CREATE TABLE aviao(
                        "codigo_aviao" INTEGER,
                        "modelo_aviao" TEXT,
                        "assentoTotalEsp" INTEGER,
                        "assentoTotal" INTEGER,
                        "assentoEspOcup" INTEGER,
                        "assentoNorOcup" INTEGER,
                        PRIMARY KEY("codigo_aviao")
                    )''')
        connection.commit()
        print('Tabela criada com sucesso')
    except:
        print('Erro ao conectar com o banco de dados. Função create_table')
    finally:
        cursor.close()
        connection.close()

def insertAviao(query):
    try:
        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Inserido com sucesso!")
        return ("Inserido com sucesso!")
    except:
        print("Erro ao tentar inserir no banco de dados!")
    finally:
        cursor.close()
        connection.close()

"""
def updateAviao():
    try:
        # Script para atualização
        connection = conexao()
        cursor = connection.cursor()
        query = 'UPDATE aviao SET codigo_aviao = 47853, modelo_aviao ="Embraer", assentoEspOcup =10, assentoNorOcup =100 WHERE codigo_aviao = 47853'
        connection.execute(query)
        connection.commit()
        print('Update feito com sucesso')
    except:
        print('Erro ao conectar com o banco de dados. Função update')
    finally:
        cursor.close()
        connection.close()
"""

def deleteAviao(query):
    try:
        #Script para a remoção de uma linha
        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Registro deletado!")
        return ("Registro deletado!")
    except:
        print('Erro ao conectar com o banco de dados. função delete')
    finally:
        cursor.close()
        connection.close()

def read_all(query):
    try:
        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall() # rows são todos os registros
        return rows
    except:
        print('Falha ao conectar-se com o banco. Função read_all')
    finally:
        cursor.close()
        connection.close()

def consultaAviao(query):
    try:
        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall() # rows são todos os registros
        return rows
    except:
        print('Falha ao conectar-se com o banco. Função read_all')
    finally:
        cursor.close()
        connection.close()


                        