Program sa zaoberá vyhotovením simulácie mestkej hromadnej dopravy v meste Prešov. Jadro programu, teda agentová simulácia na mape bežiacej vo webovom rozhraní,
bola zostrojená Ing. Marcelom Vološinom z katedry počítačov a informatiky (Technický Univerzita v Košiciach). Rozšíril som fungovanie simulácie a agentov reprezentujúcich
spoje mestskej dopravy. Tieto spoje chodili na základe sieti zastávok, ktoré som získal z ich online harmonogramov. Každému spoju bolo na úskoch medzi 2 zastávkami vygenerované meškanie
pomocou Gaussovho prerozdelenia pravdepodobnsti. Dáta na zhotovenie takéhoto generátora meškaní som zbieral z webovej stránke mesta Prešov pocom REST/API počas doby niekoľkých mesiacov.
Následne som ich spracoval, vytriedil a niektoré chybné údaje a vyhotovil z nich priemerné meškania na jednotlivých úskoch ako aj štandartnú odchýlku, ktoré som potreboval
pre vytvorenie už spomínaného generátora meškaní.
