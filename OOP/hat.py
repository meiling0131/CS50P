import random

class Hat:

    house = ["a", "b", "c", "d"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.house))

Hat.sort("Harry")