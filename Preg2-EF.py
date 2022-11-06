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

#Opción 1: Listar pokemons por generación.
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
        
#Opción 2: Listar pokemons por forma.

def menu_pokemon_forma():
    pass #borrar el pass cuando se escriba el código

#Opción 3: Listar pokemons por habilidad.

def menu_pokemon_habilidad():
    pass #borrar el pass cuando se escriba el código

#Opción 4: Listar pokemons por habitat.

def menu_pokemon_habitat():
    pass #borrar el pass cuando se escriba el código

#Opción 5: Listar pokemons por tipo.
def menu_pokemon_tipo():
    pass #borrar el pass cuando se escriba el código

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