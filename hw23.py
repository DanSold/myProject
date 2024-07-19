from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, tank_volume, speed, remaining_fuel, mileage):
        self.brand = brand
        self.tank_volume = tank_volume
        self.speed = speed
        self.remaining_fuel = remaining_fuel
        self.mileage = mileage

    def refueling(self, fuel_volume):
        if type(fuel_volume) is not float | int:
            print('Enter a number')
        if fuel_volume + self.remaining_fuel < self.tank_volume:
            self.remaining_fuel += fuel_volume
            sms = f'Refueled {fuel_volume}'
            print(sms)
        if fuel_volume + self.remaining_fuel is self.tank_volume:
            self.remaining_fuel += fuel_volume
            sms2 = f'A full tank was filled, ({fuel_volume})'
            print(sms2)
        if fuel_volume + self.remaining_fuel > self.tank_volume:
            sms3 = f'You cannot fill more gasoline than the volume of your side'
            print(sms3)
        if fuel_volume <= 0:
            print('Error, enter a positive number greater than 0')
        else:
            return

    def transfer_fuel_to_another_vehicle(self, other, fuel_volume):
        if self.remaining_fuel == 0:
            return
        if self.remaining_fuel >= fuel_volume:
            possible = fuel_volume
        else:
            possible = self.remaining_fuel
        if other.tank_volume - other.remaining_fuel >= fuel_volume:
            acceptable_volume = fuel_volume
        else:
            acceptable_volume = other.tank_volume - other.remaining_fuel
        final_value = min([acceptable_volume, possible])
        self.remaining_fuel -= final_value
        other.remaining_fuel += final_value
        return final_value

    @abstractmethod
    def __str__(self):
        pass


class Car(Vehicle):
    def __init__(self, number_of_passengers, brand, tank_volume, speed, presence_of_airbags: bool, remaining_fuel,
                 mileage):
        super().__init__(brand=brand, tank_volume=tank_volume, speed=speed, remaining_fuel=remaining_fuel,
                         mileage=mileage)
        self.number_of_passengers = number_of_passengers
        self.presence_of_airbags = presence_of_airbags

    def __str__(self):
        return f'<Car><info>\n' \
               f'number_of_passengers: {self.number_of_passengers}\n' \
               f'brand: {self.brand}\n' \
               f'tank_volume: {self.tank_volume}\n' \
               f'speed: {self.speed}\n' \
               f'presence_of_airbags: {self.presence_of_airbags}\n' \
               f'remaining_fuel: {self.remaining_fuel}\n' \
               f'milage: {self.mileage}'


class Motorbike(Vehicle):
    def __init__(self, motorcycle_cradle: bool, brand, tank_volume, speed, remaining_fuel, mileage):
        super().__init__(brand=brand, tank_volume=tank_volume, speed=speed, remaining_fuel=remaining_fuel,
                         mileage=mileage)
        self.motorcycle_cradle = motorcycle_cradle

    def __str__(self):
        return f'<Motorbike><info>\n' \
               f'brand: {self.brand}\n' \
               f'tank_volume: {self.tank_volume}\n' \
               f'speed: {self.speed}\n' \
               f'remaining_fuel: {self.remaining_fuel}\n' \
               f'milage: {self.mileage}\n' \
               f'motorcycle_cradle: {self.motorcycle_cradle}'


car = Car(number_of_passengers=4, brand='Audi', tank_volume=75, speed=305, remaining_fuel=40, mileage=5000,
          presence_of_airbags=True)
motorbike = Motorbike(motorcycle_cradle=False, brand='Honda', tank_volume=18, speed=254, remaining_fuel=10,
                      mileage=2300)
