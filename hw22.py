from datetime import datetime


class Car:
    __mileage = 0

    def __init__(self, mark, brand, fuel_consumption, graduation_year=2020):
        self.graduation_year = graduation_year
        self.mark = mark
        self.brand = brand
        self.fuel_consumption = float(fuel_consumption)

    def __str__(self):
        return f'<Car> graduation_year: {self.graduation_year},\n' \
               f'mark: {self.mark}\n' \
               f'brand: {self.brand}\n' \
               f'fuel_consumption: {self.fuel_consumption}\n' \
               f'car_age: {self.determination_of_age_in_years}'

    @property
    def determination_of_age_in_years(self):
        car_age = datetime.today().year - self.graduation_year
        return car_age


car_1 = Car(graduation_year=2013, mark='Audi RS7', brand='Audi', fuel_consumption=11.6)
car_2 = Car(mark='Porsche 911', brand='Porsche', fuel_consumption=9.4)
car_3 = Car(graduation_year=2022, mark='Ferrari 296 GTB', brand='Ferrari', fuel_consumption=6.4)
car_4 = Car(mark='Toyota Supra', brand='Toyota', fuel_consumption=9.4)
car_5 = Car(graduation_year=2013, mark='Nissan GT-R', brand='Nissan', fuel_consumption=12)
