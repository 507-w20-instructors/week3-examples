# sample.py

import datetime

date_now = datetime.datetime.now()

print(date_now.year)
print(date_now.month)
print(date_now.day)

print(date_now)
date_now = date_now.replace(2019, day=8)
print(date_now)
print(type(date_now))


# BEGIN CLASS DEFINITION
class Dog:

    def __init__(self, nm, br):
        self.name = nm
        self.breed = br

    def describe(self):
        return self.name + ' is a ' + self.breed

# END CLASS DEFINITION

d1 = Dog('Fido', 'German Shepherd')
d2 = Dog('Rufus', 'Lhasa Apso')
print(d1.describe())
print(d2.describe())


d3 = Dog('Benny', 'Mutt')
print(d3.describe())

d3.breed = 'Labradoodle'
print(d3.describe())
