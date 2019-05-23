import random
import pprint
from .magic import Spell


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Player:
    def __init__(self, hp, mp, atk, df, magic):
        self.max_hp = hp
        self.hp = hp

        self.max_mp = mp
        self.mp = mp

        self.atk_low = atk - 10
        self.atk_high = atk + 10

        self.df = df
        self.magic = magic

        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atk_low, self.atk_high)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_spell(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Spells" + bcolors.ENDC)
        for spell in self.magic:
            print(str(i) + ":", spell.name, "(Cost:", str(spell.cost) + ")")
            i += 1