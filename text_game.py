import time
import random
import cv2 as cv
you_lose = cv.imread("you_lose.jpg")
class Warrior:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
def dice(first_num, second_num):
    return random.randint(first_num, second_num)
#player
alex = Player("Alex", 830, 20)
jim = Player("Jim", 1050, 40)
max = Player("Max", 1150, 60)
luigi = Player("Luigi", 1360, 80)
mario = Player("Mario", 1470, 100)
#warrior
goblin = Warrior("Goblin", 750, 20)
troll = Warrior("Troll", 1060, 60)
dragon = Warrior("Dragon", 1400, 90)
#game starts
print("Welcome to dungeon and dragons text game")
gate1 = input("You are at the gate of the castle. Do you want to enter? (y/n): ").lower()
if gate1 == "y" or 'yes':
    #stage 1
    print('Level 1')
    print("Congratulations! You have entered the castle.")
    paths1 = input("You have two paths to choose from. Left or right? (l/r): ").lower()
    paths_choose = random.choice(["l", "r"])
    if paths1 == paths_choose:
        #stage 2
        print('Level 2')
        roll_monster = dice(1, 8)
        print(f'You have chosen the right path. You see a monster in front of you. If you roll the dice above {str(roll_monster)} you kill it.')
        print(f"Your number is")
        roll_monster1 = dice(1, 15)
        time.sleep(5)
        print(str(roll_monster1))
        if roll_monster1 > roll_monster:
            #stage3
            print('Level 3')
            print("Congratulations! You have killed the monster.")
            roll_tree = dice(1, 8)
            print(f'You see a tree in front of you. If you roll the dice above {str(roll_tree)} you will open a portal.')
            roll_tree1 = dice(1, 15)
            time.sleep(5)
            print(str(roll_tree1))
            if roll_tree1 > roll_tree:
                #stage4
                print('Level 4')
                print("Congratulations! You have opened the portal.")
                time.sleep(1)
                print('you are in a warriors dimension')
                player = random.choice([alex, jim, max, luigi, mario])
                warrior = random.choice([goblin, troll, dragon])
                print(f'You are {player.name} and you have {player.health} health and {player.attack} attack.')
                print(f'You have to fight against {warrior.name} and it has {warrior.health} health and {warrior.attack} attack.')
                time.sleep(5)
                print("The battle begins!")
                time.sleep(1)
                while player.health > 0 and warrior.health > 0:
                    player.health -= warrior.attack
                    print(f'{player.name} health: {player.health}')
                    time.sleep(2)
                    warrior.health -= player.attack
                    print(f'{warrior.name} health: {warrior.health}')
                    print('''
                    
                    ''')
                    time.sleep(2.5)
                if player.health > warrior.health:
                    #stage5
                    print('Level 5')
                    print("Congratulation! You have defeated the warrior.")
                else:
                    print("The warrior has defeated you.")
                    time.sleep(1)
                    cv.imshow("You lose", you_lose)
            else:
                print("The portal never opens and you die of starvation.")
                time.sleep(5)
                cv.imshow("You lose", you_lose)

        else:
            cv.imshow("You lose", you_lose)
            time.sleep(5)
            print("You have lost the game.")
    else:
        print("You have chosen the wrong path. You have lost the game.")
        print(f"The right path was {paths_choose}")
        time.sleep(1)
        cv.imshow("You lose", you_lose)
else:
    cv.imshow("You lose", you_lose)
    print("You have lost the game")
cv.waitKey(0)
cv.destroyAllWindows()

