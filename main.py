from classes.game import player, bcolors

#Using a Dictionary to create spells
magic = [{"Name": "Meteor Strike", "Cost": 12, "Damage": 20},
         {"Name": "Typhoon Strike", "Cost": 10, "Damage": 15},
         {"Name": "Lightning Strike", "Cost": 15, "Damage": 25},
         {"Name": "PLUS ULTRA", "Cost": 100, "Damage": 1000}]

player1 = player(100, 100, 50, 50, magic)
enemy = player(300, 100, 15, 25, magic)

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

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("The enemy attacked you for", enemy_dmg, "points of damage.")

    print("\nEnemy HP:", enemy.get_hp())
    print("Player HP:", player1.get_hp())

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "THE ENEMY HAS BEEN SLAIN!" + bcolors.ENDC)
    elif player1.get_hp()  == 0:
        print(bcolors.FAIL + "YOU HAVE BEEN SLAIN" + bcolors.ENDC)
    elif enemy.get_hp() == 0 and player1.get_hp() == 0:
        print(bcolors.FAIL + "YOU BOTH DIED")