from classes.game import Player, bcolors
from classes.magic import Spell


#Dark Spells
meteor = Spell("Meteor Strike", 20, 50, "Dark")
typhoon = Spell("Typhoon Strike", 25, 55, "Dark")
lighting = Spell("Lightning Strike", 50, 70, "Dark")
ultra = Spell("PLUS ULTRA", 100, 100, "Dark")


#Light Spells
cure = Spell("Cure", 10, 15, "Light")
cure_p = Spell("Cure +", 15, 20, "Light")


'''
Using a Dictionary to create and access spells
magic = [{"Name": "Meteor Strike", "Cost": 20, "Damage": 50},
         {"Name": "Typhoon Strike", "Cost": 25, "Damage": 55},
         {"Name": "Lightning Strike", "Cost": 50, "Damage": 70},
         {"Name": "PLUS ULTRA", "Cost": 100, "Damage": 100}]
'''


#Instantiate Player & Enemy
player1 = Player(100, 100, 50, 50, [meteor, typhoon, lighting, ultra, cure, cure_p])
enemy = Player(300, 100, 30, 25, [])

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY APPEARS!" + bcolors.ENDC)

while running:
    print("=========================")
    player1.choose_action()
    choice = input("Choose Action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player1.generate_damage()
        enemy.take_damage(dmg)
        print("\nYou attacked for", dmg, "points of damage.")
    elif index == 1:
        print("-------------------------")
        player1.choose_spell()
        spell_choice = int(input("Choose Spell:")) - 1

        spell = player1.magic[spell_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player1.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nYou do not have sufficient mana.\n" + bcolors.ENDC)
            continue

        player1.reduce_mp(spell.cost)

        if spell.type == "Light" and player1.hp is not 100:
            player1.heal(spell.damage)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(spell.damage), "HP." + bcolors.ENDC)
        elif spell.type == "Light" and player1.hp is 100:
            print("\n" + bcolors.FAIL + "You're full health" + bcolors.ENDC)
            continue
        elif spell.type == "Dark":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage." + bcolors.ENDC)
    elif index != 0 and index != 1:
        print("\n" + bcolors.FAIL + "You seemed to have entered a bad number :(. You entered:", choice + ".",
              "Your choices are '1' or '2'."+ bcolors.ENDC)
        continue




    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print(bcolors.FAIL + "The enemy attacked you for", enemy_dmg, "points of damage." + bcolors.ENDC)

    print("\nEnemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    print("Player HP:", bcolors.OKGREEN + str(player1.get_hp()) + "/" + str(player1.get_max_hp()) + bcolors.ENDC)
    print("Player MP:", bcolors.OKBLUE + str(player1.get_mp()) + "/" + str(player1.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "THE ENEMY HAS BEEN SLAIN!" + bcolors.ENDC)
        running = False
    elif player1.get_hp()  == 0:
        print(bcolors.FAIL + "YOU HAVE BEEN SLAIN" + bcolors.ENDC)
        running = False
    elif enemy.get_hp() == 0 and player1.get_hp() == 0:
        print(bcolors.FAIL + "YOU BOTH DIED")
        running = False