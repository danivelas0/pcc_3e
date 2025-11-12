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
    print(f'Ouch! Arthur took {damage_amount} damage.')
    print(f'Health is now:{player['health']}')


# calling the function
# first_fight
take_damage(20)
# second_fight
take_damage(35)

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


# --- Now we can "catch" the returned value ---
print("Using a small snack...")
current_health = heal(10)  # current_health will become 90
print(f"The variable 'current_health' is now: {current_health}")

print("\nUsing a big tonic...")
current_health = heal(50)  # current_health will become 100
print(f"The variable 'current_health' is now: {current_health}")