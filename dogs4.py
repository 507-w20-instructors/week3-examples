
class Dog:
    '''A dog that speaks!

    Attributes
    ----------
    name : string
        The dog's name

    breed : string
        The dog's breed, as defined by https://www.akc.org/dog-breeds/

    '''
    large_dogs = ['German Shepherd', 'Golden Retriever',
                  'Rottweiler', 'Collie',
                  'Mastiff', 'Great Dane']
    small_dogs = ['Lhasa Apso', 'Yorkshire Terrier',
                  'Beagle', 'Dachshund', 'Shih Tzu']


    def __init__(self, nm, br):
        self.name = nm
        self.breed = br

    def speak(self):
        '''Print the sound the dog makes, as appropriate for their breed

        Looks up the dog breed to see if it is a large or small dog, 
        then prints the appropriate dog vocalization. This function 
        prints directly, it does not return the vocalization string.

        See Dog.large_dogs and Dog.small_dogs for the lists of each.

        Parameters
        ----------
        none

        Returns
        -------
        none

        '''
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


