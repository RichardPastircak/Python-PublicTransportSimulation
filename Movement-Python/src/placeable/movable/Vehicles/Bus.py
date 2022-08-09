import sys
from copy import deepcopy
from numpy import random


from src.placeable.movable.Vehicles.Vehicle import Vehicle
from src.common.Location import Location

#zoznam zastávok a ich polohy
stops_list = {
    "Nižná Šebastová": [49.0249178, 21.2866479],
    "Pažica": [49.0236947, 21.2820367 ],
    "Vranovská": [49.0212785, 21.2761892],
    "Šarišské Lúky": [49.0179809, 21.2715838],
    "Dopravný podnik": [49.0105969, 21.2569547],
    "Rázcestie Kúty": [49.0084004, 21.2500558],
    "Duklianska": [49.0028107, 21.2415198],
    "Trojica": [48.9992387, 21.2396867],
    "Na Hlavnej": [48.9959976, 21.2417323],
    "Veľká pošta": [48.9915722, 21.2453058],
    "Čierny most": [48.9897897, 21.2466582],
    "Železničná stanica": [48.9832375, 21.2498423],
    "Škára": [48.9812425, 21.256695],
    "Solivarská": [48.9773481, 21.2665432],
    "Bohúňova": [48.978727, 21.2712906],
    "Múzeum Solivar": [48.9795254, 21.2749124],
    "Solivar": [48.9783847, 21.276888],

    "Budovateľská": [48.976918, 21.2445251],
    "Pekárne": [48.9788851, 21.2440762],
    "Priemyselné centrum": [48.9828071, 21.2433378],
    "Štúrova": [48.9853897, 21.2428959],
    "Divadlo Jonáša Záborského": [48.9933192, 21.2441363],
    "Poliklinika": [49.0008042, 21.2331503],
    "Obrancov mieru": [48.9970042, 21.22834],
    "Duchnovičovo námestie": [48.9937662, 21.2325333],
    "Prešovská univerzita": [48.9904097, 21.2354155],
    "Škultétyho": [48.9866163, 21.2416641],
    "Sabinovská": [49.0056253, 21.2383635],
    "Mičurinova": [49.0111849, 21.2367058],
    "Pod Skalkou": [49.0149063, 21.2366179],
    "Rázcestie Šidlovec": [49.0211678, 21.2352561],
    "Dúbrava": [49.0250046, 21.2323204],
    "Veterinárna nemocnica": [49.0208879, 21.2317761],
    "Bajkalská": [49.0235268, 21.2299251],

    "Sídlisko III" : [49.0233765, 21.2283951],
	"Prostějovská" : [49.020726, 21.2243781],
	"Centrum" : [49.0167729, 21.2231811],
	"VUKOV" : [49.0121509, 21.2222969],
	"Námestie Kráľovnej pokoja" : [49.0069795, 21.2213449],
	"Volgogradská" : [49.0036065, 21.2207231],
	"Clementisova" : [49.0016655, 21.2244714],
	"Lesnícka" : [48.9793574, 21.2640761],
	"Pavla Horova" : [48.9838285, 21.2639563],
	"Martina Benku" : [48.9872562, 21.2648138],
	"Laca Novomeského" : [48.9895672, 21.2674375 ],
	"Vansovej" : [48.9918572, 21.271349],
	"Pod Šalgovíkom" : [48.99338, 21.2753848],


	"Ľubochnianska" : [49.0171167, 21.2662253],
	"Strojnícka" : [49.0202434, 21.2660523],
	"Družstevná" : [49.0229484, 21.2665226],
	"Širpo" : [49.0251102, 21.2671473],

    "Jurkovičova" : [48.9943625, 21.2683662],
	"Karpatská" : [48.9972431, 21.2700389],
	"Sibírska" : [49.0008748, 21.2725694],

    "Fakultná nemocnica" : [48.9963899, 21.2527024],
	"Detská nemocnica" : [48.9985974, 21.250892],
	"Dilongova" : [48.9995248, 21.2477719],
	"Sládkovičova" : [48.9974685, 21.248418],
	"Moyzesova" : [48.9951583, 21.2501906],
	"Nový Solivar" : [48.9788267, 21.25098],
	"Košická" : [48.9711107, 21.2528325],
	"Chalupkova" : [48.9704154, 21.2551934],
	"Švábska" : [48.9713648, 21.2592392],
	"Lomnická" : [48.9743703, 21.2624879],

    "Na Rúrkach" : [49.0077615, 21.2114899],
	"Jána Béreša" : [49.0049012, 21.2148997],
	"Rázcestie Rúrky" : [49.0030844, 21.2164073],
	"Levočská" : [49.0004564, 21.2241144],
	"Rusínska" : [48.9911824, 21.2628345],
	#"Eperia" : [48.9900703, 21.2631841],
	"Suvorovova" : [48.9762467, 21.2649266],
	"Cintorín Solivar" : [48.9745336, 21.2687696],
	"Na brehu" : [48.9729511, 21.2755474],
	"Valkovská" : [48.9747687, 21.2778662],

    "Šidlovec": [49.0328304, 21.2481688],
    "Stavbárska": [49.0330559, 21.2417559],
    "Šidlovská": [49.0300655, 21.2405785], #CHANGED HERE might to sth wierd
    "Jánošíkova": [49.0263789, 21.2379147],
    "Dúbravská": [49.0310533, 21.2354002],
    "Pri kaplnke": [49.0286748, 21.2348635],
    "Marka Čulena": [48.9997132, 21.2204757],
    "Odborárska": [48.9970852, 21.2218988],
    "Sázavského": [48.9942729, 21.2234379],
    "Kollárova": [48.9921025, 21.2246325],
    "SOŠ lesnícka": [48.9927196, 21.2288377],
    "Malá stanica": [48.9950529, 21.2336333],
    "Kúpeľná": [48.9917516, 21.2383868],
    "Pavlovičovo námestie": [48.9901483, 21.2409411],
    "Šafárikova, cintorín": [49.004224, 21.2463811],
    "Lesík delostrelcov": [48.9923511, 21.249534],
    "Pod Táborom": [48.9913677, 21.2516071],
    "Nižné lúky": [48.99305, 21.2586204],

	"Nižnianska" : [49.0116274, 21.2676445],
	"Kalinčiakova" : [49.0117492, 21.2702505],
	"Ľubotice" : [49.0116772, 21.2736023],
	"Šalgovícka" : [49.0120356, 21.2794206],
	"Korabinského" : [49.0131382, 21.2808537],
	"Jána Kostru" : [49.0134527, 21.2767185],
	"Strážnická" : [49.0172499, 21.2773475],
	"Šebastovská" : [49.0201935, 21.2770165],
	"Gen. Ambruša" : [49.0211602, 21.2882358],
	"Herlianska" : [49.0192386, 21.2935741],
	"Kamence" : [49.0187171, 21.3164289 ],
	"Rázcestie Vyšná Šebastová" : [49.0177997, 21.3208208],
	"Obecný úrad Vyšná Šebastová" : [49.0165188, 21.321232],
	"Vyšná Šebastová" : [49.0119323, 21.3319766],

    "Kanaš - Stráže" : [49.0658714, 21.2301192],
    "Stará škola" : [49.0612379, 21.2280465],
    "Medzi jarkami" : [49.0582224, 21.2303978],
    "Pri kostole" : [49.0567045, 21.2326478],
    "Husí hrb" : [49.0535184, 21.232205],
    "Kozí rožok" : [49.0479003, 21.2242763 ],
	"Sordok" : [49.0443747, 21.2163942],
	"Rázcestie Kanaš" : [49.0430173, 21.210646],
    "Bikoš" : [49.0286689, 21.2205985],
    "Petrovianska" : [48.9594529, 21.2568612],
    "Logistické centrum" : [48.9509498, 21.2624949],
    # "Priemyselný park Záborské" : [48.9559946, 21.2683031], - the map didnt load that part and no its not bcs of map range
    "Rázcestie Záborské" : [48.9470186, 21.2878609],
    "Záborské - stred" : [48.9448373, 21.2892879],
    "Záborské" : [48.9423944, 21.2878617],

    "Za Kalváriou" : [48.9812157, 21.2173082],
    "Hôrka" : [48.9832965, 21.2177055],
    "Záhradkárska osada" : [48.9856422, 21.2210139],
    "Horárska" : [48.9860684, 21.2261873],
    "Zimný štadión" : [48.9875388, 21.2295931],
    "Pod Kalváriou" : [48.991008,21.229603], #NOTE had to move it bit to right
    "Centrál" : [48.9980669, 21.2271632],
    "Grešova" : [48.9931672, 21.2455265],

    "Bzenov" : [48.9551489, 21.1712417],
	"Rázcestie Janov" : [48.9472991, 21.1689037],
	"Obecný úrad Bzenov" : [48.9477402, 21.1656481],
	"Chatky" : [48.9762167, 21.1714196],
	"Čertov kameň" : [48.9797907, 21.1739052],
	"Cemjata" : [48.9838304, 21.1752816],
	"Školské lesy" : [48.9875311, 21.1763855],
	"Zabíjaná" : [48.989873, 21.1799754],
	"Kvašná voda" : [48.9900384, 21.1917662],
	"Vydumanec" : [48.992715, 21.1980421],
	"Rázcestie Cemjata" : [48.9979606, 21.2037298],
	"Mýto" : [49.0023762, 21.2154513],

	"Kukučínova" : [48.9814017, 21.2743062],
	"Kysucká" : [48.9845871, 21.2730255],

	"Regionálny úrad verejného zdravotníctva" : [48.9960535, 21.2549624],
	"Onkologický pavilón" : [48.9975643, 21.2567318],
	"Monoblok, interné oddelenie" : [48.9979419, 21.2533385],
	"Pediatria" : [48.9992861, 21.2523168],
	"Vajanského" : [49.0016416, 21.2427977],

    "Fintice" : [49.0580304, 21.2821822],
	"V kopci" : [49.0550557, 21.2831344],
	"Námestie Jozefa Kolarčíka" : [49.0514285, 21.2867003],
	"Červený mostík" : [49.0490678, 21.2850359],
	"Ihrisko" : [49.0467647, 21.2846544],
	"Gribľovec" : [49.0402656, 21.2834342],
	"Za traťou" : [49.0369582, 21.2820257],
	"Išľa" : [49.0318607, 21.2803352],
	"Fintická" : [49.029269, 21.2799352],
	"Nová" : [49.0264689, 21.2794699],

    "Teriakovce" : [48.9899681, 21.3117987],
	"OÚ Teriakovce" : [48.9906311, 21.3087729],
	"Na Kruhu" : [48.9908396, 21.3045291],
	"Rázcestie Teriakovce" : [48.9911215, 21.3017688],
	"Šalgovia" : [48.9916656, 21.2911057],
	"Labutia" : [48.9922059, 21.288569],
	"Šalgovík" : [48.996897, 21.287363],
	"Hruny" : [48.9965156, 21.284702],
	"Vyšné lúky" : [48.9931249, 21.2657213],
	"Kpt. Nálepku" : [48.9926718, 21.2468751],
	"Jahodová" : [49.0320636, 21.2427386],

    "Veľký Šariš" : [49.0414222, 21.1894379],
    "Varoš" : [49.0391691, 21.1911519],
    "Tulčícka" : [49.0337307, 21.1942398],
    "Malý Šariš" : [49.0149503, 21.1864294],
    "Šľachtiteľská stanica" : [49.0124158, 21.1856029],
    "Nákupné stredisko" : [49.0097886, 21.1821011],
    "Obecný úrad Malý Šariš" : [49.0080542, 21.1793021],
    "Rázcestie Malý Šariš" : [49.0044001, 21.1811626],
    "Telekča" : [49.0015878, 21.191693],

    "Haniska" : [48.9533081, 21.2413044],
	"Lemešianska" : [48.955635, 21.2407872],
	"Priecestie" : [48.9573443, 21.2412332],
	"Čistička" : [48.9653211, 21.2475385],
	"Gemor" : [48.967312, 21.2500164],
	"ZVL" : [48.9687578, 21.2516374],

	"Spinea - Záturecká" : [48.9536108, 21.2495795],

	"Slávičia" : [48.9860697, 21.2275593],
	"Pod Kamennou baňou" : [48.9834721, 21.2329284],
	"Mestská hala" : [48.9850843, 21.2378816],
	"Vodárenská" : [49.0023629, 21.2493413],
	"Hviezdna" : [49.0024446, 21.25234],

	"Bardejovská" : [49.0178906, 21.2755324],
	"Domašská" : [49.0149071, 21.2711828],
	"Pionierska" : [48.9688382, 21.2567828],
	"Jesenná" : [48.9643589, 21.256781],
	"Jelšová" : [48.9622265, 21.2587156],
	"Delňa" : [48.960784, 21.2603004],

	"Floriánova" : [48.997207, 21.2360256],
	"Okružná" : [48.9931546, 21.2401773],

	"Hobby park" : [48.991351, 21.2559451],

	"Pod nadjazdom" : [49.0126751, 21.267007],

    "Jilemnického" : [48.9762386, 21.2454968],

    "Hinrichs": [49.009516,21.267888],

	"Mukačevská" : [49.0110283, 21.226281],
	"Jazdecká" : [49.0087496, 21.2332361],

	"K Surdoku" : [49.008608, 21.248285],
	"Pod Šibeňou" : [49.0107628, 21.2474691],
	"Koryto" : [49.0146842, 21.2480634],
	"Rybníčky" : [49.0194888, 21.2504054],
	"Kúty" : [49.0224785, 21.2526513],
	"Za Kútami" : [49.0256829, 21.2532407],
	"Plachty" : [49.0267647, 21.2579598],
	"Pred Surdokom" : [49.0310896, 21.2558671],
	"Surdok" : [49.0344244, 21.258211 ],

	"Pod Wilecovou hôrkou" : [48.9719069, 21.2437405],
	"Wilecova hôrka" : [48.9681767, 21.244256],
	"Kamenná baňa" : [48.9631425, 21.2396651],
	"Borkút" : [48.9586574, 21.2362284],

    "Dulova Ves" : [48.952502, 21.306448],
	"Dulova Ves - kostol" : [48.9555045, 21.3012636],
	"Vlčie Doly" : [48.9626585, 21.2849292],

	"Námestie sv. Jakuba" : [49.0392749, 21.1939789],
	"Medulienka" : [49.0391163, 21.1995032],
	"Staničná" : [49.0419486, 21.2040418],
	"Pivovar" : [49.0433413, 21.2091378],

	"Soľnobanská" : [48.9820293, 21.2797335],
	"Záhradky" : [48.9811827, 21.288846],
	"Pri zámočku" : [48.9777673, 21.3189978],
	"Na Záhumní" : [48.9777777, 21.3241116],
	"Hulica" : [48.9791776, 21.3276508],
	"Ruská Nová Ves" : [48.9780779, 21.333476],

	"Námestie mládeže" : [48.9955024, 21.2295259],

    }

#počet opakovani trate pre linky
bus_counters = {
    "line1" : 18,
    "line2/5" : 16,
    "line4" : 19,
    "line7" : 17,
    "line8" : 18,
    "line38" : 19,
    "line10" : 16,
    "line11" : 16,
    "line12" : 8,
    "line13" : 14,
    "line14" : 14,
    "line15" : 16,
    "line17" : 3,
    "line18" : 7,
    "line19" : 15,
    "line21" : 18,
    "line22" : 14,
    "line23" : 2,
    "line24" : 12,
    "line26" : 6,
    "line27" : 17,
    "line28" : 19,
    "line29" : 14,
    "line30" : 1,
    "line32" : 4,
    "line32A" : 13,
    "line33" : 8,
    "line34" : 8,
    "line35" : 3,
    "line36" : 17,
    "line37" : 1,
    "line39" : 16,
    "line41" : 16,
    "line42" : 7,
    "line43" : 2,
    "line44" : 6,
    "line45" : 18,
    "line46" : 14,
    "lineN1" : 4,
    "lineN2" : 4,
}

#táto premenná obsahuje pomer odhadovaného času za ktorý sa má dostať spoj zo zastávky A do B a realny čas kolko mu to potrva (čiže odhadovaný čas + vygenerovane meškanie)
bus_delays = {
    "line1": {
        "Nižná Šebastová&Pažica" : lambda x: 60/(60-random.normal(loc=-50.104972, scale=60.59969626613287, size=1)[x]),
        "Pažica&Vranovská": lambda x: 60/(60-random.normal(loc=-86.333147, scale=98.37698823009003, size=1)[x]),
        "Vranovská&Šarišské Lúky": lambda x: 60/(60-random.normal(loc=-91.465397, scale=96.23257910857505, size=1)[x]),
        "Šarišské Lúky&Dopravný podnik": lambda x: 2*60/(2*60-random.normal(loc=-91.118175, scale=96.23257910857505, size=1)[x]),
        "Dopravný podnik&Rázcestie Kúty": lambda x: 60/(60-random.normal(loc=-85.152608, scale=116.48792135159144, size=1)[x]),
        "Rázcestie Kúty&Duklianska": lambda x: 2*60/(2*60-random.normal(loc=-117.142038, scale=142.20277488348353, size=1)[x]),
        "Duklianska&Trojica": lambda x: 2*60/(2*60-random.normal(loc=-130.495426, scale=144.01300491859234, size=1)[x]),
        "Trojica&Na Hlavnej": lambda x: 2*60/(2*60-random.normal(loc=-90.281914, scale=126.30424186825043, size=1)[x]),
        "Na Hlavnej&Veľká pošta": lambda x: 2*60/(2*60-random.normal(loc=-116.567776, scale=163.0121505286651, size=1)[x]),
        "Veľká pošta&Čierny most": lambda x: 60/(60-random.normal(loc=-112.940484, scale=161.62839398276813, size=1)[x]),
        "Čierny most&Železničná stanica": lambda x: 2*60/(2*60-random.normal(loc=-114.136016, scale=137.51936118951502, size=1)[x]),
        "Železničná stanica&Škára": lambda x: 2*60/(2*60-random.normal(loc=-121.829147, scale=142.06146080095715, size=1)[x]),
        "Škára&Solivarská": lambda x: 2*60/(2*60-random.normal(loc=-129.452453, scale=161.01065650878817, size=1)[x]),
        "Solivarská&Bohúňova": lambda x: 60/(60-random.normal(loc=-98.302791, scale=157.7132963959356, size=1)[x]),
        "Bohúňova&Múzeum Solivar": lambda x: 60/(60-random.normal(loc=-98.700171, scale=164.30342201714112, size=1)[x]),
        "Múzeum Solivar&Solivar": lambda x: 60/(60-random.normal(loc=-27.692591, scale=37.769617093941264, size=1)[x]),
    },
    #first part is from bus line 2 second from bus line 5, end lines had to be picked from other line (if it belong to 2 it was picked from 5)
    "line2/5" : {
        "Budovateľská&Pekárne" : lambda x: 60/(60-random.normal(loc=-27.173437, scale=50.042282027283115, size=1)[x]),
        "Pekárne&Priemyselné centrum" : lambda x: 60/(60-random.normal(loc=-11.786292, scale=36.505796299034316, size=1)[x]),
        "Priemyselné centrum&Štúrova" : lambda x: 60/(60-random.normal(loc=-13.554753, scale=40.71795529395303, size=1)[x]),
        "Štúrova&Čierny most" : lambda x: 2*60/(2*60-random.normal(loc=-60.257145, scale=55.58498197990983, size=1)[x]),
        "Čierny most&Divadlo Jonáša Záborského" : lambda x: 2*60/(2*60-random.normal(loc=-66.289479, scale=62.41216224810312, size=1)[x]),
        "Divadlo Jonáša Záborského&Na Hlavnej" : lambda x: 60/(60-random.normal(loc=-68.289511, scale=37.769617093941264, size=1)[x]),
        "Na Hlavnej&Trojica" : lambda x: 2*60/(2*60-random.normal(loc=-58.405658, scale=104.3149210101851, size=1)[x]),
        "Trojica&Poliklinika" : lambda x: 2*60/(2*60-random.normal(loc=-79.323387, scale=84.23701522117426, size=1)[x]),
        "Poliklinika&Obrancov mieru" : lambda x: 3*60/(3*60-random.normal(loc=-126.486395, scale=181.2277146930374, size=1)[x]),
        "Obrancov mieru&Duchnovičovo námestie" : lambda x: 2*60/(2*60-random.normal(loc=-67.323998, scale=94.41991011355195, size=1)[x]),
        "Duchnovičovo námestie&Prešovská univerzita" : lambda x: 60/(60-random.normal(loc=-66.270379, scale=83.74117720564716, size=1)[x]),
        "Prešovská univerzita&Škultétyho" : lambda x: 2*60/(2*60-random.normal(loc=-61.749869, scale=84.30845915023149, size=1)[x]),
        "Škultétyho&Čierny most" : lambda x: 2*60/(2*60-random.normal(loc=-85.239212, scale=95.3321568161177, size=1)[x]),
        #3 bustops on main road missing bcs its dictiniory A.K.A unique keys
         "Trojica&Sabinovská" : lambda x: 3*60/(3*60-random.normal(loc=-85.783939, scale=203.56790757815358, size=1)[x]),
         "Sabinovská&Mičurinova" : lambda x: 60/(60-random.normal(loc=-48.552262, scale=123.63443498063516, size=1)[x]),
         "Mičurinova&Pod Skalkou" : lambda x: 60/(60-random.normal(loc=-65.80706, scale=139.58318825840948, size=1)[x]),
         "Pod Skalkou&Rázcestie Šidlovec" : lambda x: 60/(60-random.normal(loc=-71.571313, scale=147.6273100556328, size=1)[x]),
         "Rázcestie Šidlovec&Veterinárna nemocnica" : lambda x: 60/(60-random.normal(loc=-137.685682, scale=307.32416371448676, size=1)[x]),
         "Veterinárna nemocnica&Bajkalská" : lambda x: 60/(60-random.normal(loc=-56.289772, scale=0, size=1)[x]),
    },
    "line4" : {
        "Sídlisko III&Prostějovská": lambda x: 60/(60-random.normal(loc=-44.801648, scale=126.35563172150174, size=1)[x]),
        "Prostějovská&Centrum": lambda x: 60/(60-random.normal(loc=-58.913883, scale=147.0682142634346, size=1)[x]),
        "Centrum&VUKOV": lambda x: 2*60/(2*60-random.normal(loc=-57.873496, scale=163.8487319127539, size=1)[x]),
        "VUKOV&Námestie Kráľovnej pokoja": lambda x: 60/(60-random.normal(loc=-56.882741, scale=155.73930390128862, size=1)[x]),
        "Námestie Kráľovnej pokoja&Volgogradská": lambda x: 60/(60-random.normal(loc=-67.982211, scale=166.0655143070026, size=1)[x]),
        "Volgogradská&Clementisova": lambda x: 60/(60-random.normal(loc=-76.050463, scale=176.62328496535017, size=1)[x]),
        "Clementisova&Poliklinika": lambda x: 3*60/(3*60-random.normal(loc=-88.089696, scale=160.02221070332504, size=1)[x]),
        "Poliklinika&Trojica": lambda x: 2*60/(2*60-random.normal(loc=-116.093575, scale=160.20533964154689, size=1)[x]),
        "Trojica&Na Hlavnej": lambda x: 2*60/(2*60-random.normal(loc=-75.054304, scale=143.08107220764455, size=1)[x]),
        "Na Hlavnej&Veľká pošta": lambda x: 2*60/(2*60-random.normal(loc=-32.002391, scale=137.59416375392047, size=1)[x]),
        "Veľká pošta&Čierny most": lambda x: 60/(60-random.normal(loc=-32.601592, scale=138.33419928002317, size=1)[x]),
        "Čierny most&Železničná stanica": lambda x: 2*60/(2*60-random.normal(loc=-93.783085, scale=154.1005657773412, size=1)[x]),
        "Železničná stanica&Škára": lambda x: 2*60/(2*60-random.normal(loc=-104.637849, scale=137.23545243701406, size=1)[x]),
        "Škára&Lesnícka": lambda x: 2*60/(2*60-random.normal(loc=-117.681994, scale=161.36950830454126, size=1)[x]),
        "Lesnícka&Pavla Horova": lambda x: 60/(60-random.normal(loc=-112.057551, scale=150.44719584134862, size=1)[x]),
        "Pavla Horova&Martina Benku": lambda x: 60/(60-random.normal(loc=-123.128008, scale=161.75918615611965, size=1)[x]),
        "Martina Benku&Laca Novomeského": lambda x: 2*60/(2*60-random.normal(loc=-120.38846, scale=159.40993346657052, size=1)[x]),
        "Laca Novomeského&Vansovej": lambda x: 60/(60-random.normal(loc=-104.626269, scale=163.36010318601888, size=1)[x]),
        "Vansovej&Pod Šalgovíkom": lambda x: 60/(60-random.normal(loc=-39.973507, scale=116.67156643825571, size=1)[x]),
    },
    "line7" : {
        "Budovateľská&Pekárne" : lambda x: 60/(60-random.normal(loc=-78.027379, scale=330.01938722335376, size=1)[x]),
        "Pekárne&Priemyselné centrum" : lambda x: 60/(60-random.normal(loc=-48.832403, scale=113.29978475132084, size=1)[x]),
        "Priemyselné centrum&Štúrova" : lambda x: 60/(60-random.normal(loc=-38.377052, scale=96.22423493822856, size=1)[x]),
        "Štúrova&Čierny most" : lambda x: 2*60/(2*60-random.normal(loc=-75.874232, scale=109.2673112267556, size=1)[x]),
        "Čierny most&Divadlo Jonáša Záborského" : lambda x: 2*60/(2*60-random.normal(loc=-52.947775, scale=69.82968452957458, size=1)[x]),
        "Divadlo Jonáša Záborského&Na Hlavnej" : lambda x: 60/(60-random.normal(loc=-51.302357, scale=74.08053728212931, size=1)[x]),
        "Na Hlavnej&Trojica" : lambda x: 2*60/(2*60-random.normal(loc=-51.489955, scale=95.64234248568108, size=1)[x]),
        "Trojica&Duklianska" : lambda x: 2*60/(2*60-random.normal(loc=-87.293743, scale=113.51584976974517, size=1)[x]),
        "Duklianska&Rázcestie Kúty" : lambda x: 2*60/(2*60-random.normal(loc=-57.43668, scale=107.91012303018607, size=1)[x]),
        "Rázcestie Kúty&Dopravný podnik" : lambda x: 60/(60-random.normal(loc=-49.131148, scale=73.20116345316897, size=1)[x]),
        "Dopravný podnik&Ľubochnianska" : lambda x: 2*60/(2*60-random.normal(loc=-52.398642, scale=85.68533474754713, size=1)[x]),
        "Ľubochnianska&Strojnícka" : lambda x: 60/(60-random.normal(loc=-46.159666, scale=83.9184065313563, size=1)[x]),
        "Strojnícka&Družstevná" : lambda x: 60/(60-random.normal(loc=-41.405255, scale=77.8845928433171, size=1)[x]),
        "Družstevná&Širpo" : lambda x: 60/(60-random.normal(loc=-26.025613, scale=71.68394827443348, size=1)[x]),
    },
    "line8" : {
        "Sídlisko III&Prostějovská" : lambda x: 60/(60-random.normal(loc=-43.597117, scale=109.12010739672219, size=1)[x]),
        "Prostějovská&Centrum": lambda x: 60/(60-random.normal(loc=-67.178069, scale=163.91835586349865, size=1)[x]),
        "Centrum&VUKOV": lambda x: 2*60/(2*60-random.normal(loc=-74.402053, scale=191.5141494037387, size=1)[x]),
        "VUKOV&Námestie Kráľovnej pokoja": lambda x: 60/(60-random.normal(loc=-67.449644, scale=173.05760958198604, size=1)[x]),
        "Námestie Kráľovnej pokoja&Volgogradská": lambda x: 60/(60-random.normal(loc=-80.80646, scale=188.43716034075115, size=1)[x]),
        "Volgogradská&Clementisova": lambda x: 60/(60-random.normal(loc=-93.62988, scale=209.06939955451813, size=1)[x]),
        "Clementisova&Poliklinika": lambda x: 3*60/(3*60-random.normal(loc=-96.964822, scale=173.4243579783265, size=1)[x]),
        "Poliklinika&Trojica": lambda x: 2*60/(2*60-random.normal(loc=-132.569659, scale=172.22280161041573, size=1)[x]),
        "Trojica&Na Hlavnej": lambda x: 2*60/(2*60-random.normal(loc=-90.131679, scale=161.32877580117074, size=1)[x]),
        "Na Hlavnej&Veľká pošta": lambda x: 2*60/(2*60-random.normal(loc=-30.651841, scale=129.36095877575943, size=1)[x]),
        "Veľká pošta&Čierny most": lambda x: 60/(60-random.normal(loc=-30.13953, scale=127.56532174029957, size=1)[x]),
        "Čierny most&Železničná stanica": lambda x: 2*60/(2*60-random.normal(loc=-108.061289, scale=164.0401580329712, size=1)[x]),
        "Železničná stanica&Škára": lambda x: 2*60/(2*60-random.normal(loc=-119.673597, scale=151.29941136972292, size=1)[x]),
        "Škára&Lesnícka": lambda x: 2*60/(2*60-random.normal(loc=-129.414031, scale=163.46580074346517, size=1)[x]),
        "Lesnícka&Pavla Horova": lambda x: 60/(60-random.normal(loc=-124.223889, scale=157.25541531145322, size=1)[x]),
        "Pavla Horova&Martina Benku": lambda x: 60/(60-random.normal(loc=-134.267518, scale=166.98214546602978, size=1)[x]),
        "Martina Benku&Jurkovičova": lambda x: 2*60/(2*60-random.normal(loc=-137.915397, scale=169.92200272148798, size=1)[x]),
        "Jurkovičova&Karpatská": lambda x: 60/(60-random.normal(loc=-152.09005, scale=174.73423690616247, size=1)[x]),
        "Karpatská&Sibírska": lambda x: 2*60/(2*60-random.normal(loc=-85.493055, scale=129.77488344839443, size=1)[x]),
    },
    "line38" : {
        "Sídlisko III&Prostějovská" : lambda x: 60/(60-random.normal(loc=-50.320781, scale=153.8810890059256, size=1)[x]),
        "Prostějovská&Centrum": lambda x: 60/(60-random.normal(loc=-92.480088, scale=183.76064880935982, size=1)[x]),
        "Centrum&VUKOV": lambda x: 2*60/(2*60-random.normal(loc=-98.373217, scale=198.76589405273342, size=1)[x]),
        "VUKOV&Námestie Kráľovnej pokoja": lambda x: 60/(60-random.normal(loc=-88.471443, scale=189.7836808421617, size=1)[x]),
        "Námestie Kráľovnej pokoja&Volgogradská": lambda x: 60/(60-random.normal(loc=-104.340977, scale=206.96951498790426, size=1)[x]),
        "Volgogradská&Clementisova": lambda x: 60/(60-random.normal(loc=-118.228943, scale=223.0269374332044, size=1)[x]),
        "Clementisova&Obrancov mieru": lambda x: 2*60/(2*60-random.normal(loc=-131.559597, scale=309.9393625545461, size=1)[x]),
        "Obrancov mieru&Duchnovičovo námestie" : lambda x: 2*60/(2*60-random.normal(loc=-36.253064, scale=126.2953713480603, size=1)[x]),
        "Duchnovičovo námestie&Prešovská univerzita" : lambda x: 60/(60-random.normal(loc=-91.391806, scale=158.86439448940754, size=1)[x]),
        "Prešovská univerzita&Škultétyho" : lambda x: 2*60/(2*60-random.normal(loc=-91.26322, scale=152.42783918434532, size=1)[x]),
        "Škultétyho&Železničná stanica" : lambda x: 3*60/(3*60-random.normal(loc=-107.705036, scale=159.00135070077167, size=1)[x]),
        "Železničná stanica&Škára": lambda x: 2*60/(2*60-random.normal(loc=-119.188449, scale=149.09326621626053, size=1)[x]),
        "Škára&Lesnícka": lambda x: 2*60/(2*60-random.normal(loc=-127.759031, scale=156.19921217234037, size=1)[x]),
        "Lesnícka&Pavla Horova": lambda x: 60/(60-random.normal(loc=-125.774404, scale=149.2362733031963, size=1)[x]),
        "Pavla Horova&Martina Benku": lambda x: 60/(60-random.normal(loc=-132.164064, scale=154.97872802146568, size=1)[x]),
        "Martina Benku&Jurkovičova": lambda x: 2*60/(2*60-random.normal(loc=-143.536132, scale=168.1207721587822, size=1)[x]),
        "Jurkovičova&Karpatská": lambda x: 60/(60-random.normal(loc=-154.935198, scale=168.9392242681774, size=1)[x]),
        "Karpatská&Sibírska": lambda x: 2*60/(2*60-random.normal(loc=-83.957846, scale=145.90913736501432, size=1)[x]),

    },
    "line10" : {
        "Fakultná nemocnica&Detská nemocnica" : lambda x: 60/(60-random.normal(loc=-82.025183, scale=118.75421654606056, size=1)[x]),
        "Detská nemocnica&Dilongova" : lambda x: 60/(60-random.normal(loc=-84.488048, scale=110.4732494071245129, size=1)[x]),
        "Dilongova&Sládkovičova" : lambda x: 60/(60-random.normal(loc=-96.638864, scale=116.5328657727145, size=1)[x]),
        "Sládkovičova&Moyzesova" : lambda x: 60/(60-random.normal(loc=-79.256793, scale=118.50299608492637, size=1)[x]),
        "Moyzesova&Veľká pošta" : lambda x: 3*60/(3*60-random.normal(loc=-91.881124, scale=144.5711490460287, size=1)[x]),
        "Veľká pošta&Čierny most": lambda x: 60/(60-random.normal(loc=-67.358744, scale=142.66742505706932, size=1)[x]),
        "Čierny most&Železničná stanica": lambda x: 2*60/(2*60-random.normal(loc=-114.754469, scale=139.7637320235099, size=1)[x]),
        "Železničná stanica&Nový Solivar": lambda x: 60/(60-random.normal(loc=-107.337101, scale=118.28286253174478, size=1)[x]),
        "Nový Solivar&Košická": lambda x: 60/(60-random.normal(loc=-95.892245, scale=124.42992597492878, size=1)[x]),
        "Košická&Chalupkova": lambda x: 60/(60-random.normal(loc=-109.339886, scale=120.03933373027411, size=1)[x]),
        "Chalupkova&Švábska": lambda x: 60/(60-random.normal(loc=-95.673138, scale=129.61022607712655, size=1)[x]),
        "Švábska&Lomnická": lambda x: 60/(60-random.normal(loc=-111.003722, scale=139.16190014572433, size=1)[x]),
        "Lomnická&Lesnícka": lambda x: 2*60/(2*60-random.normal(loc=-115.326821, scale=135.79021089472027, size=1)[x]),
        "Lesnícka&Pavla Horova": lambda x: 60/(60-random.normal(loc=-98.944825, scale=130.65020122100873, size=1)[x]),
        "Pavla Horova&Martina Benku": lambda x: 60/(60-random.normal(loc=-107.554858, scale=141.11640784691934, size=1)[x]),
        "Martina Benku&Jurkovičova": lambda x: 2*60/(2*60-random.normal(loc=-120.472629, scale=169.7587089963282, size=1)[x]),
        "Jurkovičova&Karpatská": lambda x: 60/(60-random.normal(loc=-133.810772, scale=165.58947527324716, size=1)[x]),
        "Karpatská&Sibírska": lambda x: 2*60/(2*60-random.normal(loc=-44.898232, scale=58.56375066060943, size=1)[x]),
    },
    "line11" : {
        "Na Rúrkach&Jána Béreša" : lambda x: 60/(60-random.normal(loc=-89.998803, scale=207.99215226753574, size=1)[x]),
        "Jána Béreša&Rázcestie Rúrky" : lambda x: 60/(60-random.normal(loc=-63.679112, scale=112.66172289747914, size=1)[x]),
        "Rázcestie Rúrky&Levočská" : lambda x: 2*60/(2*60-random.normal(loc=-63.460908, scale=151.8274662500865, size=1)[x]),
        "Levočská&Poliklinika" : lambda x: 2*60/(2*60-random.normal(loc=-81.095972, scale=138.44135187678137, size=1)[x]),
        "Poliklinika&Trojica": lambda x: 2*60/(2*60-random.normal(loc=-89.998803, scale=139.16268842264452, size=1)[x]),
        "Trojica&Na Hlavnej": lambda x: 2*60/(2*60-random.normal(loc=-57.009346, scale=135.58460390325897, size=1)[x]),
        "Na Hlavnej&Veľká pošta": lambda x: 2*60/(2*60-random.normal(loc=-35.658518, scale=86.52837648421324, size=1)[x]),
        "Veľká pošta&Čierny most": lambda x: 60/(60-random.normal(loc=-39.084629, scale=86.52837648421324, size=1)[x]),
        "Čierny most&Rusínska": lambda x: 3*60/(3*60-random.normal(loc=-115.148773, scale=128.56733218323575, size=1)[x]),
        "Rusínska&Martina Benku": lambda x: 2*60/(2*60-random.normal(loc=-96.616517, scale=112.1101710399319, size=1)[x]-random.normal(loc=-129.44932, scale=142.43816964565508, size=1)[x]), #I am missing one stop in between so I will count 2 delays together here
        "Martina Benku&Pavla Horova": lambda x: 60/(60-random.normal(loc=-96.443551, scale=123.56296347408748, size=1)[x]),
        "Pavla Horova&Lesnícka": lambda x: 60/(60-random.normal(loc=-103.02699, scale=133.6331417448475, size=1)[x]),
        "Lesnícka&Suvorovova": lambda x: 2*60/(2*60-random.normal(loc=-109.857091, scale=145.08983580944994, size=1)[x]),
        "Suvorovova&Cintorín Solivar": lambda x: 60/(60-random.normal(loc=-101.574204, scale=145.0996790331486, size=1)[x]),
        "Cintorín Solivar&Na brehu": lambda x: 60/(60-random.normal(loc=-98.397254, scale=148.15787467929147, size=1)[x]),
        "Na brehu&Valkovská": lambda x: 2*60/(2*60-random.normal(loc=-99.057993, scale=148.65118618503098, size=1)[x]-random.normal(loc=-88.275726, scale=132.60439639963673, size=1)[x]), #Pod hradkom missing repeating the process from few lines higher
        "Valkovská&Solivar": lambda x: 60/(60-random.normal(loc=-70.588298, scale=124.82470634222406, size=1)[x]),
    },
    "line12" : {
        "Šidlovec&Stavbárska" : lambda x: 60/(60-random.normal(loc=-100.090854, scale=161.3908700788826, size=1)[x]),
        "Stavbárska&Šidlovská" : lambda x: 60/(60-random.normal(loc=-110.785784, scale=153.48908937574146, size=1)[x]),
        "Šidlovská&Dúbravská" : lambda x: 60/(60-random.normal(loc=-83.195609, scale=107.91830308338731, size=1)[x]),
        "Dúbravská&Pri kaplnke" : lambda x: 60/(60-random.normal(loc=-98.850567, scale=96.12040442376664, size=1)[x]),
        "Pri kaplnke&Dúbrava" : lambda x: 2*60/(2*60-random.normal(loc=-74.347503, scale=98.19561271421871, size=1)[x]),
        "Dúbrava&Veterinárna nemocnica" : lambda x: 2*60/(2*60-random.normal(loc=-75.549814, scale=103.62601800596295, size=1)[x]),
        "Veterinárna nemocnica&Sídlisko III" : lambda x: 2*60/(2*60-random.normal(loc=-63.514407, scale=145.8232666734839, size=1)[x]),
        "Sídlisko III&Prostějovská" : lambda x: 60/(60-random.normal(loc=-62.230863, scale=132.99390839894974, size=1)[x]),
        "Prostějovská&Centrum": lambda x: 60/(60-random.normal(loc=-67.398242, scale=130.81867348464, size=1)[x]),
        "Centrum&VUKOV": lambda x: 2*60/(2*60-random.normal(loc=-52.113147, scale=133.45693909714117, size=1)[x]),
        "VUKOV&Námestie Kráľovnej pokoja": lambda x: 60/(60-random.normal(loc=-64.778165, scale=131.26711749233996, size=1)[x]),
        "Námestie Kráľovnej pokoja&Volgogradská": lambda x: 60/(60-random.normal(loc=-69.696609, scale=138.62954325277832, size=1)[x]),
        "Volgogradská&Marka Čulena": lambda x: 2*60/(2*60-random.normal(loc=-77.249385, scale=163.14552078646247, size=1)[x]),
        "Marka Čulena&Odborárska": lambda x: 60/(60-random.normal(loc=-62.731696, scale=144.80168915625262, size=1)[x]),
        "Odborárska&Sázavského": lambda x: 60/(60-random.normal(loc=-59.109619, scale=127.30642740493037, size=1)[x]),
        "Sázavského&Kollárova": lambda x: 60/(60-random.normal(loc=-92.139106, scale=270.5969908470691, size=1)[x]),
        "Kollárova&SOŠ lesnícka": lambda x: 60/(60-random.normal(loc=-65.089947, scale=120.05966798818653, size=1)[x]),
        "SOŠ lesnícka&Malá stanica": lambda x: 3*60/(3*60-random.normal(loc=-37.667029, scale=132.83438426370245, size=1)[x]),
        "Malá stanica&Kúpeľná": lambda x: 60/(60-random.normal(loc=-48.073103, scale=123.67388670976617, size=1)[x]),
        "Kúpeľná&Pavlovičovo námestie": lambda x: 60/(60-random.normal(loc=-61.028394, scale=118.57516763439719, size=1)[x]),
        "Pavlovičovo námestie&Divadlo Jonáša Záborského": lambda x: 3*60/(3*60-random.normal(loc=-51.856116, scale=134.978363615945, size=1)[x]),
        "Divadlo Jonáša Záborského&Na Hlavnej" : lambda x: 60/(60-random.normal(loc=-46.216906, scale=139.2342695583729, size=1)[x]),
        "Na Hlavnej&Trojica" : lambda x: 2*60/(2*60-random.normal(loc=-44.574048, scale=119.60851708849682, size=1)[x]),
        "Trojica&Duklianska" : lambda x: 2*60/(2*60-random.normal(loc=-55.642441, scale=127.89542000015872, size=1)[x]),
        "Duklianska&Šafárikova, cintorín" : lambda x: 60/(60-random.normal(loc=-44.553233, scale=134.16158641475946, size=1)[x]),
        "Šafárikova, cintorín&Detská nemocnica" : lambda x: 60/(60-random.normal(loc=-53.991744, scale=141.01236489061975, size=1)[x]),
        "Detská nemocnica&Fakultná nemocnica" : lambda x: 60/(60-random.normal(loc=-60.199953, scale=115.2976837521665, size=1)[x]),
        "Fakultná nemocnica&Lesík delostrelcov" : lambda x: 2*60/(2*60-random.normal(loc=-88.770292, scale=138.68025212027655, size=1)[x]),
        "Lesík delostrelcov&Pod Táborom" : lambda x: 60/(60-random.normal(loc=-86.084007, scale=126.60414406722117, size=1)[x]),
        "Pod Táborom&Nižné lúky" : lambda x: 60/(60-random.normal(loc=-76.213597, scale=131.10871837018772, size=1)[x]),
        "Nižné lúky&Jurkovičova" : lambda x: 2*60/(2*60-random.normal(loc=-90.614975, scale=150.64374956944272, size=1)[x]),
        "Jurkovičova&Karpatská": lambda x: 60/(60-random.normal(loc=-122.96367, scale=150.28606407372075, size=1)[x]),
        "Karpatská&Sibírska": lambda x: 2*60/(2*60-random.normal(loc=-76.955375, scale=87.72833141927052, size=1)[x]),
    },
    "line13" : {
        "Veľká pošta&Čierny most": lambda x: 60/(60-random.normal(loc=-50.006959, scale=97.65723632345788, size=1)[x]),
        "Čierny most&Rusínska": lambda x: 3*60/(3*60-random.normal(loc=-111.373091, scale=103.77951720081954, size=1)[x]),
        "Rusínska&Jurkovičova": lambda x: 2*60/(2*60-random.normal(loc=-131.055368, scale=148.012413014417, size=1)[x]),
        "Jurkovičova&Karpatská": lambda x: 60/(60-random.normal(loc=-140.140229, scale=147.08179458604747, size=1)[x]),
        "Karpatská&Nižnianska": lambda x: 3*60/(3*60-random.normal(loc=-125.748584, scale=146.02563450766783, size=1)[x]),
        "Nižnianska&Kalinčiakova": lambda x: 60/(60-random.normal(loc=-91.347958, scale=130.4403489382086, size=1)[x]),
        "Kalinčiakova&Ľubotice": lambda x: 60/(60-random.normal(loc=-66.547258, scale=130.32622348950966, size=1)[x]),
        "Ľubotice&Šalgovícka": lambda x: 60/(60-random.normal(loc=-89.107409, scale=128.39927763304738, size=1)[x]),
        "Šalgovícka&Korabinského": lambda x: 60/(60-random.normal(loc=-81.880706, scale=136.66229712728122, size=1)[x]),
        "Korabinského&Jána Kostru": lambda x: 60/(60-random.normal(loc=-62.303353, scale=125.10995502196121, size=1)[x]),
        "Jána Kostru&Strážnická": lambda x: 60/(60-random.normal(loc=-16.627985, scale=151.9301486070804, size=1)[x]),
        "Strážnická&Šebastovská": lambda x: 60/(60-random.normal(loc=-75.014451, scale=121.1769875079196, size=1)[x]),
        "Šebastovská&Pažica": lambda x: 60/(60-random.normal(loc=-101.412892, scale=123.9345649297214, size=1)[x]),
        "Pažica&Nižná Šebastová": lambda x: 60/(60-random.normal(loc=-86.90119, scale=120.40972952545073, size=1)[x]),
        "Nižná Šebastová&Gen. Ambruša": lambda x: 60/(60-random.normal(loc=-66.11859, scale=133.74008304462183, size=1)[x]),
        "Gen. Ambruša&Herlianska": lambda x: 60/(60-random.normal(loc=-73.168497, scale=125.0741838447014, size=1)[x]),
        "Herlianska&Kamence": lambda x: 3*60/(3*60-random.normal(loc=-71.999427, scale=114.78651399078998, size=1)[x]),
        "Kamence&Rázcestie Vyšná Šebastová": lambda x: 60/(60-random.normal(loc=-69.314069, scale=127.5266218638249, size=1)[x]),
        "Rázcestie Vyšná Šebastová&Obecný úrad Vyšná Šebastová": lambda x: 60/(60-random.normal(loc=-100.954323, scale=144.51026006787316, size=1)[x]),
        "Obecný úrad Vyšná Šebastová&Vyšná Šebastová": lambda x: 2*60/(2*60-random.normal(loc=-92.037457, scale=176.8837885934269, size=1)[x]-random.normal(loc=-44.097988, scale=156.28379602211425, size=1)[x]), #special case again
    },
    "line14" : {
        "Kanaš - Stráže&Stará škola" : lambda x: 60/(60-random.normal(loc=-82.02898, scale=114.95141834942578, size=1)[x]),
        "Stará škola&Medzi jarkami" : lambda x: 60/(60-random.normal(loc=-68.393852, scale=140.25056389568581, size=1)[x]),
        "Medzi jarkami&Pri kostole" : lambda x: 60/(60-random.normal(loc=-61.036074, scale=128.2530241666699, size=1)[x]),
        "Pri kostole&Husí hrb" : lambda x: 60/(60-random.normal(loc=-66.226289, scale=130.06323248858763, size=1)[x]),
        "Husí hrb&Kozí rožok" : lambda x: 2*60/(2*60-random.normal(loc=-64.675, scale=125.39737719592891, size=1)[x]),
        "Kozí rožok&Sordok" : lambda x: 2*60/(2*60-random.normal(loc=-66.801611, scale=122.8218199526224, size=1)[x]),
        "Sordok&Rázcestie Kanaš" : lambda x: 2*60/(2*60-random.normal(loc=-54.754391, scale=111.42785051568735, size=1)[x]),
        "Rázcestie Kanaš&Bikoš" : lambda x: 4*60/(4*60-random.normal(loc=-74.695182, scale=61.307897656303105, size=1)[x]),
        "Bikoš&Dúbrava" : lambda x: 60/(60-random.normal(loc=-41.35861, scale=124.97189093784051, size=1)[x]),
        "Dúbrava&Rázcestie Šidlovec" : lambda x: 2*60/(2*60-random.normal(loc=-22.007246, scale=118.20949676466661, size=1)[x]),
        "Rázcestie Šidlovec&Pod Skalkou" : lambda x: 60/(60-random.normal(loc=-31.966773, scale=113.25647710313821, size=1)[x]),
        "Pod Skalkou&Mičurinova" : lambda x: 60/(60-random.normal(loc=-31.389769, scale=142.8673791729123, size=1)[x]),
        "Mičurinova&Sabinovská" : lambda x: 60/(60-random.normal(loc=-58.777442, scale=146.22314163479047, size=1)[x]),
        "Sabinovská&Trojica" : lambda x: 3*60/(3*60-random.normal(loc=-53.63767, scale=132.63188477825793, size=1)[x]),
        "Trojica&Na Hlavnej": lambda x: 2*60/(2*60-random.normal(loc=-35.116135, scale=138.3280009831043, size=1)[x]),
        "Na Hlavnej&Veľká pošta": lambda x: 2*60/(2*60-random.normal(loc=-28.734789, scale=137.09562254614997, size=1)[x]),
        "Veľká pošta&Čierny most": lambda x: 60/(60-random.normal(loc=-37.483505, scale=115.17721655823551, size=1)[x]),
        "Čierny most&Železničná stanica": lambda x: 2*60/(2*60-random.normal(loc=-69.548491, scale=113.89666353337954, size=1)[x]),
        "Železničná stanica&Nový Solivar": lambda x: 60/(60-random.normal(loc=-72.229123, scale=102.69373141904497, size=1)[x]),
        "Nový Solivar&Košická": lambda x: 60/(60-random.normal(loc=-69.065471, scale=97.23394294049727, size=1)[x]),
        "Košická&Petrovianska": lambda x: 3*60/(3*60-random.normal(loc=-62.929805, scale=91.243018607392, size=1)[x]),
        "Petrovianska&Logistické centrum": lambda x: 2*60/(2*60-random.normal(loc=-45.065968, scale=91.6639311263639, size=1)[x]),
        "Logistické centrum&Rázcestie Záborské": lambda x: 3*60/(3*60-random.normal(loc=-58.460529, scale=104.23204304545774, size=1)[x]),
        "Rázcestie Záborské&Záborské - stred": lambda x: 60/(60-random.normal(loc=-75.99596, scale=112.03406085541995, size=1)[x]),
        "Záborské - stred&Záborské": lambda x: 60/(60-random.normal(loc=-53.249926, scale=134.75367583127021, size=1)[x]),
    },
    "line15" : {
        "Za Kalváriou&Hôrka" : lambda x: 60/(60-random.normal(loc=-32.152426, scale=49.62320866695444, size=1)[x]),
        "Hôrka&Záhradkárska osada" : lambda x: 60/(60-random.normal(loc=-50.626534, scale=129.04418293561017, size=1)[x]),
        "Záhradkárska osada&Horárska" : lambda x: 60/(60-random.normal(loc=-50.830955, scale=121.18268256814515, size=1)[x]),
        "Horárska&Zimný štadión" : lambda x: 60/(60-random.normal(loc=-69.491316, scale=112.58371824306592, size=1)[x]),
        "Zimný štadión&Pod Kalváriou" : lambda x: 60/(60-random.normal(loc=-86.629716, scale=69.12440423553309, size=1)[x]),
        "Pod Kalváriou&SOŠ lesnícka" : lambda x: 60/(60-random.normal(loc=-72.784229, scale=72.2296385643975, size=1)[x]),
        "SOŠ lesnícka&Kollárova" : lambda x: 60/(60-random.normal(loc=-87.397753, scale=112.65743638339278, size=1)[x]),
        "Kollárova&Sázavského" : lambda x: 60/(60-random.normal(loc=-77.399602, scale=107.82342470992062, size=1)[x]),
        "Sázavského&Odborárska" : lambda x: 60/(60-random.normal(loc=-73.613575, scale=112.54707960186516, size=1)[x]),
        "Odborárska&Centrál" : lambda x: 60/(60-random.normal(loc=-82.196621, scale=95.05309238843377, size=1)[x]),
        "Centrál&Poliklinika" : lambda x: 2*60/(2*60-random.normal(loc=-100.820312, scale=134.6994094940565, size=1)[x]),
        "Poliklinika&Trojica": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-75.57347, scale=137.41032113301745, size=1)[x]),
        "Trojica&Na Hlavnej": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-38.90688, scale=125.75868085704286, size=1)[x]),
        "Na Hlavnej&Grešova": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-36.482539, scale=132.9633603140287, size=1)[x]),
        "Grešova&Fakultná nemocnica": lambda x: 3 * 60 / (3 * 60 -random.normal(loc=-40.032727, scale=149.62580949929585, size=1)[x]),
        "Fakultná nemocnica&Detská nemocnica": lambda x: 60 / (60 + 0), #missing delays numbers in my table for unknow reason
    },
    "line17" : {
        "Sídlisko III&Prostějovská" : lambda x: 60/(60-random.normal(loc=-18.225564, scale=37.899639904391016, size=1)[x]),
        "Prostějovská&Centrum": lambda x: 60/(60-random.normal(loc=-40.436526, scale=55.72675224093754, size=1)[x]),
        "Centrum&VUKOV": lambda x: 2*60/(2*60-random.normal(loc=-39.667996, scale=86.5638293573762, size=1)[x]),
        "VUKOV&Námestie Kráľovnej pokoja": lambda x: 60/(60-random.normal(loc=-32.150907, scale=70.75932921598731, size=1)[x]),
        "Námestie Kráľovnej pokoja&Volgogradská": lambda x: 60/(60-random.normal(loc=-47.2879, scale=77.75883158682343, size=1)[x]),
        "Volgogradská&Levočská": lambda x: 2*60/(2*60-random.normal(loc=-53.604735, scale=100.7390167915397, size=1)[x]),
        "Levočská&Poliklinika": lambda x: 2*60/(2*60-random.normal(loc=-124.641587, scale=163.65541221232053, size=1)[x]),
        "Poliklinika&Duklianska": lambda x: 2*60/(2*60-random.normal(loc=-124.641587, scale=211.47127105440336, size=1)[x]),
        "Duklianska&Rázcestie Kúty" : lambda x: 2*60/(2*60-random.normal(loc=-100.317032, scale=159.6994827349009, size=1)[x]),
        "Rázcestie Kúty&Dopravný podnik" : lambda x: 60/(60-random.normal(loc=-105.50912, scale=179.1787440509759, size=1)[x]),
        "Dopravný podnik&Ľubochnianska" : lambda x: 2*60/(2*60-random.normal(loc=-114.336425, scale=180.5464888123646, size=1)[x]),
        "Ľubochnianska&Strojnícka" : lambda x: 60/(60-random.normal(loc=-101.901786, scale=167.5410642532061, size=1)[x]),
        "Strojnícka&Družstevná" : lambda x: 60/(60-random.normal(loc=-107.404075, scale=161.7463997873764, size=1)[x]),
        "Družstevná&Širpo" : lambda x: 60/(60-random.normal(loc=-18.177914, scale=81.83868017974869, size=1)[x]),
    },
    "line18" : {
        "Bzenov&Rázcestie Janov" : lambda x: 2*60/(2*60-random.normal(loc=-66.896648, scale=162.0121886807567, size=1)[x]),
        "Rázcestie Janov&Obecný úrad Bzenov" : lambda x: 60/(60-random.normal(loc=-60.003228, scale=178.86596623944607, size=1)[x]),
        "Obecný úrad Bzenov&Chatky" : lambda x: 4*60/(4*60-random.normal(loc=-63.721658, scale=186.65189266533042, size=1)[x]),
        "Chatky&Čertov kameň" : lambda x: 60/(60-random.normal(loc=-75.392273, scale=186.15412633512148, size=1)[x]),
        "Čertov kameň&Cemjata" : lambda x: 60/(60-random.normal(loc=-64.678297, scale=156.85561014060426, size=1)[x]),
        "Cemjata&Školské lesy" : lambda x: 60/(60-random.normal(loc=-48.883735, scale=104.5707863418685, size=1)[x]),
        "Školské lesy&Zabíjaná" : lambda x: 60/(60-random.normal(loc=-39.536036, scale=114.47336198131858, size=1)[x]),
        "Zabíjaná&Kvašná voda" : lambda x: 3*60/(3*60-random.normal(loc=-39.178626, scale=122.6487659084899, size=1)[x]),
        "Kvašná voda&Vydumanec" : lambda x: 2*60/(2*60-random.normal(loc=-42.944479, scale=126.22878576618415, size=1)[x]),
        "Vydumanec&Rázcestie Cemjata" : lambda x: 2*60/(2*60-random.normal(loc=-70.460685, scale=342.38839925783753, size=1)[x]),
        "Rázcestie Cemjata&Mýto" : lambda x: 60/(60-random.normal(loc=-37.793409, scale=118.4926820203492, size=1)[x]),
        "Mýto&Levočská" : lambda x: 2*60/(2*60-random.normal(loc=-43.251077, scale=124.49986337883756, size=1)[x]),
        "Levočská&Poliklinika" : lambda x: 2*60/(2*60-random.normal(loc=-82.570849, scale=118.97303744738946, size=1)[x]),
        "Poliklinika&Trojica": lambda x: 2*60/(2*60-random.normal(loc=-83.760303, scale=104.54134955865607, size=1)[x]),
        "Trojica&Na Hlavnej": lambda x: 2*60/(2*60-random.normal(loc=-61.051271, scale=101.301206347891, size=1)[x]),
        "Na Hlavnej&Veľká pošta": lambda x: 2*60/(2*60-random.normal(loc=-81.783245, scale=134.84868023914862, size=1)[x]), #using the delay from diferent stop bcs this is is not in my data
    },
    "line19" : {
        "Solivar&Kukučínova" : lambda x: 60/(60-random.normal(loc=-43.472371, scale=52.766057992281965, size=1)[x]),
        "Kukučínova&Kysucká" : lambda x: 60/(60-random.normal(loc=-111.081006, scale=150.02466668757233, size=1)[x]),
        "Kysucká&Laca Novomeského" : lambda x: 60/(60-random.normal(loc=-108.111812, scale=134.8858888373629, size=1)[x]),
        "Laca Novomeského&Martina Benku" : lambda x: 2*60/(2*60-random.normal(loc=-130.224365, scale=140.4529392860413, size=1)[x]),
        "Martina Benku&Pavla Horova": lambda x: 60 / (60 -random.normal(loc=-127.825674, scale=148.41915983437082, size=1)[x]),
        "Pavla Horova&Lesnícka": lambda x: 60 / (60 -random.normal(loc=-113.676699, scale=130.4516131127445, size=1)[x]),
        "Lesnícka&Lomnická": lambda x: 2*60 / (2*60 -random.normal(loc=-127.98462, scale=127.49937043788233, size=1)[x]),
        "Lomnická&Švábska": lambda x: 60 / (60 -random.normal(loc=-118.535495, scale=131.95349200464298, size=1)[x]),
        "Švábska&Chalupkova": lambda x: 60 / (60 -random.normal(loc=-105.958118, scale=125.63388749790806, size=1)[x]),
        "Chalupkova&Košická": lambda x: 60 / (60 -random.normal(loc=-123.10363, scale=131.69946328102262, size=1)[x]),
        "Košická&Nový Solivar": lambda x: 60 / (60 -random.normal(loc=-104.362505, scale=125.2916153301239, size=1)[x]),
        "Nový Solivar&Železničná stanica": lambda x: 60 / (60 -random.normal(loc=-115.763283, scale=114.42096746316871, size=1)[x]),
        "Železničná stanica&Čierny most": lambda x: 2*60 / (2*60 -random.normal(loc=-115.875236, scale=129.4590355172324, size=1)[x]),
        "Čierny most&Grešova": lambda x: 2*60 / (2*60 -random.normal(loc=-144.770419, scale=110.77384181546405, size=1)[x]),
        "Grešova&Fakultná nemocnica": lambda x: 3*60 / (3*60 -random.normal(loc=-131.673269, scale=116.0827115015198, size=1)[x]), #joinked from bus line 10 bcs the stuff...
    },
    "line21" : {
        "Fintice&V kopci" : lambda x: 2*60/(2*60-random.normal(loc=-37.794279, scale=61.13436328543678, size=1)[x]-random.normal(loc=-53.413738, scale=125.53206873981189, size=1)[x]), #stop missing
        "V kopci&Námestie Jozefa Kolarčíka" : lambda x: 60/(60-random.normal(loc=-52.278503, scale=123.50953306487926, size=1)[x]),
        "Námestie Jozefa Kolarčíka&Červený mostík" : lambda x: 60/(60-random.normal(loc=-44.742182, scale=116.86218549491755, size=1)[x]),
        "Červený mostík&Ihrisko" : lambda x: 60/(60-random.normal(loc=-42.14433, scale=112.9302270867057, size=1)[x]),
        "Ihrisko&Gribľovec" : lambda x: 60/(60-random.normal(loc=-44.263625, scale=108.13778341311583, size=1)[x]),
        "Gribľovec&Za traťou" : lambda x: 60/(60-random.normal(loc=-42.037495, scale=108.0453882388663, size=1)[x]),
        "Za traťou&Išľa" : lambda x: 60/(60-random.normal(loc=-46.299268, scale=106.84283845020731, size=1)[x]),
        "Išľa&Fintická" : lambda x: 60/(60-random.normal(loc=-40.279023, scale=110.79296498257139, size=1)[x]),
        "Fintická&Nová" : lambda x: 60/(60-random.normal(loc=-31.125628, scale=108.60900422410694, size=1)[x]),
        "Nová&Vranovská" : lambda x: 2*60/(2*60-random.normal(loc=-36.885146, scale=113.00243075905667, size=1)[x]),
        "Vranovská&Šarišské Lúky" : lambda x: 60/(60-random.normal(loc=-51.565058, scale=109.89909691799957, size=1)[x]),
        "Šarišské Lúky&Dopravný podnik" : lambda x: 2*60/(2*60-random.normal(loc=-47.678929, scale=105.41527066665945, size=1)[x]),
        "Dopravný podnik&Rázcestie Kúty": lambda x: 60/(60-random.normal(loc=-63.114898, scale=103.08707066154825, size=1)[x]),
        "Rázcestie Kúty&Duklianska": lambda x: 2*60/(2*60-random.normal(loc=-75.932908, scale=118.65320288906403, size=1)[x]),
        "Duklianska&Trojica": lambda x: 2*60/(2*60+0),  #missing data
    },
    "line22" : {
        "Teriakovce&OÚ Teriakovce" : lambda x: 60/(60-random.normal(loc=-37.437742, scale=70.92558270848164, size=1)[x]),
        "OÚ Teriakovce&Na Kruhu" : lambda x: 60/(60-random.normal(loc=-78.939274, scale=171.63757027249542, size=1)[x]),
        "Na Kruhu&Rázcestie Teriakovce" : lambda x: 30/(30-random.normal(loc=-85.527969, scale=169.69713476720432, size=1)[x]), #less then minute well thats great, what about tell me precise seconds -_-
        "Rázcestie Teriakovce&Šalgovia" : lambda x: 60/(60-random.normal(loc=-87.862455, scale=169.69713476720432, size=1)[x]),
        "Šalgovia&Labutia" : lambda x: 60/(60-random.normal(loc=-83.616064, scale=161.7770950937114, size=1)[x]),
        "Labutia&Šalgovík" : lambda x: 60/(60-random.normal(loc=-90.527766, scale=159.04450252799973, size=1)[x]),
        "Šalgovík&Hruny" : lambda x: 2*60/(2*60-random.normal(loc=-43.579072, scale=110.09850022226878, size=1)[x]-random.normal(loc=-21.276217, scale=91.58547390259403, size=1)[x]), #missing bus stop on the map
        "Hruny&Pod Šalgovíkom" : lambda x: 60/(60-random.normal(loc=-16.099736, scale=141.08415525977995, size=1)[x]),
        "Pod Šalgovíkom&Vansovej" : lambda x: 60/(60-random.normal(loc=-116.005618, scale=199.98298371925673, size=1)[x]),
        "Vansovej&Laca Novomeského" : lambda x: 60/(60-random.normal(loc=-118.955012, scale=169.9554953794131, size=1)[x]),
        "Laca Novomeského&Vyšné lúky" : lambda x: 2*60/(2*60-random.normal(loc=-122.704022, scale=177.75379292055513, size=1)[x]),
        "Vyšné lúky&Nižné lúky" : lambda x: 60/(60-random.normal(loc=-81.434033, scale=151.21852803292225, size=1)[x]),
        "Nižné lúky&Pod Táborom" : lambda x: 60/(60-random.normal(loc=-80.588631, scale=154.6441477914826, size=1)[x]),
        "Pod Táborom&Lesík delostrelcov" : lambda x: 60/(60-random.normal(loc=-54.45338, scale=111.68843693118279, size=1)[x]),
        "Lesík delostrelcov&Kpt. Nálepku" : lambda x: 60/(60-random.normal(loc=-63.410005, scale=125.15995401281515, size=1)[x]),
        "Kpt. Nálepku&Divadlo Jonáša Záborského" : lambda x: 2*60/(2*60-random.normal(loc=-59.088862, scale=110.0622918718092, size=1)[x]),
        "Divadlo Jonáša Záborského&Na Hlavnej" : lambda x: 60/(60-random.normal(loc=-56.629138, scale=113.4790665109584, size=1)[x]),
        "Na Hlavnej&Trojica" : lambda x: 2*60/(2*60-random.normal(loc=-58.588906, scale=107.60756594585627, size=1)[x]),
        "Trojica&Sabinovská" : lambda x: 3*60/(3*60-random.normal(loc=-104.529038, scale=152.714225697113, size=1)[x]),
        "Sabinovská&Mičurinova" : lambda x: 60/(60-random.normal(loc=-99.531812, scale=193.9954181238862, size=1)[x]),
        "Mičurinova&Pod Skalkou" : lambda x: 60/(60-random.normal(loc=-103.501821, scale=175.1816029059332, size=1)[x]),
        "Pod Skalkou&Rázcestie Šidlovec" : lambda x: 60/(60-random.normal(loc=-86.473029, scale=105.7794256106936, size=1)[x]),
        "Rázcestie Šidlovec&Jánošíkova" : lambda x: 2*60/(2*60-random.normal(loc=-52.852956, scale=126.7995638861728, size=1)[x]),
        "Jánošíkova&Šidlovská" : lambda x: 60/(60-random.normal(loc=-39.064145, scale=134.25143948060145, size=1)[x]),
        "Šidlovská&Jahodová" : lambda x: 60/(60-random.normal(loc=-27.714834, scale=130.30876533665804, size=1)[x]),
        "Jahodová&Šidlovec" : lambda x: 60/(60+0), #corrupted data I guess? 1963 ahead of time
    },
    "line23" : {
        "Veľký Šariš&Varoš" : lambda x: 60/(60-random.normal(loc=-28.446384, scale=24.07102423294628, size=1)[x]),
        "Varoš&Tulčícka" : lambda x: 60/(60-random.normal(loc=-27.594096, scale=24.07102423294628, size=1)[x]),
        "Tulčícka&Malý Šariš" : lambda x: 4*60/(4*60-random.normal(loc=-12.715796, scale=61.35382231038649, size=1)[x]),
        "Malý Šariš&Šľachtiteľská stanica" : lambda x: 60/(60-random.normal(loc=-25.842738, scale=36.53200243790298, size=1)[x]),
        "Šľachtiteľská stanica&Nákupné stredisko" : lambda x: 60/(60-random.normal(loc=-9.19309, scale=98.10666896931585, size=1)[x]),
        "Nákupné stredisko&Obecný úrad Malý Šariš" : lambda x: 60/(60-random.normal(loc=-8.366928, scale=97.07363089312926, size=1)[x]),
        "Obecný úrad Malý Šariš&Rázcestie Malý Šariš" : lambda x: 60/(60-random.normal(loc=-17.368778, scale=93.16423656708801, size=1)[x]),
        "Rázcestie Malý Šariš&Telekča" : lambda x: 2*60/(2*60-random.normal(loc=-21.609133, scale=99.7435237967014, size=1)[x]),
        "Telekča&Rázcestie Cemjata" : lambda x: 2*60/(2*60-random.normal(loc=-14.66058, scale=101.72778473744724, size=1)[x]),
        "Rázcestie Cemjata&Mýto" : lambda x: 60/(60-random.normal(loc=-20.918495, scale=101.6043633304872, size=1)[x]),
        "Mýto&Levočská": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-23.571168, scale=108.0509951088345, size=1)[x]),
        "Levočská&Poliklinika": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-49.343573, scale=108.67720452281415, size=1)[x]),
        "Poliklinika&Trojica": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-21.20354, scale=70.70744403764648, size=1)[x]),
    },
    "line24" : {
        "Haniska&Lemešianska" : lambda x: 60/(60-random.normal(loc=-29.804107, scale=63.95233581531636, size=1)[x]),
        "Lemešianska&Priecestie" : lambda x: 60/(60-random.normal(loc=-7.124472, scale=81.74328870896684, size=1)[x]),
        "Priecestie&Čistička" : lambda x: 2*60/(2*60-random.normal(loc=-7.515488, scale=86.18464131594698, size=1)[x]),
        "Čistička&Gemor" : lambda x: 60/(60-random.normal(loc=-17.22655, scale=105.5308551956262, size=1)[x]),
        "Gemor&ZVL" : lambda x: 60/(60-random.normal(loc=-7.018667, scale=85.7139252682368, size=1)[x]),
        "ZVL&Košická" : lambda x: 60/(60-random.normal(loc=-17.840986, scale=87.36098738349396, size=1)[x]),
        "Košická&Nový Solivar": lambda x: 60 / (60 -random.normal(loc=-39.544335, scale=94.99464510543343, size=1)[x]),
        "Nový Solivar&Železničná stanica": lambda x: 60 / (60 -random.normal(loc=-41.085126, scale=105.29757787631176, size=1)[x]),
        "Železničná stanica&Čierny most": lambda x: 2*60 / (2*60 -random.normal(loc=-51.380011, scale=96.39586575997707, size=1)[x]),
        "Čierny most&Divadlo Jonáša Záborského": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-72.791092, scale=97.77713062476539, size=1)[x]),
        "Divadlo Jonáša Záborského&Na Hlavnej": lambda x: 60 / (60 -random.normal(loc=-70.718946, scale=99.85076093408112, size=1)[x]),
        "Na Hlavnej&Trojica": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-60.569565, scale=122.61002843863967, size=1)[x]),
        "Trojica&Poliklinika": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-100.854779, scale=125.3937733552782, size=1)[x]),
        "Poliklinika&Obrancov mieru": lambda x: 3 * 60 / (3 * 60 + 0), #missing data
    },
    "line26" : {
        "Veľká pošta&Čierny most": lambda x: 60/(60-random.normal(loc=-39.285188, scale=50.039370146762, size=1)[x]),
        "Čierny most&Železničná stanica": lambda x: 2*60/(2*60-random.normal(loc=-65.268075, scale=67.32246668615139, size=1)[x]),
        "Železničná stanica&Nový Solivar": lambda x: 60/(60-random.normal(loc=-47.335363, scale=74.47348736088524, size=1)[x]),
        "Nový Solivar&Košická": lambda x: 60/(60-random.normal(loc=-52.729666, scale=70.16144173932541, size=1)[x]),
        "Košická&Spinea - Záturecká": lambda x: 5*60/(5*60-random.normal(loc=-19.21864, scale=47.22057672005057, size=1)[x]-random.normal(loc=-17.656556, scale=57.66399612578062, size=1)[x]), #corrupted data using back road
    },
    "line27" : {
        "Za Kalváriou&Hôrka" : lambda x: 60/(60-random.normal(loc=-24.506826, scale=85.6985795707101, size=1)[x]),
        "Hôrka&Záhradkárska osada" : lambda x: 60/(60-random.normal(loc=-60.944095, scale=121.75790138525193, size=1)[x]),
        "Záhradkárska osada&Horárska" : lambda x: 60/(60-random.normal(loc=-73.107243, scale=127.72496532964037, size=1)[x]),
        "Horárska&Slávičia" : lambda x: 60/(60-random.normal(loc=-8.497596, scale=59.83147401395914, size=1)[x]),
        "Slávičia&Pod Kamennou baňou" : lambda x: 2*60/(2*60-random.normal(loc=6.004841, scale=67.81770867483107, size=1)[x]), #no this is not mistake its serously doesnt have a delay but its going faster then graficon
        "Pod Kamennou baňou&Mestská hala" : lambda x: 60/(60-random.normal(loc=-32.926868, scale=106.90529062181265, size=1)[x]),
        "Mestská hala&Škultétyho" : lambda x: 60/(60-random.normal(loc=-39.08377, scale=115.81470554974479, size=1)[x]),
        "Škultétyho&Čierny most" : lambda x: 2*60/(2*60-random.normal(loc=-47.370273, scale=116.96002515307332, size=1)[x]),
        "Čierny most&Divadlo Jonáša Záborského": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-26.086439, scale=89.57603204096719, size=1)[x]),
        "Divadlo Jonáša Záborského&Na Hlavnej": lambda x: 60 / (60 -random.normal(loc=-34.879752, scale=87.11839033442521, size=1)[x]),
        "Na Hlavnej&Trojica": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-34.003375, scale=107.85553484176494, size=1)[x]),
        "Trojica&Duklianska": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-62.693252, scale=114.94019374674262, size=1)[x]),
        "Duklianska&Šafárikova, cintorín": lambda x: 60 / (60 -random.normal(loc=7.917971, scale=143.29147424101038, size=1)[x]), #fast bus again
        "Šafárikova, cintorín&Vodárenská": lambda x: 60 / (60 -random.normal(loc=-6.277514, scale=90.8709503680014, size=1)[x]),
        "Vodárenská&Hviezdna": lambda x: 60 / (60 -random.normal(loc=-70.540757, scale=91.52487902252771, size=1)[x]),
    },
    "line28" : {
        "Ľubotice&Šalgovícka" : lambda x: 60/(60-random.normal(loc=-41.999275, scale=65.06196960794749, size=1)[x]),
        "Šalgovícka&Korabinského" : lambda x: 60/(60-random.normal(loc=-43.265692, scale=48.55187522660749, size=1)[x]),
        "Korabinského&Jána Kostru" : lambda x: 60/(60-random.normal(loc=-37.475772, scale=51.900928894659806, size=1)[x]),
        "Jána Kostru&Strážnická" : lambda x: 60/(60-random.normal(loc=-43.606984, scale=53.88073498350462, size=1)[x]),
        "Strážnická&Bardejovská" : lambda x: 60/(60-random.normal(loc=-50.880145, scale=55.046570630667325, size=1)[x]),
        "Bardejovská&Domašská" : lambda x: 60/(60-random.normal(loc=-53.669136, scale=59.91698985192526, size=1)[x]),
        "Domašská&Kalinčiakova" : lambda x: 60/(60-random.normal(loc=-43.301695, scale=61.339966303005255, size=1)[x]),
        "Kalinčiakova&Nižnianska" : lambda x: 60/(60-random.normal(loc=-48.785865, scale=75.41416295135305, size=1)[x]),
        "Nižnianska&Dopravný podnik" : lambda x: 3*60/(3*60-random.normal(loc=-47.341596, scale=80.61147037329474, size=1)[x]),
        "Dopravný podnik&Rázcestie Kúty": lambda x: 60/(60-random.normal(loc=-43.330595, scale=85.23117322647275, size=1)[x]),
        "Rázcestie Kúty&Duklianska": lambda x: 2*60/(2*60-random.normal(loc=-68.511975, scale=117.99101385831175, size=1)[x]),
        "Duklianska&Trojica": lambda x: 2*60/(2*60-random.normal(loc=-89.488098, scale=120.64471809561482, size=1)[x]),
        "Trojica&Na Hlavnej": lambda x: 2*60/(2*60-random.normal(loc=-50.702116, scale=102.73239042896063, size=1)[x]),
        "Na Hlavnej&Veľká pošta": lambda x: 2*60/(2*60-random.normal(loc=-61.141894, scale=134.5393380269022, size=1)[x]),
        "Veľká pošta&Čierny most": lambda x: 60/(60-random.normal(loc=-58.287459, scale=136.90115996036167, size=1)[x]),
        "Čierny most&Železničná stanica": lambda x: 2*60/(2*60-random.normal(loc=-67.297706, scale=119.41180577588693, size=1)[x]),
        "Železničná stanica&Škára": lambda x: 2*60/(2*60-random.normal(loc=-89.671346, scale=128.12551729237575, size=1)[x]),
        "Škára&Lomnická": lambda x: 3*60/(3*60-random.normal(loc=-84.807413, scale=136.9312146121631, size=1)[x]),
        "Lomnická&Švábska": lambda x: 60/(60-random.normal(loc=-67.577705, scale=126.99102359626848, size=1)[x]),
        "Švábska&Pionierska": lambda x: 60/(60-random.normal(loc=-69.932089, scale=148.33392472610132, size=1)[x]),
        "Pionierska&Jesenná": lambda x: 60/(60-random.normal(loc=-66.580701, scale=140.48258966851753, size=1)[x]),
        "Jesenná&Jelšová": lambda x: 60/(60-random.normal(loc=-59.568331, scale=118.42888332065841, size=1)[x]),
        "Jelšová&Delňa": lambda x: 60/(60-random.normal(loc=-46.478383, scale=49.77221042354581, size=1)[x]),
    },
    "line29" : {
        "Sídlisko III&Prostějovská" : lambda x: 60/(60-random.normal(loc=-37.444444, scale=51.15701629647711, size=1)[x]),
        "Prostějovská&Centrum": lambda x: 60/(60-random.normal(loc=-64.133562, scale=133.82773494585967, size=1)[x]),
        "Centrum&VUKOV": lambda x: 2*60/(2*60-random.normal(loc=-70.785216, scale=158.51790978053253, size=1)[x]),
        "VUKOV&Námestie Kráľovnej pokoja": lambda x: 60/(60-random.normal(loc=-73.971301, scale=152.9798289289838, size=1)[x]),
        "Námestie Kráľovnej pokoja&Volgogradská": lambda x: 60/(60-random.normal(loc=-83.388738, scale=173.92734095528155, size=1)[x]),
        "Volgogradská&Levočská": lambda x: 2*60/(2*60-random.normal(loc=-86.079118, scale=161.11617230074887, size=1)[x]),
        "Levočská&Poliklinika": lambda x: 2*60/(2*60-random.normal(loc=-118.115344, scale=187.36185234840244, size=1)[x]),
        "Poliklinika&Floriánova": lambda x: 60/(60-random.normal(loc=-109.628474, scale=198.7028197552184, size=1)[x]),
        "Floriánova&Okružná": lambda x: 2*60/(2*60-random.normal(loc=-87.030599, scale=176.6887975507185, size=1)[x]),
        "Okružná&Grešova": lambda x: 2*60/(2*60-random.normal(loc=-82.716384, scale=188.27255500195338, size=1)[x]),
        "Grešova&Fakultná nemocnica": lambda x: 3 * 60 / (3 * 60 -random.normal(loc=-75.892441, scale=176.05717619192976, size=1)[x]),
        "Fakultná nemocnica&Detská nemocnica": lambda x: 60 / (60 -random.normal(loc=-180.0, scale=8.0, size=1)[x]),
    },
    "line30" : {
        "Železničná stanica&Štúrova" : lambda x: 2*60/(2*60-random.normal(loc=-114.286689, scale=62.87329254125813, size=1)[x]),
        "Štúrova&Priemyselné centrum" : lambda x: 60/(60-random.normal(loc=-32.187293, scale=74.35790902223236, size=1)[x]),
        "Priemyselné centrum&Pekárne" : lambda x: 60/(60-random.normal(loc=-22.527969, scale=68.46809380329303, size=1)[x]),
        "Pekárne&Budovateľská" : lambda x: 60/(60+0), #missing data
    },
    "line32" : {
        "Sibírska&Karpatská" : lambda x: 2*60/(2*60-random.normal(loc=-61.235383, scale=75.42610451446879, size=1)[x]),
        "Karpatská&Jurkovičova" : lambda x: 60/(60-random.normal(loc=-178.461518, scale=187.22259058997025, size=1)[x]),
        "Jurkovičova&Rusínska" : lambda x: 2*60/(2*60-random.normal(loc=-176.2562, scale=187.22025705002923, size=1)[x]),
        "Rusínska&Hobby park" : lambda x: 60/(60-random.normal(loc=-58.394794, scale=78.62965189135397, size=1)[x]),
        "Hobby park&Čierny most" : lambda x: 2*60/(2*60-random.normal(loc=-105.166539, scale=125.55148252439918, size=1)[x]),
        "Čierny most&Divadlo Jonáša Záborského": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-135.341939, scale=139.83800724544508, size=1)[x]),
        "Divadlo Jonáša Záborského&Na Hlavnej": lambda x: 60 / (60 -random.normal(loc=-128.80991, scale=141.14919233346075, size=1)[x]),
        "Na Hlavnej&Trojica": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-70.551538, scale=117.92313189571693, size=1)[x]),
    },
    "line32A" : {
        "Sibírska&Karpatská" : lambda x: 2*60/(2*60-random.normal(loc=-40.379324, scale=56.78627334076701, size=1)[x]),
        "Karpatská&Jurkovičova" : lambda x: 60/(60-random.normal(loc=-62.650235, scale=63.62047092705811, size=1)[x]),
        "Jurkovičova&Rusínska" : lambda x: 2*60/(2*60-random.normal(loc=-62.964016, scale=66.24866007012237, size=1)[x]),
        "Rusínska&Čierny most" : lambda x: 3*60/(3*60-random.normal(loc=-39.823997, scale=66.6489922652994, size=1)[x]-random.normal(loc=-60.279083, scale=84.9906842044125, size=1)[x]), #missing data combing 2 stops together
        "Čierny most&Okružná" : lambda x: 3*60/(3*60-random.normal(loc=-111.142857, scale=165.57383210384128, size=1)[x]),
    },
    "line33" : {
        "Delňa&Jelšová" : lambda x: 60/(60-random.normal(loc=-26.998199, scale=52.30496841263711, size=1)[x]),
        "Jelšová&Jesenná" : lambda x: 60/(60-random.normal(loc=-44.591309, scale=107.97007730031301, size=1)[x]),
        "Jesenná&Pionierska" : lambda x: 60/(60-random.normal(loc=-50.671256, scale=128.63504399602863, size=1)[x]),
        "Pionierska&Švábska" : lambda x: 60/(60-random.normal(loc=-42.970772, scale=121.38762418143686, size=1)[x]),
        "Švábska&Lomnická": lambda x: 60/(60-random.normal(loc=-55.966088, scale=117.77982708042317, size=1)[x]),
        "Lomnická&Lesnícka": lambda x: 2*60/(2*60-random.normal(loc=-67.62882, scale=125.60792539074735, size=1)[x]),
        "Lesnícka&Pavla Horova": lambda x: 60/(60-random.normal(loc=-65.631604, scale=124.44995448377144, size=1)[x]),
        "Pavla Horova&Martina Benku": lambda x: 60/(60-random.normal(loc=-59.679834, scale=109.50183068734903, size=1)[x]),
        "Martina Benku&Jurkovičova": lambda x: 2*60/(2*60-random.normal(loc=-66.143128, scale=101.62885202868615, size=1)[x]),
        "Jurkovičova&Karpatská": lambda x: 60/(60-random.normal(loc=-86.141755, scale=113.5539636091512, size=1)[x]),
        "Karpatská&Pod nadjazdom": lambda x: 3*60/(3*60-random.normal(loc=-139.289655, scale=118.41615204607159, size=1)[x]),
        "Pod nadjazdom&Ľubochnianska": lambda x: 3*60/(3*60-random.normal(loc=-100.624362, scale=96.83516050248615, size=1)[x]),
        "Ľubochnianska&Strojnícka": lambda x: 60 / (60 -random.normal(loc=-27.942373, scale=74.72326391854563, size=1)[x]),
        "Strojnícka&Družstevná": lambda x: 60 / (60 -random.normal(loc=-25.496011, scale=65.97777257112197, size=1)[x]),
        "Družstevná&Širpo": lambda x: 60 / (60 -random.normal(loc=-19.773134, scale=70.87025686482612, size=1)[x]),
    },
    "line34" : {
        "Sídlisko III&Prostějovská" : lambda x: 60/(60-random.normal(loc=-30.203102, scale=40.80160136375221, size=1)[x]),
        "Prostějovská&Centrum": lambda x: 60/(60-random.normal(loc=-37.825624, scale=129.85141228856665, size=1)[x]),
        "Centrum&VUKOV": lambda x: 2*60/(2*60-random.normal(loc=-32.540291, scale=150.06462436373366, size=1)[x]),
        "VUKOV&Námestie Kráľovnej pokoja": lambda x: 60/(60-random.normal(loc=-37.001457, scale=134.54756809199512, size=1)[x]),
        "Námestie Kráľovnej pokoja&Volgogradská": lambda x: 60/(60-random.normal(loc=-47.6461, scale=138.95035962541078, size=1)[x]),
        "Volgogradská&Levočská": lambda x: 2*60/(2*60-random.normal(loc=-56.626932, scale=130.59410111202303, size=1)[x]),
        "Levočská&Obrancov mieru": lambda x: 2*60/(2*60-random.normal(loc=-62.300198, scale=149.9922709874895, size=1)[x]),
        "Obrancov mieru&Duchnovičovo námestie" : lambda x: 2*60/(2*60-random.normal(loc=-21.113779, scale=63.33916885459662, size=1)[x]),
        "Duchnovičovo námestie&Prešovská univerzita" : lambda x: 60/(60-random.normal(loc=-39.821058, scale=129.96450510110478, size=1)[x]),
        "Prešovská univerzita&Štúrova" : lambda x: 3*60/(3*60-random.normal(loc=16.531338, scale=67.01984892438658, size=1)[x]), #fast bus
        "Štúrova&Priemyselné centrum" : lambda x: 60/(60-random.normal(loc=-23.747703, scale=67.56797352267839, size=1)[x]),
        "Priemyselné centrum&Pekárne" : lambda x: 60/(60-random.normal(loc=-37.335938, scale=128.6078606986996, size=1)[x]),
        "Pekárne&Jilemnického" : lambda x: 60/(60-random.normal(loc=7.231145, scale=65.67446944752135, size=1)[x]), #fast bus
        "Jilemnického&Košická" : lambda x: 2*60/(2*60-random.normal(loc=14.426015, scale=67.95294865701524, size=1)[x]), #fast bus
        "Košická&Chalupkova": lambda x: 60/(60-random.normal(loc=-22.788829, scale=75.54388215311887, size=1)[x]),
        "Chalupkova&Švábska": lambda x: 60/(60-random.normal(loc=-69.909782, scale=133.4391404585443, size=1)[x]),
        "Švábska&Lomnická": lambda x: 60/(60-random.normal(loc=-81.530548, scale=134.57108400367534, size=1)[x]),
        "Lomnická&Lesnícka": lambda x: 2*60/(2*60-random.normal(loc=-97.959516, scale=138.52903192262465, size=1)[x]),
        "Lesnícka&Pavla Horova": lambda x: 60/(60-random.normal(loc=-82.362004, scale=136.79915144217, size=1)[x]),
        "Pavla Horova&Martina Benku": lambda x: 60/(60-random.normal(loc=-93.843103, scale=152.18330360386886, size=1)[x]),
        "Martina Benku&Laca Novomeského": lambda x: 2*60/(2*60-random.normal(loc=-90.054477, scale=160.65915348335017, size=1)[x]),
        "Laca Novomeského&Vansovej": lambda x: 60/(60-random.normal(loc=-79.266836, scale=172.72504871208744, size=1)[x]),
        "Vansovej&Pod Šalgovíkom": lambda x: 60/(60-random.normal(loc=-27.49635, scale=119.75195835540381, size=1)[x]),
    },
    "line35" : {
        "Delňa&Jelšová" : lambda x: 60/(60-random.normal(loc=-56.153119, scale=129.8397339674426, size=1)[x]),
        "Jelšová&Jesenná" : lambda x: 60/(60-random.normal(loc=-35.483607, scale=96.64556112596895, size=1)[x]),
        "Jesenná&Pionierska" : lambda x: 60/(60-random.normal(loc=-11.11284, scale=95.14387482562645, size=1)[x]),
        "Pionierska&Švábska" : lambda x: 60/(60-random.normal(loc=-0.043732, scale=88.78693899730493, size=1)[x]),
        "Švábska&Lomnická": lambda x: 60/(60-random.normal(loc=-13.912424, scale=86.91322584810437, size=1)[x]),
        "Lomnická&Lesnícka": lambda x: 2*60/(2*60-random.normal(loc=-24.42595, scale=98.03801764911887, size=1)[x]),
        "Lesnícka&Pavla Horova": lambda x: 60/(60-random.normal(loc=-27.640964, scale=105.18430758875776, size=1)[x]),
        "Pavla Horova&Martina Benku": lambda x: 60/(60-random.normal(loc=-37.074866, scale=96.47044614650552, size=1)[x]),
        "Martina Benku&Rusínska": lambda x: 2*60/(2*60-random.normal(loc=-92.665263, scale=114.32875750812559, size=1)[x]),
        "Rusínska&Hobby park": lambda x: 60/(60-random.normal(loc=-71.283843, scale=127.14885802484946, size=1)[x]),
        "Hobby park&Lesík delostrelcov": lambda x: 60/(60-random.normal(loc=-128.602041, scale=157.29023055640855, size=1)[x]),
        "Lesík delostrelcov&Fakultná nemocnica": lambda x: 2*60/(2*60-random.normal(loc=-115.765006, scale=171.55067971393422, size=1)[x]),
        "Fakultná nemocnica&Detská nemocnica": lambda x: 60/(60-random.normal(loc=-102.212366, scale=168.46021692317103, size=1)[x]),
        "Detská nemocnica&Rázcestie Kúty": lambda x: 2*60/(2*60-random.normal(loc=-128.783352, scale=193.1002682833733, size=1)[x]),

        "Rázcestie Kúty&Dopravný podnik" : lambda x: 60/(60-random.normal(loc=-143.856509, scale=188.12434151867674, size=1)[x]),
        "Dopravný podnik&Ľubochnianska" : lambda x: 2*60/(2*60-random.normal(loc=-169.966474, scale=191.12952369993428, size=1)[x]),
        "Ľubochnianska&Strojnícka" : lambda x: 60/(60-random.normal(loc=-169.447887, scale=190.69914204638346, size=1)[x]),
        "Strojnícka&Družstevná" : lambda x: 60/(60-random.normal(loc=-151.152542, scale=198.5255449181836, size=1)[x]),
        "Družstevná&Širpo" : lambda x: 60/(60+0), #missing data
    },
    "line36" : {
        "Pod Šalgovíkom&Vansovej" : lambda x: 60/(60-random.normal(loc=-3.815014, scale=179.12931607112148, size=1)[x]),
        "Vansovej&Laca Novomeského" : lambda x: 60/(60-random.normal(loc=-106.949364, scale=153.5226168945758, size=1)[x]),
        "Laca Novomeského&Rusínska" : lambda x: 2*60/(2*60-random.normal(loc=-121.892886, scale=171.89299745322938, size=1)[x]),
        "Rusínska&Čierny most" : lambda x: 3*60/(3*60-random.normal(loc=-108.646494, scale=171.96639356352125, size=1)[x]),
        "Čierny most&Divadlo Jonáša Záborského" : lambda x: 2*60/(2*60-random.normal(loc=-125.211355, scale=205.98513965217023, size=1)[x]),
        "Divadlo Jonáša Záborského&Na Hlavnej" : lambda x: 60/(60-random.normal(loc=-124.877612, scale=212.55365128104526, size=1)[x]),
        "Na Hlavnej&Trojica" : lambda x: 2*60/(2*60-random.normal(loc=-18.187371, scale=127.397719880039, size=1)[x]),
    },
    "line37" : {
        "Hinrichs&Karpatská" : lambda x: 3*60/(3*60-random.normal(loc=-54.504673, scale=83.91100913944217, size=1)[x]),
        "Karpatská&Jurkovičova" : lambda x: 60/(60-random.normal(loc=-110.620561, scale=84.94875831860331, size=1)[x]),
        "Jurkovičova&Martina Benku" : lambda x: 2*60/(2*60-random.normal(loc=-96.469645, scale=92.14211249636075, size=1)[x]),
        "Martina Benku&Pavla Horova": lambda x: 60 / (60 -random.normal(loc=-86.772429, scale=95.22825662107641, size=1)[x]),
        "Pavla Horova&Lesnícka": lambda x: 60 / (60 -random.normal(loc=-89.912409, scale=92.47172049748394, size=1)[x]),
        "Lesnícka&Škára": lambda x: 2*60 / (2*60 -random.normal(loc=- 146.6875, scale=117.58664333122128, size=1)[x]),
        "Škára&Železničná stanica": lambda x: 2*60 / (2*60 + 0), #missing data
    },
    "line39" : {
        "Sídlisko III&Prostějovská" : lambda x: 60/(60-random.normal(loc=-40.999313, scale=81.5014817585075, size=1)[x]),
        "Prostějovská&Centrum": lambda x: 60/(60-random.normal(loc=-91.390619, scale=147.1010987406818, size=1)[x]),
        "Centrum&VUKOV": lambda x: 2*60/(2*60-random.normal(loc=-53.380219, scale=102.95796719196669, size=1)[x]),
        "VUKOV&Mukačevská": lambda x: 60/(60-random.normal(loc=-36.585774, scale=88.2668427544579, size=1)[x]),
        "Mukačevská&Jazdecká": lambda x: 2*60/(2*60-random.normal(loc=-92.740344, scale=161.7247721980737, size=1)[x]),
        "Jazdecká&Sabinovská": lambda x: 60/(60-random.normal(loc=-63.667103, scale=100.37248906829, size=1)[x]),
        "Sabinovská&Trojica": lambda x: 3*60/(3*60-random.normal(loc=-91.781473, scale=108.139674552084, size=1)[x]),
        "Trojica&Na Hlavnej": lambda x: 2*60/(2*60-random.normal(loc=-86.714767, scale=150.29786556087578, size=1)[x]),
        "Na Hlavnej&Veľká pošta": lambda x: 2*60/(2*60-random.normal(loc=-43.314878, scale=112.97998960269305, size=1)[x]),
        "Veľká pošta&Čierny most": lambda x: 60/(60-random.normal(loc=-48.320532, scale=113.7653227598018, size=1)[x]),
        "Čierny most&Železničná stanica": lambda x: 2*60/(2*60-random.normal(loc=-112.461357, scale=147.83653346007878, size=1)[x]),
        "Železničná stanica&Škára": lambda x: 2*60/(2*60-random.normal(loc=-105.859262, scale=120.79660838695725, size=1)[x]),
        "Škára&Lomnická": lambda x: 3*60/(3*60-random.normal(loc=-209.0, scale=65.18179704999446, size=1)[x]),
    },
    "line41" : {
        "Divadlo Jonáša Záborského&Na Hlavnej" : lambda x: 60/(60-random.normal(loc=-59.137799, scale=87.08705982734253, size=1)[x]),
        "Na Hlavnej&Trojica" : lambda x: 2*60/(2*60-random.normal(loc=-19.340966, scale=90.84255195735601, size=1)[x]),
        "Trojica&Duklianska" : lambda x: 2*60/(2*60-random.normal(loc=-24.112937, scale=90.76176569500461, size=1)[x]),
        "Duklianska&K Surdoku" : lambda x: 2*60/(2*60-random.normal(loc=-0.444162, scale=82.71101457474674, size=1)[x]),
        "K Surdoku&Pod Šibeňou" : lambda x: 60/(60-random.normal(loc=-12.74451, scale=78.10021202885243, size=1)[x]),
        "Pod Šibeňou&Koryto" : lambda x: 60/(60-random.normal(loc=-17.173179, scale=79.11498696751404, size=1)[x]),
        "Koryto&Rybníčky" : lambda x: 60/(60-random.normal(loc=-15.88757, scale=73.79172792143648, size=1)[x]),
        "Rybníčky&Kúty" : lambda x: 60/(60-random.normal(loc=-21.508484, scale=98.07585328513463, size=1)[x]),
        "Kúty&Za Kútami" : lambda x: 2*60/(2*60-random.normal(loc=-13.604764, scale=86.92689271149766, size=1)[x]),
        "Za Kútami&Plachty" : lambda x: 60/(60-random.normal(loc=-17.716095, scale=88.12434199198293, size=1)[x]),
        "Plachty&Pred Surdokom" : lambda x: 60/(60-random.normal(loc=-19.525116, scale=93.7924151705974, size=1)[x]),
        "Pred Surdokom&Surdok" : lambda x: 60/(60-random.normal(loc=-53.196224, scale=88.14150895731652, size=1)[x]),
    },
    "line42" : {
        "Veľká pošta&Čierny most": lambda x: 60/(60-random.normal(loc=-57.942308, scale=125.9718664140175, size=1)[x]),
        "Čierny most&Železničná stanica": lambda x: 2*60/(2*60-random.normal(loc=-68.195867, scale=118.69690198918624, size=1)[x]),
        "Železničná stanica&Nový Solivar": lambda x: 60/(60-random.normal(loc=-83.40382, scale=122.4738778790807, size=1)[x]),
        "Nový Solivar&Jilemnického": lambda x: 2*60/(2*60-random.normal(loc=-31.160338, scale=110.25507537386562, size=1)[x]),
        "Jilemnického&Pod Wilecovou hôrkou": lambda x: 2*60/(2*60-random.normal(loc=-54.940859, scale=114.41869231357633, size=1)[x]),
        "Pod Wilecovou hôrkou&Wilecova hôrka": lambda x: 60/(60-random.normal(loc=-58.869443, scale=104.77591306582808, size=1)[x]),
        "Wilecova hôrka&Kamenná baňa": lambda x: 2*60/(2*60-random.normal(loc=-35.998722, scale=87.43351170999846, size=1)[x]),
        "Kamenná baňa&Borkút": lambda x: 60/(60-random.normal(loc=-38.813167, scale=43.8994702941128, size=1)[x]),
    },
    "line43" : {
        "Železničná stanica&Škultétyho" : lambda x: 3*60/(3*60-random.normal(loc=-12.53913, scale=45.863793990945155, size=1)[x]),
        "Škultétyho&Mestská hala" : lambda x: 60/(60-random.normal(loc=-21.194539, scale=41.68048099263576, size=1)[x]),
        "Mestská hala&Pod Kamennou baňou" : lambda x: 60/(60-random.normal(loc=1.599119, scale=44.84699980259796, size=1)[x]), #fast bus
        "Pod Kamennou baňou&Zimný štadión" : lambda x: 60/(60-random.normal(loc=3.800595, scale=45.22916647082601, size=1)[x]), #fast bus
        "Zimný štadión&Pod Kalváriou" : lambda x: 60/(60-random.normal(loc=1.133603, scale=45.74460836764237, size=1)[x]), #fast bus
        "Pod Kalváriou&SOŠ lesnícka" : lambda x: 60/(60-random.normal(loc=-11.57868, scale=52.10035369468166, size=1)[x]),
        "SOŠ lesnícka&Kollárova" : lambda x: 60/(60-random.normal(loc=-32.133489, scale=36.7902909215276, size=1)[x]),
        "Kollárova&Sázavského" : lambda x: 60/(60-random.normal(loc=-27.185567, scale=46.329352076774796, size=1)[x]),
        "Sázavského&Odborárska" : lambda x: 60/(60-random.normal(loc=-12.234615, scale=44.61470473619909, size=1)[x]),
        "Odborárska&Marka Čulena" : lambda x: 60/(60-random.normal(loc=-20.422492, scale=56.767490202931405, size=1)[x]),
        "Marka Čulena&Volgogradská" : lambda x: 2*60/(2*60-random.normal(loc=-41.325215, scale=84.04325172653922, size=1)[x]),
        "Volgogradská&Námestie Kráľovnej pokoja" : lambda x: 60/(60-random.normal(loc=-73.971182, scale=113.12426810393343, size=1)[x]),
        "Námestie Kráľovnej pokoja&VUKOV" : lambda x: 60/(60-random.normal(loc=-64.68125, scale=110.64701034568212, size=1)[x]),
        "VUKOV&Centrum" : lambda x: 2*60/(2*60-random.normal(loc=-55.363817, scale=116.7923887525177, size=1)[x]),
        "Centrum&Prostějovská" : lambda x: 60/(60-random.normal(loc=-55.86646, scale=117.58138793230364, size=1)[x]),
        "Prostějovská&Bajkalská" : lambda x: 60/(60-random.normal(loc=-66.986911, scale=119.98157509680112, size=1)[x]),
        "Bajkalská&Veterinárna nemocnica" : lambda x: 60/(60-random.normal(loc=-80.16242, scale=121.22391657931881, size=1)[x]),
        "Veterinárna nemocnica&Rázcestie Šidlovec" : lambda x: 60/(60-random.normal(loc=-136.480469, scale=139.56317037377835, size=1)[x]),
        "Rázcestie Šidlovec&Pod Skalkou" : lambda x: 60/(60-random.normal(loc=-146.620219, scale=148.7388349153444, size=1)[x]),
        "Pod Skalkou&Mičurinova" : lambda x: 60/(60-random.normal(loc=-269.813808, scale=201.52554386546788, size=1)[x]),
        "Mičurinova&Sabinovská" : lambda x: 60/(60-random.normal(loc=-405.282222, scale=299.285445901392, size=1)[x]),
        "Sabinovská&Duklianska" : lambda x: 3*60/(3*60-random.normal(loc=-364.853234, scale=351.93041325399037, size=1)[x]),
        "Duklianska&Šafárikova, cintorín" : lambda x: 60/(60-random.normal(loc=-345.40678, scale=349.9103962127519, size=1)[x]),
        "Šafárikova, cintorín&Detská nemocnica" : lambda x: 60/(60-random.normal(loc=-371.401656, scale=361.28396543793184, size=1)[x]),
        "Detská nemocnica&Fakultná nemocnica" : lambda x: 60/(60-random.normal(loc=-513.507353, scale=401.001595205928, size=1)[x]),
        "Fakultná nemocnica&Kpt. Nálepku" : lambda x: 4*60/(4*60+0),   #missing data
    },
    "line44" : {
        "Dulova Ves&Dulova Ves - kostol" : lambda x: 60/(60-random.normal(loc=-46.315827, scale=39.61779950054211, size=1)[x]),
        "Dulova Ves - kostol&Vlčie Doly" : lambda x: 2*60/(2*60-random.normal(loc=-81.421805, scale=111.20510089077492, size=1)[x]),
        "Vlčie Doly&Valkovská" : lambda x: 3*60/(3*60-random.normal(loc=-22.201923, scale=49.33418241955807, size=1)[x]),
        "Valkovská&Solivar" : lambda x: 60/(60-random.normal(loc=-84.321575, scale=140.5785477614217, size=1)[x]),
        "Solivar&Kukučínova" : lambda x: 60/(60-random.normal(loc=-79.117547, scale=128.7513198640109, size=1)[x]),
        "Kukučínova&Kysucká" : lambda x: 60/(60-random.normal(loc=-83.211089, scale=119.18940797864279, size=1)[x]),
        "Kysucká&Laca Novomeského" : lambda x: 60/(60-random.normal(loc=-90.472034, scale=110.99270632034893, size=1)[x]),
        "Laca Novomeského&Rusínska" : lambda x: 2*60/(2*60-random.normal(loc=-88.508261, scale=100.55312276719948, size=1)[x]),
        "Rusínska&Hobby park": lambda x: 60 / (60 -random.normal(loc=-54.543657, scale=106.06741967933031, size=1)[x]),
        "Hobby park&Čierny most": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-48.72389, scale=96.07279628694053, size=1)[x]),
        "Čierny most&Kpt. Nálepku": lambda x: 2 * 60 / (2 * 60 + 0), #corrupted data cant find proper replacement
    },
    "line45" : {
        "Veľký Šariš&Varoš" : lambda x: 60/(60-random.normal(loc=-26.160966, scale=52.48240694864299, size=1)[x]),
        "Varoš&Námestie sv. Jakuba" : lambda x: 60/(60-random.normal(loc=-89.152357, scale=133.71074428616285, size=1)[x]),
        "Námestie sv. Jakuba&Medulienka" : lambda x: 60/(60-random.normal(loc=-79.959686, scale=119.47698621931029, size=1)[x]),
        "Medulienka&Staničná" : lambda x: 60/(60-random.normal(loc=-95.249613, scale=151.35249097977103, size=1)[x]),
        "Staničná&Pivovar" : lambda x: 60/(60-random.normal(loc=-97.644481, scale=125.53204077913918, size=1)[x]),
        "Pivovar&Bikoš" : lambda x: 4*60/(4*60-random.normal(loc=-103.430368, scale=101.92030193518625, size=1)[x]),
        "Bikoš&Rázcestie Šidlovec" : lambda x: 3*60/(3*60-random.normal(loc=-66.21958, scale=121.75830957439656, size=1)[x]),
        "Rázcestie Šidlovec&Pod Skalkou" : lambda x: 60/(60-random.normal(loc=-57.936055, scale=134.83297221347007, size=1)[x]),
        "Pod Skalkou&Mičurinova" : lambda x: 60/(60-random.normal(loc=-76.325293, scale=155.5409568372933, size=1)[x]),
        "Mičurinova&Sabinovská" : lambda x: 60/(60-random.normal(loc=-88.253861, scale=196.59211846389266, size=1)[x]),
        "Sabinovská&Trojica" : lambda x: 3*60/(3*60-random.normal(loc=-75.60659, scale=170.91853203322768, size=1)[x]),
        "Trojica&Na Hlavnej": lambda x: 2*60/(2*60-random.normal(loc=-47.950753, scale=162.96939756100318, size=1)[x]),
        "Na Hlavnej&Veľká pošta": lambda x: 2*60/(2*60-random.normal(loc=-58.931851, scale=183.01642421359446, size=1)[x]),
        "Veľká pošta&Čierny most": lambda x: 60/(60-random.normal(loc=-63.470431, scale=189.8567863746861, size=1)[x]),
        "Čierny most&Železničná stanica": lambda x: 2*60/(2*60-random.normal(loc=-64.756177, scale=151.07708362574473, size=1)[x]),
        "Železničná stanica&Škára": lambda x: 2*60/(2*60-random.normal(loc=-84.996841, scale=158.29524369407932, size=1)[x]),
        "Škára&Lomnická": lambda x: 3*60/(3*60-random.normal(loc=-88.870148, scale=171.90019780403813, size=1)[x]),
        "Lomnická&Švábska": lambda x: 60/(60-random.normal(loc=-75.52567, scale=161.34684735105876, size=1)[x]),
        "Švábska&Pionierska": lambda x: 60/(60-random.normal(loc=-80.100419, scale=179.02038371157593, size=1)[x]),
        "Pionierska&Jesenná": lambda x: 60/(60-random.normal(loc=-93.321528, scale=191.3139943042, size=1)[x]),
        "Jesenná&Jelšová": lambda x: 60/(60-random.normal(loc=-77.710377, scale=171.811566589253, size=1)[x]),
        "Jelšová&Delňa": lambda x: 60/(60-random.normal(loc=-39.891641, scale=41.91418172665774, size=1)[x]),
    },
    "line46" : {
        "Veľká pošta&Čierny most": lambda x: 60/(60-random.normal(loc=-56.00398, scale=105.73899144836327, size=1)[x]),
        "Čierny most&Železničná stanica": lambda x: 2*60/(2*60-random.normal(loc=-59.919333, scale=156.13847560204223, size=1)[x]),
        "Železničná stanica&Škára": lambda x: 2*60/(2*60-random.normal(loc=-85.556914, scale=145.97457491814635, size=1)[x]),
        "Škára&Solivarská": lambda x: 2*60/(2*60-random.normal(loc=-79.817468, scale=143.70259261069418, size=1)[x]),
        "Solivarská&Bohúňova": lambda x: 60/(60-random.normal(loc=-57.145128, scale=154.19407843064454, size=1)[x]),
        "Bohúňova&Múzeum Solivar": lambda x: 60/(60-random.normal(loc=-56.676127, scale=154.68436692172187, size=1)[x]),
        "Múzeum Solivar&Soľnobanská": lambda x: 60/(60-random.normal(loc=-61.683272, scale=153.4864747143879, size=1)[x]),
        "Soľnobanská&Záhradky": lambda x: 60/(60-random.normal(loc=-54.014208, scale=145.50924117989115, size=1)[x]),
        "Záhradky&Pri zámočku": lambda x: 4*60/(4*60-random.normal(loc=-49.770966, scale=143.3337037510525, size=1)[x]),
        "Pri zámočku&Na Záhumní": lambda x: 60/(60-random.normal(loc=-51.180773, scale=142.71124685847195, size=1)[x]),
        "Na Záhumní&Hulica": lambda x: 60/(60-random.normal(loc=-53.201141, scale=144.98148574679112, size=1)[x]),
        "Hulica&Ruská Nová Ves": lambda x: 60/(60-random.normal(loc=-46.230918, scale=134.39550644450725, size=1)[x]),
    },
    "lineN1" : {
        "Pod Šalgovíkom&Vansovej" : lambda x: 60/(60-random.normal(loc=-87.25744, scale=78.37978418979802, size=1)[x]),
        "Vansovej&Laca Novomeského" : lambda x: 60/(60-random.normal(loc=-51.121457, scale=251.21169320462383, size=1)[x]),
        "Laca Novomeského&Martina Benku" : lambda x: 60/(60-random.normal(loc=-7.525701, scale=149.34742303184623, size=1)[x]),
        "Martina Benku&Pavla Horova": lambda x: 60 / (60 -random.normal(loc=10.265475, scale=131.86231285235385, size=1)[x]), #fast bus
        "Pavla Horova&Lesnícka": lambda x: 60 / (60 -random.normal(loc=-3.098341, scale=110.13742405442063, size=1)[x]),
        "Lesnícka&Lomnická": lambda x: 2*60 / (2*60 -random.normal(loc=-99.877907, scale=129.143821246554, size=1)[x]),
        "Lomnická&Švábska": lambda x: 60 / (60 -random.normal(loc=-45.677696, scale=79.17957248314436, size=1)[x]),
        "Švábska&Chalupkova": lambda x: 60 / (60 -random.normal(loc=-45.082153, scale=89.09962939936436, size=1)[x]),
        "Chalupkova&Košická": lambda x: 60 / (60 -random.normal(loc=-56.572614, scale=91.22031859873637, size=1)[x]),
        "Košická&Nový Solivar": lambda x: 60 / (60 -random.normal(loc=- 53.418938, scale=84.77036810398691, size=1)[x]),
        "Nový Solivar&Železničná stanica": lambda x: 60 / (60 -random.normal(loc=-58.617962, scale=111.24387504220078, size=1)[x]),
        "Železničná stanica&Škultétyho": lambda x: 2*60 / (2*60 -random.normal(loc=-61.096361, scale=93.85586010695256, size=1)[x]),
        "Škultétyho&Prešovská univerzita": lambda x: 60 / (60 -random.normal(loc=-52.998942, scale=77.69267854342233, size=1)[x]),
        "Prešovská univerzita&Duchnovičovo námestie": lambda x: 60 / (60 -random.normal(loc=-44.409722, scale=102.61123119127606, size=1)[x]),
        "Duchnovičovo námestie&Námestie mládeže": lambda x: 60 / (60 -random.normal(loc=-73.768577, scale=129.17188284746277, size=1)[x]),
        "Námestie mládeže&Obrancov mieru": lambda x: 60 / (60 -random.normal(loc=-51.559524, scale=126.4416250771643, size=1)[x]),
        "Obrancov mieru&Clementisova": lambda x: 60 / (60 -random.normal(loc=-50.496793, scale=89.77987150955795, size=1)[x]),
        "Clementisova&Volgogradská": lambda x: 60 / (60 -random.normal(loc=-34.818367, scale=82.0937969603992, size=1)[x]),
        "Volgogradská&Námestie Kráľovnej pokoja": lambda x: 60 / (60 -random.normal(loc=-26.404884, scale=75.27792089717288, size=1)[x]),
        "Námestie Kráľovnej pokoja&VUKOV": lambda x: 60 / (60 -random.normal(loc=-25.248861, scale=84.08169325395308, size=1)[x]),
        "VUKOV&Centrum": lambda x: 60 / (60 -random.normal(loc=-24.397709, scale=95.66130717448324, size=1)[x]),
        "Centrum&Prostějovská": lambda x: 60 / (60 -random.normal(loc=-56.454829, scale=100.7567873770335, size=1)[x]),
        "Prostějovská&Sídlisko III": lambda x: 60 / (60 -random.normal(loc=-87.723947, scale=71.74165481996906, size=1)[x]),
    },
    "lineN2" : {
        "Nižná Šebastová&Pažica" : lambda x: 60/(60-random.normal(loc=-118.232975, scale=101.44329165408553, size=1)[x]),
        "Pažica&Vranovská": lambda x: 60/(60-random.normal(loc=-101.148837, scale=127.69754710656605, size=1)[x]),
        "Vranovská&Šarišské Lúky": lambda x: 60/(60-random.normal(loc=-331.983664, scale=673.5768191936759, size=1)[x]),
        "Šarišské Lúky&Sibírska": lambda x: 4*60/(4*60-random.normal(loc=-61.800535, scale=75.34528309621953, size=1)[x]),
        "Sibírska&Karpatská" : lambda x: 2*60/(2*60-random.normal(loc=-53.19295, scale=111.57777722659665, size=1)[x]),
        "Karpatská&Jurkovičova" : lambda x: 60/(60-random.normal(loc=-44.498611, scale=105.09026542434788, size=1)[x]),
        "Jurkovičova&Martina Benku" : lambda x: 2*60/(2*60-random.normal(loc=-48.381124, scale=100.72948402553705, size=1)[x]),
        "Martina Benku&Pavla Horova": lambda x: 60 / (60 -random.normal(loc=-35.239281, scale=99.40354349713598, size=1)[x]),
        "Pavla Horova&Lesnícka": lambda x: 60 / (60 -random.normal(loc=-43.720418, scale=92.0970159602443, size=1)[x]),
        "Lesnícka&Lomnická": lambda x: 2*60 / (2*60 -random.normal(loc=-35.254447, scale=88.52574130222655, size=1)[x]),
        "Lomnická&Švábska": lambda x: 60 / (60 -random.normal(loc=-40.786484, scale=137.84523200232817, size=1)[x]),
        "Švábska&Chalupkova": lambda x: 60 / (60 -random.normal(loc=-23.191868, scale=99.85205083447406, size=1)[x]),
        "Chalupkova&Košická": lambda x: 60 / (60 -random.normal(loc=-35.46206, scale=97.81551296592873, size=1)[x]),
        "Košická&Nový Solivar": lambda x: 60 / (60 -random.normal(loc=-28.48318, scale=87.26406649474835, size=1)[x]),
        "Nový Solivar&Železničná stanica": lambda x: 60 / (60 -random.normal(loc=-20.845098, scale=81.66928482492007, size=1)[x]),
        "Železničná stanica&Čierny most": lambda x: 2*60 / (2*60 -random.normal(loc=-25.230437, scale=87.78720340823216, size=1)[x]),
        "Čierny most&Divadlo Jonáša Záborského": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-25.900867, scale=74.01481874961796, size=1)[x]),
        "Divadlo Jonáša Záborského&Na Hlavnej": lambda x: 60 / (60 -random.normal(loc=-31.804878, scale=80.42208065167185, size=1)[x]),
        "Na Hlavnej&Trojica": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-46.095238, scale=75.81739011592872, size=1)[x]),
        "Trojica&Sabinovská": lambda x: 2 * 60 / (2 * 60 -random.normal(loc=-55.09375, scale=76.78423556893199, size=1)[x]),
        "Sabinovská&Mičurinova" : lambda x: 60/(60-random.normal(loc=-40.077409, scale=85.82451333034317, size=1)[x]),
        "Mičurinova&Pod Skalkou" : lambda x: 60/(60-random.normal(loc=-15.415144, scale=80.74507789066436, size=1)[x]),
        "Pod Skalkou&Rázcestie Šidlovec" : lambda x: 60/(60-random.normal(loc=-0.737123, scale=76.57048546003436, size=1)[x]),
        "Rázcestie Šidlovec&Veterinárna nemocnica" : lambda x: 60/(60-random.normal(loc=-6.435028, scale=85.97074468976828, size=1)[x]),
        "Veterinárna nemocnica&Sídlisko III" : lambda x: 60/(60+0), #corrupted data didnt find any proper replacement
    },

    "TestLine" : {"Trojica&Na Hlavnej" : 0.1, "Na Hlavnej&Veľká pošta" : 0.2}
}

class Bus(Vehicle):

    def __init__(self, locationsTable, map, stops, weather, stations):
        """
        Bus instance drives around the route determined by added bus-stops
        """
        super(Bus, self).__init__(locationsTable, map, stops[0])
        self.name  = stops.pop(0)
        self.stops_names = stops
        self.stops = self.makeStops(stops)
        self.currStopNum = 1
        self.direction = "T"
        self.counter = bus_counters.get(self.name)
        # self.counter = 1
        self.defaultSpeed = 2
        self.weathertype = weather
        self.stations = stations
        self.passangers = []

        self.parking = Location() #dont ask me why do I have to write it this way...
        self.parking.setLatitude(48.987013)
        self.parking.setLongitude(21.250291)

#ked autobus dorazí na zastávku zavolá sa táto funkcia
    def changeStopNum(self): #used in ActorCollection on line 66
        tmp = +1 if self.direction == "T" else -1
        self.arrivedAtStop(tmp)
        delay = random.normal(loc=1, scale=2, size=1)

        #výpis textov a priprava vplyvy počasia na rýchlosť
        weather_slow = 0 if self.weathertype == "sunny" else 11 if self.weathertype == "wet road" else 50 if self.weathertype == "snow storm" else 12
        #dont get confused here the tmp has to be change with -1 otherwise it will get delays from the following stops rather then actuall ones
        stopname_delays = self.stops_names[self.currStopNum] + "&" + self.stops_names[self.currStopNum - tmp] if self.direction == "P" else self.stops_names[self.currStopNum - tmp] + "&" + \
                                                                  self.stops_names[self.currStopNum]
        # print("\nThe bus " + self.name + " is located between stops: " + str(stopname_delays))
        delay = bus_delays.get(self.name).get(stopname_delays)(0)
        while delay <= 0:
            # print("Help im stuck!!! " + self.name + " " + stopname_delays)
            delay = bus_delays.get(self.name).get(stopname_delays)(0)

        print("Bus " + self.name + "'s next stop is going to be: " + str(self.stops_names[self.currStopNum]))
        print("The weather condition " + self.weathertype + " has caused the bus to slow by " + str(weather_slow) + "%.")
        print("It is going at " + str(round(delay*100,2)) + "% of his maximum speed due the delays")

        #ak sme na konci trate zmen smer autobusu
        if self.currStopNum == (len(self.stops)-1) or self.currStopNum == 0:
            self.direction = "P" if self.direction == "T" else "T"
            tmp = +1 if self.direction == "T" else -1
            if self.direction == "T":
                self.counter -= 1

        #aktualizuj rýchlosť a zastávku na ktorej sa autobus nachádzal naposledy
        self.currStopNum = self.currStopNum+tmp
        self.setSpeed(round((self.defaultSpeed * (1-weather_slow/100)) * delay,2))

    #nástup a vástyp ludí
    def arrivedAtStop(self, offset):
        station = self.stations.get(self.stops_names[self.currStopNum - offset])
        peoples = station.getPassengers()

        #vystupujuci ludia
        exiting = 0
        for i in self.passangers.copy():
            if i.getGoal() == station.name:
                exiting += 1
                self.passangers.pop(self.passangers.index(i))

        #nastupujuci ludia
        entering = 0
        for i in peoples.copy():
            if i.getPrefferedBus() == self.name:
                self.passangers.append(i)
                peoples.pop(peoples.index(i))
                entering += 1

        #dotvor ludí na zastávke podla toho kolko ich vystúpilo
        print("\nOn the stop " + station.name + " " + str(exiting) + " people got of the bus " + self.name + " and " + str(entering) + " people has got on. The number of passengers in bus is " + str(len(self.passangers)))
        station.allocate_people(exiting)


    #vyhotovenie trate po ktorej bude autobus jazdit
    def makeStops(self, stops):
        field = []

        if len(stops) == 0:
            raise Exception("Empty stop field from user")
        for i in stops:
            tmp = stops_list.get(i, -1) #-1 reprezentuej hodnotu ktorá funkcia vráti ak sa nenašla hodnota i v premmenej stops_list
            if tmp != -1:
                location = Location()
                location.setLatitude(tmp[0])
                location.setLongitude(tmp[1])
                field.append(location)
            else:
                raise Exception("Bus stop" + str(i) + "not in list of know stops")
        return field



    #Not my stuff form here down
    def addStop(self, point=Location):
        '''
        adds GPS Location point to the bus route
        @param point: Location of point
        @return: no return
        '''
        self.stops.append(point)
        if (len(self.stops) > 1):
            self.makeRouteFromStops()

    def addStops(self, points):
        '''
        adds GPS Location pointa to the bus route
        @param points: list of Location objects
        @return: no return
        '''
        self.stops.extend(points)
        if (len(self.stops) > 1):
            self.makeRouteFromStops()

    def makeRouteFromStops(self):
        '''
        makes route from the given list of bus-stop locations
        @return: no return value
        '''
        # print("making route from stops called, initial location is: ", self.stops[0].toJson())
        self.route = []
        self.locationRoute = [] #possible nodes on roude to visit
        points = len(self.stops)
        i = 0
        # while (i < (points - 1)):
        #     self.route.extend(self.city.getRoute(self.stops[i], self.stops[i + 1]))
        #     i = i + 1
        # self.route.extend(self.city.getRoute(self.stops[points - 1], self.stops[0]))
        # self.locationRoute = self.city.routeToLocations(self.route)
        # self.location = self.locationRoute[0]

        while (i < (points - 1)):
            self.route.extend(self.map.getRouteBetweenNodes(self.stops[i], self.stops[i + 1]))
            i = i + 1
        self.route.extend(self.map.getRouteBetweenNodes(self.stops[points-1], self.stops[0]))
        self.locationRoute = self.stops[1::-1]
        self.location = self.stops[0]
        return;

    def walk(self):
        '''
        Overrides Walkable method, moves Bus around defined route
        @return:
        '''
        self.drive()


    def drive(self):
        '''
        Drives Bus around defined route repeatedly
        @return: no return
        '''
        #self.movementsMade = 1
        #print(">>Drive called by Bus with ID: ", self.id)
        #print("(so far made ", self.movementsMade, "movements)")
        print("Current location: " + self.location.toJson(), " (becoming origin location)")
        self.originLocation = deepcopy(self.location)
        distanceToWalk = 2000 #CHANGE from self.speed to flat 2
        #print("Going to drive ", distanceToWalk, " meters")

        while (distanceToWalk > 0):
            # print("while| ", distanceToWalk, "m still remaining")

            self.destinationLocation = self.locationRoute[0]
            print("destination to walk is: " + self.destinationLocation.toJson())
            distanceToDestination = self.com.getReal2dDistance(self.location, self.destinationLocation)
            print("distance to given location is: ", distanceToDestination)
            if (distanceToDestination < distanceToWalk):
                print("it was closer than planned drive this iteration, therfore")
                distanceToWalk = distanceToWalk - distanceToDestination #count how much of movement I have left
                self.location = self.destinationLocation #change my location as I reached my goal
                print("moving to new location ", self.location)
                print("with remaining distance to drive this iteration: ", distanceToWalk)
                self.locationRoute.append(self.locationRoute[0]) #add my first location in routes to the and of list
                self.locationRoute.pop(0) #drop the lucation from first position so we can continue to the next
            else:
                self.location = self.com.getLocationFromPathAndDist(distanceToWalk, self.location,
                                                                    self.destinationLocation) #return new location that can be reached
                print("Managed to move desired distance, my new location is: ", self.location.toJson())
                distanceToWalk = 0

        #self.movementsMade = self.movementsMade + 1 CHANGE just commented it
        self.updatePassangersLocation()
