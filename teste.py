from classes import *
from PyQt5 import uic, QtWidgets
import sys
import bancoDadosAviao

aeronave = Aeronave()
voo = Voo()

voo.calcularOcupacao(10)
voo.__str__

#Janela Gerenciamento de matriculas
def pesquisar():
    # atualizando todos os registros
    if tela.radioButton_5.isChecked():
        tela.lineEdit.setText('')
        atualiza_tabela_principal()
        return

    # Verificando se o texto da caixa pesquisa esta vazio
    pesquisa = tela.lineEdit.text()
    if pesquisa == '':
        QtWidgets.QMessageBox.about(tela, 'Alerta', 'Por favor digite um valor para a pesquisa')
        return
    
    ##Radio button id aluno(validações para poder consultar banco de dados)
    if tela.radioButton.isChecked():
        id_aluno = pesquisa
        try:
            id_aluno = int(id_aluno)
        except:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'Por favor digite um valor inteiro para pesquisar por id')
            return
        if id_aluno < 1 or id_aluno > 300:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'Por favor digite um id válido')
            return
        
        # Pesquisa no banco de dados
        rows = bancoDadosAviao.read_one_id(id_aluno)
        if rows == None:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'Valor não encontrado na tabela')
            return

        limpa_tabela(len(rows))
        for i in range(len(rows)): #linha
            for j in range(len(rows[0])): #coluna
                item = QtWidgets.QTableWidgetItem(f"{rows[i][j]}")
                tela.tableWidget.setItem(i,j, item)
    ## Fim radio button id aluno
     ## Radio button matricula ativa (Validações para consultar banco de dados)
    if tela.radioButton_2.isChecked():
        matricula_ativa = pesquisa
        try:
            matricula_ativa = int(matricula_ativa)
        except:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'Por favor digite um valor inteiro para pesquisar por matricula')
            return
        if matricula_ativa > 1 or matricula_ativa < 0:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'Por favor digite um valor de matrícula válido')
            return

        # Pesquisa no banco de dados
        rows = bancoDadosAviao.read_matricula_ativa(matricula_ativa)
        if rows == None:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'Valor não encontrado na tabela')
            return
        
        limpa_tabela(len(rows))
        for i in range(len(rows)): #linha
            for j in range(len(rows[0])): #coluna
                item = QtWidgets.QTableWidgetItem(f"{rows[i][j]}")
                tela.tableWidget.setItem(i,j, item)
        ## Fim radio button matricula ativa

    ## Radio button tipo da matricula (Validações para consultar banco de dados)
    if tela.radioButton_3.isChecked():
        tipo_matricula = pesquisa
        try:
            tipo_matricula = int(tipo_matricula)
        except:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'Por favor digite um valor inteiro para pesquisar tipo da matrícula')
            return

        matriculas_validas = [30, 90, 180, 360]
        if tipo_matricula not in matriculas_validas:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'Por favor digite um valor de tipo de matrícula válido')
            return

        # Pesquisa no banco de dados
        rows = bancoDadosAviao.read_tipo_matricula(tipo_matricula)
        if rows == None:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'Valor não encontrado na tabela')
            return
        
        limpa_tabela(len(rows))
        for i in range(len(rows)): #linha
            for j in range(len(rows[0])): #coluna
                item = QtWidgets.QTableWidgetItem(f"{rows[i][j]}")
                tela.tableWidget.setItem(i,j, item)
    ## Fim radio button tipo da matricula.

    # Radio button data inicio (validações para consultar banco de dados)
    if tela.radioButton_4.isChecked():
        data_inicio = pesquisa.split('-')
        print(data_inicio)
        if len(data_inicio) != 3:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'Formato inválido. Pesquisa a data no formato: aaaa-mm-dd')
            return

        try:
            teste1 = len(data_inicio[0])
            teste2 = len(data_inicio[1])
            teste3 = len(data_inicio[2])
        except:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'Formato inválido. Use apenas números para pesquisar por data de inicio')
            return

        if teste1 != 4:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'O ano precisa ter 4 digitos')
            return
        if teste2 != 2:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'O mês precisa ter 2 digitos')
            return
        if teste3 != 2:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'O dia precisa ter 2 digitos')
            return    

        try:
            ano = int(data_inicio[0])
            mes = int(data_inicio[1])
            dia = int(data_inicio[2])
        except:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'Formato inválido. Use apenas números para pesquisar por data de inicio')
            return

        rows = bancoDadosAviao.read_data_inicio(f'{data_inicio[0]}-{data_inicio[1]}-{data_inicio[2]}')
        if rows == None:
            QtWidgets.QMessageBox.about(tela, 'Alerta', 'Valor não encontrado na tabela')
            return
        
        limpa_tabela(len(rows))
        for i in range(len(rows)): #linha
            for j in range(len(rows[0])): #coluna
                item = QtWidgets.QTableWidgetItem(f"{rows[i][j]}")
                tela.tableWidget.setItem(i,j, item)

    # Radio button nome do aluno(validações para consulta do banco de dados)
    if tela.radioButton_6.isChecked():
        pesquisa = tela.lineEdit.text()
        rows = bancoDadosAviao.read_nome_aluno(pesquisa)
        print('chego')
        limpa_tabela(len(rows))
        for i in range(len(rows)): #linha
            for j in range(len(rows[0])): #coluna
                item = QtWidgets.QTableWidgetItem(f"{rows[i][j]}")
                tela.tableWidget.setItem(i,j, item)


def limpa_tabela(valor):
    # Valor é o valor de linhas que terá a tabela
    if valor == 1:
        tela.tableWidget.setRowCount(1)
        tela.tableWidget.setColumnCount(len(bancoDadosAviao.read_all()[0]))
        tela.tableWidget.setHorizontalHeaderLabels(["id aluno","nome do aluno", "matricula ativa", "tipo matricula", "data inicio", "data fim"])
    else:
        tela.tableWidget.setRowCount(valor)
        tela.tableWidget.setColumnCount(len(bancoDadosAviao.read_all()[0]))
        tela.tableWidget.setHorizontalHeaderLabels(["id aluno","nome do aluno", "matricula ativa", "tipo matricula", "data inicio", "data fim"])


def voltar():
    tela_inseririculas.close()
    tela.close()

def atualiza_tabela_principal():
    # Setando numero de linhas, colunas e nome das colunas
    tela.tableWidget.setRowCount(len(bancoDadosAviao.read_all()))
    tela.tableWidget.setColumnCount(len(bancoDadosAviao.read_all()[0]))
    tela.tableWidget.setHorizontalHeaderLabels(["id aluno","nome do aluno", "matricula ativa", "tipo matricula", "data inicio", "data fim"])

    # Inserindo os dados na tabela
    rows = bancoDadosAviao.read_all()

    for i in range(len(rows)): #linha
        for j in range(len(rows[0])): #coluna
            item = QtWidgets.QTableWidgetItem(f"{rows[i][j]}")
            tela.tableWidget.setItem(i,j, item)
# Fim janela janela gerenciamento de matriculas

# Janela inserir
def abrir_janela_inserir():
    tela_inseririculas.show()

def fechar_janela_inserir():
    atualiza_tabela_principal()
    tela_inseririculas.lineEdit.setText('')
    tela_inseririculas.lineEdit_2.setText('')
    tela_inseririculas.lineEdit_3.setText('')
    tela_inseririculas.lineEdit_4.setText('')
    tela_inseririculas.close()

def inserir_dados():
    # Parte de teste para verificar se os dados são válidos
    tipos_de_matriculas = [30, 90, 180, 360]
    numeros = '123456789'
    carcteres_especiais = "!@#$%¨&*()-=+[]"
    try:
        # Resgatando o valor dos campos de texto da janela inserir
        id_aluno = tela_inseririculas.lineEdit.text()
        matricula_ativa = tela_inseririculas.lineEdit_2.text()
        tipo_matricula = tela_inseririculas.lineEdit_3.text()
        nome_aluno = tela_inseririculas.lineEdit_4.text()

        # Verificando se os 3 campos da janela inserir estão vazios
        if matricula_ativa == '' or id_aluno == '' or tipo_matricula == '':
            QtWidgets.QMessageBox.about(tela_inseririculas, 'Erro', 'Por favor preencha todos os campos antes de inserir')
            return

        # Verificando se o id do aluno está entre 1 e 300
        id_aluno = int(id_aluno)
        if id_aluno < 1 or id_aluno > 300:
            QtWidgets.QMessageBox.about(tela_inseririculas, 'Erro', 'Por favor insira um id de aluno válido')
            return

        # Verificando se o valor de matricula ativa é valido
        matricula_ativa = int(matricula_ativa)
        if matricula_ativa > 1 or matricula_ativa < 0:
            QtWidgets.QMessageBox.about(tela_inseririculas, 'Erro', 'Por favor insira um valor válido para o campo matricula ativa')
            return

        # Verificando se o valor pego existe na minha lista com matriculas válidas.
        tipo_matricula = int(tipo_matricula)
        if tipo_matricula not in tipos_de_matriculas:
            QtWidgets.QMessageBox.about(tela_inseririculas, 'Erro', 'Por favor insira um valor válido para o campo tipo matricula')
            return

        
        lista_nome_aluno = []
        for i in nome_aluno:
            lista_nome_aluno.append(i)

        for i in numeros:
            if i in lista_nome_aluno:
                QtWidgets.QMessageBox.about(tela_inseririculas, 'Erro', 'Por favor não insira números para registrar o nome do aluno')
                return
        print(nome_aluno)
        for j in carcteres_especiais:
            if j in nome_aluno:
                QtWidgets.QMessageBox.about(tela_inseririculas, 'Erro', 'Por favor não use carctéres especiais para registrar o nome do aluno')
                return


        
    except Exception:
        QtWidgets.QMessageBox.about(tela_inseririculas, 'Erro', 'Insira apenas números')
        return
    #Fim dos testes

    # Parte da inserção no banco de dados
    resposta = bancoDadosAviao.insert(int(id_aluno), nome_aluno, int(matricula_ativa), int(tipo_matricula))
    atualiza_tabela_principal()
    QtWidgets.QMessageBox.about(tela_inseririculas, 'Conexão banco de dados', resposta)
    
    return  
# Fim janela inserir

# Janela de atualizar dados
def abrir_janela_atualizar():
    tela_atualizar.show()

def fechar_janela_atualizar():
    atualiza_tabela_principal()
    tela_atualizar.lineEdit.setText('')
    tela_atualizar.lineEdit_2.setText('')
    tela_atualizar.lineEdit_3.setText('')
    tela_atualizar.lineEdit_4.setText('')
    tela_atualizar.close()


def atualizar_dados():
    tipos_de_matriculas = [30, 90, 180, 360]
    numeros = '123456789'
    carcteres_especiais = "!@#$%¨&*()-=+[]"
    try:
        # resgatando os valores do campos de texto da tela atualizar
        id_aluno = tela_atualizar.lineEdit.text()
        matricula_ativa = tela_atualizar.lineEdit_2.text()
        tipo_matricula = tela_atualizar.lineEdit_3.text()
        nome_aluno = tela_atualizar.lineEdit_4.text()

        # Verificando se os 3 campos da janela inserir estão vazios
        if matricula_ativa == '' or id_aluno == '' or tipo_matricula == '':
            QtWidgets.QMessageBox.about(tela_atualizar, 'Erro', 'Por favor preencha todos os campos antes de atualizar')
            return

        # Verificando se o id do aluno está entre 1 e 300
        id_aluno = int(id_aluno)
        if id_aluno < 1 or id_aluno > 300:
            QtWidgets.QMessageBox.about(tela_atualizar, 'Erro', 'Por favor insira um id de aluno válido')
            return

        # Verificando se o valor de matricula ativa é valido
        matricula_ativa = int(matricula_ativa)
        if matricula_ativa > 1 or matricula_ativa < 0:
            QtWidgets.QMessageBox.about(tela_atualizar, 'Erro', 'Por favor insira um valor válido para o campo matricula ativa')
            return

        # Verificando se o valor pego existe na minha lista com matriculas válidas.
        tipo_matricula = int(tipo_matricula)
        if tipo_matricula not in tipos_de_matriculas:
            QtWidgets.QMessageBox.about(tela_atualizar, 'Erro', 'Por favor insira um valor válido para o campo tipo matricula')
            return

        
        lista_nome_aluno = []
        for i in nome_aluno:
            lista_nome_aluno.append(i)

        for i in numeros:
            if i in lista_nome_aluno:
                QtWidgets.QMessageBox.about(tela_atualizar, 'Erro', 'Por favor não insira números para atualizar o nome do aluno')
                return
        print(nome_aluno)
        for j in carcteres_especiais:
            if j in nome_aluno:
                QtWidgets.QMessageBox.about(tela_atualizar, 'Erro', 'Por favor não use carctéres especiais para atualizar o nome do aluno')
                return


        
    except Exception:
        QtWidgets.QMessageBox.about(tela_atualizar, 'Erro', 'Insira apenas números')
        return
    #Fim dos testes

    # Parte da inserção no banco de dados
    resposta = bancoDadosAviao.update_table(int(matricula_ativa), nome_aluno,  int(tipo_matricula),int(id_aluno))
    atualiza_tabela_principal()
    QtWidgets.QMessageBox.about(tela_atualizar, 'Conexão banco de dados', 'Atualização feita com sucesso')
    
    return  
#Fim janela atualizar

# Janela excluir
def abrir_janela_excluir():
    tela_excluir.show()

def fechar_janela_excluir():
    atualiza_tabela_principal()
    tela_excluir.lineEdit.setText('')
    tela_excluir.close()

def excluir_dados():
    try:
        id_aluno = tela_excluir.lineEdit.text()
        id_aluno = int(id_aluno)
        if id_aluno < 1 or id_aluno > 300:
            QtWidgets.QMessageBox.about(tela_excluir, 'Erro', 'Por favor insira um id de aluno válido')
            return
        response = bancoDadosAviao.read_one_id(id_aluno)
        if response == None:
            QtWidgets.QMessageBox.about(tela_excluir, 'Erro', 'Falha ao excluir, id inexistente na tabela')
            return

    except Exception:
        QtWidgets.QMessageBox.about(tela_excluir, 'Erro', 'Insira apenas números')
        return

    # Parte da inserção no banco de dados
    resposta = bancoDadosAviao.delete(id_aluno)
    atualiza_tabela_principal()
    QtWidgets.QMessageBox.about(tela_excluir, 'Conexão banco de dados', 'Registro excluido com sucesso')
    
    return  

def main():
    #Carregar janelas
    app = QtWidgets.QApplication(sys.argv)
    tela = uic.loadUi('tela.ui')
    tela_inserir = uic.loadUi('inserir.ui')
    tela_atualizar = uic.loadUi('atualizar.ui')
    tela_excluir = uic.loadUi('tela_excluir')

    # Conectando os botoes da janela principal as funções da janela principal
    tela.pushButton_2.clicked.connect(abrir_janela_inserir)
    tela.pushButton_7.clicked.connect(pesquisar)
    tela.pushButton_3.clicked.connect(abrir_janela_atualizar)
    tela.pushButton_5.clicked.connect(voltar)
    tela.pushButton_4.clicked.connect(abrir_janela_excluir)

    # Conectando os botões da janela de inserir as funções da janela de inserir
    tela_inserir.pushButton_2.clicked.connect(fechar_janela_inserir)
    tela_inserir.pushButton.clicked.connect(inserir_dados)

    # Conectando os botões da jenala atualizar as funções da janela atualizar
    tela_atualizar.pushButton_2.clicked.connect(fechar_janela_atualizar)
    tela_atualizar.pushButton.clicked.connect(atualizar)

    # Conectando os botões da janela excluir as funções da janela excluir
    tela_excluir.pushButton_2.clicked.connect(fechar_janela_excluir)
    tela_excluir.pushButton.clicked.connect(excluir_dados)

if __name__ == "__main__":
    main()