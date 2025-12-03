# TEXT ADVENTURE GAME
# where a player fights monsters and saves their high score.

import random


class Character:
    '''A class representing a character'''

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.is_alive = True

    def take_damage(self, amount):
        '''A method that lowers help if the player is attacked'''
        self.hp -= amount

        if self.hp <= 0:
            self.is_alive = False
            print('You are DEAD!')


class Player(Character):
    '''A simple model from character'''

    def __init__(self, name):
        '''Initialize a player'''
        super().__init__(name, 100)
        self.inventory = []  # empty list

    def add_item(self, item):
        self.inventory.append(item)


class Monster(Character):
    '''A monster model from character'''

    def __init__(self, name, hp, strength):
        '''Initialize a monster'''
        super().__init__(name, hp)
        self.strength = strength


def generate_monster():
    monster_names = ['Goblin', 'Skeleton', 'Dragon', 'Slime', 'Zombie']
    chose_monster = random.choice(monster_names)
    monster_hp = random.randint(10, 20)
    monster_strength = random.randint(5, 10)
    return Monster(chose_monster, monster_hp, monster_strength)


def combat_round(Player, Monster):
    # Player Attacks
    damage = random.randint(5, 15)
    print(f'You hit the {Monster.name} for {damage} damage!')
    Monster.take_damage(damage)

    # Monster Counter attacks
    if Monster.is_alive:
        print(f'Monster hit the {Player.name} player!')
        Player.take_damage(Monster.strength)
    else:
        print(f'Monster {Monster.name} is Dead!')
    return {'player_hp': Player.hp, 'monster_hp': Monster.hp}


print('====== 🐍⚔️ Welcome to Python Dungeon 🐍⚔️ =====')
hero_name = input('Enter the Name of your Hero: ')
hero = Player(hero_name)


while hero.is_alive:
    prompt = input('"What do you want to do? (explore/inventory/quit): ')

    if prompt.lower() == 'quit' or prompt.lower() == 'q':
        break
    elif prompt.lower() == 'inventory':
        print(hero.inventory)
    elif prompt.lower() == 'explore':

        # New Monster is created

        new_enemy = generate_monster()
        print(f'A wild {new_enemy.name} appears!')

        # Combat or Run motherfucker
        while hero.is_alive and new_enemy.is_alive:
            prompt_2 = input('What dou you want to do? (combat/run): ')
            if prompt_2.lower() == 'run':
                print('You fucking pussy')
                break
            elif prompt_2.lower() == 'combat':
                combat_round(hero, new_enemy)
            else:
                print('You can only pick the 3 choices available.')

    else:
        print('You can only pick the 3 choices available.')
