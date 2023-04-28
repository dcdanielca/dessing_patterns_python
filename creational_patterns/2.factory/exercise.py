class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    index = -1
    def create_person(self, name):
        self.index += 1
        return Person(self.index ,name)