import datetime
import sqlite3
from sqlite3.dbapi2 import Cursor, connect

def conexao():
    try:
        # Conexão ao banco de dados
        connection = sqlite3.connect("dataBaseVoo.db")
        return connection
    except:
        print('Erro ao conectar ao banco de dados')

def create_table():
    try:
        # Script para criar tabela
        sql = '''
                CREATE TABLE voo(
                    codigo_voo integer primary key,
                    dataPartida text,
                    valorPassagem real,
                )'''

        # Criando o cursor
        connection = conexao()
        cursor = connection.cursor()
        # Executando meu código sql acima
        cursor.execute(sql)
        # Efetivo a criação da tabela
        connection.commit()

        print('Tabela criada com sucesso')

    except:
        print('Erro ao conectar com o banco de dados. Função create_table')

    finally:
        # Sempre fecha o cursor e a conexão
        cursor.close()
        connection.close()

def insertVoo(codigo_voo, dataPartida, valorPassagem):
    existe_na_tabela = read_one_id(codigo_voo)
    if existe_na_tabela != None:
        return 'Este codigo já existe na tabela'
    
    try:
        # Script para inserção
        sql = '''INSERT INTO voo( codigo_vooviao, dataPartida, valorPassagem)
             VALUES (?, ?, ?)'''
    
        connection = conexao()
        cursor = connection.cursor()
        # Método em que passo a string, e uma lista que substituirá os simbolos "?" respectivamente.
        cursor.execute(sql, [ codigo_voo, dataPartida, valorPassagem])
        connection.commit()
        print("Inserido com sucesso!")
        return ("Inserido com sucesso!")


    except:
        print('Erro ao conectar com o banco de dados. Função insert')
        return ('Erro ao conectar com o banco de dados.')

    finally:
        cursor.close()
        connection.close()

def update_table(codigo_voo, dataPartida, valorPassagem):
    try:
        # Script para atualização
        update = '''
                UPDATE voo
                SET codigo_voo = ?, dataPartida = ?, valorPassagem = ?
                WHERE  codigo_voo = ?
                '''
        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(update, [codigo_voo, dataPartida, valorPassagem])
        connection.commit()
        print('Update feito com sucesso')

    except:
        print('Erro ao conectar com o banco de dados. Função update')

    finally:
        cursor.close()
        connection.close()

def delete(codigo_voo):
    try:
        #Script para a remoção de uma linha
        delete = '''DELETE FROM voo WHERE  codigo_voo = ?'''

        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(delete, [codigo_voo] )
        connection.commit()
        print('Registro deletado')

    except:
        print('Erro ao conectar com o banco de dados. função delete')

    finally:
        cursor.close()
        connection.close()

def read_all():
    try:
        # Script para ler todos os dados
        sql = '''SELECT * FROM voo'''

        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(sql)

        # rows são todos os meus registros
        rows = cursor.fetchall()

        return rows


    except:
        print('Falha ao conectar-se com o banco. Função read_all')
    finally:
        cursor.close()
        connection.close()


def read_one_id(codigo_voo):
    try:
        # Script para ler apenas um dado
        sql = '''SELECT * FROM voo WHERE codigo_voo = ?'''

        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(sql, [codigo_voo])

        # row é apenas um registro
        row = cursor.fetchall()
        
        return row
        #print(f'Id do Cliente: {row[0]}, Nome: {row[1]}, Comentario: {row[2]}')

    except:
        print('Falha ao conectar-se com o banco. Função read_one_id')
    finally:
        cursor.close()
        connection.close()


def read_dataPartida(dataPartida):
    try:
        # Script para ler apenas um dado
        sql = '''SELECT * FROM voo WHERE dataPartida = ?'''

        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(sql, [dataPartida])

        # row é apenas um registro
        rows = cursor.fetchall()
        return rows

    except:
        print('Falha ao conectar-se com o banco. Função read_one_dataPartida')
    finally:
        cursor.close()
        connection.close()


def read_valorPassagem(valorPassagem):
    try:
        # Script para ler apenas um dado
        sql = '''SELECT * FROM voo WHERE valorPassagem = ?'''

        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(sql, [valorPassagem])

        # row é apenas um registro
        rows = cursor.fetchall()
        return rows

    except:
        print('Falha ao conectar-se com o banco. Função read_one_valorPassagem')
    finally:
        cursor.close()
        connection.close()


if __name__ == '__main__':
    '''
    #insert(1, 1, 90)
    #insert(2, 1, 30)
    #insert(3, 1, 180)
    #insert(4, 1, 360)
    #update_table(0, 90, 4)
    #delete(4)
    #print(read_all())
    #print(read_one(1)  )'''

