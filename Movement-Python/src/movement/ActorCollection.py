import json
import sys

from src.city.ZoneType import ZoneType
from src.common.CommonFunctions import CommonFunctions
from src.common.FemtocellLoader import FemtocellLoader
from src.common.Location import Location
from src.movement.LocationsTable import LocationsTable
from src.movement.movementStrategies.MovementStrategyFactory import MovementStrategyFactory
from src.movement.movementStrategies.MovementStrategyType import MovementStrategyType
from src.placeable.movable.Drone import Drone
from src.placeable.movable.Movable import Movable
from src.placeable.movable.MovementActivity import MovementActivity
from src.placeable.movable.MovementActivityType import MovementActivityType
from src.placeable.movable.Person import Person
from src.movement.LocationPredictor import LocationPredictor
from random import randint
from datetime import datetime
from src.common.SimulationClock import *
import time

from src.common.MacrocellLoader import MacrocellLoader
from src.placeable.movable.Vehicles.Bus import Bus
from src.placeable.movable.Vehicles.Car import Car
from src.placeable.stationary.Attractor import Attractor
import numpy as np

from src.placeable.stationary.BusStation import BusStation


class ActorCollection:

    def __init__(self, name, map, ableOfMovement, movementStrategy, mapGrid, secondsPerTick):
        self.name = name
        self.map = map
        self.ableOfMovement = ableOfMovement
        self.locationsTable = LocationsTable(mapGrid)
        self.actorSet = {}
        self.mapGrid = mapGrid
        self.secondsPerTick = secondsPerTick
        self.movementStrategy = MovementStrategyFactory().getStrategy(movementStrategy, self.locationsTable,
                                                                      self.actorSet, self.map, self.mapGrid)
        self.attractors = []
        self.guiEnabled = False
        self.com = CommonFunctions()

        self.parked_busses = 0

    def setGuiEnabled(self, value: bool) -> 'ActorCollection':
        self.guiEnabled = value
        return self


    def step(self, newDay: bool):
        # print("step_ New day:", newDay)
        # print(self.locationsTable.getTable())
        if (newDay):
            for key, movable in self.actorSet.items():
                self.movementStrategy.onDayChange(movable) #nothing for Random.City.Waypoint
        self.attractorEffects()
        for id in self.locationsTable.getIdsInDestinations(): #get all ids of actors?
            walkable: object = self.actorSet[int(id)] #for each actor found by ID?
            # if agent has no MovementActivity in queue, it is needed to create some
            # print(f"walkable with id: {id} is in destination {walkable.getLocation().toJson()}")
            # print("Size of its activity queue is: ", len(walkable.activityQueue)) #the queue of activities for people
            if walkable.getCurrentMovementActivity() == None:
                # route will be obtained from movement activity

                #autobus zaparkoval odstav jeho pohyb
                if walkable.counter < 0:
                    tablerow = walkable.getTableRow()
                    walkable.setSpeed(0)
                    self.parked_busses += 1
                    print("\nThe bus " + walkable.name + " is parked in the garage.")

                    #pridaj nočné linky ak všetky denne spoje zaparkovali
                    if self.parked_busses == 38:
                        print("\nAll day busses are parked in the garage. The night lines (lineN1 and lineN2) has started operating.")
                        self.addBuses(38,40, "sunny")
                else:
                    locationRoute = None
                    #ak bus skončil svoju dennu službu zaparkuj ho
                    if walkable.counter == 0:
                        print("\nThe bus " + walkable.name + " has ended its shift. It's going to park near bus station.")
                        locationRoute = self.movementStrategy.getRouteTo(walkable, walkable.parking)
                        walkable.counter = -1
                    #bus ešte neskončil svoju prevázdku pošli ho na jeho ďalšiu zastávku
                    else:
                        locationRoute = self.movementStrategy.getRouteTo(walkable, walkable.stops[walkable.currStopNum])
                        walkable.changeStopNum()
                        print("Speed of this vehicle is: " + str(walkable.getSpeed()))

                    #locationRoute = self.movementStrategy.getNewRoute(walkable) #creates a route between current and random selected location

                    #print("Actor has no activity, so we create one using route: ", locationRoute)
                    # for location in locationRoute:
                    #     print(f"{location.toJson()}")
                    destination = locationRoute[-1]
                    # print("movement destination will be: ", destination.toJson())
                    activity = MovementActivity(
                        destination=destination,
                        startTime=None,
                        endTime=None,
                        importance=0,
                        name="generated by StepNew",
                        type=MovementActivityType.REGULAR_ACTIVITY,
                        routePlanningRequired=False  # no need, because we route will be assigned in next step
                    )
                    # assignment of route to the freshly created activity
                    activity.route = locationRoute
                    # print("New activity is:", activity.toJson())
                    # activity is appended to the queue of agent
                    walkable.appendMovementActivity(activity)

            # First activity is obtained from agents queue
            activity = None if walkable.getSpeed() == 0 else walkable.getCurrentMovementActivity()
           # print("Acitivity for " + walkable.name + "is : " + str(activity))
            # print("ACTOR HAS ACTIVITY:", activity.toJson())
            if activity is not None and  activity.getStarted(): #return true if the actvity started aka curr time is biger than start time or start time is None
                # if current activity is already started, its location route is used to plan target location
                # but first we need to check whether route planning should be performed
                # print("it even started!")
                if activity.getRoutePlanningRequired(): #this is in current Flase
                    # print("But planning is required")
                    activity.route = self.movementStrategy.getRouteTo(walkable, activity.getDestination())
                    activity.setRoutePlanningRequired(False)
                    # print("thus new route will be:", activity.route)
                # else:
                # print("Planning was not required")
                targetLocation = activity.getNextLoctionFromRouteAndPopIt()#we do have route set at line 79 so this will just returned first node from it and pop it?
                if (targetLocation == None):
                    raise ValueError('TargetLocation is None for bus ' + walkable.name)
                walkable.setTargetLocation(targetLocation)
                walkable.setTargetReached(False)
                # print("Target location was changed to:", walkable.getTargetLocation().toJson(), " and target reached is False")
            elif activity is not None:
            #     # if activity not yet started, agent should stay at current possition
                # print("But activity is not activated yet")
                walkable.setTargetReached(False)

            # print("Decision about removal of activity: ", activity.toJson())
            if activity is not None and activity.routeEmpty() and activity.getFinished(): #getFisnished is true if time end has passed or was set to None and routeEmpty if we dont have route var
                # if route of current activity is empty, and activity finish time passed, activity can be removed
                # print("Removing activity!")
                walkable.removeFirstActivity() #??????
                # print("AfterRemoval")
                # for acti in walkable.activityQueue:
                #     print(acti.toJson())

        # all agents in collection should have destinations configured now, we can move them using movements strategy
        # move method
        self.movementStrategy.move() #looks like creating a threat for moving stuff?

    def getLocationPredictionsForNextIterations(self, nuOfIterations, movementBackwardsAllowed=True):
        """
        This method returns possible locations of agent moving along routes
        !NOTE! that this method should be called right afer step() method
        :param nuOfIterations:
        :return: dictionary of lists with LocationPrediction objects
        """

        if (self.movementStrategy.strategyType not in [MovementStrategyType.RANDOM_INTERSECTION_WAYPOINT_CITY_CUDA]):
            raise ValueError('Location prediction is not available for collection with set MovementStrategyType:',
                             self.movementStrategy.strategyType)
        if (movementBackwardsAllowed == False):
            raise ValueError(
                'You required prediction that will ignore ability to move backwards, but mobility pattern may allow it')

        for actorId in self.locationsTable.getAllIds():
            walkable: Movable = self.actorSet[int(actorId)]
            # destination == node of open street map
            # update is done to find out which walkables are located at intersection nodes
            isAtIntersection = self.map.isIntersection(walkable.getLocation())
            walkable.setIsAtIntersection(isAtIntersection)
        locationPredictor = LocationPredictor()
        return locationPredictor.predictLocationsForNextIterations(self.map, self.getActorsInDestinations(),
                                                                          self.actorSet, self.secondsPerTick,
                                                                          nuOfIterations, movementBackwardsAllowed)

    def addPlaceables(self, placeables) -> 'ActorCollection':
        """
        before using this method, Placeables need to have their locations set (same with speed for Movables)
        :param placeables: list of Placeables that will be added to the actor set of ActorCollection
        :return: self
        """

        for placeable in placeables:
             self.actorSet[placeable.id] = placeable
        return self

    """
        Start - prvý spoj ktorý sa zo zoznamu vytvorí
        End - posledný spoj ktorý sa zo zoznamu vytvorí
        
        Počasie može mať jednu z nasledujúcich hodnot: 
        nulový vplyv na dopravu - sunny
        malý vplyv na dopravu - wet road
        stredný vplyv na dopravu - rain, strong wind, fog
        silný vpluv na dopravu - snow storm
    """
    def addBuses(self, start, end, weather) -> 'ActorCollection':
        #just NOTE the bus number shown in webbrowser cannot by changed just by chaging the ID in table
        #NOTE - D is another bus which has same majority of the bus stops but the end/start line is some blind spot in city (its different)

        #samotné linky spoj a ich trate
        busstops = {
            #line 1
            0: ["line1","Nižná Šebastová", "Pažica", "Vranovská", "Šarišské Lúky", "Dopravný podnik", "Rázcestie Kúty", "Duklianska", "Trojica", "Na Hlavnej", "Veľká pošta",
                "Čierny most", "Železničná stanica", "Škára", "Solivarská", "Bohúňova", "Múzeum Solivar", "Solivar"],
            # line 2/5 - There is special turn around at the end which could need remodeling + D variation
            1: ["line2/5","Budovateľská", "Pekárne", "Priemyselné centrum", "Štúrova", "Čierny most", "Divadlo Jonáša Záborského", "Na Hlavnej", "Trojica", "Poliklinika", "Obrancov mieru",
                "Duchnovičovo námestie", "Prešovská univerzita", "Škultétyho", "Čierny most", "Divadlo Jonáša Záborského", "Na Hlavnej", "Trojica", "Sabinovská",
                "Mičurinova", "Pod Skalkou", "Rázcestie Šidlovec", "Veterinárna nemocnica", "Bajkalská"],
            #line 4
            2: ["line4","Sídlisko III", "Prostějovská", "Centrum", "VUKOV", "Námestie Kráľovnej pokoja", "Volgogradská", "Clementisova", "Poliklinika", "Trojica", "Na Hlavnej",
                "Veľká pošta", "Čierny most", "Železničná stanica", "Škára", "Lesnícka", "Pavla Horova", "Martina Benku", "Laca Novomeského", "Vansovej", "Pod Šalgovíkom"],
            # line 7/7A - 7A ide len po Dopravý podnik momentalne vynechávam + same issue with the end turn around as in 2/5 #Budovatelska stuff
            3: ["line7","Budovateľská", "Pekárne", "Priemyselné centrum", "Štúrova", "Čierny most", "Divadlo Jonáša Záborského", "Na Hlavnej", "Trojica", "Duklianska", "Rázcestie Kúty",
                "Dopravný podnik", "Ľubochnianska", "Strojnícka", "Družstevná", "Širpo"],
            #line 8 - more variants
            4: ["line8","Sídlisko III", "Prostějovská", "Centrum", "VUKOV", "Námestie Kráľovnej pokoja", "Volgogradská", "Clementisova", "Poliklinika", "Trojica", "Na Hlavnej",
                "Veľká pošta", "Čierny most", "Železničná stanica", "Škára", "Lesnícka", "Pavla Horova", "Martina Benku", "Jurkovičova", "Karpatská", "Sibírska"],
            # line 38 - at 9th line should be only when returning namestie mladeze stop + univezita a skultetyho by mala mat medzi sebou pomocny bod aby to bolo presne ako na obrazku
            5: ["line38","Sídlisko III", "Prostějovská", "Centrum", "VUKOV", "Námestie Kráľovnej pokoja", "Volgogradská", "Clementisova", "Obrancov mieru", "Duchnovičovo námestie",
                "Prešovská univerzita", "Škultétyho", "Železničná stanica", "Škára", "Lesnícka", "Pavla Horova", "Martina Benku", "Jurkovičova", "Karpatská", "Sibírska"],
            # line 10 - NOTE the T and P directions are in reality kinda different bcs of the point where bus line turns around, doing the longer (first) part
            6: ["line10","Fakultná nemocnica", "Detská nemocnica", "Dilongova", "Sládkovičova", "Moyzesova", "Veľká pošta", "Čierny most", "Železničná stanica", "Nový Solivar",
                "Košická", "Chalupkova", "Švábska", "Lomnická", "Lesnícka", "Pavla Horova", "Martina Benku", "Jurkovičova", "Karpatská", "Sibírska"],
            # line 11 - 2 special cases + one line is allways different according to direction it travels, doing first one
            # bus stop Pod Hrádkom missing at OSM
            #bus stop Euporia cannot be reaged bcs that road is not on the map + Pod hrádkom cannot be fined on the maps + Surovova isnt realy named on the map its just on the streat called Surovova so its improvissation/deduction
            7: ["line11","Na Rúrkach", "Jána Béreša", "Rázcestie Rúrky", "Levočská", "Poliklinika", "Trojica", "Na Hlavnej", "Veľká pošta", "Čierny most", "Rusínska",
                "Martina Benku", "Pavla Horova", "Lesnícka", "Suvorovova", "Cintorín Solivar", "Na brehu", "Valkovská", "Solivar"],
            # line 12 - loooot of varations
            8: ["line12","Šidlovec", "Stavbárska", "Šidlovská", "Dúbravská", "Pri kaplnke", "Dúbrava", "Veterinárna nemocnica", "Sídlisko III", "Prostějovská", "Centrum", "VUKOV",
                "Námestie Kráľovnej pokoja", "Volgogradská", "Marka Čulena", "Odborárska", "Sázavského", "Kollárova", "SOŠ lesnícka", "Malá stanica", "Kúpeľná", "Pavlovičovo námestie",
                "Divadlo Jonáša Záborského", "Na Hlavnej", "Trojica", "Duklianska", "Šafárikova, cintorín", "Detská nemocnica", "Fakultná nemocnica", "Lesík delostrelcov",
                "Pod Táborom", "Nižné lúky", "Jurkovičova", "Karpatská", "Sibírska"],
            # line 13 - again lot of varibility, improvised bus lines bcs of missing: Kamenec (changed to Vyšná Šebestová dol. koniec), Rázcestie, Vyšná Šebestová
            # also missing Pod Monglovcom bus stop at the pre last space
            # possible the end stops might work bit wierd bcs of map range
            9: ["line13","Veľká pošta", "Čierny most", "Rusínska", "Jurkovičova", "Karpatská", "Nižnianska", "Kalinčiakova", "Ľubotice", "Šalgovícka", "Korabinského", "Jána Kostru",
                "Strážnická", "Šebastovská", "Pažica", "Nižná Šebastová", "Gen. Ambruša", "Herlianska", "Kamence", "Rázcestie Vyšná Šebastová", "Obecný úrad Vyšná Šebastová",
                "Vyšná Šebastová"],
            # line 14 - seems the lot of variations is becoming standart
            10: ["line14","Kanaš - Stráže", "Stará škola", "Medzi jarkami", "Pri kostole", "Husí hrb", "Kozí rožok", "Sordok", "Rázcestie Kanaš", "Bikoš", "Dúbrava", "Rázcestie Šidlovec",
                 "Pod Skalkou", "Mičurinova", "Sabinovská", "Trojica", "Na Hlavnej", "Veľká pošta", "Čierny most", "Železničná stanica", "Nový Solivar", "Košická", "Petrovianska",
                 "Logistické centrum", "Rázcestie Záborské", "Záborské - stred", "Záborské"],
            #line 15 - its doing circle in reality but you didnt find out till writing down delays
            11: ["line15","Za Kalváriou", "Hôrka", "Záhradkárska osada", "Horárska", "Zimný štadión", "Pod Kalváriou", "SOŠ lesnícka", "Kollárova", "Sázavského", "Odborárska",
                 "Centrál", "Poliklinika", "Trojica", "Na Hlavnej", "Grešova", "Fakultná nemocnica", "Detská nemocnica"],
            #line 17
            12: ["line17","Sídlisko III", "Prostějovská", "Centrum", "VUKOV", "Námestie Kráľovnej pokoja", "Volgogradská", "Levočská", "Poliklinika", "Duklianska", "Rázcestie Kúty",
                 "Dopravný podnik", "Ľubochnianska", "Strojnícka", "Družstevná", "Širpo"],
            #line 18
            13: ["line18","Bzenov", "Rázcestie Janov", "Obecný úrad Bzenov", "Chatky", "Čertov kameň", "Cemjata", "Školské lesy", "Zabíjaná", "Kvašná voda", "Vydumanec", "Rázcestie Cemjata",
                 "Mýto", "Levočská", "Poliklinika", "Trojica", "Na Hlavnej", "Veľká pošta"],
            #Line 19 - its combinaning with line 10
            14: ["line19","Solivar", "Kukučínova", "Kysucká", "Laca Novomeského", "Martina Benku", "Pavla Horova", "Lesnícka", "Lomnická", "Švábska", "Chalupkova", "Košická", "Nový Solivar",
                 "Železničná stanica", "Čierny most", "Grešova", "Fakultná nemocnica"],
            #line 20 - cannot be used bcs the map cannot create a route there
            #15: ["Trojica", "Na Hlavnej", "Grešova", "Regionálny úrad verejného zdravotníctva", "Onkologický pavilón", "Monoblok, interné oddelenie", "Pediatria", "Vajanského"],

            #line 21 - Pri lipe (between Fintice and V kopci) missing on map
            15: ["line21","Fintice", "V kopci", "Námestie Jozefa Kolarčíka", "Červený mostík", "Ihrisko", "Gribľovec", "Za traťou", "Išľa", "Fintická", "Nová", "Vranovská", "Šarišské Lúky",
                 "Dopravný podnik", "Rázcestie Kúty", "Duklianska", "Trojica"],
            #line 22 - Šalgovia should be Regionálny úrad verejného zdravotníctva however this bus stop is at totally different space as its neighbors so I changed it to sth more on the way
            #between Šalkogivík and Hrunny bus stop Kamenná missing
                #chyba nastala Harry Potter lietajucimi autobusmi
            16: ["line22","Teriakovce", "OÚ Teriakovce", "Na Kruhu", "Rázcestie Teriakovce", "Šalgovia", "Labutia", "Šalgovík", "Hruny",
                 "Pod Šalgovíkom", "Vansovej", "Laca Novomeského", "Vyšné lúky", "Nižné lúky", "Pod Táborom", "Lesík delostrelcov", "Kpt. Nálepku", "Divadlo Jonáša Záborského",
                 "Na Hlavnej", "Trojica", "Sabinovská", "Mičurinova", "Pod Skalkou", "Rázcestie Šidlovec", "Jánošíkova", "Šidlovská", "Jahodová", "Šidlovec"],
            #line 23
            17: ["line23","Veľký Šariš", "Varoš", "Tulčícka", "Malý Šariš", "Šľachtiteľská stanica", "Nákupné stredisko", "Obecný úrad Malý Šariš", "Rázcestie Malý Šariš", "Telekča",
                 "Rázcestie Cemjata", "Mýto", "Levočská", "Poliklinika", "Trojica"],
            #line 24
            18: ["line24","Haniska", "Lemešianska", "Priecestie", "Čistička", "Gemor", "ZVL", "Košická", "Nový Solivar", "Železničná stanica", "Čierny most", "Divadlo Jonáša Záborského",
                 "Na Hlavnej", "Trojica", "Poliklinika", "Obrancov mieru"],
            #line 26 - Spenia - Zaturcka is on road that is not on the map however it should drive close to it so I will use it
            19 : ["line26","Veľká pošta", "Čierny most", "Železničná stanica", "Nový Solivar", "Košická", "Spinea - Záturecká"],

            #line 27
            20 : ["line27","Za Kalváriou", "Hôrka", "Záhradkárska osada", "Horárska", "Slávičia", "Pod Kamennou baňou", "Mestská hala", "Škultétyho", "Čierny most", "Divadlo Jonáša Záborského",
                  "Na Hlavnej", "Trojica", "Duklianska", "Šafárikova, cintorín", "Vodárenská", "Hviezdna"],
            #line 28
            21: ["line28","Ľubotice", "Šalgovícka", "Korabinského", "Jána Kostru", "Strážnická", "Bardejovská", "Domašská", "Kalinčiakova", "Nižnianska", "Dopravný podnik", "Rázcestie Kúty",
                 "Duklianska", "Trojica", "Na Hlavnej", "Veľká pošta", "Čierny most", "Železničná stanica", "Škára", "Lomnická", "Švábska", "Pionierska", "Jesenná", "Jelšová", "Delňa"],
            #line 29
            22: ["line29","Sídlisko III", "Prostějovská", "Centrum", "VUKOV", "Námestie Kráľovnej pokoja", "Volgogradská", "Levočská", "Poliklinika", "Floriánova", "Okružná", "Grešova",
                 "Fakultná nemocnica", "Detská nemocnica"],
            #line 30
            23: ["line30","Železničná stanica", "Štúrova", "Priemyselné centrum", "Pekárne", "Budovateľská"],
            #line 32
            24: ["line32","Sibírska", "Karpatská", "Jurkovičova", "Rusínska", "Hobby park", "Čierny most", "Divadlo Jonáša Záborského", "Na Hlavnej", "Trojica"],
            #line 32A
            25: ["line32A","Sibírska", "Karpatská", "Jurkovičova", "Rusínska", "Čierny most", "Okružná"],
            #line 33
            26: ["line33","Delňa", "Jelšová", "Jesenná", "Pionierska", "Švábska", "Lomnická", "Lesnícka", "Pavla Horova", "Martina Benku", "Jurkovičova", "Karpatská", "Pod nadjazdom",
                 "Ľubochnianska", "Strojnícka", "Družstevná", "Širpo"],
            #line 34
            27: ["line34","Sídlisko III", "Prostějovská", "Centrum", "VUKOV", "Námestie Kráľovnej pokoja", "Volgogradská", "Levočská", "Obrancov mieru", "Duchnovičovo námestie",
                 "Prešovská univerzita", "Štúrova", "Priemyselné centrum", "Pekárne", "Jilemnického", "Košická", "Chalupkova", "Švábska", "Lomnická", "Lesnícka", "Pavla Horova",
                 "Martina Benku", "Laca Novomeského", "Vansovej", "Pod Šalgovíkom"],
            #line 35
            28: ["line35","Delňa", "Jelšová", "Jesenná", "Pionierska", "Švábska", "Lomnická", "Lesnícka", "Pavla Horova", "Martina Benku", "Rusínska", "Hobby park", "Lesík delostrelcov",
                 "Fakultná nemocnica", "Detská nemocnica", "Rázcestie Kúty", "Dopravný podnik", "Ľubochnianska", "Strojnícka", "Družstevná", "Širpo"],
            #line 36
            29: ["line36","Pod Šalgovíkom", "Vansovej", "Laca Novomeského", "Rusínska", "Čierny most", "Divadlo Jonáša Záborského", "Na Hlavnej", "Trojica"],
            #line 37 - Hinrichs bust stop improvised bcs its not on the map
            30: ["line37","Hinrichs", "Karpatská", "Jurkovičova", "Martina Benku", "Pavla Horova", "Lesnícka", "Škára", "Železničná stanica"],
            #line 39
            31: ["line39","Sídlisko III", "Prostějovská", "Centrum", "VUKOV", "Mukačevská", "Jazdecká", "Sabinovská", "Trojica", "Na Hlavnej", "Veľká pošta", "Čierny most", "Železničná stanica",
                 "Škára", "Lomnická"],
            #line 41
            32: ["line41","Divadlo Jonáša Záborského", "Na Hlavnej", "Trojica", "Duklianska", "K Surdoku", "Pod Šibeňou", "Koryto", "Rybníčky", "Kúty", "Za Kútami", "Plachty", "Pred Surdokom",
                 "Surdok"],
            #line 42
            33: ["line42","Veľká pošta", "Čierny most", "Železničná stanica", "Nový Solivar", "Jilemnického", "Pod Wilecovou hôrkou", "Wilecova hôrka", "Kamenná baňa", "Borkút"],
            #line43
            34: ["line43","Železničná stanica", "Škultétyho", "Mestská hala", "Pod Kamennou baňou", "Zimný štadión", "Pod Kalváriou", "SOŠ lesnícka", "Kollárova", "Sázavského",
                 "Odborárska", "Marka Čulena", "Volgogradská", "Námestie Kráľovnej pokoja", "VUKOV", "Centrum", "Prostějovská", "Bajkalská", "Veterinárna nemocnica",
                 "Rázcestie Šidlovec", "Pod Skalkou", "Mičurinova", "Sabinovská", "Duklianska", "Šafárikova, cintorín", "Detská nemocnica", "Fakultná nemocnica",
                 "Kpt. Nálepku"],
            #line 44
            35: ["line44","Dulova Ves", "Dulova Ves - kostol", "Vlčie Doly", "Valkovská", "Solivar", "Kukučínova", "Kysucká", "Laca Novomeského", "Rusínska", "Hobby park", "Čierny most",
                 "Kpt. Nálepku"],
            #line 45
            36: ["line45","Veľký Šariš", "Varoš", "Námestie sv. Jakuba", "Medulienka", "Staničná", "Pivovar", "Bikoš", "Rázcestie Šidlovec", "Pod Skalkou", "Mičurinova", "Sabinovská",
                 "Trojica", "Na Hlavnej", "Veľká pošta", "Čierny most", "Železničná stanica", "Škára", "Lomnická", "Švábska", "Pionierska", "Jesenná", "Jelšová", "Delňa"],
            #line 46
            37: ["line46","Veľká pošta", "Čierny most", "Železničná stanica", "Škára", "Solivarská", "Bohúňova", "Múzeum Solivar", "Soľnobanská", "Záhradky", "Pri zámočku", "Na Záhumní",
                 "Hulica", "Ruská Nová Ves"],
            #line N1
            38: ["lineN1","Pod Šalgovíkom", "Vansovej", "Laca Novomeského", "Martina Benku", "Pavla Horova", "Lesnícka", "Lomnická", "Švábska", "Chalupkova", "Košická", "Nový Solivar",
                 "Železničná stanica", "Škultétyho", "Prešovská univerzita", "Duchnovičovo námestie", "Námestie mládeže", "Obrancov mieru", "Clementisova", "Volgogradská",
                 "Námestie Kráľovnej pokoja", "VUKOV", "Centrum", "Prostějovská", "Sídlisko III"],
            #line N2
            39 : ["lineN2","Nižná Šebastová", "Pažica", "Vranovská", "Šarišské Lúky", "Sibírska", "Karpatská", "Jurkovičova", "Martina Benku", "Pavla Horova", "Lesnícka", "Lomnická",
                  "Švábska", "Chalupkova", "Košická", "Nový Solivar", "Železničná stanica", "Čierny most", "Divadlo Jonáša Záborského", "Na Hlavnej", "Trojica", "Sabinovská",
                  "Mičurinova", "Pod Skalkou", "Rázcestie Šidlovec", "Veterinárna nemocnica", "Sídlisko III"],
            #test line
            # 40: ["TestLine","Trojica", "Na Hlavnej", "Veľká pošta"],
        }
        weather_types = ["sunny", "wet road", "rain", "strong wind", "fog", "snow storm"]

        if weather not in weather_types:
            raise Exception("Incorrect weather type please use one of followings: sunny, wet road, rain, strong wind, fog, snow storm")

        stations_obj = {}
        # chod cez zoznam spojov
        for i in range(start,end):
            tmp = busstops.get(i)[1::]
            # prechádzaj všetky autobusové zastávky daného spoju
            for j in tmp:
                tmp_station = stations_obj.get(j, -1)
                # ak pre danu zastavku neexistuju objekt reprezentujuci ju vytvor ho
                if tmp_station == -1:
                    stations_obj.update({j: BusStation(j, busstops.get(i).copy())})
                # ak existuje pridaj do zoznamu spojov ktorý ju navšetevuju tento
                else:
                    tmp_station.update_available_lines(busstops.get(i).copy())
        #vytvor ludí na zastávkach
        for i in stations_obj:
            stations_obj.get(i).allocate_people(100)

        #vytvor spoje
        for i in range (start, end):
            bus = Bus(self.locationsTable, self.map, busstops.get(i), weather, stations_obj)
            bus.tableRow = self.locationsTable.insertNewActor(bus)
            bus.setSpeed(2 * self.secondsPerTick)
            bus.setMap(self.map)


            location_start = bus.stops[0]
            x, y = self.mapGrid.getGridCoordinates(location_start)
            location_start.setGridCoordinates(x, y)
            bus.setLocation(location_start)
            bus.home = location_start
            bus.setTargetLocation(location_start)
            bus.setTargetReached(True)
            self.actorSet[bus.id] = bus
        return  self


    def addPersons(self, count, withInitialMove=False) -> 'ActorCollection':
        """
        adds persons to the simulation model with the random location within the simulated space
        @param count: number of persons to be added
        @param withInitialMove: True/False make steps in random direction to leave the initial location
        @return: no return value
        """
        for i in range(0, count):
            location = self.map.getRandomIntersectionNode()
            person = Person(self.locationsTable, self.map)
            person.tableRow = self.locationsTable.insertNewActor(person)
            person.setSpeed(2 * self.secondsPerTick)
            person.setMap(self.map)
            x, y = self.mapGrid.getGridCoordinates(location)
            location.setGridCoordinates(x, y)
            person.setLocation(location)
            person.home = location
            person.setTargetLocation(location)
            person.setTargetReached(True)
            if (self.movementStrategy.strategyType == MovementStrategyType.PERSON_BEHAVIOUR_CITY_CUDA):
                person.location = self.map.getRandomBuildingFromZoneType(ZoneType.HOUSING).getCentroid()
                person.work = self.map.getRandomBuildingFromZoneType(ZoneType.WORK).getCentroid()
                person.generateDailyActivityQueue()
            self.actorSet[person.id] = person
            person.setTargetReached(True)

        if withInitialMove:
            for key, person in self.actorSet.items():
                person.setSpeed(randint(0, 50))

            for i in range(0, 100):
                self.step()

            for key, person in self.actorSet.items():
                person.setSpeed(2 * self.secondsPerTick)

        return self

    def addDrones(self, count) -> 'ActorCollection':
        for i in range(0, count):
            location = self.map.getRandomPoint()
            location.setAltitude(10)
            x, y = self.mapGrid.getGridCoordinates(location)
            location.setGridCoordinates(x, y)
            drone = Drone(self.locationsTable, self.map)
            drone.tableRow = self.locationsTable.insertNewActor(drone)
            drone.setSpeed(2 * self.secondsPerTick)
            drone.setMap(self.map)
            drone.setLocation(location)
            drone.setTargetLocation(location)
            drone.setTargetReached(False)
            self.actorSet[drone.id] = drone
        return self

    def addAttractor(self, location: Location, radius, startTime, endtime) -> 'ActorCollection':
        location.setAltitude(0)
        x, y = self.mapGrid.getGridCoordinates(location)
        location.setGridCoordinates(x, y)
        attractor = Attractor(locationsTable=self.locationsTable, map=self.map, radius=radius, startTime=startTime,
                              endTime=endtime)
        attractor.tableRow = self.locationsTable.insertNewActor(attractor)
        attractor.setLocation(location)
        attractor.startTime = startTime
        attractor.endTime = endtime
        self.actorSet[attractor.id] = attractor
        return self

    def loadMacrocells(self, networks) -> 'ActorCollection':
        macrocellLoader = MacrocellLoader()
        macrocells = macrocellLoader.getMacrocells("147.232.40.82",
                                                   self.map.latitudeInterval[0],
                                                   self.map.latitudeInterval[1],
                                                   self.map.longitudeInterval[0],
                                                   self.map.longitudeInterval[1],
                                                   self.locationsTable,
                                                   self.map,
                                                   networks)
        for cell in macrocells:
            self.actorSet[cell.id] = cell
        return self

    def generateFemtocells(self, count, minRadius) -> 'ActorCollection':
        femtocellLoader = FemtocellLoader()
        femtocells = femtocellLoader.getFemtocells(self.locationsTable, self.map, count, minRadius)
        for cell in femtocells:
            self.actorSet[cell.id] = cell
        return self

    def storeFemtoCells(self, filename) -> 'ActorCollection':
        print("Actor set", self.actorSet)
        list = []
        for key, value in self.actorSet.items():
            list.append(value)
        femtocellLoader = FemtocellLoader()
        femtocellLoader.storePlaceablesLocationsIntoFile(list, filename)
        return self

    def loadFemtocellsFromFile(self, filename) -> 'ActorCollection':
        femtocellLoader = FemtocellLoader()
        femtocells = femtocellLoader.loadSmallCellsFromFile(self.locationsTable, self.map, filename)
        for cell in femtocells:
            self.actorSet[cell.id] = cell
        return self

    def getFeaturesGeoJson(self):
        features = []
        for key, movable in self.actorSet.items():
            features.append(movable.getGeoStruct())
        return features

    def getActorsAtIntersections(self):
        return list(map(self.actorSet.get, self.locationsTable.getIdsAtIntersections()))

    def getActorsInDestinations(self):
        return list(map(self.actorSet.get, self.locationsTable.getIdsInDestinations()))

    def logMovement(self, newDay) -> 'ActorCollection':
        for id in self.locationsTable.getIdsInDestinations():
            walkable = self.actorSet[int(id)]
            walkable.logLocation(newDay)
        return self

    def getMovablesAtGridXY(self, x, y):
        ids = self.locationsTable.getIdsAtGridXY(x, y)
        movables = []
        for id in ids:
            movables.append(self.actorSet[id])
        return movables

    def attractorEffects(self) -> 'ActorCollection':
        global DATETIME
        for attractor in self.attractors:
            if attractor.startTime <= getDateTime() <= attractor.endTime:
                usersInArea = self.mapGrid.getActorsInRadius(attractor.radius, [self.name], attractor.getLocation())
                for user in usersInArea:
                    if user.getCurrentMovementActivity() == None or \
                            ((
                                     not user.getCurrentMovementActivity().getType() == MovementActivityType.ATTRACTOR_ACTIVITY) and user.getCurrentMovementActivity().importance < attractor.severity):
                        attractorActivity = MovementActivity(
                            attractor.getLocation(),
                            startTime=None,
                            endTime=attractor.endTime,
                            importance=attractor.severity,
                            name=attractor.name,
                            routePlanningRequired=False,
                            type=MovementActivityType.ATTRACTOR_ACTIVITY
                        )
                        locationRoute = self.movementStrategy.getRouteTo(user, attractor.getLocation())
                        attractorActivity.pushLocationListToRoute(locationRoute)
                        user.storeMovementActivity(attractorActivity, asFirst=True)

        self.attractors[:] = (x for x in self.attractors if x.endTime > getDateTime())
        return self

    def compareCurrentLocationsWithPredictions(self, predictionDict):
        for id, actor in self.actorSet.items():
            dictKey = (actor.id, getDateTime().strftime("%m/%d/%Y, %H:%M:%S.%f"))

            if (dictKey in predictionDict):
                predictions = predictionDict[dictKey]

                correctPredictionFound = False
                for prediction in predictions:
                    if prediction.location.equlsWithLocation(actor.getLocation()):
                        print(
                            f"Correct!!! Current location {actor.getLocation().toJson()} of actor {actor.id} corresponds to the prediction {prediction.toJson()}")
                        correctPredictionFound = True
                        break
                    else:
                        print(f"Prediction: {prediction.toJson()}")
                        print(f"Current location {actor.getLocation().toJson()}")
                        print("Note this is not the right prediction!")
                if (correctPredictionFound == False):
                    print(
                        f"Error will follow but this might be interesting: {actor.getLocation().toJson()} is intersection: {self.map.isIntersection(actor.getLocation())}")
                    raise ValueError(f"Not found in predictions {actor.getLocation().toJson()} of actor {actor.id} ")
            else:
                print(f"dict key not even in prediction {dictKey}")

    # def saveLocationsFile(self) -> 'ActorCollection':
    #     locations = ""
    #     for key, person in self.actorSet.items():
    #         location = person.getLocation()
    #         locations = locations + str(location.getLatitude()) + ", " + str(location.getLongitude()) + ", \n"
    #     self.com.appendToFile("locationsDebug", locations)
    #     return self
