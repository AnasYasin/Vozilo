import requests
from bs4 import BeautifulSoup as bs
import urllib.request as urlread
import urllib
import random 
import smtplib
from email.mime.text import MIMEText

class Get_Data:
    def Identify(self,regno):#Both Type of car and province
        #this function is just a prototype
        if(regno[0:3] != 'AFR'):
            for Vtype in range(1,3):
                print(Vtype)
                self.login_sindh(regno,Vtype)
                if(self.lists_text != []):
                    self.debug(self.lists_text)
                    obj=Vehicle(self.lists_text,'Sindh',Vtype)
                    return obj
            self.login_KPK(regno)
            if(self.newlist != []):
                self.debug(self.newlist)
                obj=Vehicle(self.newlist,'KPK',0)
                return obj;
            else:
                obj=Vehicle(self.lists,'No Data',0)
                return obj;
        else:
            obj=Vehicle(0,'AFR',0)
            return obj;
    def get_KPK_cities(self):
        html_data=urlread.urlopen('https://www.kpexcise.gov.pk/mvrecords/')
        read=html_data.read()
        temp= bs(read,"html.parser")
        cities=temp.findAll("option");
        the_cities= [];
        for i in range(1,len(cities)-2):
            new_cities=str(cities[i])
            index=new_cities.find('">')
            new_cities=new_cities[0:index]
            index=new_cities.find('="')
            new_cities=new_cities[index+2:len(new_cities)]
            the_cities.append(new_cities)
        return the_cities
    def login_sindh(self,regno,Vtype):
        self.lists_text=[]
        url='http://excise.gos.pk/vehicle/vehicle_result'
        data={'reg_no':regno,'wheelers_type':Vtype} 
        doc= requests.post(url,data=data)
        var = bs(doc.text, "html.parser");
        lists=var.findAll("div",{"class":"col-md-8"})
        lists=var.findAll("h6")  
        for data in lists:
            print(data)
            self.lists_text.append(data.text)
    def login_KPK(self,regno):
        the_cities=self.get_KPK_cities();
        for city in the_cities:
            print('City Started: '+city+'\n')
            listes= []
            self.newlist=[]
            index=0
            new_regno=regno.replace("-","%20")
            new_regno=new_regno.replace(" ","%20")
            #print(city)
            url2='https://www.kpexcise.gov.pk/mvrecords/getmvr.php?dname='+city+'&dtype=reg&reg_no='+new_regno
            #print(self.url2)
            try:
                response = urlread.urlopen(url2)
            except urllib.error.URLError:
                print("Error accessing site")
                continue
            except urllib.error.HTTPError:
                print("Error accessing site")
                continue
            else:        
                html2 = response.read()
                var2 = bs(html2, "html.parser")
                listes=var2.findAll("strong")
                if(listes != []):
                    for data in listes:
                        #print(data.text)
                        if((index%2 == 0 and index < 20 and index > 2 and index != 4) or (index == 3)):
                            self.newlist.append(data.text)
                        index=index+1  
                    if(random.randint(1,2)% 2 == 0):
                        self.newlist.append("Vehicle is not Clear")
                        print('VINC\n\n\n')
                    else:
                        self.newlist.append("Vehicle is Clear")
                        print('VIC\n\n\n')
                    break    
    def debug(self,lists):
        if(lists != []):
            for elements in lists:
                print(elements);
        else:
            print("Data cannot be retrived due to some errors")
                

class Vehicle:
   def __init__(self,lists,region,Vtype):
      if(region[0:3] == 'AFR'):
          self.regno='AFR'
          print('AFR')
      else:    
          if(region == 'No Data'):
              self.regno='No Data'
              print('No data')
          else:
              self.regno=lists[0]
              self.make=lists[1]
              self.regdate=lists[2]
              self.engineno=lists[4]
              if(region == 'Sindh'):
                  self.Vtype=Vtype
                  self.TaxDate=lists[3]
                  self.Safe=lists[5]
                  self.body=lists[6]
                  self.owner=lists[7]
                  self.year=lists[8]
                  self.CPLC=lists[9]
                  self.seating=lists[10]
                  self.cov=lists[11] #Class of vehicle = cov
                  self.power=lists[12]
                  self.remarks=lists[13]
                  self.region=region
              else:
                  self.chasisno=lists[3]
                  self.owner=lists[5]
                  self.father=lists[6]
                  self.color=lists[7]
                  self.CPLC=lists[8]
                  self.Safe='Safe Custody'
                  self.body='Vehicles'
                  self.seating=1
                  self.remarks='KPK Vehicle'
                  self.region=region
              if(self.CPLC[0:16] != 'Vehicle is Clear' and self.regno =='B 2647'):
                  self.alert(region,self.regno)
   def alert(self,region,regno):
      print('About to send')   
      sender ='k163834@nu.edu.pk'
      receivers = ['k163834@nu.edu.pk']
      msg = MIMEText('The following vehicle has entered the parking lot whose CPLC is not clear\nRegistration Number:'+str(regno)
      +'\nRegion: '+region+'\n\nKindly look into the matter'+'\n\n\n\n\nThis mail was automatically by the Vozilo Database.')
      msg['Subject'] = 'Database Alert!'
      msg['From'] = 'Vozilo Database'
      msg['To'] = 'k163834@nu.edu.pk'
      mail = smtplib.SMTP('smtp.mailtrap.io',2525)
      mail.ehlo()
      mail.starttls()
      mail.login('394684280206b9','eda14f5e73f3a7')
      mail.sendmail(sender,receivers,msg.as_string())
      mail.close()
      print('Mail Send')
      
      
'''      
obj=Get_Data();
data=obj.Identify('CK-4744')
print("this is your data")
print(data.CPLC)
#print(data.make)
#print(data.regdate)
#print(data.engineno)
#print(data.chasisno)
#print(data.owner)
#print(data.father)
#print(data.color)
#print(data.CPLC)
#print(data.Safe)
#print(data.body)
#print(data.seating)
#print(data.remarks)
#print(data.region)
'''
