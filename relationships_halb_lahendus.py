from enum import Enum

class Person:
    def __init__(self, name: str):
        self.name = name

class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3

class Relationships:
    
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

class Research(Relationships):
    
    def __init__(self, relationships):
        for person1, rel, person2 in relationships.relations:
            if person1.name == "John" and rel == Relationship.PARENT:
                print("John has a child called", person2.name)

parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)
            
Research(relationships)

