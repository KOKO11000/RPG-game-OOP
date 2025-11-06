import random
class Orc:
    def __init__(self, name, hp, speed, power, armor_rating, weapon, type = "orc"):
        self.name = "orc"
        self.hp = 50
        self.speed = random.randint(0,5)
        self.power = random.randint(10,15)
        self.armor_rating = random.randint(2,8)
        self.weapon = random("knife","ax","sword")
        self.type = type

    def speak(self):
       print(f"I'm {self.type} my name {self.name}\n{self.name} want to eat hero!!!") 

    def attack(self, roll_dice):
        roll_dice += self.speed
        return self.speed
