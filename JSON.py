import json

filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='Latin-1')


player1 = {
    'PlayerName': "Donald Trump",
    'Score': 345,
    'awards': ["OR", "NV", "NY"]
}

player2 = {
    'PlayerName': "Clinton Hillary",
    'Score': 346,
    'awards': ["WT", "TX", "MI"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)


json.dump(myplayers, myfile)
myfile.close()


myfile= open(filename, mode='r', encoding='Latin-1')
json_data = json.load(myfile)

for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Name is: " + str(user['Score']))
    print("Player Name is: " + str(user['awards'][0]))
    print("Player Name is: " + str(user['awards'][1]))
    print("Player Name is: " + str(user['awards'][2]))