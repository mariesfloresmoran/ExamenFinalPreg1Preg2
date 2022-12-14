"""
La tarea gira en torno a la PokeAPI: https://pokeapi.co/docs/v2 utilizar la API v2 y el paquete requests de Python

Escribir un programa que tenga las siguientes opciones:

Opción 1: Listar pokemons por generación. Se ingresa alguna generación (1, 2, 3, ..) y se listan todos los pokemon respectivos.
Opción 2: Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores) y se listan todos los pokemons respectivos.
Opción 3: Listar pokemons por habilidad. Se deben sugerir opciones a ingresar para interactuar.
Opción 4: Listar pokemons por habitat. Se deben sugerir opciones a ingresar para interactuar.
Opción 5: Listar pokemons por tipo. Se deben sugerir opciones a ingresar para interactuar.
Nota: listar pokemons involucra: nombre, habilidad y URL de la imagen
"""
# BASE

import requests
print("1**************************************************************************")
import json
print("2**************************************************************************")
url_pokeapi = 'https://pokeapi.co/api/v2'

#Opción 1: Listar pokemons por generación

def menu_pokemon_generacion():
    generacion = int(input ("Ingrese la generación a buscar (1-8): "))
    url_gen = f"https://pokeapi.co/api/v2/generation/{generacion}/"
    url_pokemon_base = 'https://pokeapi.co/api/v2/pokemon/'
    pokemonsSpecies = requests.get(url_gen).json()['pokemon_species']
    for pokemonSpecie in pokemonsSpecies:
        pokemonName = pokemonSpecie['name']
        pokemon = requests.get(url_pokemon_base + pokemonName).json()
        pokemonData = {'name': pokemonName, 'abilities': [ability['ability']['name'] for ability in pokemon['abilities']], 'image': pokemon['sprites']['front_default']}
        print(pokemonData)

#Opción 2: Listar pokemons por forma

def shape(option):
  pokemonForms = requests.get(
    f"{url_pokeapi}/pokemon-shape/{option}/").json()['pokemon_species']
  for pf in pokemonForms:
    pokemonNumber = pf['url'].replace(
      'https://pokeapi.co/api/v2/pokemon-species/', '').rstrip('/')
    pokemon = requests.get(f"{url_pokeapi}/pokemon/{pokemonNumber}").json()
    pokemonData = {
      'name':
      pokemon['name'],
      'abilities':
      [ability['ability']['name'] for ability in pokemon['abilities']],
      'image':
      pokemon['sprites']['front_default']
    }
    print(pokemonData)


def menu_pokemon_forma():
    while True:
        print("Elija la forma del Pokemon:")
        print("1. Ball")
        print("2. Squiggle")
        print("3. Fish")
        print("4. Arms")
        print("5. Blob")
        print("6. Upright")
        print("7. Legs")
        print("8. Quadruped")
        print("9. Wings")
        print("10. Tentacles")
        print("11. Humanoid")
        print("12. Bug-Wings")
        print("13. Armor")
        print("14. Volver al Menú Principal")

        option = int(input("Opción: "))

        if option == 1:
            shape(option)
        elif option == 2:
            shape(option)
        elif option == 3:
            shape(option)
        elif option == 4:
            shape(option)
        elif option == 5:
            shape(option)
        elif option == 6:
            shape(option)
        elif option == 7:
            shape(option)
        elif option == 8:
            shape(option)
        elif option == 9:
            shape(option)
        elif option == 10:
            shape(option)
        elif option == 11:
            shape(option)
        elif option == 12:
            shape(option)
        elif option == 13:
            shape(option)
        elif option == 14:
            break

#Opción 3: Listar pokemons por habilidad

def menu_pokemon_habilidad():
  print('Estos son las habilidades')
  url_ability = f'{url_pokeapi}/ability'
  pokemonAbilities = requests.get(url_ability).json()['results']
  i = 1
  for pf in pokemonAbilities:
    print(f"{i}. {pf['name']}")
    i += 1

  ability = input("Ingresa el numero de la habilidad que buscas: ")
  print(ability)

  pokemons = requests.get(f'{url_ability}/{ability}').json()['pokemon']

  for pf in pokemons:
    pokemon = requests.get(pf['pokemon']['url']).json()
    pokemonData = {
      'name':
      pokemon['name'],
      'abilities':
      [ability['ability']['name'] for ability in pokemon['abilities']],
      'image':
      pokemon['sprites']['front_default']
    }
    print(pokemonData)

#Opción 4: Listar pokemons por habitat

def menu_pokemon_habitat():
  print('Estos son los habitats')
  url_habitat = f'{url_pokeapi}/pokemon-habitat'
  pokemonHabitats = requests.get(url_habitat).json()['results']
  i = 1
  for pf in pokemonHabitats:
    print(f"{i}. {pf['name']}")
    i += 1

  habitat = input("Ingresa el numero del habitat que buscas: ")
  print(habitat)

  pokemons = requests.get(f'{url_habitat}/{habitat}').json()['pokemon_species']

  for pf in pokemons:
    pokemonNumber = pf['url'].replace(f'{url_pokeapi}/pokemon-species/',
                                      '').rstrip('/')
    pokemon = requests.get(f"{url_pokeapi}/pokemon/{pokemonNumber}").json()
    pokemonData = {
      'name':
      pokemon['name'],
      'abilities':
      [ability['ability']['name'] for ability in pokemon['abilities']],
      'image':
      pokemon['sprites']['front_default']
    }
    print(pokemonData)



#Opción 5: Listar pokemons por tipo

def menu_pokemon_tipo():
    print('Estos son los tipos: ')
    url_tipo = f'{url_pokeapi}/type'
    pokemonTipo = requests.get(url_tipo).json()['results']
  
    for pf in pokemonTipo:
        print(f"{pf['name']}")
  
    Types = input("Ingresa el tipo de pokemon que buscas: ")
    print(Types)

    pokemonss = requests.get(f'{url_tipo}/{Types}').json()['pokemon']
 
    for pf in pokemonss:
        print(pf)
        pokemonNumber = pf['pokemon']['url'].replace(f'{url_pokeapi}/pokemon/',
                                      '').rstrip('/')
        pokemon = requests.get(f"{url_pokeapi}/pokemon/{pokemonNumber}").json()
        pokemonData = {
        'name':
        pokemon['name'],
        'abilities':
        [ability['ability']['name'] for ability in pokemon['abilities']],
        'image':
        pokemon['sprites']['front_default']
        }
    print(pokemonData)

#MENU PRINCIPAL
def mainmenu():
    while True:
        print("\n")
        print("            Bienvenidos            ")
        print("               Menú                ")
        print("\n")
        print("Seleccione una de las siguientes opciones: ");
        print("1. Listar pokemons por generación.")
        print("2. Listar pokemons por forma.")
        print("3. Listar pokemons por habilidad.")
        print("4. Listar pokemons por habitat.")
        print("5. Listar pokemons por tipo")

        opcion = int(input("Ocpción: "))
        if opcion == 1:
            menu_pokemon_generacion()
        elif opcion == 2:
            menu_pokemon_forma()
        elif opcion == 3:
            menu_pokemon_habilidad()
        elif opcion == 4:
            menu_pokemon_habitat()
        elif opcion == 5:
            menu_pokemon_tipo()
        elif opcion == 6:
            break
mainmenu()
