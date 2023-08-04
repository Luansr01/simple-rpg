from random import randint, choice
import os
import copy

from modules import log, entity, enemies

clear = lambda : os.system('cls')    

log = log.Log()

quit_game = False
menu = True


player = None



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
    player = None

    clear()

    print("What is your name?")
    inp = input("\n:")
    player = entity.Player(20, 10, 1, 1, inp)

def game_over():
    global player
    global quit_game

    player = None

    clear()

    print("GAME OVER\n\nDo you want to play again? (y/N)")
    inp = input("\n:").lower().strip()

    match inp:
        case "n" | "N":
            quit_game = True

def main_menu():
    global quit_game

    clear()

    print("1. New Game\nq. Quit")
    inp = input("\n:").lower().strip()

    match inp:
        case "1":
            new_game()
        case "q":
            quit_game = True
        case _:
             print("Please select a valid option\n")

def battle(enemy):
    global player

    def nextRound():
        enemy_dmg = calcDamage(player, enemy)
        player.hp -= enemy_dmg
        log.AddLine(f"You were dealt {enemy_dmg} Damage by {enemy.name}")
    

    
    while(player.is_alive and enemy.hp > 0):
        # UI code start
        clear()
        print(f"HP:{player.hp}/{player.max_hp} ATK:{player.atk} DEF:{player.defense} EVADE:{player.evade} EXP:{player.exp}/{player.required_exp}")
        print(f"\n{enemy.name} ({enemy.hp}/{enemy.max_hp})\n")
        log.Print()
        print("\n1. Attack\n2. Defend\n3. Heal\n\nc. Clear Log\nf. Flee")
        # Ui code end

        inp = input("\n:").lower().strip()
        match inp:
            case "1":
                # Calculates and constrains damage dealt by player to not exceed the current enemy hp.
                # If the enemy still has 1 or more hp, run nextRound()
                dmg = calcDamage(enemy, player)
                enemy.hp -= dmg

                # If the damage dealt by the player is 0, logs that the enemy dodged.
                if dmg > 0:
                    log.AddLine(f"You dealt {dmg} Damage to {enemy.name}")
                else:
                    log.AddLine(f"{enemy.name} Dodged!")
                
            case "2":
                # Doubles the player's defense for this round.
                player.defense *= 2
                nextRound()
                player.defense = player.base_defense
            case "3":
                # Heals the player for 10% of max hp.
                heal = player.max_hp_percent(10)
                player.hp += heal
                log.AddLine(f"You healed yourself by {heal} HP!")
            case "c" | "C":
                # Calls log #clear
                log.Clear()
            case "f" | "F":
                pass
            case _:
                log.AddLine("Please select a valid option.")

        if player.is_alive:
            nextRound()

    # If the enemy hp is 0 or less, the player gains exp, and that gain is logged.
    if enemy.hp <= 0 and player.hp > 0:
        player.exp += enemy.exp_gain
        log.AddLine(f"{enemy.name} Defeated! {enemy.exp_gain} experience gained.")


def main_loop():
    global player

    while(quit_game == False):
        clear()
        
        if(player == None):
            main_menu()
        elif player.hp > 0:
            battle(choice(enemies.enemy_list)())
        else:
            game_over()


if __name__ == '__main__':
    main_loop()

    
