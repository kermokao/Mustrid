class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    def __init__(self):
        self.current_id = 0
        self.name_list = set()

    def create_person(self, name):
        if name in self.name_list:
            return None
        else:
            person = Person(self.next_id, name)
            self.name_list.add(name)
            self.current_id += 1
            return person
        

factory = PersonFactory()

p1 = factory.create_person("Anna")
p2 = factory.create_person("Mark")

print(p1.id, p1.name)
print(p2.id, p2.name)
