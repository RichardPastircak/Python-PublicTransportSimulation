
<h1>Popis programu</h1>
Program sa zaoberá vyhotovením simulácie mestkej hromadnej dopravy v meste Prešov. Jadro programu, teda agentová simulácia na mape bežiacej vo webovom rozhraní,
bola zostrojená Ing. Marcelom Vološinom z katedry počítačov a informatiky (Technický Univerzita v Košiciach). Rozšíril som fungovanie simulácie a agentov reprezentujúcich
spoje mestskej dopravy. Tieto spoje chodili na základe sieti zastávok, ktoré som získal z ich online harmonogramov po mape zostrojenej pomocou knižnice OSMNx. Každému spoju bolo na úskoch medzi 2 zastávkami vygenerované meškanie
pomocou Gaussovho rozdelenia pravdepodobnsti. Dáta na zhotovenie takéhoto generátora meškaní som zbieral z webovej stránke mesta Prešov pocom REST/API počas doby niekoľkých mesiacov.
Následne som ich spracoval, vytriedil niektoré chybné údaje a vyhotovil z nich priemerné meškania na jednotlivých úskoch ako aj štandartnú odchýlku, ktoré som potreboval
pre vytvorenie už spomínaného generátora meškaní.

Jednotlivé spoje na každej zastávke aj pracovali s objektmi cestujúcich, ktorý mali zadané, ktorým autobusom sa chcú na akú zastávku dostať a boli pravidelne vytváraný nový aby sa týmto vytvoril dojdem cikulácie populácie po meste. Simulácie sa okrajovo aj zaoberá vplyvom počasie no to len na toľko že je možné nastaviť jeden z niekoľkých typov čo zmení rýchlosť pohybu vozidiel.

<h1> Obsah jednotlivých súborov </h1>

<h2>Movement-Python</h2> 
  Hlavný program obsahujúci samotnú simuláciu
<h2>Vyhodnotenie_dat</h2> 
  Program, ktorý spracovával zozbierané údaje o pohybe MHD spojov, tu prebiehal výpočet aritmetického priemeru a štandartnej odchýlky
<h2>Zber_dat_MHD</h2>
  Samotné zbieranie dát z webového portálu mesta Prešov

<h1>Link na video ukážku</h1>
https://youtu.be/Ua7KFobkYJY
