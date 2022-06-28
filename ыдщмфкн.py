enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudak',
}

print(enemy)

print("location x = " + str(enemy['loc_x']))

print("location y = " + str(enemy['loc_y']))

print("His name is: " + enemy['name'])

enemy['rank'] = 'Admiral'
print(enemy)

del enemy['rank']
print(enemy)

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = 'yellow'

print(enemy)

print(enemy.keys())
print(enemy.values())

print('--------------------------------------------')


print((lambda x: (x+2) * 5/2)(2))



enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudak',
}

all_enemies =[]

all_enemies.append(enemy)
all_enemies.append(enemy)
all_enemies.append(enemy)

print(all_enemies)

for x in range(0,10):
    all_enemies.append(enemy)


for ene in all_enemies:
    print(ene)




