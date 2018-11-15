from Person import Person


class BabsonPerson(Person):
    nextIdNum = 0
    # next ID number to assign
    #before definition, global variable for this class, all objects in this class, we need (), babsonperson is the child of person
    #we put () around father

    def __init__(self, name):
        # initialize Person attributes
        Person.__init__(self, name)
        # new BabsonPerson attribute: a unique ID number
        #copy from person
        self.idNum = BabsonPerson.nextIdNum    #注意！
        BabsonPerson.nextIdNum += 1  #increment by 1

    # sorting Babson people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum   #sort by id

    def speak(self, utterance):
        return (self.name + " says: " + utterance)


# p1 = BabsonPerson('Zhi')
# p2 = BabsonPerson('Jack')
# p3 = BabsonPerson('Steve')
# p4 = Person('John')     #person does not have speak 

# print (p2. speak ('i feel good today'))

# print (p4. speak " i dont feel good today")