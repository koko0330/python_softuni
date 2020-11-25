class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25
    fuel_consumption: float
    fuel: float
    horse_power: int

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        used_fuel = kilometers * self.DEFAULT_FUEL_CONSUMPTION

        if self.fuel - used_fuel >= 0:
            self.fuel -= float(used_fuel)


