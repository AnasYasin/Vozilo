from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
import ctypes 
import time 

class Ui_MainWindow2(object):
    def load_data(self):
        
        if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
            temp=0
            checked = False 
            conn =pyodbc.connect(DRIVER='{SQL Server}', Server='LAPTOP-MC1OQKMI\MSSQLSERVER01', Database='VOZILO_DB', Username='a', Password='123')
            cur = conn.cursor()

                
            sql1='''
            create or alter procedure record_Vehicle
                @regno nvarchar(20)
            as
            Begin
                select * from VOZILO_DB.dbo.VEHICLE as V,VOZILO_DB.dbo.FREQUENCY as F where (V.REGNO  = F.REG_NO) and (V.REGNO = @regno);
            end;
            '''
            sql2='''
            create procedure GetList
                @TOV nvarchar (4)
            AS
            BEGIN
                select Reg_no,count(reg_no) FROM VOZILO_DB.dbo.frequency,VOZILO_DB.dbo.Vehicle WHERE VOZILO_DB.dbo.frequency.REG_NO=VOZILO_DB.dbo.VEHICLE.REGNO and VOZILO_DB.dbo.VEHICLE.TOV=@TOV  group by (reg_no) order by (count(reg_no)) desc;
            END;
            '''
            sql3='''
            Create or Alter procedure C_Unclear
            AS
            BEGIN
                select * from VOZILO_DB.dbo.CPLC_UNCLEAR;    
            END;
            '''
            sql4='''
            create procedure GetInVehicles
                @TOV nvarchar(4)
            AS
            BEGIN
                select * FROM VOZILO_DB.dbo.frequency,VOZILO_DB.dbo.VEHICLE WHERE VOZILO_DB.dbo.frequency.REG_NO=VOZILO_DB.dbo.VEHICLE.REGNO and
                VOZILO_DB.dbo.frequency.Exit_Time is NULL and VOZILO_DB.dbo.VEHICLE.TOV=@TOV;
            END;	
            '''
            sql5='''
            create procedure GetAFR
            as
            BEGIN
                select * from VOZILO_DB.dbo.AFR;
            END;
            '''
            sql6='''
            create procedure GetDates
                    @date date,@TOV nvarchar(4)
            as
            BEGIN
                SELECT * FROM VOZILO_DB.dbo.frequency,VOZILO_DB.dbo.VEHICLE WHERE VOZILO_DB.dbo.frequency.REG_NO=VOZILO_DB.dbo.VEHICLE.REGNO and
                VOZILO_DB.dbo.frequency.Current_Date_ = @date and VOZILO_DB.dbo.VEHICLE.TOV=@TOV;
            END;
            '''
        
            cur.execute(sql1)
            cur.execute(sql2)
            cur.execute(sql3)
            cur.execute(sql4)
            cur.execute(sql5)
            cur.execute(sql6)


            #self.storedProc()      
            if(self.radioButton.isChecked()):
                text = self.comboBox_2.currentText()
                if(text == "Records of a vehicle (time, date ... tuples) by registration no."):
                    value = self.lineEdit.text()
                    
                    query = """\
                    EXEC record_Vehicle @regno=?
                    """
                    params = (value)
                    temp=1
                if(text == "Sort by most visited vehicle"):
                    value = self.lineEdit.text()
                    
                    query = """\
                    EXEC GetList @TOV=?
                    """
                    params = ('1')
                    
                    #query = ""
                if(text == "CPLC uncleared vehicle"):
                    value = self.lineEdit.text()
                    
                    query = """\
                    EXEC C_Unclear
                    """
                    params = ('')
                    
                    #query = ""
                if(text == "Present vehicles"):
                    value = self.lineEdit.text()
                
                    query = """\
                    EXEC GetInVehicles @TOV=?
                    """
                    params = ('1')
                    
                    
                if(text == "AFR Cars"):
                    value = self.lineEdit.text()
                    query = """\
                    EXEC GetAFR 
                    """
                    params = ('')

                if(text == "Records by date"):
                    value = self.lineEdit.text()
                    if (value.isalnum() or value==''):
                        params=''
                        temp=1
                    else:            
                        query = """\
                        EXEC GetDates @date=?, @TOV=?
                        """
                        params = (value, '1')
                    
            
            else:
                text = self.comboBox_2.currentText()
                if(text == "Records of a vehicle (time, date ... tuples) by registration no."):
                    value = self.lineEdit.text()
                    query='exec record_Vehicle'+value+';' 
                
                    query = """\
                    EXEC record_Vehicle @regno=?
                    """
                    params = (value)
                    temp=1
                     
                if(text == "Most visited vehicle"):
                    value = self.lineEdit.text()
                    
                    query = """\
                    EXEC GetList @TOV=?
                    """
                    params = ('2')
                if(text == "CPLC uncleared vehicle"):
                    value = self.lineEdit.text()
                
                    query = """\
                    EXEC C_Unclear
                    """
                    params = ('')
                
                if(text == "Present vehicles"):
                    value = self.lineEdit.text()
                    
                    query = """\
                    EXEC GetInVehicles @TOV=?
                    """
                    params = ('2')

                if(text == "AFR Cars"):
                    value = self.lineEdit.text()
                
                    query = """\
                    EXEC GetAFR 
                    """
                    params = ('')
                    
                if(text == "Records by date"):
                    value = self.lineEdit.text()
                    if (value.isalnum() or value==''):
                        params=''
                        temp=1
                    else:            
                        query = """\
                        EXEC GetDates @date=?, @TOV=?
                        """
                        params = (value, '2')
                        
                        

            if  (params=='' and temp==1):
                ctypes.windll.user32.MessageBoxW(0, "Please give the appropriate information in the text box. ", "Insufficient Information", 0)
                result=''
                
            elif (params=='' and temp==0) :
                result=cur.execute(query)
            
            else:
                result=cur.execute(query, params)
            
            print(result)
            if (result==''):
                ctypes.windll.user32.MessageBoxW(0, '''Make sure that input is in the same form as, "Reg No -> AMT-399"   and   "Date  ->  2018-12-5"''', "No data Found", 0)



            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data))) 
            cur.close()
            conn.close()
        else:
            ctypes.windll.user32.MessageBoxW(0, "Please select atleast one from Car or Bike", "SOMETHING WENT WRONG", 0)
            

            
            






        
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1280)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1280))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(650, 310, 101, 31))
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.radioButton.setAcceptDrops(False)
        self.radioButton.setStyleSheet("color: rgb(0,0,0);\n"
"font: 20pt \"Agency FB\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(930, 310, 95, 31))
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.radioButton_2.setAcceptDrops(False)
        self.radioButton_2.setStyleSheet("color: rgb(255, 255, 25rgb(0, 0, 0)5);\n"
"font: 20pt \"Agency FB\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(460, 400, 651, 51))
        self.comboBox_2.setStyleSheet("font: 20pt \"Agency FB\";\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.CREATE_NEW_ACCOUNT_PUSH_BUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.CREATE_NEW_ACCOUNT_PUSH_BUTTON.setGeometry(QtCore.QRect(1140, 400, 241, 41))
        self.CREATE_NEW_ACCOUNT_PUSH_BUTTON.setStyleSheet("font: 20pt \"Agency FB\";\n"
"color: rgb(0,0,0);")
        self.CREATE_NEW_ACCOUNT_PUSH_BUTTON.setObjectName("CREATE_NEW_ACCOUNT_PUSH_BUTTON")
        self.CREATE_NEW_ACCOUNT_PUSH_BUTTON.clicked.connect(self.load_data)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(340, 520, 1131, 431))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1140, 460, 241, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 20, 641, 231))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 25rgb(0, 0, 0)5);\n"
"font: 20pt \"Agency FB\";")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("VoziloLogo.png"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "CAR"))
        self.radioButton_2.setText(_translate("MainWindow", "BIKE"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Records of a vehicle (time, date ... tuples) by registration no."))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Sort by most visited vehicle"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "CPLC uncleared vehicle"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Present vehicles"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "AFR Cars"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Records by date"))
        self.CREATE_NEW_ACCOUNT_PUSH_BUTTON.setText(_translate("MainWindow", "GET RECORDS"))

#    def storedProc(self):

        


    


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setup(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())

