from datetime import datetime


class Human:
    __population = 0

    def __init__(self, name, surname, birthday):
        self.name = name
        self.surname = surname
        self.__class__.__population += 1
        self.birthday = birthday

    def __str__(self):
        return f'<Human> name:{self.name}, surname: {self.surname}, birthday: {self.birthday}'

    @property
    def age(self):
        my_age = datetime.today() - self.birthday
        return my_age


person1 = Human('Alex', 'Prokopenko', datetime(1990, 5, 12))
print(person1)
