from src.placeable.movable.Vehicles.Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, locationsTable, map):
        super(Car, self).__init__(locationsTable, map)

    def walk(self):
        super(Car, self).walk()
        self.updatePassangersLocation()

        return
