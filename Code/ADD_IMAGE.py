import pyodbc
import cv2
import time
import pytesseract
import IPython.display
import numpy as np
import string
import re
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageFilter
from PyQt5 import QtCore, QtGui, QtWidgets
from WebScarping import Get_Data
from OCR import Recognise
from Webcam import Camera

obj=Get_Data()   #fetch
text=Recognise() #OCR

class Ui_MainWindow1(object):
    #CarID = -1
    #def __init__ (self):
    #   CarID = CarID + 1

    def insertData(self, data):
        #CPLC UNCLEAR P YE CODE CHALY GA "RETURN NONE" TK CHALY GA ISS KO COMMENT MEIN REHNY DENA
        if(data.regno == 'AFR'):
            print("AFR wali gari hy")
            conn = pyodbc.connect(DRIVER='{SQL Server}', Server='LAPTOP-MC1OQKMI\MSSQLSERVER01', Database='VOZILO_DB', Username='a', Password='123')
            cur = conn.cursor()
            cur.execute('SELECT count(*) FROM  VOZILO_DB.dbo.AFR')
            row = cur.fetchone()
            value = row[0]
            value = value + 1
            final = str(value)
            print(final)
            a = "INSERT INTO VOZILO_DB.dbo.AFR VALUES('"+final+"',SYSDATETIME(),CONVERT(TIME,SYSDATETIME()))"
            cur.execute(a)
            conn.commit()
            cur.close()
            conn.close()
            return None

        
        if(data.CPLC == 'Vehicle is not Clear'):
            print("CPLC clear nahi hy")
            conn = pyodbc.connect(DRIVER='{SQL Server}', Server='LAPTOP-MC1OQKMI\MSSQLSERVER01', Database='VOZILO_DB', Username='a', Password='123')
            cur = conn.cursor()
            dregno = data.regno
            #dname = data.owner
            a = "INSERT INTO VOZILO_DB.dbo.CPLC_UNCLEAR VALUES('"+dregno+"','NA',SYSDATETIME(),CONVERT(TIME,SYSDATETIME()))"
            cur.execute(a)
            conn.commit()
            cur.close()
            conn.close()
            return None

        #AFR P YE CODE CHALY GA "RETURN NONE" TK CHALY GA 
            
        

        exists = False
        conn = pyodbc.connect(DRIVER='{SQL Server}', Server='LAPTOP-MC1OQKMI\MSSQLSERVER01', Database='VOZILO_DB', Username='a', Password='123')
        cur = conn.cursor()
        cur.execute('SELECT REGNO FROM  VOZILO_DB.dbo.VEHICLE')
        for row in cur:
           if(row.REGNO == data.regno):
              print("car exists")
              exists = True
        cur.close()
        conn.close()

        if(exists == True and data.region == "Sindh"):
           conn = pyodbc.connect(DRIVER='{SQL Server}', Server='LAPTOP-MC1OQKMI\MSSQLSERVER01', Database='VOZILO_DB', Username='a', Password='123')
           cur = conn.cursor()
           cur.execute('SELECT * FROM  VOZILO_DB.dbo.FREQUENCY')
           inserted = False
           for row in cur:
              if(row.REG_NO == data.regno and row.Exit_Time is None):
                  print("yahan tk aaya hy")
                  #cur.execute("UPDATE VOZILO_DB.dbo.FREQUENCY SET Exit_Time = CONVERT(TIME,SYSDATETIME())  WHERE Enter_Time = (?) AND REG_NO = (?)", (row.Enter_Time,row.REG_NO))
                  cur.execute("UPDATE VOZILO_DB.dbo.FREQUENCY SET Exit_Time = CONVERT(TIME,SYSDATETIME())  WHERE Enter_Time = (?) AND REG_NO = (?)", (row.Enter_Time,row.REG_NO))
                  conn.commit()
                  inserted = True
                  break
                  
           cur.close()
           conn.close()

           if(inserted == False):
               conn = pyodbc.connect(DRIVER='{SQL Server}', Server='LAPTOP-MC1OQKMI\MSSQLSERVER01', Database='VOZILO_DB', Username='a', Password='123')
               cur = conn.cursor()
               dregno2 = data.regno
               b = "INSERT INTO VOZILO_DB.dbo.FREQUENCY(REG_NO,Enter_Time,Current_Date_) VALUES('"+dregno2+"',CONVERT(TIME,SYSDATETIME()),SYSDATETIME())"
               cur.execute(b)
               conn.commit()
               cur.close()
               conn.close()
               
           
           print("car exists")

        elif(data.region == "Sindh"):
            print("this is your data")
            print(data.TaxDate)
            print(data.Safe)
            print(data.body)
            print(data.owner)
            print(data.year)
            print(data.CPLC)
            print(data.seating)
            print(data.cov)
            print(data.power)
            print(data.remarks)
            print(data.region)
            print(data.regno)
            print(data.make)
            print(data.regdate)
            print(data.engineno)
            print(data.Vtype)
            dTaxDate=data.TaxDate
            dSafe=data.Safe
            dbody=data.body
            downer=data.owner
            dyear=data.year
            dCPLC=data.CPLC
            dseating=data.seating
            dcov=data.cov
            dpower=data.power
            dremarks=data.remarks
            dregion=data.region
            dregno=data.regno
            dmake=data.make
            dregdate=data.regdate
            dengineno=data.engineno
            dvtype=str(data.Vtype)
            print("car does not exist")
            conn = pyodbc.connect(DRIVER='{SQL Server}', Server='LAPTOP-MC1OQKMI\MSSQLSERVER01', Database='VOZILO_DB', Username='a', Password='123')
            cur = conn.cursor()
            #a = "INSERT INTO VOZILO_DB.dbo.VEHICLE VALUES('"+dregno+"','"+dvtype+"', '"+dmake+"','"+dregdate+"','"+dengineno+"','"+dTaxDate+"','"+dSafe+"','"+dbody+"','"+downer+"','"+dyear+"','"+dCPLC+"','"+dseating+"','"+dcov+"','"+dpower+"','"+dremarks+"','NA','NA','NA','"+dregion+"')"
            b = "INSERT INTO VOZILO_DB.dbo.FREQUENCY(REG_NO,Enter_Time,Current_Date_) VALUES('"+dregno+"',CONVERT(TIME,SYSDATETIME()),SYSDATETIME())"
            hy = "INSERT INTO VOZILO_DB.dbo.VEHICLE VALUES('"+dregno+"', '"+dvtype+"', '"+dmake+"','"+dregdate+"','"+dengineno+"','"+dTaxDate+"','"+dSafe+"','"+dbody+"','"+downer+"','"+dyear+"','"+dCPLC+"','"+dseating+"','"+dcov+"','"+dpower+"','"+dremarks+"','NA','NA','NA','"+dregion+"')"
            cur.execute(hy)
            cur.execute(b)
            conn.commit()
            cur.close()
            conn.close()



        #YE KPK KI GAAARI K LIYE CHALY GA ISS MEIN KISI QUERY KO NHI CHERNA


        elif(exists == True and data.region == 'KPK'):
            print("successfully detected region")
            conn = pyodbc.connect(DRIVER='{SQL Server}', Server='LAPTOP-MC1OQKMI\MSSQLSERVER01', Database='VOZILO_DB', Username='a', Password='123')
            cur = conn.cursor()
            cur.execute('SELECT * FROM  VOZILO_DB.dbo.FREQUENCY')
            inserted = False
            for row in cur:
                
                if(row.REG_NO == data.regno and row.Exit_Time is None):
                    
                    print("yahan tk aaya hy")
                    #cur.execute("UPDATE VOZILO_DB.dbo.FREQUENCY SET Exit_Time = CONVERT(TIME,SYSDATETIME())  WHERE Enter_Time = (?) AND REG_NO = (?)", (row.Enter_Time,row.REG_NO))
                    cur.execute("UPDATE VOZILO_DB.dbo.FREQUENCY SET Exit_Time = CONVERT(TIME,SYSDATETIME())  WHERE Enter_Time = (?) AND REG_NO = (?)", (row.Enter_Time,row.REG_NO))
                    conn.commit()
                    inserted = True
                    break
                  
            cur.close()
            conn.close()

            if(inserted == False):
                
                conn = pyodbc.connect(DRIVER='{SQL Server}', Server='LAPTOP-MC1OQKMI\MSSQLSERVER01', Database='VOZILO_DB', Username='a', Password='123')
                cur = conn.cursor()
                dregno2 = data.regno
                b = "INSERT INTO VOZILO_DB.dbo.FREQUENCY(REG_NO,Enter_Time,Current_Date_) VALUES('"+dregno2+"',CONVERT(TIME,SYSDATETIME()),SYSDATETIME())"
                cur.execute(b)
                conn.commit()
                cur.close()
                conn.close()
               
           
            print("car exists")

        elif(data.region == 'KPK'):
            print("KPK object has been created")
            print("this is your data")
            print(data.regno)
            print(data.make)
            print(data.regdate)
            print(data.engineno)
            print(data.chasisno)
            print(data.owner)
            print(data.father)
            print(data.color)
            print(data.CPLC)
            print(data.Safe)
            print(data.body)
            print(data.seating)
            print(data.remarks)
            print(data.region)

            dSafe=data.Safe

            dbody=data.body

            downer=data.owner

            dCPLC=data.CPLC

            dseating=data.seating
            dremarks=data.remarks
            dregion=data.region

            dregno=data.regno

            dmake=data.make

            dregdate=data.regdate

            dengineno=data.engineno
            dchasisno=data.chasisno
            dfather=data.father
            dcolor=data.color
            #dvtype=str(data.Vtype)
            print("car does not exist")
            conn = pyodbc.connect(DRIVER='{SQL Server}', Server='LAPTOP-MC1OQKMI\MSSQLSERVER01', Database='VOZILO_DB', Username='a', Password='123')
            cur = conn.cursor()
            print("yahan tk aya hy KPK")
            #a = "INSERT INTO VOZILO_DB.dbo.VEHICLE VALUES('"+dregno+"','"+dvtype+"', '"+dmake+"','"+dregdate+"','"+dengineno+"','"+dTaxDate+"','"+dSafe+"','"+dbody+"','"+downer+"','"+dyear+"','"+dCPLC+"','"+dseating+"','"+dcov+"','"+dpower+"','"+dremarks+"','NA','NA','NA','"+dregion+"')"
            b = "INSERT INTO VOZILO_DB.dbo.FREQUENCY(REG_NO,Enter_Time,Current_Date_) VALUES('"+dregno+"',CONVERT(TIME,SYSDATETIME()),SYSDATETIME())"
            hy = "INSERT INTO VOZILO_DB.dbo.VEHICLE(REGNO,TOV,MAKE,REGDATE,ENGINENO,TAXDATE,SAFE,BODY_,OWNER,YEAR_,CPLC,CLASSOFVEHICLE,POWER_,REMARKS,CHASIS_NO,FATHER,COLOR,REGION) VALUES('"+dregno+"', '1', '"+dmake+"', '"+dregdate+"', '"+dengineno+"', 'NA', '"+dSafe+"', '"+dbody+"', '"+downer+"', 'NA', '"+dCPLC+"', 'NA', 'NA', '"+dremarks+"', '"+dchasisno+"' , '"+dfather+"', '"+dcolor+"', '"+dregion+"')"
            
            
            cur.execute(hy)
            cur.execute(b)
            conn.commit()
            cur.close()
            conn.close()

            



    def ad_im_file(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        regNo=text.imageToString(file_path)
        data=obj.Identify(regNo) #Fetching
        self.insertData(data)     

        

    
    def ok(self):
        camm=Camera()   #camera
        camm.captureImage('1')
        print('here')
    #   regNo=text.imageToString('1')          #OC
    #   data=obj.Identify(regNo)               #Fetching
    #   self.insertData(data)     

    
              
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1280)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1280))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ADD_IMAGE_FILE_PUSHBUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.ADD_IMAGE_FILE_PUSHBUTTON.setGeometry(QtCore.QRect(790, 400, 221, 49))
        self.ADD_IMAGE_FILE_PUSHBUTTON.setStyleSheet("font: 20pt \"Agency FB\";\n"
"")
        self.ADD_IMAGE_FILE_PUSHBUTTON.setObjectName("ADD_IMAGE_FILE_PUSHBUTTON")
        self.ADD_IMAGE_FILE_PUSHBUTTON.clicked.connect(self.ad_im_file)
        self.USE_WEB_CAM_PUSHBUTTON = QtWidgets.QPushButton(self.centralwidget)
        self.USE_WEB_CAM_PUSHBUTTON.setGeometry(QtCore.QRect(790, 500, 221, 49))
        self.USE_WEB_CAM_PUSHBUTTON.setStyleSheet("font: 20pt \"Agency FB\";\n"
";")
        self.USE_WEB_CAM_PUSHBUTTON.setObjectName("USE_WEB_CAM_PUSHBUTTON")
        self.USE_WEB_CAM_PUSHBUTTON.clicked.connect(self.ok)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 100, 601, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("VoziloLogo.png"))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ADD_IMAGE_FILE_PUSHBUTTON.setText(_translate("MainWindow", "ADD IMAGE FILE"))
        self.USE_WEB_CAM_PUSHBUTTON.setText(_translate("MainWindow", "USE WEB-CAM"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

