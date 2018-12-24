class Database:
    def createaccount(self,Username,Password,AdminPassword):
        hasuser=False
        conn = pyodbc.connect(DRIVER='{SQL Server}', Server='DESKTOP-OVOOI09', Database='VOZILO_DB', Username='sa', Password='123')
        cur = conn.cursor()
        cur.execute('SELECT * FROM  VOZILO_DB.dbo.LOGIN')
        for row in cur:
            if(row.USERNAME == Usernamec):
                hasuser-=True;
                print("In Login")
        if(hasuser == False):        
            db_cd1="INSERT INTO VOZILO_DB.dbo.LOGIN VALUES ('"+Usernamec+"','"+Passwordc+"',0)"
            cur.execute(db_cd1)
            conn.commit()
        cur.close()
        conn.close()
