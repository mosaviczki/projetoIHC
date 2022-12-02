################################################################################
## Form generated automatic 
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        Form.setMinimumSize(QSize(640, 480))
        Form.setMaximumSize(QSize(640, 480))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 641, 481))
        self.widget.setStyleSheet(u"background-color: rgb(42, 42, 63);")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 390, 141, 41))
        font = QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px\n"
"")
        self.label_1 = QLabel(self.widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(230, 20, 181, 51))
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_1.setFont(font1)
        self.label_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.line_6 = QFrame(self.widget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(10, 360, 621, 16))
        self.line_6.setStyleSheet(u"border-color: rgb(255, 255, 255);")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 80, 141, 31))
        font2 = QFont()
        font2.setFamily(u"MS PGothic")
        font2.setPointSize(12)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 240, 371, 31))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(380, 230, 251, 41))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.progressBarContainer = QFrame(self.widget)
        self.progressBarContainer.setObjectName(u"progressBarContainer")
        self.progressBarContainer.setGeometry(QRect(420, 60, 190, 150))
        self.progressBarContainer.setMinimumSize(QSize(150, 150))
        self.progressBarContainer.setMaximumSize(QSize(190, 150))
        self.progressBarContainer.setStyleSheet(u"")
        self.progressBarContainer.setFrameShape(QFrame.StyledPanel)
        self.progressBarContainer.setFrameShadow(QFrame.Raised)
        self.progressBar = roundProgressBar(self.progressBarContainer)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 30, 100, 100))
        self.progressBar.setMinimumSize(QSize(100, 100))
        self.progressBar.setMaximumSize(QSize(100, 100))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.rpb_setMaximum(100)
        self.progressBar.rpb_setValue(96)
        self.label_9 = QLabel(self.progressBarContainer)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, -10, 191, 41))
        font3 = QFont()
        font3.setFamily(u"Arial Black")
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_1 = QLineEdit(self.widget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(10, 120, 251, 71))
        self.lineEdit_1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(136, 136, 136);\n"
"border-radius: 10px\n"
"")
        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 270, 251, 71))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(136, 136, 136);\n"
"border-radius: 10px\n"
"")
        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(380, 270, 251, 71))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(136, 136, 136);\n"
"border-radius: 10px\n"
"")
        self.pushButton.raise_()
        self.line_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_11.raise_()
        self.progressBarContainer.raise_()
        self.lineEdit_1.raise_()
        self.lineEdit_4.raise_()
        self.lineEdit_5.raise_()
        self.label_1.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"VOLTAR", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"RELATORIO", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"OCUPA\u00c7\u00c3O", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"ASSENTOS TOTAIS", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"ASSENTOS OCUPADOS", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"OCUPA\u00c7\u00c3O VOO", None))
    # retranslateUi

