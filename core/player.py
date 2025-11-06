import random
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 50 
        self.speed = random.randint(5,10)
        self.power = random.randint(5,10)                
        self.armor_rating = random.randint(5,15)

        self.profession = random.choice(["cure","fighter"])

        if self.profession == "cure":
            self.hp += 10
        if self.hp <= 0:
            return "Player dead"
        if self.profession == "fighter":
            self.power += 2
    def speak(self):
        print(f"Hello my name is {self.name} let's start play")

    def attack(self, roll_dice):
        roll_dice += self.speed
        return self.speed
        