
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

# addig money

player['money'] += 15.50
print (f'Money after: {player['money']}')