from random import randint, choice
import os
import copy

clear = lambda : os.system('cls')

class Entity:
    def __init__(self, max_hp, atk, evade, base_defense):
        self.hp = max_hp
        self.max_hp = max_hp
        self.atk = atk
        self.evade = evade
        self.base_defense = base_defense
        self.defense = base_defense

class Enemy(Entity):
    def __init__(self, name, max_hp, atk, evade, base_defense, exp_gain):
        super().__init__(max_hp, atk, evade, base_defense)
        self.name = name
        self.exp_gain = exp_gain

class Player(Entity):
    def __init__(self, max_hp, atk, evade, base_defense, exp):
        super().__init__(max_hp, atk, evade, base_defense)
        self.exp = exp


ENEMIES = {"slime": Enemy("Slime", 10, 2, 5, 1, 2),
           "goblin": Enemy("Goblin", 15, 4, 5, 1, 2)}
MAX_LOG = 5


inp = None
quit_game = False
log = []

def logAddLine(txt):
    global log
    line_count = len(log)

    if(line_count > MAX_LOG):
        log.pop(0)
        
    log.append("> " + txt)

def logClear():
    global log
    log = []

def calcDamage(defendant, attacker):
    if(randint(1, 100) > defendant.evade):
        dmg = randint(int(attacker.atk/2), attacker.atk) - defendant.defense
        if dmg > 0:
            return dmg
        else:
            return 0
    else:
        return 0
    

def new_game():
    global player
    player = Player(10, 10, 1, 1, 0)
    main_loop()

def main_menu():
    menu = True
    while(menu == True):
        print("1. New Game\nq. Quit")
        inp = input("\n:")

        match inp:
            case "1":
                new_game()
                break
            case "q":
                quit_game = True
                menu = False
                break
            case _:
                print("Please select a valid option\n")
        
def main_loop():
    while(quit_game == False):
        clear()
        battle(ENEMIES[choice(list(ENEMIES.keys()))])

def battle(enemy_template):
    def nextRound():
        enemy_dmg = calcDamage(player, enemy)
        player.hp -= enemy_dmg
        logAddLine(f"You were dealt {enemy_dmg} Damage by {enemy.name}")
    
    enemy = copy.deepcopy(enemy_template)
    global player
    
    battle = True
    while(battle == True):
        clear()
        print(f"HP:{player.hp}/{player.max_hp} ATK:{player.atk} DEF:{player.defense} EVADE:{player.evade} EXP:{player.exp}")
        print(f"\n{enemy.name} ({enemy.hp}/{enemy.max_hp})\n")
        print("\n".join(log))
        print("\n1. Attack\n2. Defend\n\nc. Clear Log\nf. Flee")

        if enemy.hp == 0:
            battle = False
            player.exp += enemy.exp_gain
            logAddLine(f"{enemy.name} Defeated! {enemy.exp_gain} experience gained.")
        else:
            inp = input("\n:").lower()
            match inp:
                case "1":
                    dmg = calcDamage(enemy, player)
                    if enemy.hp - dmg < 0:
                        enemy.hp = 0
                    else:
                        enemy.hp -= dmg
                        nextRound()
                    if dmg > 0:
                        logAddLine(f"You dealt {dmg} Damage to {enemy.name}")
                    else:
                        logAddLine(f"{enemy.name} Dodged!")
                    
                case "2":
                    player.defense *= 2
                    nextRound()
                    player.defense = player.base_defense
                    pass
                case "c":
                    logClear()
                case "f":
                    pass
                case _:
                    pass

main_menu()
    
