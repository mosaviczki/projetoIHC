import sys, sqlite3
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from db import bancoDadosAviao, bancoDadosVoo

#Função para fechar janelas ao clicar em voltar
def voltar():
    telaAviao.close()
    inserirVoo.close()
    alterarVoo.close()
    excluirVoo.close()
    inserirAviao.close()
    alterarAviao.close()
    excluirAviao.close()
    telaRelatorio.close()
    telaRelatorioI.close()

def relatorioCod():
    telaRelatorioI.show()
    telaRelatorioI.pushButton.clicked.connect(voltar)
    telaRelatorioI.pushButton_2.clicked.connect(relatorio)

def relatorio():
    codigo_voo = telaRelatorioI.lineEdit.text()
    telaRelatorio.show()
    codigo_aviao = codVoo(codigo_voo)
    total = calculaTotal(codigo_aviao)
    ocupado = calculaOcupado(codigo_aviao)
    ocupacao = ((ocupado*100)/total)
    ocup = (f'{ocupacao:.2f}%')
    telaRelatorio.label_6.setText(str(ocup))
    telaRelatorio.label_7.setText(str(total)) 
    telaRelatorio.label_8.setText(str(ocupado)) 
    telaRelatorio.pushButton.clicked.connect(voltar)

def codVoo(codigo_voo):
    db = bancoDadosVoo
    a = db.consultaVoo("SELECT codigo_aviao FROM voo WHERE codigo_voo = {}".format(codigo_voo))
    total = []
    for x in a:
        for y in x:
            total.append(y)
    som = sum(total)
    return som

def calculaTotal(codigo_aviao):
    db = bancoDadosAviao
    a = db.consultaAviao("SELECT assentoTotalEsp, assentoTotal FROM aviao WHERE codigo_aviao = {}".format(codigo_aviao))
    total = []
    for x in a:
        for y in x:
            total.append(y)
    som = sum(total)
    return som

def calculaOcupado(codigo_aviao):
    db = bancoDadosAviao
    a = db.consultaAviao("SELECT assentoEspOcup, assentoNorOcup FROM aviao WHERE codigo_aviao = {}".format(codigo_aviao))
    total = []
    for x in a:
        for y in x:
            total.append(y)
    som = sum(total)
    return som

################ DADOS VOO ################
def inserirVooWindow():
    inserirVoo.show()
    consultaCod()
    dadosVoo()
    inserirVoo.pushButton.clicked.connect(voltar)
    inserirVoo.pushButton_2.clicked.connect(inserirDadosVoo)

def dadosVoo():
    query = "SELECT * FROM voo"
    dbVoo = bancoDadosVoo
    lista = dbVoo.read_all(query)
    telaInicial.tableWidget.setRowCount(len(dbVoo.read_all(query)))
    telaInicial.tableWidget.setColumnCount(len(dbVoo.read_all(query)[0]))
    
    # Inserindo os dados na tabela
    for i in range(len(lista)): #linha
        for j in range(len(lista[0])): #coluna
            item = QtWidgets.QTableWidgetItem(f"{lista[i][j]}")
            telaInicial.tableWidget.setItem(i,j, item)

def inserirDadosVoo():
    codigo_voo = inserirVoo.lineEdit.text()
    dataPartida = inserirVoo.lineEdit_2.text()
    valorPassagem = inserirVoo.lineEdit_3.text()
    codigo_aviao = inserirVoo.comboBox.currentText() 
    dbVoo = bancoDadosVoo
    
    try:
        dbVoo.insertVoo("INSERT INTO voo (codigo_voo, dataPartida, valorPassagem, codigo_aviao) VALUES ({},'{}',{}, {})".format(int(codigo_voo), dataPartida, float(valorPassagem), int(codigo_aviao)))
        modelo_aviao = consultaMod(codigo_aviao)
        updateModelo(modelo_aviao, codigo_voo)
        QMessageBox.about(inserirVoo, "Sucesso", "Dados de voo inserido com sucesso")
    except sqlite3.Error as erro:
        QMessageBox.about(inserirVoo, "ERRO", "Erro ao inserir no banco de dados")

def consultaCod():
    dbAv = bancoDadosAviao
    listaDado = dbAv.consultaAviao("SELECT codigo_aviao FROM aviao")
    for r in listaDado:
        for x in r:
            inserirVoo.comboBox.addItem(str(x))
            alterarVoo.comboBox.addItem(str(x))
    
def consultaMod(codigo_aviao):
    dbAv = bancoDadosAviao
    modelo = dbAv.consultaAviao("SELECT modelo_aviao FROM aviao WHERE codigo_aviao={}".format(codigo_aviao))
    for name in modelo:
        for model in name:
            return model

def alterarVooWindow():
    alterarVoo.show()
    dadosVoo()
    alterarVoo.pushButton.clicked.connect(voltar)
    alterarVoo.pushButton_2.clicked.connect(updateVoo)

def updateVoo():
    codigo_voo = alterarVoo.lineEdit.text()
    dataPartida = alterarVoo.lineEdit_2.text()
    valorPassagem = alterarVoo.lineEdit_3.text()
    codigo_aviao = alterarVoo.comboBox.currentText()
    print(codigo_aviao) 
    dbVoo = bancoDadosVoo
    try:
        dbVoo.update_table(codigo_voo, dataPartida, valorPassagem, codigo_aviao)
        modelo_aviao = consultaMod(codigo_aviao)
        updateModelo(modelo_aviao, codigo_voo)
        QMessageBox.about(alterarVoo, "Sucesso", "Dados de voo alterado com sucesso")
    except:
        QMessageBox.about(alterarVoo, "ERRO", "Erro de conexão")

def updateModelo(modelo_aviao, codigo_voo):
    dbVoo = bancoDadosVoo
    try:
        dbVoo.update_table_modelo(modelo_aviao, codigo_voo)
        dadosVoo()
    except:
        print("Erro de conexão")

def excluirVooWindow():
    excluirVoo.show()
    dadosVoo()
    excluirVoo.pushButton.clicked.connect(voltar)
    excluirVoo.pushButton_2.clicked.connect(deletarVoo)

def deletarVoo():
    codigo_voo = excluirVoo.lineEdit.text()
    dbVoo = bancoDadosVoo
    #dadosAviao()
    try:
        dbVoo.deleteVoo("DELETE FROM voo WHERE codigo_voo = {}".format(int(codigo_voo)))
        QMessageBox.about(excluirVoo, "Sucesso", "Dados de voo deletado com sucesso")
    except:
        QMessageBox.about(excluirVoo, "ERRO", "Erro de conexão")

################ DADOS AVIÃO ################
def aviaoWindow():
    telaAviao.show()
    #dadosAviao()
    telaAviao.pushButton.clicked.connect(voltar)
    telaAviao.pushButton_2.clicked.connect(inserirAviaoWindow)
    telaAviao.pushButton_3.clicked.connect(alterarAviaoWindow)
    telaAviao.pushButton_4.clicked.connect(excluirAviaoWindow)
    dadosAviao()

def dadosAviao():
    query = "SELECT * FROM aviao"

    dbAv = bancoDadosAviao
    lista = dbAv.read_all(query)
    telaAviao.tableWidget.setRowCount(len(dbAv.read_all(query)))
    telaAviao.tableWidget.setColumnCount(len(dbAv.read_all(query)[0]))
    
    # Inserindo os dados na tabela
    for i in range(len(lista)): #linha
        for j in range(len(lista[0])): #coluna
            item = QtWidgets.QTableWidgetItem(f"{lista[i][j]}")
            telaAviao.tableWidget.setItem(i,j, item)

def inserirAviaoWindow():
    inserirAviao.show()
    inserirAviao.pushButton.clicked.connect(voltar)
    inserirAviao.pushButton_2.clicked.connect(inserirDadosAviao)

def inserirDadosAviao():
    dbAv = bancoDadosAviao
    codigo_aviao = inserirAviao.lineEdit.text()
    modelo_aviao = inserirAviao.lineEdit_2.text()
    assentoTotalEsp = inserirAviao.lineEdit_3.text()
    assentoTotal = inserirAviao.lineEdit_4.text()
   
    try:
        dbAv.insertAviao("INSERT INTO aviao(codigo_aviao, modelo_aviao, assentoTotalEsp, assentoTotal) VALUES({},'{}',{},{})".format(int(codigo_aviao), modelo_aviao, int(assentoTotalEsp), int(assentoTotal)))
        dadosAviao()
        QMessageBox.about(inserirAviao, "Sucesso", "Dados do avião inserido com sucesso")
    except:
        QMessageBox.about(inserirAviao, "ERRO", "Erro de conexão")

def alterarAviaoWindow():
    alterarAviao.show()
    alterarAviao.pushButton.clicked.connect(voltar)
    alterarAviao.pushButton_2.clicked.connect(update)

def update():
    codigo_aviao = alterarAviao.lineEdit.text()
    modelo_aviao = alterarAviao.lineEdit_2.text()
    assentoEspOcup = alterarAviao.lineEdit_3.text()
    assentoNorOcup = alterarAviao.lineEdit_4.text()
    dbAv = bancoDadosAviao
    try:
        dbAv.update_table(codigo_aviao, modelo_aviao, assentoEspOcup, assentoNorOcup)
        QMessageBox.about(alterarAviao, "Sucesso", "Dados do avião alterado com sucesso")
    except:
         QMessageBox.about(alterarAviao, "ERRO", "Erro de conexão")

def excluirAviaoWindow():
    excluirAviao.show()
    excluirAviao.pushButton.clicked.connect(voltar)
    excluirAviao.pushButton_2.clicked.connect(deletarAviao)

def deletarAviao():
    codigo_aviao = excluirAviao.lineEdit.text()
    dbAv = bancoDadosAviao
    #dadosAviao()
    try:
        dbAv.deleteAviao("DELETE FROM aviao WHERE codigo_aviao = {}".format(int(codigo_aviao)))
        QMessageBox.about(deletarAviao, "Sucesso", "Dados do avião deletado com sucesso")
    except:
        QMessageBox.about(inserirAviao, "ERRO", "Erro de conexão")

#def main():
app = QtWidgets.QApplication(sys.argv)
telaInicial = uic.loadUi("ui/telaInicial.ui")
telaAviao = uic.loadUi("ui/telaAviao.ui")
inserirVoo = uic.loadUi("ui/inserirVoo.ui")
alterarVoo = uic.loadUi("ui/alterarVoo.ui")
excluirVoo = uic.loadUi("ui/excluirVoo.ui")
inserirAviao = uic.loadUi("ui/inserirAviao.ui")
alterarAviao = uic.loadUi("ui/alterarAviao.ui")
excluirAviao = uic.loadUi("ui/excluirAviao.ui")
telaRelatorio = uic.loadUi("ui/relatorio.ui")
telaRelatorioI = uic.loadUi("ui/relatorioInicial.ui")
telaInicial.show()
#dadosVoo()
telaInicial.pushButton_2.clicked.connect(aviaoWindow)
telaInicial.pushButton_3.clicked.connect(relatorioCod)
telaInicial.pushButton_4.clicked.connect(inserirVooWindow)
telaInicial.pushButton_5.clicked.connect(alterarVooWindow)
telaInicial.pushButton_6.clicked.connect(excluirVooWindow)


telaInicial.show()
app.exec_()




