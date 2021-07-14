from pprint import pprint

############################
# Англо-Французкий Словарь
############################


vocabulary = {
    "cat": "chatte",
    "dog": "chienne",
    "home": "domicile",
    "fish": "poisson",
    "horse": "jument"
}


############################
# добавление
############################

new_words = {
    "pig": "porc"
}
vocabulary.update(new_words)

############################
# удаление
############################

del vocabulary["cat"]

############################
# поиск
############################

pprint(vocabulary.get("dog"))
pprint(vocabulary.get("doggg"))

############################
# изменение данных
############################

vocabulary ["pig"] = "truie"

pprint(vocabulary)