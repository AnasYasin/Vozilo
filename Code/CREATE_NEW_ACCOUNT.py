# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CREATE_NEW_ACCOUNT.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import ctypes 
import tkinter as tk

root = tk.Tk()
root.withdraw()

class Ui_CREATE_NEW_ACCOUNT1(object):
    def ok(self):
        hasaccount=False
        Usernamel=self.USERNAMEC_LINE_EDIT.text()
        Passwordl=self.PASSWORDC_LINE_EDIT.text()
        AdminPassword="KT91aa"
        AdminPasswordl=self.ADMIN_PASSWORD_LINE_EDIT.text()
        print(Usernamel)
        print(Passwordl)
        print(AdminPasswordl)
        conn = pyodbc.connect(DRIVER='{SQL Server}', Server='LAPTOP-MC1OQKMI\MSSQLSERVER01', Database='VOZILO_DB', Username='a', Password='123')
        cur = conn.cursor()
        cur.execute('SELECT * FROM  VOZILO_DB.dbo.LOGIN')
        while(Usernamel == None or Passwordl == None):
            ctypes.windll.user32.MessageBoxW(0, "USERNAME OR PASSWORD CAN'T BE NULL", "SOMETHING WENT WRONG", 0)
            break
            






        
        for row in cur:
            if(row.USERNAME == Usernamel or row.PASSWORD == Passwordl):
                print("Username or Password already occupied")
                ctypes.windll.user32.MessageBoxW(0, "USERNAME OR PASSWORD ALREADY OCCUPIED", "SOMETHING WENT WRONG", 0)
                hasaccount=True

        while(hasaccount!=True):
            if(hasaccount == False and AdminPasswordl == "KT91aa"):
                db_cd33="INSERT INTO VOZILO_DB.dbo.LOGIN VALUES ('"+Usernamel+"','"+Passwordl+"',0)"
                cur.execute(db_cd33)
                conn.commit()
                cur.close()
                conn.close()
                hasaccount=True
                ctypes.windll.user32.MessageBoxW(0, "Account created successfully", "Welcome", 0)
                root.destroy()
                
            else:
                print("Admin Password not correct")
                ctypes.windll.user32.MessageBoxW(0, "YOU ARE NOT AN ADMIN", "SOMETHING WENT WRONG", 0)
                break
                
            
        
        
        
    def setup(self, CREATE_NEW_ACCOUNT):
        CREATE_NEW_ACCOUNT.setObjectName("CREATE_NEW_ACCOUNT")
        CREATE_NEW_ACCOUNT.resize(1920, 1280)
        CREATE_NEW_ACCOUNT.setMinimumSize(QtCore.QSize(1920, 1280))
        CREATE_NEW_ACCOUNT.setStyleSheet("background-image: url(:/newPrefix/Speedhunters_IATS_Supra_F-_gM4aQ.jpg);")
        self.centralwidget = QtWidgets.QWidget(CREATE_NEW_ACCOUNT)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(610, 490, 201, 41))
        self.label.setStyleSheet("font: 20pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 590, 201, 41))
        self.label_2.setStyleSheet("font: 20pt \"Agency FB\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(610, 540, 201, 41))
        self.label_3.setStyleSheet("font: 20pt \"Agency FB\";")
        self.label_3.setObjectName("label_3")
        self.USERNAMEC_LINE_EDIT = QtWidgets.QLineEdit(self.centralwidget)
        self.USERNAMEC_LINE_EDIT.setGeometry(QtCore.QRect(860, 490, 281, 41))
        self.USERNAMEC_LINE_EDIT.setMaximumSize(QtCore.QSize(281, 41))
        self.USERNAMEC_LINE_EDIT.setStyleSheet("font: 20pt \"Agency FB\";")
        self.USERNAMEC_LINE_EDIT.setText("")
        self.USERNAMEC_LINE_EDIT.setMaxLength(8)
        self.USERNAMEC_LINE_EDIT.setObjectName("USERNAMEC_LINE_EDIT")
        self.PASSWORDC_LINE_EDIT = QtWidgets.QLineEdit(self.centralwidget)
        self.PASSWORDC_LINE_EDIT.setGeometry(QtCore.QRect(860, 540, 281, 41))
        self.PASSWORDC_LINE_EDIT.setStyleSheet("font: 20pt \"Agency FB\";")
        self.PASSWORDC_LINE_EDIT.setText("")
        self.PASSWORDC_LINE_EDIT.setMaxLength(10)
        self.PASSWORDC_LINE_EDIT.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PASSWORDC_LINE_EDIT.setObjectName("PASSWORDC_LINE_EDIT")
        self.ADMIN_PASSWORD_LINE_EDIT = QtWidgets.QLineEdit(self.centralwidget)
        self.ADMIN_PASSWORD_LINE_EDIT.setGeometry(QtCore.QRect(860, 590, 281, 41))
        self.ADMIN_PASSWORD_LINE_EDIT.setStyleSheet("font: 20pt \"Agency FB\";")
        self.ADMIN_PASSWORD_LINE_EDIT.setText("")
        self.ADMIN_PASSWORD_LINE_EDIT.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ADMIN_PASSWORD_LINE_EDIT.setObjectName("ADMIN_PASSWORD_LINE_EDIT")
        self.CREATE_ACCOUNTC_PUSH_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.CREATE_ACCOUNTC_PUSH_BUTTON.setGeometry(QtCore.QRect(900, 650, 241, 41))
        self.CREATE_ACCOUNTC_PUSH_BUTTON.setStyleSheet("font: 20pt \"Agency FB\";\n"
"")
        self.CREATE_ACCOUNTC_PUSH_BUTTON.setObjectName("CREATE_ACCOUNTC_PUSH_BUTTON")
        self.CREATE_ACCOUNTC_PUSH_BUTTON.clicked.connect(self.ok)
        #self.CANCEL_PUSH_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        #self.CANCEL_PUSH_BUTTON.setGeometry(QtCore.QRect(900, 710, 241, 41))
        #self.CANCEL_PUSH_BUTTON.setStyleSheet("font: 20pt \"Agency FB\";\n"
#"")
        #self.CANCEL_PUSH_BUTTON.setObjectName("CANCEL_PUSH_BUTTON")
        #self.CANCEL_PUSH_BUTTON.clicked.connect(self.bnd)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(770, 400, 231, 41))
        self.label_4.setStyleSheet("font: 20pt \"Agency FB\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 120, 651, 261))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("VoziloLogo.png"))
        self.label_5.setObjectName("label_5")
        CREATE_NEW_ACCOUNT.setCentralWidget(self.centralwidget)

        self.retranslateUi(CREATE_NEW_ACCOUNT)
        QtCore.QMetaObject.connectSlotsByName(CREATE_NEW_ACCOUNT)

    def retranslateUi(self, CREATE_NEW_ACCOUNT):
        _translate = QtCore.QCoreApplication.translate
        CREATE_NEW_ACCOUNT.setWindowTitle(_translate("CREATE_NEW_ACCOUNT", "MainWindow"))
        self.label.setText(_translate("CREATE_NEW_ACCOUNT", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">USERNAME</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("CREATE_NEW_ACCOUNT", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">ADMIN PASSWORD</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("CREATE_NEW_ACCOUNT", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">PASSWORD</span></p><p align=\"center\"><span style=\" color:#ffffff;\"><br/></span></p></body></html>"))
        self.USERNAMEC_LINE_EDIT.setToolTip(_translate("CREATE_NEW_ACCOUNT", "<html><head/><body><p><span style=\" color:#ffffff;\">ddfgdgdfgddg</span></p></body></html>"))
        self.PASSWORDC_LINE_EDIT.setToolTip(_translate("CREATE_NEW_ACCOUNT", "<html><head/><body><p><span style=\" color:#ffffff;\">ddfgdgdfgddg</span></p></body></html>"))
        self.ADMIN_PASSWORD_LINE_EDIT.setToolTip(_translate("CREATE_NEW_ACCOUNT", "<html><head/><body><p><span style=\" color:#ffffff;\">ddfgdgdfgddg</span></p></body></html>"))
        self.CREATE_ACCOUNTC_PUSH_BUTTON.setToolTip(_translate("CREATE_NEW_ACCOUNT", "<html><head/><body><p><span style=\" color:#ffffff;\">LOGINDFDDDFGDFVRFER</span></p></body></html>"))
        self.CREATE_ACCOUNTC_PUSH_BUTTON.setText(_translate("CREATE_NEW_ACCOUNT", "CREATE ACCOUNT"))
        #self.CANCEL_PUSH_BUTTON.setText(_translate("CREATE_NEW_ACCOUNT", "CANCEL"))
        self.label_4.setText(_translate("CREATE_NEW_ACCOUNT", "<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">CREATE NEW ACCOUNT</span></p><p align=\"center\"><br/></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CREATE_NEW_ACCOUNT = QtWidgets.QMainWindow()
    ui = Ui_CREATE_NEW_ACCOUNT1()
    ui.setup(CREATE_NEW_ACCOUNT)
    CREATE_NEW_ACCOUNT.show()
    sys.exit(app.exec_())

