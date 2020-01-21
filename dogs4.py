
class Dog:

    large_dogs = ['German Shepherd', 'Golden Retriever',
                  'Rottweiler', 'Collie',
                  'Mastiff', 'Great Dane']
    small_dogs = ['Lhasa Apso', 'Yorkshire Terrier',
                  'Beagle', 'Dachshund', 'Shih Tzu']


    def __init__(self, nm, br):
        self.name = nm
        self.breed = br

    def speak(self):
        if self.breed in Dog.large_dogs:
            print('woof')
        elif self.breed in Dog.small_dogs:
            print('yip')
        else:
            print('rrrrr')


kennel = [
    Dog('Fido', 'German Shepherd'),
    Dog('Rufus', 'Lhasa Apso'),
    Dog('Fred', 'Mutt')
    ]

for dog in kennel:
    dog.speak()


