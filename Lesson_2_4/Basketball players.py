from pprint import pprint

#################
# баскетболисты
#################

basketball_players = {
    "Леброн Джеймс": "2.05",
    "Майкл Джордан": "1.98",
    "Коби Брайант": "1.97",
    "Кевин Дюрант": "2.08"
}
pprint(basketball_players)

################
# добавление 
################

new_player = {"Шакил О’Нил": "2.16"}
basketball_players.update(new_player)

pprint(basketball_players)

################
# удаление
################

del basketball_players["Леброн Джеймс"]

pprint(basketball_players)

################
# замены данных
################

basketball_players["Майкл Джордан"] = "2.0"
pprint(basketball_players)

################
# поиск данных
################

pprint(basketball_players.get("Майкл Джордан"))
pprint(basketball_players.get("Майкл Джорданссс"))

