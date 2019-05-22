from classes.game import player, bcolors

#Using a Dictionary to create spells
magic = [{"Name": "Meteor Strike", "Cost": 12, "Damage": 20},
         {"Name": "Typhoon Strike", "Cost": 10, "Damage": 15},
         {"Name": "Lightning Strike", "Cost": 15, "Damage": 25},
         {"Name": "PLUS ULTRA", "Cost": 100, "Damage": 1000}]

player1 = player(100, 100, 50, 50, magic)
enemy = player(500, 100, 15, 25, magic)

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
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player1.take_damage(enemy_dmg)
    print("The enemy attacked you for", enemy_dmg, "points of damage. Your HP:", player1.get_hp())