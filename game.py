from core import goblin,player, orc
import random

class Game:
    def __init__(self):
        pass

    def start(self):
        print("Hello player ☻ welcome!!!")
        self.show_menu()

        


    def show_menu(self):
        menu = input("Do you want Fight or Exit? (f/e)")
        return menu

    def create_player(self):
        new_player = player.Player("Nate")
        return new_player

    def choose_random_monster(self):
        monster = random.choice([goblin.Goblin, orc.Orc])
        return monster
    
    def battle(self, player, monster):
    
        
        player += self.roll_dice(1,6)
        monster += self.roll_dice(1,6)
        if player > monster or player1 == monster:
            player  
        else:
            monster 
        
        player1 += self.roll_dice(1,20)
        if player1 > self.choose_random_monster(self.hp):
            player.Player.attack()


    def roll_dice(self, sides):
        rids20 = random.randint(1,20)
        rids6 = random.randint(1,6)
        if sides == 6:
            return rids6
        elif sides == 20:
            return rids20

