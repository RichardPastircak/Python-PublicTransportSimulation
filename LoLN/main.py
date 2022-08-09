from os.path import exists
import csv


def LoLN():
    files = ["1", "2", "3", "4", "5", "6", "7", "8"]
    bus_delays = {}
    differences = {}

    lines_to_skip = ["ZL:", " 5D:", "SK:", "DP:", "OBJ:"]
    file_to_read = None

    for i in files:
        #Otváraj postupne všetky intervaly dát
        print("Now procesing file MHD_Presov_delays" + i + "csv.")
        #reset variables
        bus_delays2 = {}
        current_bus = None
        differences = {
        " 1:": [],
        " 8:": [],
        "38:": [],
        "39:": [],
        " 4:": [],
        "11:": [],
        " 7:": [],
        "45:": [],
        "21:": [],
        "32:": [],
        " 2:": [],
        "12:": [],
        " 5:": [],
        "14:": [],
        "22:": [],
        "20:": [],
        "19:": [],
        "42:": [],
        "27:": [],
        "41:": [],
        "36:": [],
        "13:": [],
        "28:": [],
        "34:": [],
        "15:": [],
        "23:": [],
        "46:": [],
        "44:": [],
        "30:": [],
        "26:": [],
        "32A:": [],
        "18:": [],
        "24:": [],
        "33:": [],
        "37:": [],
        "10:": [],
        "29:": [],
        "N1:": [],
        "N2:": [],
        "17:": [],
        "35:": [],
        "43:": [],
    }
        #Open file with delays
        if not exists("MHD_Presov_delays" + i + ".csv"):
            raise Exception("Missing file MHD_Presov_delays" + i + ".csv")
        file_to_read = "MHD_Presov_delays" + i + ".csv"
        file = open(file_to_read)
        csvreader = csv.reader(file)

        #prechádzaj ich dhonoty a vytvor slovník liniek a ich meškaní v jednotlivých usekoch
        for j in csvreader:
            #ak sa jedná o prázdny riadok alebo jednu z chybných liniek pokračuj na ďalší riadok
            if not j or j[0] in lines_to_skip:
                current_bus = None if not j else j[0]
                continue
            #ak sa jedná o meškanie na nejakom useku
            elif len(j[0]) > 3 and j[0] != "32A:" and current_bus not in lines_to_skip:
                if current_bus is None:
                    raise Exception("This delays doesnt belong to any bus " + str(j[0][1:-2]))

                #upravj jeho tvar a ulož ho
                tmp = j[0][1:-2].split(",")
                for k in range(3):
                    tmp[k] = tmp[k].strip().strip("\"").strip("'")
                bus_delays2.get(current_bus).update({tmp[0]+"&"+tmp[1]:tmp[2]})
            #ak sa jedná o autobus pridaj ho do slovníka
            elif current_bus not in lines_to_skip:
                bus_delays2.update({j[0]:{}})
                current_bus = j[0]

        file.close()

        #ak sa prečítali aspoň 2 intervali vyrátaj rozdli medzi nimi
        if bus_delays != {}:
            for j in bus_delays2:
                for k in bus_delays2.get(j):
                    #rozdiely rátaj len pre linky ktoré boli aj v prvom z 2 intervalov
                    if bus_delays.get(j).get(k,-1) != -1:
                        if float(bus_delays.get(j).get(k)) <= 0 and float(bus_delays2.get(j).get(k)) <= 0 or float(bus_delays.get(j).get(k)) >= 0 and float(bus_delays2.get(j).get(k)) >= 0:
                            differences.get(j).append([k,abs(abs(float(bus_delays.get(j).get(k))) - abs(float(bus_delays2.get(j).get(k))))])
                        else:
                            differences.get(j).append([k, abs(float(bus_delays.get(j).get(k)) - float(bus_delays2.get(j).get(k)))])
        bus_delays = bus_delays2.copy()

    #zapíš vyrátané rozdiely do súboru LoLN.csv ked sa prešlo posledným intervalom
    file_to_write = open("LoLN.csv", "w", newline="")
    csvwriter = csv.writer(file_to_write)
    for i in differences:
        print(i + ": " + str(differences.get(i)))
        csvwriter.writerow([])
        csvwriter.writerow([i])
        for j in differences.get(i):
            tmp = j[0].split("&")
            tmp.append(round(float(j[1]),5))
            csvwriter.writerow(tmp)


if __name__ == '__main__':
    LoLN()




