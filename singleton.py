class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

def create_singleton():
    return Database()

class Check:
    def is_singleton(self, factory):
        object1 = factory()
        object2 = factory()
        return object1 is object2

check = Check()
print(check.is_singleton(create_singleton))

class User:
    pass

def create_user():
    return User()

print(check.is_singleton(create_user))
