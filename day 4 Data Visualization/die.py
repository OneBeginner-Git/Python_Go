from random import randint

class Die():

    def __init__(self, sides_num = 6):
        self.sides_num = sides_num

    def roll(self):
        return randint(1,self.sides_num)