from src.city.ZoneType import ZoneType
from src.placeable.movable.Movable import Movable
from src.common.CommonFunctions import CommonFunctions
from datetime import datetime, time, timedelta

from src.placeable.movable.MovementActivity import MovementActivity


#class Person(Movable):
class Person():
    def __init__(self, current_stop, preffered_bus, goal):
        self.startin_stop = current_stop
        self.preffered_bus = preffered_bus
        self.goal = goal
        self.goal_reached = False

    def getPrefferedBus(self):
        return  self.preffered_bus

    def getGoal(self):
        return self.goal

    def goalReached(self):
        self.goal_reached = True

    # def __init__(self, current_stop, locationsTable, map, operator=None):
    #     super(Person, self).__init__(locationsTable, map, "passenger")
    #     self.com = CommonFunctions()
    #     self.operator = operator
    #
    #     self.startin_stop = current_stop
    #     self.goal_station = 0
        # self.home = None
        # self.work = None
        #
        # self.workStartTime = self.com.getTimeFromNormalDistribution(7,0.5,True)
        # self.workLeavingTime = self.com.timePlusHoursMinutes(self.workStartTime, deltaHours=8)
        # self.goingHomeTime = self.com.timePlusHoursMinutes(self.workLeavingTime, deltaHours=2)


    # def getNextActivityLocation(self):
    #     if not self.activityQueue:
    #         return None
    #     else:
    #         if(self.activityQueue[0].isReadyForActivation()):
    #             location = self.activityQueue[0].destination
    #             self.activityQueue.pop(0)
    #             return location
    #         else:
    #             return None
    #
    # def generateDailyActivityQueue(self):
    #     # plan going to work
    #     if self.work is None:
    #         raise ValueError('Generating daily activity for person, but work is None')
    #     if self.home is None:
    #         raise ValueError('Generating daily activity for person, but home is None')
    #
    #     self.appendMovementActivity(
    #         MovementActivity(destination=self.work,
    #                          startTime=self.com.getTodaysDaytimeFromTime(self.workStartTime),
    #                          endTime=self.com.getTodaysDaytimeFromTime(self.workLeavingTime),
    #                          importance=100,
    #                          name="Going to work"))
    #
    #     # plan Going to random location from zone type Entertainment
    #     self.appendMovementActivity(
    #         MovementActivity(destination=self.map.getRandomBuildingFromZoneType(ZoneType.ENTERTAINMENT).getCentroid(),
    #                          startTime=self.com.getTodaysDaytimeFromTime(self.workLeavingTime),
    #                          endTime=None,
    #                          importance=0,
    #                          name="Going shopping"))
    #     # plan going home
    #     self.appendMovementActivity(
    #         MovementActivity(destination=self.home,
    #                          startTime=self.com.getTodaysDaytimeFromTime(
    #                              self.com.timePlusHoursMinutes(self.workLeavingTime, deltaHours=2)),
    #                          endTime=self.com.getTomorrowsDate(self.com.getTodaysDaytimeFromTime(self.workStartTime)),
    #                          importance=0,
    #                          name="Going home"))
