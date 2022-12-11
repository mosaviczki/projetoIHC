import sqlite3

def conexao():
    try:
        conn = sqlite3.connect("dataBaseVoo.db")
        return conn
    except:
        print('Erro ao conectar ao banco de dados')

def create_table():
    try:
        connection = conexao()
        cursor = connection.cursor()
        cursor.execute('''
                        CREATE TABLE voo(
                        "codigo_voo" INTEGER primary key,
                        "dataPartida" TEXT,
                        "valorPassagem" REAL,
                        "codigo_aviao" INTEGER,
                        "modelo_aviao" INTEGER
                    )''')
        connection.commit()
        print('Tabela criada com sucesso')
    except:
        print('Erro ao conectar com o banco de dados. Função create_table')
    finally:
        # Sempre fecha o cursor e a conexão
        cursor.close()
        connection.close()

def insertVoo(query):
    try:
        connection = conexao()
        cursor = connection.cursor()
        print(query)
        cursor.execute(query)
        connection.commit()
        print("Voo inserido com sucesso!")
        return ("Inserido com sucesso!")
    except:
        print("Erro ao tentar inserir no banco de dados!")
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

def deleteVoo(query):
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
