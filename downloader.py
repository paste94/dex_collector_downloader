#%%
# import pokebase as pb
import requests
import json 

#%% 
POKEMON_LIMIT = 10
FILENAME = 'pokemon_list.json'

pokemon_list = requests.get(f'https://pokeapi.co/api/v2/pokemon-species?limit={POKEMON_LIMIT}')
pokemon_list = json.loads(pokemon_list.text)

#%% Get single pokemon species
species_list = []
for p in pokemon_list['results']:
    url = p['url']
    # print(url)
    species_list.append(json.loads(requests.get(url).text))

#%%
pokemon_list = []
for specie in species_list:
    variety_list = specie['varieties']
    for v in variety_list:
        url = v['pokemon']['url']
        variety = json.loads(requests.get(url).text)
        # print(variety)
        pokemon = {
            'id': variety['id'],
            'name': variety['name'],
            'img': variety['sprites']['front_default'],
            'img_shiny': variety['sprites']['front_shiny'],
            'generation': specie['generation']['name'],
            'color': specie['color']['name'],
        }
        pokemon_list.append(pokemon)
# %%
json.dump(pokemon_list, open(FILENAME, 'w'))