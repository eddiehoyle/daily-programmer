 
import re
import urllib2
 
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

		# Some Pokemon can be multiple types
		re_types = re.compile(r"%s-[%sA-Za-z]+Type:([A-Z][a-z]+)/?(|[A-Z][a-z]+)Locations" % (i, name))
		types = re_types.search(between).groups()

		# Remove any empty strings from types array if Pokemon
		# only has one Type
		pokemon[name] = filter(None, types)
	return pokemon

# The data I mined doesn't have all 1000 Pokemon or what ever there is now,
# so I've limited the range of Pokemon to return to original 151. Let's be
# honest, they're the only cool ones
print get_pokemon()