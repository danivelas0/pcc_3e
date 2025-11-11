# defining attributes - player data

# _______________________________________________________

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

# ______________________________________________________

# DICTIONARY - PLAYER DATA STORED - STATIC DATA

player = {
    'name': 'Arthur Morgan',
    'health': 100,
    'stamina': 100,
    'level': 1,
    'money': 100.0,
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
