# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LOGIN_PAGE.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from CREATE_NEW_ACCOUNT import *
from SUCCESSFUL_LOGIN import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import ctypes 
import socket
import requests


class Ui_MainWindow(object):
        
    def is_connected(self):
        try:
            # connect to the host -- tells us if the host is actually
            # reachable
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False
            
    def ok(self):
        if (self.is_connected()):
            pass
        else:
            ctypes.windll.user32.MessageBoxW(0, "Please connect to internet! ", "NO INTERNET", 0)
            sys.exit()
        hasaccount=False
        Usernamel=self.USERNAME_LINE_EDIT.text()
        Passwordl=self.PASSWORD_LINE_EDIT.text()
        print(Usernamel)
        print(Passwordl)
        if(Usernamel is None or Passwordl is None):
            ctypes.windll.user32.MessageBoxW(0, "USERNAME AND PASSWORD CAN'T BE EMPTY", "SOMETHING WENT WRONG", 0)
            while(Usernamel is not None and Passwordl is not None):
                ctypes.windll.user32.MessageBoxW(0, "USERNAME AND PASSWORD CAN'T BE EMPTY", "SOMETHING WENT WRONG", 0)
                if(Usernamel is not None and  Passwordl is not None):
                    break
           
        else:
            conn = pyodbc.connect(DRIVER='{SQL Server}', Server='LAPTOP-MC1OQKMI\MSSQLSERVER01', Database='VOZILO_DB', Username='a', Password='123')
            cur = conn.cursor()
            cur.execute('SELECT * FROM  VOZILO_DB.dbo.LOGIN')
            for row in cur:
                if(row.USERNAME == Usernamel and row.PASSWORD == Passwordl):
                    print("Login Successful!")
                    hasaccount=True
            cur.close()
            conn.close()
            if(hasaccount == True):
                self.window=QtWidgets.QMainWindow()
                self.ui=Ui_SUCCESSFUL_LOGIN1()
                self.ui.setup(self.window)
                self.window.show()
            if(hasaccount == False):
                print("No way")
                ctypes.windll.user32.MessageBoxW(0, "USERNAME OR PASSWORD IS INCORRECT", "SOMETHING WENT WRONG", 0)
            
                
                
            






    def ok2(self):
        if (self.is_connected()):
            pass
        else:
            ctypes.windll.user32.MessageBoxW(0, "Please connect to internet! ", "NO INTERNET", 0)
            sys.exit()
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_CREATE_NEW_ACCOUNT1()
        self.ui.setup(self.window)
        self.window.show()

                
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1280)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1280))
        font = QtGui.QFont()
        font.setPointSize(18)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 350, 131, 41))
        self.label.setStyleSheet("font: 20pt \"Agency FB\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.USERNAME_LINE_EDIT = QtWidgets.QLineEdit(self.centralwidget)
        self.USERNAME_LINE_EDIT.setGeometry(QtCore.QRect(790, 350, 281, 41))
        self.USERNAME_LINE_EDIT.setStyleSheet("font: 20pt \"Agency FB\";")
        self.USERNAME_LINE_EDIT.setText("")
        self.USERNAME_LINE_EDIT.setObjectName("USERNAME_LINE_EDIT")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(650, 400, 131, 41))
        self.label_2.setStyleSheet("font: 20pt \"Agency FB\";")
        self.label_2.setObjectName("label_2")
        self.PASSWORD_LINE_EDIT = QtWidgets.QLineEdit(self.centralwidget)
        self.PASSWORD_LINE_EDIT.setGeometry(QtCore.QRect(790, 400, 281, 41))
        self.PASSWORD_LINE_EDIT.setStyleSheet("font: 20pt \"Agency FB\";")
        self.PASSWORD_LINE_EDIT.setText("")
        self.PASSWORD_LINE_EDIT.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PASSWORD_LINE_EDIT.setObjectName("PASSWORD_LINE_EDIT")
        self.LOGIN_PUSH_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.LOGIN_PUSH_BUTTON.setGeometry(QtCore.QRect(822, 450, 241, 41))
        self.LOGIN_PUSH_BUTTON.setStyleSheet("font: 20pt \"Agency FB\";\n"
"\n"
"")
        self.LOGIN_PUSH_BUTTON.setObjectName("LOGIN_PUSH_BUTTON")
        self.LOGIN_PUSH_BUTTON.clicked.connect(self.ok)
        self.CREATE_NEW_ACCOUNT_PUSH_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.CREATE_NEW_ACCOUNT_PUSH_BUTTON.setGeometry(QtCore.QRect(820, 500, 241, 41))
        self.CREATE_NEW_ACCOUNT_PUSH_BUTTON.setStyleSheet("font: 20pt \"Agency FB\";\n"
"")
        self.CREATE_NEW_ACCOUNT_PUSH_BUTTON.setObjectName("CREATE_NEW_ACCOUNT_PUSH_BUTTON")
        self.CREATE_NEW_ACCOUNT_PUSH_BUTTON.clicked.connect(self.ok2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 70, 801, 231))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("VoziloLogo.png"))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">USERNAME</span></p><p align=\"center\"><br/></p></body></html>"))
        self.USERNAME_LINE_EDIT.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">ddfgdgdfgddg</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">PASSWORD</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.PASSWORD_LINE_EDIT.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">ddfgdgdfgddg</span></p></body></html>"))
        self.LOGIN_PUSH_BUTTON.setText(_translate("MainWindow", "LOGIN"))
        self.CREATE_NEW_ACCOUNT_PUSH_BUTTON.setText(_translate("MainWindow", "CREATE NEW ACCOUNT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

