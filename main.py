import sys, os, sqlite3, bancoDadosAviao, bancoDadosVoo
from PyQt5 import uic, QtWidgets, QtGui, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPen, QBrush, QIcon, QPainter
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2extn.RoundProgressBar import roundProgressBar
from ui_relatorio import * 

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

def aviaoWindow():
    telaAviao.show()
    telaAviao.pushButton_3.clicked.connect(voltar)
    telaAviao.pushButton_4.clicked.connect(inserirAviaoWindow)
    telaAviao.pushButton_5.clicked.connect(alterarAviaoWindow)
    telaAviao.pushButton_6.clicked.connect(excluirAviaoWindow)

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

def alterarVooWindow():
    alterarVoo.show()
    alterarVoo.pushButton.clicked.connect(voltar)

def excluirVooWindow():
    excluirVoo.show()
    excluirVoo.pushButton.clicked.connect(voltar)

def inserirAviaoWindow():
    inserirAviao.show()
    inserirAviao.pushButton.clicked.connect(voltar)

def alterarAviaoWindow():
    alterarAviao.show()
    alterarAviao.pushButton.clicked.connect(voltar)

def excluirAviaoWindow():
    excluirAviao.show()
    excluirAviao.pushButton.clicked.connect(voltar)


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


