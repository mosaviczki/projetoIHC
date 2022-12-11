import sys, sqlite3, bancoDadosAviao, bancoDadosVoo
from PyQt5 import uic, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.QtWidgets import *
#from PySide2 import QtCore, QtGui
from ui_relatorio import * 
from bancoDadosAviao import *

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



def relatorio():
    telaRelatorio.show()

class RelatorioWindow(QWidget):
    def __init__(self):
        super(RelatorioWindow, self).__init__()
        self.ui = Ui_Form() 
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(voltar) 

def inserirVooWindow():
    inserirVoo.show()
    inserirVoo.pushButton.clicked.connect(voltar)
    inserirVoo.pushButton_2.clicked.connect(inserirDadosVoo)
    dbVoo = bancoDadosAviao()
    inserirVoo.comboBox.addItem([])

def inserirDadosVoo():
    codigo_voo = inserirVoo.lineEdit.text()
    dataPartida = inserirVoo.lineEdit_2.text()
    valorPassagem = inserirVoo.lineEdit_3.text()
    try:
        bancoDadosVoo.insertVoo(codigo_voo, dataPartida, valorPassagem)
    except sqlite3.Error as erro:
        print("Erro ao inserir no banco de dados")

def alterarVooWindow():
    alterarVoo.show()
    alterarVoo.pushButton.clicked.connect(voltar)

def excluirVooWindow():
    excluirVoo.show()
    excluirVoo.pushButton.clicked.connect(voltar)

################ DADOS AVIÃO ################
def aviaoWindow():
    telaAviao.show()
    #dadosAviao()
    telaAviao.pushButton_3.clicked.connect(voltar)
    telaAviao.pushButton_4.clicked.connect(inserirAviaoWindow)
    telaAviao.pushButton_5.clicked.connect(alterarAviaoWindow)
    telaAviao.pushButton_6.clicked.connect(excluirAviaoWindow)
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
        #dadosAviao()
    except:
        print("Erro de conexão")

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
    #dadosAviao()
    try:
        dbAv.updateAviao("UPDATE aviao SET modelo_aviao = '{}', assentoEspOcup = {}, assentoNorOcup = {} WHERE  codigo_aviao = {}".format(modelo_aviao, int(assentoEspOcup), int(assentoNorOcup), int(codigo_aviao)))
    except:
        print("Erro de conexão")

def excluirAviaoWindow():
    excluirAviao.show()
    excluirAviao.pushButton.clicked.connect(voltar)
    excluirAviao.pushButton_2.clicked.connect(deletar)

def deletar():
    codigo_aviao = excluirAviao.lineEdit.text()
    dbAv = bancoDadosAviao
    #dadosAviao()
    try:
        dbAv.deleteAviao("DELETE FROM aviao WHERE codigo_aviao = {}".format(int(codigo_aviao)))
    except:
        print("Erro de conexão")

#def main():
app = QtWidgets.QApplication(sys.argv)
telaInicial = uic.loadUi("telaInicial.ui")
telaAviao = uic.loadUi("telaAviao.ui")
inserirVoo = uic.loadUi("inserirVoo.ui")
alterarVoo = uic.loadUi("alterarVoo.ui")
excluirVoo = uic.loadUi("excluirVoo.ui")
inserirAviao = uic.loadUi("inserirAviao.ui")
alterarAviao = uic.loadUi("alterarAviao.ui")
excluirAviao = uic.loadUi("excluirAviao.ui")
telaRelatorio = RelatorioWindow()

#telaInicial.pushButton.clicked.connect(pesquisarInicial)
telaInicial.pushButton_2.clicked.connect(aviaoWindow)
telaInicial.pushButton_3.clicked.connect(relatorio)
telaInicial.pushButton_4.clicked.connect(inserirVooWindow)
telaInicial.pushButton_5.clicked.connect(alterarVooWindow)
telaInicial.pushButton_6.clicked.connect(excluirVooWindow)


telaInicial.show()
app.exec_()


'''
RELATORIO
class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
  
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
'''  


