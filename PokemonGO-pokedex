#!/usr/bin/env python
# Usage:
# $ pokemonGO-pokedex
# Enter the Pokedex number from Pokemon GO Application.
#
# import library
import requests
import json

id = raw_input('Enter Pokedex number from Pokemon GO: ') # Generate id based on user input
url = ('http://pokeapi.co/api/v2/pokemon/' + id ) # URL from pokeapi.co using pokemon list API

r = requests.get(url)
pokedex_data = json.loads(r.text)

print "Pokemon name is: ", pokedex_data[u'name'] # print Pokemon name
