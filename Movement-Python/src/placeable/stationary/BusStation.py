import sys

from src.placeable.movable.Person import Person
import random


class BusStation():
    def __init__(self, name, bus):
        self.name = name
        self.passengers = []
        self.available_busses = [bus.pop(0)]
        self.available_stops = [bus]
        self.test_num = 0

    #aktualizuj zoznam spojov zastavujucich na tejto zastavke
    def update_available_lines(self, newLine):
        if newLine[0] not in self.available_busses:
            self.available_busses.append(newLine.pop(0))
            self.available_stops.append(newLine)

    #vytvor ludi na zastavku
    def allocate_people(self, count):
        tmp = count
        minimum_people = random.randint(0,5)
        if len(self.passengers) < minimum_people:
            tmp = minimum_people - len(self.passengers)
        for i in range(tmp):
            random_bus = random.randint(0, len(self.available_busses) - 1)
            random_stop = random.randint(0, len(self.available_stops[random_bus]) - 1)
            #neumožňuje mať pridať passažierový cielovú destináciu ktorá by bola rovnaka zastávke na ktorej stoji
            while self.available_stops[random_bus][random_stop] == self.name:
                random_stop = random.randint(0, len(self.available_stops[random_bus]) - 1)
            self.passengers.append(Person(self.name, self.available_busses[random_bus], self.available_stops[random_bus][random_stop]))

    def getPassengers(self):
        return self.passengers

