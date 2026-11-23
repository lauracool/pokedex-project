import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
def name(data):
    for pokemon in data:
        print(data[0]["name"])

# Add a language choice feature and print the pokemons name based on the user input 
print("english, japanese, chinese, french")
language = input("Select a language above: ").lower()

if language == "english":
    print(data[0]["name"]["english"])
elif language == "japanese":
    print(data[0]["name"]["japanese"])
elif language == "chinese":
    print(data[0]["name"]["chinese"])
elif language == "french":
    print(data[0]["name"]["french"])
else: 
    print("You did not type a valid language")
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that yype inform the user
search = input("Search for a pokemon: ")
def search():
    searched = []
    if search == ["name"]:
        print(search)
        searched.append(search)
    else:
        print("No pokemon was found")

    
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
def get_pokemon(pokemon):
    for search in data:
        if search in data:
            return get_pokemon
        else:
            print("No pokemon was found")



#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
import json
moves = open("./moves.json", encoding="utf8")

def get_moves(poke):
    x = get_pokemon(poke)

i = int(input("Select a number: "))
print(data[i]["name"]["english"])
print(data[i]["type"])
print(data["moves"])

