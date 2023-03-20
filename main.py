from pokedex import Pokedex
from save_json import writeAJson

db = Pokedex(database="dex", collection="pokemons")
db.resetDatabase()

#Pesquisando tipos psiquicos
pokemon = db.collection.find({"type": "Psychic"})
writeAJson(pokemon, "psychic")

#Pesquisando tipos eletricos com ataque menor que 50
pokemon = db.collection.find({"type": "Electric", "base.Attack": { "$lte": 50 }})
writeAJson(pokemon, "pokemon_electric_low_atk")

#Pesquisando pokemon com nome com mais de 6 letras
def get_6_letters_or_more(collection):
  names = collection.find({}, {"name": 1})
  six_letters_or_more = []
  for name in names:
    if len(name["name"].keys()) >= 6:
      if all(len(word) <= 4 for word in name["name"].values()):
        six_letters_or_more.append(name["name"].values())
  return six_letters_or_more

writeAJson(get_6_letters_or_more(db.collection), "pokemon_4_words_or_less")

#Pesquisando tipos aquaticos
pokemon = db.collection.find({"type": "Water"})
writeAJson(pokemon, "water")

#Pesquisando tipos fogo
pokemon = db.collection.find({"type": "Fire"})
writeAJson(pokemon, "fire")
