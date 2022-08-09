import csv
import math
import time
from os import path
import time as t
from os.path import exists

#Rozny formy error ktoré treba odstrániť pred samotným spracovívaním meškani
garbage1 = [
    "<html xmlns=\"http://www.w3.org/1999/xhtml\">",
    "<head>",
    "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=iso-8859-1\"/>",
    "<title>500 - Internal server error.</title>",
    "<style type=\"text/css\">",
    "<!--",
    "body{margin:0;font-size:.7em;font-family:Verdana  Arial  Helvetica  sans-serif;background:#EEEEEE;}",
    "fieldset{padding:0 15px 10px 15px;} ",
    "h1{font-size:2.4em;margin:0;color:#FFF;}",
    "h2{font-size:1.7em;margin:0;color:#CC0000;} ",
    "h3{font-size:1.2em;margin:10px 0 0 0;color:#000000;} ",
    "#header{width:96%;margin:0 0 0 0;padding:6px 2% 6px 2%;font-family:\"trebuchet MS\"  Verdana  sans-serif;color:#FFF;",
    "background-color:#555555;}",
    "#content{margin:0 0 0 2%;position:relative;}",
    ".content-container{background:#FFF;width:96%;margin-top:8px;padding:10px;position:relative;}",
    "-->",
    "</style>",
    "</head>",
    "<body>",
    "<div id=\"header\"><h1>Server Error</h1></div>",
    "<div id=\"content\">",
    " <div class=\"content-container\"><fieldset>",
    "  <h2>500 - Internal server error.</h2>",
    "  <h3>There is a problem with the resource you are looking for  and it cannot be displayed.</h3>",
    " </fieldset></div>",
    "</div>",
    "</body>",
    "</html>",
]
garbage2 = [
    "<HTML><HEAD><TITLE>Service Unavailable</TITLE>",
    "<META HTTP-EQUIV=\"Content-Type\" Content=\"text/html; charset=us-ascii\"></HEAD>",
    "<BODY><h2>Service Unavailable</h2>",
    "<hr><p>HTTP Error 503. The service is unavailable.</p>",
    "</BODY></HTML>",
]
garbage3 = "ROUTE_NUMBER;PLANNED_START;DIRECTION;BUS_STOP_ORDER_NUM;BUS_STOP_NAME_1;BUS_STOP_NUM_1;BUS_STOP_SUB_NUM_1;BUS_STOP_NAME_2;BUS_STOP_NUM_2;BUS_STOP_SUB_NUM_2;PLANNED_ROAD;REAL_ROAD;LATITUDE;LONGITUDE;VARIATION;VEHICLE_NUMBER;DATE_TIME"

#Zákon veľkých čísle - príprava súborov pre vyhodnotenie kvality modelu volá sa nakonci funkcie preprocessing()
def LoLN(delays):
    files = ["1","2","3", "4", "5", "6", "7", "8"]
    file_to_write = None

    #vyber meno súboru ktoré ešte neexistuje
    for i in files:
        if not exists("MHD_Presov_delays"+i+".csv"):
            file_to_write = "MHD_Presov_delays"+i+".csv"
            break

    if file_to_write == None:
        raise ValueError("Run out of names for new files")

    #otvor súbor a zapíš doň meškania získane z funkcie preprocessing
    file = open(file_to_write, "w", newline="")
    csv_writer = csv.writer(file)
    for i in delays:
        # print("\n" + str(i[0]) + ":")
        csv_writer.writerow([])
        csv_writer.writerow([i[0] + ":"])
        for j in i[1]:
            csv_writer.writerow([j])
            # print(j)

#funkcia odstráni niektoré chybné dáta zo súboru a pripravý ho na ďalšie spracovani meškaní
def deleteHTMLerrors():
    #otvor subor so stiahnutými meškaniami a súbor kde sa uloží ich opravená verzia
    file_read = open("MHD_Presov.csv")
    file = open("MHD_Presov_repairedversion.csv", "w", newline="")

    #nahraď čiarky medzermi lebo inač to zle spraví polia pre metóde split() a zapíš takto zmenená dáta do súboru
    text_colons = file_read.read()
    text_colons = text_colons.replace(",", " ")
    file.write(text_colons)
    file_read.close()
    file.close()

    #otvor súbor s upravenými meškaniami, nahraď nulové bajti a priprav pole kde sa uložia neskor len validné dáta bez chýb spomenutých na začiatku programu
    file_read = open("MHD_Presov_repairedversion.csv")
    csvreader = csv.reader(x.replace('\0', '') for x in file_read)
    repaired_data = []

    #prechádzaj dáta a ak sa jedná o jeden z 3 spomenutých chýb na začiatku programu ignoruj ich
    for i in csvreader:
        if not i:
            continue
        elif i[0] not in garbage1 and i[0] not in garbage2 and i[0] != garbage3:
            repaired_data.append(i[0])

    #otvor súbor a zapíš doň upravné dáta bez spomínaných chýb
    file_read.close()
    file = open("MHD_Presov_repairedversion.csv", "w", newline="")
    csv_writer = csv.writer(file)

    for i in repaired_data:
        if (i[0] == "D"):
            csv_writer.writerow([])
        csv_writer.writerow([i])

    file.close()

#zoznam výpadkov použití pri vytváraní intervalov pre vyhodnocovanie kvality modelu pomocou Zákona veľkých čísel
"""
#Start of the collectin: 11.2.2022 13:27
#14.2 11:05 vypadok - 17.2 0:14
#24.2 14:15 vypadok - 1.3 21:17
#2022-03-06 15:30:08.086432 - 7.3 19:50
#7.3 okolo 21:30 moje saskovanie pre vylepsenie stability
#2022-03-08 15:06:50 - 2022-03-09  16:37:58 vypadok presov mhd serverva
# 2022-03-18 14:50 - 2022-03-20 19:55 vypadok mhd servera
#2022-03-23 14:51 - 2022-03-24 09:04 tuke server down
# 2022-03-31 17:44:55.863667 - 2022-04-05 19:55 - vypadok stranky an too much for  to check
#2022-04-06 15:24:34.495195 - 2022-04-06 20:37 - tuke server down
#Datetime: 2022-04-15 07:53: - 13:38 - webserver down
#Datetime: 2022-04-19 17:33  - 20.4 23:58 - TUKE server down
END -2022-04-25 19:44
"""

#použité intervaly rátajúc vždy od začiatku do spomenútého dátumu/konca
#till 21.2
#till 4.3
#till 10.3
#till 17.3
#till 27.3
#till  8.4
#till 16.4
#till END

def preprocessing():
    #skontroluj či existuje opravené verzia stiahnutých dát ak nie vytvor ju pomocou funkcie deleteHTMLerrors()
    if not path.exists("MHD_Presov_repairedversion.csv"):
        print(
            "It seems you don't have the version of csv file which has removed HTML errors. In that case I will have to create it. It may take some time I will let you know when I am done.")
        deleteHTMLerrors()
        print(
            "The HTML errors have been deleted from file MHD_Presov and new version is saved in MHD_Presov_repairedversion.csv I am starting preprocessing part...")

    #otvor súvor pre s upravenými dátami a priprav premenné pre prácu s dátami
    file = open('MHD_Presov_repairedversion.csv')
    csvreader = csv.reader(file)
    curr_date = "2022-02-11"
    curr_time = ""
    busses = [] #zoznam všetkých liniek a ich meškaní
    active_busses = [] #zoznam aktívnych liniek
    bus_found = False
    dayle_statistics = []

    #prechádzaj dáta po riadkoch
    for row in csvreader:
        #ak je riadok prázny preskoč ho
        if not row: continue

        #ak riadok obsahuje časový údaj o vytvorení daného záznamu (ten sa nachádza vždy na jeho začiatku)
        if row[0][0:8] == "Datetime":
            curr_time = row[0][10:29]
            # zmaž všetky spoje dáta spojov ktoré sa vyskytli menej ako 5 krát pred tým než zmizli zo zápisov (indikuje vadné dáta)
            for i in active_busses:
                #chybná linka odstranuje sa z pozorovania aj z uložených dát
                if i[1] < 5 and not i[2]:
                    busses.pop(busses.index(i[0]))
                    active_busses.pop(active_busses.index(i))
                #linka má dostatok výskytov a už sa nevyskutje v zápisoch taže prestaneme držať jej dáta v zoznamé aktívnych liniek
                elif not i[2]:
                    active_busses.pop(active_busses.index(i))
                #linka je stále katívna pokračuj v jej sledovaní
                else:
                    i[2] = False

            #ak v pozorovaných dáta dôjdeme na nový deň aktualizuj premennu
            if row[0][10:20] != curr_date:
                #dayle_statistics.append([curr_date])
                curr_date = row[0][10:20]
            print(row[0])

            #používané pri robení intervalov pre Zákon velkých čísel odkomentuje nasledujúce 2 riadky a v 1. zmeň dátum na čas kedy chceš aby sa končil daný interval, dátum zadaj vo formáte RRRR-MM-DD
            # if curr_date == "2022-02-12":
            #     break
            continue

        bus_found = False
        #ak sa jedná o riadok kde je linka sprav z toho pole
        line = row[0].split(";")
        for i in active_busses:
            bus_found = False

            #Vysvetlivky indexov pola: 0 - číslo linky, 1 - čas vyrazenia z 1. zastávky, 2 - smer (T/P/D/Z/R), 4 - zastávka 1, 7 - zastávka 2,
                # 14 - meškanie, 15 - číslo autobusu, 16 - čas kedy prišli údaje od daného spoju na server

            #táto linka sa už nachádza v zoznamke aktulne sledovaných spojov podľa jej čísla, času vyrazenie a čísla autobusu
            if line[0] == i[0][0] and line[1] == i[0][1] and line[15] == i[0][2]:
                bus_found = True

                # táto linka je chybná lebo jej zastávky sú rovnaké alebo nemajú názov preto ju ignoruj a chod na dalšiu
                if line[16] == i[0][4] or line[4] == '' or line[7] == '':
                    break

                bus_curr_time = t.strptime(curr_time, "%Y-%m-%d %H:%M:%S")
                bus_previous_time = t.strptime(i[0][3], "%Y-%m-%d %H:%M:%S")
                #porovnaj či sú časy od seba zápisov od seba dostatočne krátko vzdialené inač sa jedná o novú ale chybnú linku
                if (time.mktime(bus_curr_time) - time.mktime(bus_previous_time)) <= 20:
                    index = busses.index(i[0])

                    #ak už su zapísani meškania na tomto useku trate pridaj nove meškani k nim //cheching last stop well bcs its either last stop or new one
                    if (i[0][-1][0] == line[4] and i[0][-1][1] == line[7]):
                        busses[index][-1][2].append(line[14])
                        i[0][-1][2].append(line[14])
                    #ak nie su vytvor nový úsek trate v nasledujúcom formate -> [zaastávka1,zastávka2,[meškanie]]
                    else:
                        busses[index].append([line[4], line[7], [line[14]]])
                        i[0].append([line[4], line[7], [line[14]]])

                    # aktualizuj časy pre porovnávanie kontinuality spomenutej vyššie a taktiež premmenné sledujúce či sa spoj vyskytol aspo 5 krát
                    busses[index][3] = curr_time
                    i[0][3] = curr_time
                    busses[index][4] = line[16]
                    i[0][4] = line[16]
                    i[1] += 1
                    i[2] = True

                #naraz može existovať len 1 taká linka ďalšie hladanie zhody teda nenutné, pokračuj na nový riadok v zápisoch
                break
        #táto linka sa ešte nenachádza v zoznamie liniek a zároveň sa nejedná o linku s označením # ktorá reprezentuje dojazd/prejazd/manipulačnú jazdu prípadne nejaké chybné údaje
            #a zároveň jej zastávky majú pomenovanie
        if not bus_found and line[0].find("#") == -1 and line[4] != '' and line[7] != '':
            busses.append([line[0], line[1], line[15], curr_time, line[16], [line[4], line[7], [line[14]]]])
            active_busses.append([[line[0], line[1], line[15], curr_time, line[16], [line[4], line[7], [line[14]]]], 0, True])

    #koniec prehladávania dát
    # štatistika čast 1 - skombinuj všetko do pola
    for i in busses:
        tmp = False
        for j in dayle_statistics:
            #ak je už linka v poli tak...
            if i[0] == j[0]:
                #zober všetky spoje zo starého spoja
                for k in i[5:-1]:
                    tmp1 = False
                    #zober všetky spoje z toho pola
                    for l in j[1]:
                        #ak sa useky trate zhoduju pridaj ich meškania
                        if l[0] == k[0] and l[1] == k[1] or l[0] == k[1] and l[1] == k[0]:  # linky možu byť v opačnom poradí a stále sa jedna o rovnaký úsek
                            l.append(k[2])
                            tmp1 = True
                    #ak sa nenašla zhoda pridaj cely usek trate
                    if not tmp1:
                        j[1].append(k)
                #každá linka je unikatna pokračovanie v hladní je zbytočne
                tmp = True
                break
        #ak sa nenašla taká linka pridaj ju celu
        if not tmp:
            dayle_statistics.append([i[0], i[5:-1]])

    # sštatiska časť 2 - výrataj priemerné meškania
    tmp_save = []

    #prechádzaj linkami
    for i in dayle_statistics:
        print(i[0])
        #prejdi každu linku
        for j in i[1]:
            #prejdi všetky useky trate
            together = 0
            count = 0

            #count avreage
            for k in j[2::]:
                #prejdi všetky meškania na danom useky, spočítaj ich hodnoty a počet
                for l in k:
                    together += int(l)
                count += len(k)

            #after that count SD
            count_SD = 0
            SD = 0
            for k in j[2::]:
                for l in k:
                    count_SD += pow(abs(int(l) - round(together / count, 6)), 2)
            SD = math.sqrt(count_SD/count)
            print(j[0] + " " + j[1] + " " + str(SD))
            #miesto meškaní pridaj priemerné meškanie
            testus = i[1].index(j)
            i[1][testus] = [j[0], j[1], round(together / count, 6)]




    #pošli priemerné meškania to funkcie LoLN(autobusy_s_priemernými_meškaniami) pre vyhotovenie súborov potrebných k vyhodnoteniu kvality modelu
    LoLN(dayle_statistics)
    print(curr_time)
if __name__ == '__main__':
    preprocessing()


# zoznam zvlaštnych liniek, ktoré sa vyskytujú v dátach ale nie v harmonograme Prešova ['', '#', ' 5D', 'ZL', ' #', 'SK', 'DP', '  #', 'OBJ']

