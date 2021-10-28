# classes_exercise.py

"""
1. Create a class according to the following requirements:
It's name is Vehicle and it has the following attributes/methods:
Attributes/properties:
  name: str
  max_speed: int
  capacity: int
Methods:
    vroom() -> None
        Prints "Vroom" max_speed times
2. Create a child/subclass of Vehicle called Bus with the following methods:
Methods:
    fare(age: float) -> None
        Prints "The fare of the bus ride is {}."
            Price depends on age:
                0-17 years - Free
                18-60 years - $5
                61+ years - Free
"""


class Vehicle:
    """Represents a vehicle
    Attributes:
        name: A str of the name
        max_speed: An int of max speed
        capacity: An int of the capacity"""
    def __init__(self):
        """Creates a new vehicle with default values"""
        self.name = "Mikethebike"
        self.max_speed = 1000
        self.capacity = 2

    def vroom(self) -> str:
        """Prints "Vroom" max_speed times"""
        return "Vroom\n" * self.max_speed


class Bus(Vehicle):
    """Represents a Bus which is a vehicle

    Attributes:
        rider_age: A float indicating the age
    """
    def __init__(self, rider_age: float = 90):
        """Creates the age of riders"""
        self.rider_age = rider_age
        self.bus_fare = 5
        super().__init__()

    def fare(self) -> str:
        """Returns the bus fare of the ride"""
        if self.rider_age <= 17 or self.rider_age >= 61:
            return f"Fare is free."
        else:
            return f"The bus fare is ${self.bus_fare}."


some_vehicle = Vehicle()
print(some_vehicle.vroom())

some_bus = Bus()
print(some_bus.fare())
