import datetime
import sqlite3
from sqlite3.dbapi2 import Cursor, connect

#CRUD Create, read, Update e delete

def conexao():
    try:
        # Conexão ao banco de dados
        connection = sqlite3.connect("dataBase.db")
        return connection
    except:
        print('Erro ao conectar ao banco de dados')

def create_table():
    try:
        # Script para criar tabela
        sql = '''
                CREATE TABLE aviao(
                    codigo_aviao integer primary key,
                    modelo_aviao varchar(100),
                    qtdAssento integer,
                    qtdAssentoEspecial integer,
                    qtdAssentoTotal integer
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


def insert( codigo_aviao,modelo_aviao, qtdAssento, qtdAssentoEspecial, qtdAssentoTotal):
    existe_na_tabela = read_one_id(codigo_aviao)
    if existe_na_tabela != None:
        return 'Este codigo já existe na tabela'
    
    try:
        # Script para inserção
        sql = '''INSERT INTO aviao( codigo_aviao, modelo_aviao, qtdAssento, qtdAssentoEspecial, qtdAssentoTotal)
             VALUES (?, ?, ?, ?, ?)'''
    
        connection = conexao()
        cursor = connection.cursor()
        # Método em que passo a string, e uma lista que substituirá os simbolos "?" respectivamente.
        cursor.execute(sql, [ codigo_aviao, modelo_aviao, qtdAssento, qtdAssentoEspecial, qtdAssentoTotal])
        connection.commit()
        print("Inserido com sucesso!")
        return ("Inserido com sucesso!")


    except:
        print('Erro ao conectar com o banco de dados. Função insert')
        return ('Erro ao conectar com o banco de dados.')

    finally:
        cursor.close()
        connection.close()

def update_table(qtdAssento, modelo_aviao, qtdAssentoEspecial, codigo_aviao, qtdAssentoTotal):
    try:
        # Script para atualização
        update = '''
                UPDATE aviao
                SET qtdAssento = ?, modelo_aviao = ? ,qtdAssentoEspecial = ?
                WHERE  codigo_aviao = ?
                '''
        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(update, [qtdAssento, modelo_aviao, qtdAssentoEspecial,  codigo_aviao, qtdAssentoTotal ])
        connection.commit()
        print('Update feito com sucesso')

    except:
        print('Erro ao conectar com o banco de dados. Função update')

    finally:
        cursor.close()
        connection.close()

def delete(codigo_aviao):
    try:
        #Script para a remoção de uma linha
        delete = '''DELETE FROM aviao WHERE  codigo_aviao = ?'''

        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(delete, [codigo_aviao] )
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
        sql = '''SELECT * FROM aviao'''

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


def read_one_id( codigo_aviao):
    try:
        # Script para ler apenas um dado
        sql = '''SELECT * FROM aviao WHERE  codigo_aviao = ?'''

        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(sql, [ codigo_aviao])

        # row é apenas um registro
        row = cursor.fetchall()
        
        return row
        #print(f'Id do Cliente: {row[0]}, Nome: {row[1]}, Comentario: {row[2]}')

    except:
        print('Falha ao conectar-se com o banco. Função read_one_id')
    finally:
        cursor.close()
        connection.close()


def read_qtdAssentoEspecial(qtdAssentoEspecial):
    try:
        # Script para ler apenas um dado
        sql = '''SELECT * FROM aviao WHERE qtdAssentoEspecial = ?'''

        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(sql, [qtdAssentoEspecial])

        # row é apenas um registro
        rows = cursor.fetchall()
        return rows

    except:
        print('Falha ao conectar-se com o banco. Função read_one_qtdAssentoEspecial ')
    finally:
        cursor.close()
        connection.close()


def read_qtdAssento(qtdAssento):
    try:
        # Script para ler apenas um dado
        sql = '''SELECT * FROM aviao WHERE qtdAssento = ?'''

        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(sql, [qtdAssento])

        # row é apenas um registro
        rows = cursor.fetchall()
        return rows

    except:
        print('Falha ao conectar-se com o banco. Função read_one_qtdAssento')
    finally:
        cursor.close()
        connection.close()


def read_qtdAssentoTotal(qtdAssentoTotal):
    try:
        # Script para ler apenas um dado
        sql = '''SELECT * FROM aviao WHERE qtdAssentoTotal = ?'''

        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(sql, [qtdAssentoTotal])

        # row é apenas um registro
        rows = cursor.fetchall()
        return rows

    except:
        print('Falha ao conectar-se com o banco. Função read_one_qtdAssentoTotal')
    finally:
        cursor.close()
        connection.close()

def read_modelo_aviao(modelo_aviao):
    try:
        modelo_aviao = ('%'+ modelo_aviao + '%')
        # Script para ler apenas um dado
        sql =  '''SELECT * FROM aviao WHERE modelo_aviao like ? '''

        connection = conexao()
        cursor = connection.cursor()
        cursor.execute(sql, [modelo_aviao])

        # row é apenas um registro
        rows = cursor.fetchall()
        return rows

    except:
        print('Falha ao conectar-se com o banco. Função read_one_qtdAssentoTotal')
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

