import requests
import time
from datetime import datetime

url = 'https://egov.presov.sk/geodatakatalog/dpmp.csv'

while True:
    #stiahni subor z webu prešova
    r = requests.get(url, allow_redirects=True)
    r = r.content.decode("ANSI")

    #zmaž nadpis zo stiahnutého csv súboru, znaky pre nový riadok a pridaj medzeru pre lepšiu prehliadnosť ked to bude uložene
    noheading_data = r[r.find('\n')+1:]
    noheading_data = noheading_data.replace("\n","")
    noheading_data += '\n\n'

    #otvor súbor pre zapisovanie a vlož do neho stiahnuté, zeditované dáta a čas kedy to bolo vykonané
    file = open('MHD_Presov.csv', 'a')
    file.write("Datetime: " + str(datetime.now()) + '\n' + noheading_data)
    file.close()

    #len pre prehliadnosť toho či program beži
    print("Datetime: " + str(datetime.now()) + " writting done.")

    #pauza 15 sekúnd kvoli intervalu aktualizovania dát na portály
    time.sleep(15)


#Zoznam výpadkov zberu dat

#Start of the collectin: 11.2.2022 13:27
#14.2 11:05 vypadok
#24.2 14:15 vypadok
#2022-03-06 15:30:08.086432 - 7.3 19:50
#7.3 okolo 21:30 moje saskovanie pre vylepsenie stability
#2022-03-08 15:06:50 - 2022-03-09  16:37:58 vypadok presov mhd serverva
# 2022-03-18 14:50 - 2022-03-20 19:55 vypadok mhd servera
#2022-03-23 14:51 - 2022-03-24 09:04 tuke server down
# 2022-03-31 17:44:55.863667 - 2022-04-05 19:55 - vypadok stranky an too much for  to check
#2022-04-06 15:24:34.495195 - 2022-04-06 20:37 - tuke server down
#Datetime: 2022-04-15 07:53: - 13:38 - webserver down
#Datetime: 2022-04-19 17:33  - 20.4 23:58 - TUKE server down
#Datetime: 2022-04-25 19:44:25.599868 - END #1