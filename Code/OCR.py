from PIL import Image, ImageFilter
import pytesseract
import IPython.display
import numpy as np
import string
import re


class Recognise:
    nameID=-1
    def __init__ (self):
        Recognise.nameID+=1

    def imageToString(self, name):
        Recognise.nameID+=1
       # name+='.jpg'
        im=Image.open(name)

        w, h = im.size
        #print (w,h)  
        #size = 250, 130    
        #im = im.resize(size, Image.ANTIALIAS)

        
        #im.save(str(Recognise.nameID)+'.png') 

        text=pytesseract.image_to_string(im, lang = 'eng')
        temp2=text
        
        
        print('text:',text)

        text=re.sub('[^A-Za-z0-9]+', '', text)
        text.upper()
        #print(text)
        #i=0
        #temp =0
        #while i<len(text):
        #   if(temp>)




        i=len(text)-1
        while i >= 0:
            if (text[i].isalpha()):
                i-=1
            else:
                break

        text=text[0:i+1]
        #print(text)
        i=len(text)-1
        while i >= 0:
            if (text[i].isdigit()):
                i-=1
            else:
                break

        text=text[0:i+1] + '-' + text[i+1:len(text)]

        text=text.upper()
        if(temp2=='AFR'):
            return temp2
        else:
            return text


