from PyQt5 import QtCore, QtGui, QtWidgets
from ACCESS_RECORDS import *
from ADD_IMAGE import *
import sys

class Ui_SUCCESSFUL_LOGIN1(object):
    def exit(self):
        sys.exit()

    def ok2(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow1()
        self.ui.setup(self.window)
        self.window.show()




    def ok(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow2()
        self.ui.setup(self.window)
        self.window.show()





    def setup(self, SUCCESSFUL_LOGIN):
        SUCCESSFUL_LOGIN.setObjectName("SUCCESSFUL_LOGIN")
        SUCCESSFUL_LOGIN.resize(1920, 1280)
        SUCCESSFUL_LOGIN.setMinimumSize(QtCore.QSize(1920, 1280))
        self.centralwidget = QtWidgets.QWidget(SUCCESSFUL_LOGIN)
        self.centralwidget.setObjectName("centralwidget")
        self.ACCESS_RECORDS_PUSHBUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.ACCESS_RECORDS_PUSHBUTTON.setGeometry(QtCore.QRect(810, 440, 241, 41))
        self.ACCESS_RECORDS_PUSHBUTTON.setStyleSheet("font: 20pt \"Agency FB\";\n"
"")
        self.ACCESS_RECORDS_PUSHBUTTON.setObjectName("ACCESS_RECORDS_PUSHBUTTON")
        self.ACCESS_RECORDS_PUSHBUTTON.clicked.connect(self.ok)
        self.ADD_IMAGE_PUSHBUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.ADD_IMAGE_PUSHBUTTON.setGeometry(QtCore.QRect(810, 490, 241, 41))
        self.ADD_IMAGE_PUSHBUTTON.setStyleSheet("font: 20pt \"Agency FB\";\n"
"")
        self.ADD_IMAGE_PUSHBUTTON.setObjectName("ADD_IMAGE_PUSHBUTTON")
        self.ADD_IMAGE_PUSHBUTTON.clicked.connect(self.ok2)
        self.EXIT_PUSHBUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.EXIT_PUSHBUTTON.setGeometry(QtCore.QRect(810, 540, 241, 41))
        self.EXIT_PUSHBUTTON.setStyleSheet("font: 20pt \"Agency FB\";\n"
"")
        self.EXIT_PUSHBUTTON.setObjectName("EXIT_PUSHBUTTON")
        self.EXIT_PUSHBUTTON.clicked.connect(self.exit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(610, 90, 651, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("VoziloLogo.png"))
        self.label.setObjectName("label")
        SUCCESSFUL_LOGIN.setCentralWidget(self.centralwidget)

        self.retranslateUi(SUCCESSFUL_LOGIN)
        QtCore.QMetaObject.connectSlotsByName(SUCCESSFUL_LOGIN)

    def retranslateUi(self, SUCCESSFUL_LOGIN):
        _translate = QtCore.QCoreApplication.translate
        SUCCESSFUL_LOGIN.setWindowTitle(_translate("SUCCESSFUL_LOGIN", "MainWindow"))
        self.ACCESS_RECORDS_PUSHBUTTON.setText(_translate("SUCCESSFUL_LOGIN", "ACCESS RECORDS"))
        self.ADD_IMAGE_PUSHBUTTON.setText(_translate("SUCCESSFUL_LOGIN", "ADD IMAGE"))
        self.EXIT_PUSHBUTTON.setText(_translate("SUCCESSFUL_LOGIN", "EXIT"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SUCCESSFUL_LOGIN = QtWidgets.QMainWindow()
    ui = Ui_SUCCESSFUL_LOGIN1()
    ui.setup(SUCCESSFUL_LOGIN)
    SUCCESSFUL_LOGIN.show()
    sys.exit(app.exec_())

