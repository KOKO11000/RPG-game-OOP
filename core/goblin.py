import random
class Goblin:
    def __init__(self, name, hp, speed, power, armor_rating, weapon, type = "goblin"):
        self.name = "goblin"
        self.hp = 20
        self.speed = random.randint(5,10)
        self.power = random.randint(5,10)
        self.armor_rating = 1
        self.weapon = random("knife","ax","sword")
        self.type = type


    def speak(self):
        print(f"I'm {self.type} my name {self.name}\nI want to kill humen and you can stop me hero")

    def attack(self, roll_dice):
        roll_dice += self.speed
        return self.speed

    def run_away(self):
        pass