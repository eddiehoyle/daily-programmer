"""
"""
 
import re
import urllib2
import os

def get_pokemon():
	'''Get dict of pokemon and types'''

	start = 1
	end = 151
	# To save on attacking GameFAQs bandwidth, I downloaded this text and 
	# tested locally
	url = 'http://db.gamefaqs.com/portable/gbadvance/file/pokemon_frlg_pokedex.txt'
	data = urllib2.urlopen(url).read()

	# Cut down the massive wall of text to be the Pokemon list section and 
	# join into a single line string. This avoids \r\n characters
	between = "".join(data[data.find("{III. Pokedex}"):data.find("{IV. FAQ}")].split())

	# Find the Pokemon!
	pokemon = {}
	indexes = ["%03d" % i for i in range(start, end+1)]
	for i in indexes:

		# The name of the Pokemon looks like 001-Bulbasaur, easy enough to find.
		# However, Mr.Mime has a non-alphanumeric character with following text,
		# same with Farfetch'd. Need to cater towards these fancy Pokemon.
		re_name = re.compile(r"%s\-(([A-Z][a-z]+)(\W*\w+))Type" % i)
		name = re_name.search(between).groups()[0]
		pokemon[name] = []

		# Some Pokemon can have multiple types. This expression looks for a 
		# pattern that looks like 001-BulbasaurType:Grass/PoisonLocations and extracts
		# Grass, Poison into a tuple
		re_types = re.compile(r"%s-[%sA-Za-z]+Type:([A-Z][a-z]+)/?(|[A-Z][a-z]+)Locations" % (i, name))
		types = re_types.search(between).groups()

		# Remove any empty strings from types array if Pokemon
		# only has one Type
		pokemon[name] = filter(None, types)
	return pokemon

# The data I mined doesn't have all 1000 Pokemon or what ever there is now,
# so I've limited the range of Pokemon to return to original 151. Let's be
# honest, they're the only cool ones
# get_pokemon()

POKEMON = {'Oddish': ('Poison', 'Grass'), 'Weezing': ('Poison',), 'Magikarp': ('Water',), 'Jynx': ('Ice', 'Psychic'), 'Paras': ('Bug', 'Grass'), 'Kadabra': ('Psychic',), 'Sandslash': ('Ground',), 'Beedrill': ('Bug', 'Poison'), 'Hitmonlee': ('Fighting',), 'Poliwrath': ('Water', 'Fighting'), 'Machamp': ('Fighting',), 'Butterfree': ('Bug', 'Flying'), 'Raichu': ('Electric',), 'Omanyte': ('Rock', 'Water'), 'Tangela': ('Grass',), 'Slowpoke': ('Water', 'Psychic'), 'Mew': ('Psychic',), 'Diglett': ('Ground',), 'Rhydon': ('Rock', 'Ground'), 'Poliwhirl': ('Water',), "Farfetch'd": ('Normal', 'Flying'), 'Raticate': ('Normal',), 'Tentacool': ('Water', 'Poison'), 'Magnemite': ('Electric', 'Steel'), 'Ditto': ('Normal',), 'Aerodactyl': ('Rock', 'Flying'), 'Koffing': ('Poison',), 'Shellder': ('Water',), 'Magmar': ('Fire',), 'Mankey': ('Fighting',), 'Dratini': ('Dragon',), 'Nidoqueen': ('Poison', 'Ground'), 'Charmeleon': ('Fire',), 'Psyduck': ('Water',), 'Slowbro': ('Water', 'Psychic'), 'Snorlax': ('Normal',), 'Arcanine': ('Fire',), 'Omastar': ('Rock', 'Water'), 'Growlithe': ('Fire',), 'Articuno': ('Ice', 'Flying'), 'Blastoise': ('Water',), 'Golem': ('Rock', 'Ground'), 'Krabby': ('Water',), 'Pinsir': ('Bug',), 'Cloyster': ('Water', 'Ice'), 'Kangaskhan': ('Normal',), 'Tauros': ('Normal',), 'Fearow': ('Normal', 'Flying'), 'Bulbasaur': ('Grass', 'Poison'), 'Jigglypuff': ('Normal',), 'Abra': ('Psychic',), 'Arbok': ('Poison',), 'Doduo': ('Normal', 'Flying'), 'Muk': ('Poison',), 'Marowak': ('Ground',), 'Wartortle': ('Water',), 'Wigglytuff': ('Normal',), 'Porygon': ('Normal',), 'Graveler': ('Rock', 'Ground'), 'Chansey': ('Normal',), 'Geodude': ('Rock', 'Ground'), 'Pidgeotto': ('Normal', 'Flying'), 'Rattata': ('Normal',), 'Mewtwo': ('Psychic',), 'Primeape': ('Fighting',), 'Squirtle': ('Water',), 'Vulpix': ('Fire',), 'Zapdos': ('Flying', 'Electric'), 'Bellsprout': ('Grass', 'Poison'), 'Jolteon': ('Electric',), 'Venusaur': ('Grass', 'Poison'), 'Poliwag': ('Water',), 'Spearow': ('Normal', 'Flying'), 'Golduck': ('Water',), 'Ekans': ('Poison',), 'Alakazam': ('Psychic',), 'Kabutops': ('Rock', 'Water'), 'Seel': ('Water',), 'NidoranMale': ('Poison',), 'Voltorb': ('Electric',), 'Dragonite': ('Dragon', 'Flying'), 'Gyarados': ('Water', 'Flying'), 'Vaporeon': ('Water',), 'Metapod': ('Bug',), 'Dragonair': ('Dragon',), 'Ponyta': ('Fire',), 'Lickitung': ('Normal',), 'Haunter': ('Poison', 'Ghost'), 'Ivysaur': ('Grass', 'Poison'), 'Onix': ('Rock', 'Ground'), 'Gastly': ('Poison', 'Ghost'), 'Drowzee': ('Psychic',), 'Goldeen': ('Water',), 'Pidgey': ('Normal', 'Flying'), 'Hypno': ('Psychic',), 'Machoke': ('Fighting',), 'Exeggutor': ('Grass', 'Psychic'), 'Meowth': ('Normal',), 'Eevee': ('Normal',), 'Sandshrew': ('Ground',), 'Venomoth': ('Bug', 'Poison'), 'Victreebel': ('Grass', 'Poison'), 'Nidorino': ('Poison',), 'Nidorina': ('Poison',), 'Pidgeot': ('Normal', 'Flying'), 'Tentacruel': ('Water', 'Poison'), 'Kingler': ('Water',), 'Exeggcute': ('Grass', 'Psychic'), 'Weepinbell': ('Grass', 'Poison'), 'Golbat': ('Poison', 'Flying'), 'Gengar': ('Poison', 'Ghost'), 'Rapidash': ('Fire',), 'Parasect': ('Bug', 'Grass'), 'Dugtrio': ('Ground',), 'Dodrio': ('Normal', 'Flying'), 'Seadra': ('Water',), 'Persian': ('Normal',), 'Nidoking': ('Poison', 'Ground'), 'Scyther': ('Bug', 'Flying'), 'Zubat': ('Poison', 'Flying'), 'Charmander': ('Fire',), 'Electrode': ('Electric',), 'Moltres': ('Flying', 'Fire'), 'Gloom': ('Poison', 'Grass'), 'Flareon': ('Fire',), 'Kabuto': ('Rock', 'Water'), 'Mr.Mime': ('Psychic',), 'Electabuzz': ('Electric',), 'Venonat': ('Bug', 'Poison'), 'Charizard': ('Fire', 'Flying'), 'Pikachu': ('Electric',), 'Machop': ('Fighting',), 'Caterpie': ('Bug',), 'Kakuna': ('Bug', 'Poison'), 'Horsea': ('Water',), 'Seaking': ('Water',), 'Dewgong': ('Water', 'Ice'), 'Hitmonchan': ('Fighting',), 'Clefable': ('Normal',), 'NidoranFemale': ('Poison',), 'Starmie': ('Water', 'Psychic'), 'Rhyhorn': ('Rock', 'Ground'), 'Ninetales': ('Fire',), 'Cubone': ('Ground',), 'Weedle': ('Bug', 'Poison'), 'Vileplume': ('Poison', 'Grass'), 'Clefairy': ('Normal',), 'Grimer': ('Poison',), 'Magneton': ('Electric', 'Steel'), 'Lapras': ('Water', 'Ice'), 'Staryu': ('Water',)}
TYPES = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon']
VALUES = [['1', '1', '1', '1', '1', '0.5', '1', '0', '1', '1', '1', '1', '1', '1', '1'], ['2', '1', '0.5', '0.5', '1', '2', '0.5', '0', '1', '1', '1', '1', '0.5', '2', '1'], ['1', '2', '1', '1', '1', '0.5', '2', '1', '1', '1', '2', '0.5', '1', '1', '1'], ['1', '1', '1', '0.5', '0.5', '0.5', '2', '0.5', '1', '1', '2', '1', '1', '1', '1'], ['1', '1', '0', '2', '1', '2', '0.5', '1', '2', '1', '0.5', '2', '1', '1', '1'], ['1', '0.5', '2', '1', '0.5', '1', '2', '1', '2', '1', '1', '1', '1', '2', '1'], ['1', '0.5', '0.5', '2', '1', '1', '1', '0.5', '0.5', '1', '2', '1', '2', '1', '1'], ['0', '1', '1', '1', '1', '1', '1', '2', '1', '1', '1', '1', '0', '1', '1'], ['1', '1', '1', '1', '1', '0.5', '2', '1', '0.5', '0.5', '2', '1', '1', '2', '0.5'], ['1', '1', '1', '1', '2', '2', '1', '1', '2', '0.5', '0.5', '1', '1', '1', '0.5'], ['1', '1', '0.5', '0.5', '2', '2', '0.5', '1', '0.5', '2', '0.5', '1', '1', '1', '0.5'], ['1', '1', '2', '1', '0', '1', '1', '1', '1', '2', '0.5', '0.5', '1', '1', '0.5'], ['1', '2', '1', '2', '1', '1', '1', '1', '1', '1', '1', '1', '0.5', '1', '1'], ['1', '1', '2', '1', '2', '1', '1', '1', '1', '0.5', '2', '1', '1', '0.5', '2'], ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '2']]

def get_multiplier(attack, defense):
	attack_num = TYPES.index(attack)
	defense_num = TYPES.index(defense)
	return VALUES[attack_num][defense_num]



moves2 = "".join("""<td class="cell-icon-string"><a class="ent-name" href="/move/absorb" title="View details for Absorb">Absorb</a></td><td class="cell-icon"><a class="type-icon type-grass"  href="/type/grass" >Grass</a></td><td class="cell-icon"><i class="icon-move-cat special" title="Special">Special</i></td> <td class="num">20</td> <td class="num" >100</td> <td class="num">25</td> 
			<td class="num"></td>
			<td class="long-text">User recovers half the HP inflicted on opponent.</td>
			<td class="num">-</td>
		</tr>
			<tr>
			<td class="cell-icon-string"><a class="ent-name" href="/move/acid" title="View details for Acid">Acid</a></td><td class="cell-icon"><a class="type-icon type-poison"  href="/type/poison" >Poison</a></td><td class="cell-icon"><i class="icon-move-cat special" title="Special">Special</i></td> <td class="num">40</td> <td class="num" >100</td> <td class="num">30</td> 
			<td class="num"></td>
			<td class="long-text">May lower opponent's Special Defense.</td>
			<td class="num">10</td>
		</tr>
			<tr>
			<td class="cell-icon-string"><a class="ent-name" href="/move/acid-armor" title="View details for Acid Armor">Acid Armor</a></td><td class="cell-icon"><a class="type-icon type-poison"  href="/type/poison" >Poison</a></td><td class="cell-icon"><i class="icon-move-cat status" title="Status">Status</i></td> <td class="num">-</td> <td class="num" >-</td> <td class="num">20</td> 
			<td class="num"></td>
			<td class="long-text">Sharply raises user's Defense.</td>
			<td class="num">-</td>
		</tr>""".split())

def get_moves():
	# Using website: http://pokemondb.net/move/all
	f = open("/Users/eddiehoyle/Sites/dailyProgrammer/102/python/moves.txt")
	html = f.read()
	moves = "".join(html[html.find('id="moves"'):].split())
	f.close()
 	return re.findall(r'Viewdetailsfor(\w+).+?/type/.+?>(\w+).+?num.+?>(\-|\w+)', moves)



