import requests
import os
import traceback
from progress.bar import ChargingBar
idSound="2217805877"
ignor=0
donload=1
print("roblox_donloadMusic by maxsspeaker")
idSound=str(input("idsound: "))
try:
      print("скачиваем html")
      r = requests.get("https://www.roblox.com/library/"+idSound+"/", stream=True)
      i=0
      print("скачиваем html")
      with open("Treak.html", 'wb') as f:
            for block in r.iter_content(1024):
                 f.write(block)
                 i+=1
                 if i <= 100:
                       pass
                       # titleTreak.config(text=("загрузка трека"))
      print("html ok")
      file_name = "Treak.html"
        
      f = open(file_name, 'r')
      if f.name == file_name:
            for i in f:
                try:
                    if(ignor==0):
                          filter3=i.split('<h2>')[1]
                          filter5=filter3.split('</h2>')[0]
                          trekName=filter5
                          print(trekName)
                          #print(filter5)
                          ignor=1
                          print("ok_getTrekName")
                except:
                    pass
                try:
                   if not("(Removed for copyright)"==trekName):
                    filter1=i.split('data-mediathumb-url="')[1]
                    print("ok_getTrekUrl")
                    print("ok_all")
                except:
                    pass
            f.close()
      if not("(Removed for copyright)"==trekName):
            try: trekUrl=filter1.split('">')[0]; donload=0
            except: print("не удалось скачать трек")
      if (donload==0):
         
         print(" ")
         print(trekUrl)
         print("скачиваем Трек")
         bar = ChargingBar(' Loadig_Trek', suffix='%(index)d')
         r = requests.get(trekUrl, stream=True)
         i=0
         with open(trekName+".mp3", 'wb') as f:
               for block in r.iter_content(1024):
                   f.write(block)
                   i+=1
                   if i <= 100:
                       # titleTreak.config(text=("загрузка трека"))
                        #print("скачиваем:",i, end='%\n')
                        bar.goto(i)
         bar.finish()
         print("сохраненно как: "+trekName+".mp3")
      if("(Removed for copyright)"==trekName):
            print("Ошибка! Данный трек удалённ иза нарушения авторских прав")
except:
       print('Erorr code:\n', traceback.format_exc())
       str(input(""))

#data-mediathumb-url="
str(input(""))
