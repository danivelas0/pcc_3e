# defining attributes - player data

# ________________________________________________________________________________

# --- Core Stats ---
player_name = "Arthur Morgan"
player_health = 100
player_stamina = 100
player_dead_eye = 0.0   # Let's start his Dead Eye at 0%
player_level = 1

# --- Status ---
player_money = 100.0   # Using 1000.0 makes it a float
player_honor = 0.0      # Using 0.0 makes it a float
player_weight = 85.0
player_body_temperature = 37.5

# --- Inventory ---
player_ammunition = 100
player_has_weapon = True
player_inventory_weapons = ['bow',
                            'arrows', 'knife', 'revolver', 'pistol', 'rifle']
player_inventory_equipment = [
    'lasso', 'binoculars', 'holster', 'fishing rod', 'lantern']
player_inventory_consumables = ['chewing tobaco', 'cigarettes',
                                'oatcakes', 'brandy', 'chocolate bar', 'canned salmon']

# ______________________________________________________________________________

# DICTIONARY - PLAYER DATA STORED - STATIC DATA

player = {
    'name': 'Arthur Morgan',
    'health': 100,
    'stamina': 100,
    'level': 1,
    'money': 100.0,
    'honor': 1.0,
    'inventory_weapons': ['bow',
                          'arrows', 'knife', 'revolver', 'pistol', 'rifle'],
    'inventory_equipment': [
        'lasso', 'binoculars', 'holster', 'fishing rod', 'lantern'],
    'inventory_consumables': ['chewing tobacco', 'cigarettes',
                              'oatcakes', 'brandy',],

}
# retrieving data from dictionary

player_health = player.get('health')
print(player_health)

for key, value in player.items():
    if 'inventory' in key:
        continue
    else:
        print(f'{key}:{value}')

# Adding money - modifying

player['money'] += 15.50
print(f'Money after: {player['money']}')

# Adding new items
player['law_status'] = 'Wanted'
player['stamina_bonus'] = 10

# Removing items
del player['stamina_bonus']

# Looping dictionary

for key in player:
    if 'inventory' in key:
        print(key)

# Nesting dictionary
# Changing inventory_weapon list for a dictionary

player['inventory_weapons'] = {
    'revolver': {
        'type': 'firearm',
        'ammo': '100',
        'damage': 25,
    },
    'knife': {
        'type': 'melee',
        'damage': 15,
    },
}
# accessing nested data
# chaining keys

print(player['inventory_weapons']['revolver']['ammo'])

# ______________________________________________________________________________

# IF STATEMENTS AND WHILE LOOPS

# Arthur's Honor
player['honor'] = -0.5
if player['honor'] >= 0.75:
    print('You\'re a paragon')
elif player['honor'] <= -0.25:
    print('You are dishonorable')
else:
    print('You are walking the middle path.')

# stamina
player['stamina'] = 50

While player['stamina'] < 100:
    # adds 10 to stamina
    player['stamina'] += 10
    # prints the new stamina
    print(f'Your stamina is now: {player['stamina']}')
print('Stamina is full')

# FUNCTIONS______________________________________________________________________

# fighting action
player = {
    'name': 'Arthur Morgan',
    'health': 80,
    'stamina': 100,
    'level': 1,
    'money': 100.0,
    'honor': 1.0,
    'inventory_weapons': ['bow',
                          'arrows', 'knife', 'revolver', 'pistol', 'rifle'],
    'inventory_equipment': [
        'lasso', 'binoculars', 'holster', 'fishing rod', 'lantern'],
    'inventory_consumables': ['chewing tobacco', 'cigarettes',
                              'oatcakes', 'brandy',],

}


def take_damage(damage_amount):
    player['health'] -= damage_amount
    # cheking if player is alive
    if player['health'] > 0:
        print(f'Ouch! Arthur took {damage_amount} damage.')
        # display current health
        print(f'Health is now:{player['health']}')
        return True
    # player is dead
    else:
        player['health'] = 0
        print('DEAD')
        return False


# healing_action
MAX_HEALTH = 100  # GLOBAL_VARIABLE


def heal(heal_amount):
    player['health'] += heal_amount
    if player['health'] > MAX_HEALTH:
        player['health'] = MAX_HEALTH
        print('You are at full health')
    else:
        print(f'You healed! Health is now:{player['health']}')
    return player['health']


# MAIN CODE GAME----------------------------------------------------------------
