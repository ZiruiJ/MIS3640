from BabsonPerson import BabsonPerson
from Person import Person

class Professor (BabsonPerson):
    def __init__(self, name):
        BabsonPerson.__init__(self, name)

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return BabsonPerson.speak(self, " Dude, " + utterance)