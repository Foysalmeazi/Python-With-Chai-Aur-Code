favourite_game = {"game1": "Cricket", "game2": "football", "game3": "Badminton"}
print(favourite_game)

print(favourite_game["game2"])

for key, value in favourite_game.items():
    print(key, value)

if favourite_game["game2"]:
    print("My 2nd fav game is: ", favourite_game["game2"])

favourite_game["game4"] = "Hocky"
print(favourite_game)

favourite_game.pop("game4")
print(favourite_game)

print(len(favourite_game))

sports_shop = {
    'cricket': {'Halmat': 'Black', 'Bat': 'White', 'Ball': 'Red'},
    'football': {'Kepper': 'Hamid', 'Winger': 'Ramim', 'Defence': 'Foysal'}
}

print(sports_shop['cricket']['Halmat'])

queebe_num = {x:x**3 for x in range (10)}
print(queebe_num)
queebe_num.clear()
print(queebe_num)


fruits =  ['Mango', 'Lemon', 'Orange', 'Passionfruit']

fruits_default_value = 'Tasty'

new_fruits = dict.fromkeys(fruits, fruits_default_value)
print(new_fruits)