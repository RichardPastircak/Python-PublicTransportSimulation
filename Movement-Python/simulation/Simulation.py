from src.IISMotion import IISMotion
from src.city.ZoneType import ZoneType
from src.common.Location import Location
from src.common.CommonFunctions import CommonFunctions
from src.common.SimulationClock import *
import asyncio
import time

from src.movement.movementStrategies.MovementStrategyType import MovementStrategyType

fun = CommonFunctions()

# Setting location that will be simulated
location = Location()
location.setLatitude(49.001831)
location.setLongitude(21.239311)
location.setAltitude(0)
radius =7250  # radius around the location that will be included

oneway = False  # oneways are disabled so agents will not get stuck at the edges of simulated area #CHANGE from false tu true
guiEnabled = True  # gui enabled, to see the agents, open /frontend/index.html in your browser while simulation running
guiTimeout = 0.2  # in seconds, sleep between simulations steps (gui is unable to keep up with updates at full speed)
intersectionCheck = True  # check whether agents are located at the intersection nodes
gridRows = 30  # grid that world is split into (used to find closest pairs of agents when needed)

secondsPerTick = 1  # each iteration will increment clock by 1 second
noOfTicks = 86400  # number of iterations simulation will take //86400 - should be whole day 24*60*60
predictIterations = 15

iismotion = IISMotion(radius=radius,
                      location=location,
                      oneWayEnabled=oneway,
                      guiEnabled=guiEnabled,
                      gridRows=gridRows,
                      secondsPerTick=secondsPerTick,
                      removeDeadends=False)  # initialize IISMotion

# # Defining multiple zones
# iismotion.addMapZone("OC Galeria",  # zone name
#                      ZoneType.ENTERTAINMENT,  # zone type
#                      80,  # probability of being chosen
#                      [Location(48.715232, 21.234898),
#                       Location(48.71584, 21.2389540),
#                       Location(48.71417088, 21.239554),
#                       Location(48.713519, 21.2356710)
#                       ]  # polygon of locations that surround a zone
#                      )
# # Spolocensky pavilon
# iismotion.addMapZone("Spolocensky pavilon", ZoneType.ENTERTAINMENT, 20,
#                      [Location(48.708224129, 21.23837471), Location(48.70860644, 21.2458419),
#                       Location(48.7049955, 21.2429881)])
# # # Od Toryskej po spolocensky pavilon (vratane)
# iismotion.addMapZone("Terasa byvanie", ZoneType.HOUSING, 100,
#                      [Location(48.713165652, 21.23562812), Location(48.7150345, 21.24687194),
#                       Location(48.7028289622, 21.2433528900)])
# # Hronska az Stefanikova trieda
# iismotion.addMapZone("Hronska-Stefanikova praca", ZoneType.WORK, 100,
#                      [Location(48.718064, 21.22601509), Location(48.71814916, 21.233310),
#                       Location(48.709710885, 21.236400604), Location(48.70750197, 21.2284612)])

# Adding persons with random waypoint walk along the drive network downloaded from OSM
# collection with given movement type is created


userCollection = iismotion.createActorCollection("userCollection", True,
                                                 MovementStrategyType.RANDOM_WAYPOINT_CITY) \
    .addBuses(0,38, "sunny") \
    .setGuiEnabled(guiEnabled)
    #0-38
# Manually setting locations to persons
# userLocation1 = Location(48.7095434, 21.2400651)
# userLocation2 = Location(48.7093694, 21.2387051)
# userIds = userCollection.locationsTable.getAllIds()
# userCollection.actorSet[int(userIds[0])].setLocation(userLocation1)
# userCollection.actorSet[int(userIds[1])].setLocation(userLocation1)


# method that moves agents for desired number of iterations
# async because of "GUI"
async def simulate():
    print("=================== Simulation started ===================")
    start = time.time()
    # predictions = []
    #for step in range(0, noOfTicks):
    while userCollection.parked_busses < 40: #40
        newDay = updateSimulationClock(secondsPerTick) #did the time move? - more like move the time in console by 1 second
        #print(f"---------------- step: {step} ---------------- dateTime : {getDateTime()} ----------------")
        # print(datetime.now().strftime("%H:%M:%S"))
        stepStart = time.time()
        iismotion.stepAllCollections(newDay)  # move all collections with ableOfMovement=True
        stepEnd = time.time()

        #print("step took ", stepEnd - stepStart)
        global DATETIME
        if (guiEnabled == True):
            await asyncio.sleep(guiTimeout)
        end = time.time()

    elapsed = end - start
    print("================== Simulation finished ===================")
    print("elapsed time:", elapsed)


#main method that will execute simulation based on guiEnabled param
def main():
    if (guiEnabled):
        loop = asyncio.get_event_loop()
        loop.create_task(simulate())
        loop.run_until_complete(iismotion.frontend.start_server)
        loop.run_forever()
    else:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(simulate())

if __name__ == '__main__':
    main()
    # cProfile.run('main()')
