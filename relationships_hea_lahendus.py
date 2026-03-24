from enum import Enum
from abc import ABC, abstractmethod

class RelationshipBrowser(ABC):
    
    @abstractmethod
    def find_all_children_of(self, name):
        pass

class Person:
    def __init__(self, name: str):
        self.name = name

class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3

class Relationships(RelationshipBrowser):
    
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, child))
    
    def find_all_children_of(self, name):
        return [child for parent, child in self.relations if parent.name == name]


class Research():

    def __init__(self, browser: RelationshipBrowser):
        self.browser = browser

    def find_all(self, name):
        children = self.browser.find_all_children_of(name)
        for child in children:
            print(f"{name} has a child called {child.name}")

parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships).find_all("John")
