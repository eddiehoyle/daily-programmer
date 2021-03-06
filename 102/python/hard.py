"""
# 102, Hard
http://www.reddit.com/r/dailyprogrammer/comments/10pfsf/9302012_challenge_102_difficult_pok%C3%A9mon_types/

Ah, who doesn't remember the endless hours wasted playing Pokemon games on a Game Boy during long car rides? I sure do. Pokemon had an interesting battle system, and one of the nice mechanics was the type system.
For this challenge, you'll be writing a function, type_effect, that takes two string arguments -- the offending move's name and the defending Pokemon's name -- and returns a multiplier like 2.0 or 0.25.
Generally, you take the offending move's type, look up the multipliers for all the defending Pokemon's types in the type chart, and multiply them together. As an example, we'll run through the calculations for type_effect("Ice Beam", "Dragonite").
	(Optionally, use enums instead of strings, like type_effect(M_ICE_BEAM, P_DRAGONITE)).
	Ice Beam[1] is an Ice move.
	Dragonite[2] has multiple types, Dragon and Flying.
	According to the type chart[3] , Ice vs. Dragon has a 2.0 bonus, and Ice vs. Flying has a 2.0 bonus, too. Multiplying these together, you get 4.0, so return 4.0.
"""
 
import re, urllib2, os

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

def get_moves():
	'''Get list of moves from 5 generations of Pokemon'''
	# Using website: http://pokemondb.net/move/all
	
	url = 'http://pokemondb.net/move/all'
	html = urllib2.urlopen(url).read()
	moves = "".join(html[html.find('id="moves"'):].split())

	# ---------------- #
	# Open file, read html
	# f = open("/Users/eddiehoyle/Sites/dailyProgrammer/102/python/moves.txt")
	# html = f.read()
	# moves = "".join(html[html.find('id="moves"'):].split())
	# f.close()
	
	# Split up into (Name, Type, Attack) eg: (Acid, Posion, 20) tuple
	data = {}
	found = re.findall(r"Viewdetailsfor(\w+).+?/type/.+?>(\w+).+?num.+?>(\-|\w+)", moves)
	for m in found:

		# Replace the status effects to be zeros
		m = list(m)
		if m[2] == '-':
			m[2] = 0

		# Assign move and type
		data[m[0]]=(m[1], int(m[2]))

 	return data

# ========================================================================= #
# The data I mined doesn't have all 1000 Pokemon or what ever there is now,
# so I've limited the range of Pokemon to return to original 151. Let's be
# honest, they're the only cool ones. However I ended up using moves from 
# all 5 generations because I realised I was regexing the wrong page. Oops.
# ========================================================================= #
POKEMON = {'Oddish': ('Poison', 'Grass'), 'Weezing': ('Poison',), 'Magikarp': ('Water',), 'Jynx': ('Ice', 'Psychic'), 'Paras': ('Bug', 'Grass'), 'Kadabra': ('Psychic',), 'Sandslash': ('Ground',), 'Beedrill': ('Bug', 'Poison'), 'Hitmonlee': ('Fighting',), 'Poliwrath': ('Water', 'Fighting'), 'Machamp': ('Fighting',), 'Butterfree': ('Bug', 'Flying'), 'Raichu': ('Electric',), 'Omanyte': ('Rock', 'Water'), 'Tangela': ('Grass',), 'Slowpoke': ('Water', 'Psychic'), 'Mew': ('Psychic',), 'Diglett': ('Ground',), 'Rhydon': ('Rock', 'Ground'), 'Poliwhirl': ('Water',), "Farfetch'd": ('Normal', 'Flying'), 'Raticate': ('Normal',), 'Tentacool': ('Water', 'Poison'), 'Magnemite': ('Electric', 'Steel'), 'Ditto': ('Normal',), 'Aerodactyl': ('Rock', 'Flying'), 'Koffing': ('Poison',), 'Shellder': ('Water',), 'Magmar': ('Fire',), 'Mankey': ('Fighting',), 'Dratini': ('Dragon',), 'Nidoqueen': ('Poison', 'Ground'), 'Charmeleon': ('Fire',), 'Psyduck': ('Water',), 'Slowbro': ('Water', 'Psychic'), 'Snorlax': ('Normal',), 'Arcanine': ('Fire',), 'Omastar': ('Rock', 'Water'), 'Growlithe': ('Fire',), 'Articuno': ('Ice', 'Flying'), 'Blastoise': ('Water',), 'Golem': ('Rock', 'Ground'), 'Krabby': ('Water',), 'Pinsir': ('Bug',), 'Cloyster': ('Water', 'Ice'), 'Kangaskhan': ('Normal',), 'Tauros': ('Normal',), 'Fearow': ('Normal', 'Flying'), 'Bulbasaur': ('Grass', 'Poison'), 'Jigglypuff': ('Normal',), 'Abra': ('Psychic',), 'Arbok': ('Poison',), 'Doduo': ('Normal', 'Flying'), 'Muk': ('Poison',), 'Marowak': ('Ground',), 'Wartortle': ('Water',), 'Wigglytuff': ('Normal',), 'Porygon': ('Normal',), 'Graveler': ('Rock', 'Ground'), 'Chansey': ('Normal',), 'Geodude': ('Rock', 'Ground'), 'Pidgeotto': ('Normal', 'Flying'), 'Rattata': ('Normal',), 'Mewtwo': ('Psychic',), 'Primeape': ('Fighting',), 'Squirtle': ('Water',), 'Vulpix': ('Fire',), 'Zapdos': ('Flying', 'Electric'), 'Bellsprout': ('Grass', 'Poison'), 'Jolteon': ('Electric',), 'Venusaur': ('Grass', 'Poison'), 'Poliwag': ('Water',), 'Spearow': ('Normal', 'Flying'), 'Golduck': ('Water',), 'Ekans': ('Poison',), 'Alakazam': ('Psychic',), 'Kabutops': ('Rock', 'Water'), 'Seel': ('Water',), 'NidoranMale': ('Poison',), 'Voltorb': ('Electric',), 'Dragonite': ('Dragon', 'Flying'), 'Gyarados': ('Water', 'Flying'), 'Vaporeon': ('Water',), 'Metapod': ('Bug',), 'Dragonair': ('Dragon',), 'Ponyta': ('Fire',), 'Lickitung': ('Normal',), 'Haunter': ('Poison', 'Ghost'), 'Ivysaur': ('Grass', 'Poison'), 'Onix': ('Rock', 'Ground'), 'Gastly': ('Poison', 'Ghost'), 'Drowzee': ('Psychic',), 'Goldeen': ('Water',), 'Pidgey': ('Normal', 'Flying'), 'Hypno': ('Psychic',), 'Machoke': ('Fighting',), 'Exeggutor': ('Grass', 'Psychic'), 'Meowth': ('Normal',), 'Eevee': ('Normal',), 'Sandshrew': ('Ground',), 'Venomoth': ('Bug', 'Poison'), 'Victreebel': ('Grass', 'Poison'), 'Nidorino': ('Poison',), 'Nidorina': ('Poison',), 'Pidgeot': ('Normal', 'Flying'), 'Tentacruel': ('Water', 'Poison'), 'Kingler': ('Water',), 'Exeggcute': ('Grass', 'Psychic'), 'Weepinbell': ('Grass', 'Poison'), 'Golbat': ('Poison', 'Flying'), 'Gengar': ('Poison', 'Ghost'), 'Rapidash': ('Fire',), 'Parasect': ('Bug', 'Grass'), 'Dugtrio': ('Ground',), 'Dodrio': ('Normal', 'Flying'), 'Seadra': ('Water',), 'Persian': ('Normal',), 'Nidoking': ('Poison', 'Ground'), 'Scyther': ('Bug', 'Flying'), 'Zubat': ('Poison', 'Flying'), 'Charmander': ('Fire',), 'Electrode': ('Electric',), 'Moltres': ('Flying', 'Fire'), 'Gloom': ('Poison', 'Grass'), 'Flareon': ('Fire',), 'Kabuto': ('Rock', 'Water'), 'Mr.Mime': ('Psychic',), 'Electabuzz': ('Electric',), 'Venonat': ('Bug', 'Poison'), 'Charizard': ('Fire', 'Flying'), 'Pikachu': ('Electric',), 'Machop': ('Fighting',), 'Caterpie': ('Bug',), 'Kakuna': ('Bug', 'Poison'), 'Horsea': ('Water',), 'Seaking': ('Water',), 'Dewgong': ('Water', 'Ice'), 'Hitmonchan': ('Fighting',), 'Clefable': ('Normal',), 'NidoranFemale': ('Poison',), 'Starmie': ('Water', 'Psychic'), 'Rhyhorn': ('Rock', 'Ground'), 'Ninetales': ('Fire',), 'Cubone': ('Ground',), 'Weedle': ('Bug', 'Poison'), 'Vileplume': ('Poison', 'Grass'), 'Clefairy': ('Normal',), 'Grimer': ('Poison',), 'Magneton': ('Electric', 'Steel'), 'Lapras': ('Water', 'Ice'), 'Staryu': ('Water',)}
TYPES = ['Normal', 'Fighting', 'Flying', 'Poison', 'Ground', 'Rock', 'Bug', 'Ghost', 'Fire', 'Water', 'Grass', 'Electric', 'Psychic', 'Ice', 'Dragon']
VALUES = [['1',  '1',   '1',   '1',   '1',   '0.5', '1',   '0',   '1',   '1',   '1',   '1',   '1',   '1',   '1'], 
		  ['2',  '1',   '0.5', '0.5', '1',   '2',   '0.5', '0',   '1',   '1',   '1',   '1',   '0.5', '2',   '1'], 
		  ['1',  '2',   '1',   '1',   '1',   '0.5', '2',   '1',   '1',   '1',   '2',   '0.5', '1',   '1',   '1'], 
		  ['1',  '1',   '1',   '0.5', '0.5', '0.5', '2',   '0.5', '1',   '1',   '2',   '1',   '1',   '1',   '1'], 
	  	  ['1',  '1',   '0',   '2',   '1',   '2',   '0.5', '1',   '2',   '1',   '0.5', '2',   '1',   '1',   '1'], 
	  	  ['1',  '0.5', '2',   '1',   '0.5', '1',   '2',   '1',   '2',   '1',   '1',   '1',   '1',   '2',   '1'], 
	  	  ['1',  '0.5', '0.5', '2',   '1',   '1',   '1',   '0.5', '0.5', '1',   '2',   '1',   '2',   '1',   '1'], 
	  	  ['0',  '1',   '1',   '1',   '1',   '1',   '1',   '2',   '1',   '1',   '1',   '1',   '0',   '1',   '1'], 
	  	  ['1',  '1',   '1',   '1',   '1',   '0.5', '2',   '1',   '0.5', '0.5', '2',   '1',   '1',   '2',   '0.5'], 
	  	  ['1',  '1',   '1',   '1',   '2',   '2',   '1',   '1',   '2',   '0.5', '0.5', '1',   '1',   '1',   '0.5'], 
	  	  ['1',  '1',   '0.5', '0.5', '2',   '2',   '0.5', '1',   '0.5', '2',   '0.5', '1',   '1',   '1',   '0.5'], 
	  	  ['1',  '1',   '2',   '1',   '0',   '1',   '1',   '1',   '1',   '2',   '0.5', '0.5', '1',   '1',   '0.5'], 
	  	  ['1',  '2',   '1',   '2',   '1',   '1',   '1',   '1',   '1',   '1',   '1',   '1',   '0.5', '1',   '1'], 
	  	  ['1',  '1',   '2',   '1',   '2',   '1',   '1',   '1',   '1',   '0.5', '2',   '1',   '1',   '0.5', '2'], 
	  	  ['1',  '1',   '1',   '1',   '1',   '1',   '1',   '1',   '1',   '1',   '1',   '1',   '1',   '1',   '2']]
MOVES = {'Spite': ('Ghost', 0), 'Detect': ('Fighting', 0), 'Fissure': ('Ground', 0), 'MagnetRise': ('Electric', 0), 'SteelWing': ('Steel', 70), 'Self': ('Normal', 200), 'V': ('Fire', 180), 'MistBall': ('Psychic', 70), 'Psyshock': ('Psychic', 80), 'RelicSong': ('Normal', 75), 'Soak': ('Water', 0), 'WorrySeed': ('Grass', 0), 'Stomp': ('Normal', 65), 'Struggle': ('Normal', 50), 'Infestation': ('Bug', 20), 'Psywave': ('Psychic', 0), 'HighJumpKick': ('Fighting', 130), 'WaterPledge': ('Water', 80), 'Minimize': ('Normal', 0), 'RockClimb': ('Normal', 90), 'HeadCharge': ('Normal', 120), 'PsychoCut': ('Psychic', 70), 'Refresh': ('Normal', 0), 'Hypnosis': ('Psychic', 0), 'AquaTail': ('Water', 90), 'FreezeShock': ('Ice', 140), 'Punishment': ('Dark', 0), 'BlazeKick': ('Fire', 85), 'DragonDance': ('Dragon', 0), 'VineWhip': ('Grass', 45), 'BulkUp': ('Fighting', 0), 'HeatCrash': ('Fire', 0), 'Teleport': ('Psychic', 0), 'Moonblast': ('Fairy', 95), 'WringOut': ('Normal', 0), 'Endeavor': ('Normal', 0), 'Bulldoze': ('Ground', 60), 'Attract': ('Normal', 0), 'ThunderPunch': ('Electric', 75), 'SearingShot': ('Fire', 100), 'Nightmare': ('Ghost', 0), 'Gravity': ('Psychic', 0), 'LuckyChant': ('Normal', 0), 'DefendOrder': ('Bug', 0), 'WaterGun': ('Water', 40), 'SeedBomb': ('Grass', 80), 'RoarofTime': ('Dragon', 150), 'LusterPurge': ('Psychic', 70), 'FieryDance': ('Fire', 80), 'IceBurn': ('Ice', 140), 'HeavySlam': ('Steel', 0), 'Twister': ('Dragon', 40), 'CalmMind': ('Psychic', 0), 'Pluck': ('Flying', 60), 'Barrage': ('Normal', 15), 'GyroBall': ('Steel', 0), 'AirSlash': ('Flying', 75), 'Swift': ('Normal', 60), 'Octazooka': ('Water', 65), 'TrickRoom': ('Psychic', 0), 'AquaJet': ('Water', 40), 'StormThrow': ('Fighting', 60), 'MilkDrink': ('Normal', 0), 'RockTomb': ('Rock', 60), 'LunarDance': ('Psychic', 0), 'Thrash': ('Normal', 120), 'Bide': ('Normal', 0), 'SkyUppercut': ('Fighting', 85), 'Rototiller': ('Ground', 0), 'GastroAcid': ('Poison', 0), 'BoltStrike': ('Electric', 130), 'ThunderShock': ('Electric', 40), 'Hail': ('Ice', 0), 'Freeze': ('Ice', 70), 'MeteorMash': ('Steel', 90), 'Smog': ('Poison', 30), 'MistyTerrain': ('Fairy', 0), 'HealBell': ('Normal', 0), 'Leer': ('Normal', 0), 'FlowerShield': ('Fairy', 0), 'ShadowPunch': ('Ghost', 60), 'Electrify': ('Electric', 0), 'Captivate': ('Normal', 0), 'AcidArmor': ('Poison', 0), 'Synchronoise': ('Psychic', 120), 'SuckerPunch': ('Dark', 80), 'IceBeam': ('Ice', 90), 'HydroPump': ('Water', 110), 'Inferno': ('Fire', 100), 'KnockOff': ('Dark', 55), 'PowerWhip': ('Grass', 120), 'RollingKick': ('Fighting', 60), 'PowerGem': ('Rock', 80), 'Belch': ('Poison', 120), 'PoisonPowder': ('Poison', 0), 'PartingShot': ('Dark', 0), 'SuperFang': ('Normal', 0), 'Supersonic': ('Normal', 0), 'Land': ('Ground', 90), 'ReflectType': ('Normal', 0), 'PowerSwap': ('Psychic', 0), 'FirePledge': ('Fire', 80), 'SludgeWave': ('Poison', 95), 'ShellSmash': ('Normal', 0), 'DefenseCurl': ('Normal', 0), 'Whirlwind': ('Normal', 0), 'Blizzard': ('Ice', 110), 'PetalBlizzard': ('Grass', 90), 'Flatter': ('Dark', 0), 'Torment': ('Dark', 0), 'Present': ('Normal', 0), 'Wrap': ('Normal', 15), 'Twineedle': ('Bug', 25), 'MagnetBomb': ('Steel', 60), 'MeFirst': ('Normal', 0), 'Hurricane': ('Flying', 110), 'MindReader': ('Normal', 0), 'EggBomb': ('Normal', 100), 'FeintAttack': ('Dark', 60), 'HornAttack': ('Normal', 65), 'DoubleHit': ('Normal', 35), 'PinMissile': ('Bug', 25), 'DisarmingVoice': ('Fairy', 40), 'Extrasensory': ('Psychic', 80), 'StealthRock': ('Rock', 0), 'FlareBlitz': ('Fire', 120), 'Spark': ('Electric', 65), 'Memento': ('Dark', 0), 'Powder': ('Bug', 0), 'DarkVoid': ('Dark', 0), 'ShadowBall': ('Ghost', 80), 'ToxicSpikes': ('Poison', 0), 'Will': ('Fire', 0), 'SandTomb': ('Ground', 35), 'RockBlast': ('Rock', 25), 'FakeOut': ('Normal', 40), 'Constrict': ('Normal', 10), 'IcicleCrash': ('Ice', 85), 'MegaPunch': ('Normal', 80), 'CrossChop': ('Fighting', 100), 'Facade': ('Normal', 70), 'PainSplit': ('Normal', 0), 'FlameWheel': ('Fire', 60), 'DragonTail': ('Dragon', 60), 'Copycat': ('Normal', 0), 'CrushClaw': ('Normal', 75), 'BugBite': ('Bug', 60), 'Tailwind': ('Flying', 0), 'RockPolish': ('Rock', 0), 'CrushGrip': ('Normal', 0), 'FrostBreath': ('Ice', 60), 'Haze': ('Ice', 0), 'FalseSwipe': ('Normal', 40), 'Amnesia': ('Psychic', 0), 'BoneClub': ('Ground', 65), 'ShadowSneak': ('Ghost', 40), 'QuiverDance': ('Bug', 0), 'FireBlast': ('Fire', 110), 'Synthesis': ('Grass', 0), 'RazorShell': ('Water', 75), 'ViceGrip': ('Normal', 55), 'Absorb': ('Grass', 20), 'Assist': ('Normal', 0), 'VoltSwitch': ('Electric', 70), 'Snarl': ('Dark', 55), 'MeanLook': ('Normal', 0), 'RockWrecker': ('Rock', 150), 'Sing': ('Normal', 0), 'Snore': ('Normal', 50), 'PoisonGas': ('Poison', 0), 'RainDance': ('Water', 0), 'TrumpCard': ('Normal', 0), 'MachPunch': ('Fighting', 40), 'MagicRoom': ('Psychic', 0), 'ChipAway': ('Normal', 70), 'WaterSpout': ('Water', 150), 'Clamp': ('Water', 35), 'SonicBoom': ('Normal', 0), 'CometPunch': ('Normal', 18), 'Spore': ('Grass', 0), 'AttackOrder': ('Bug', 90), 'SpikeCannon': ('Normal', 20), 'VenomDrench': ('Poison', 0), 'ConfuseRay': ('Ghost', 0), 'VacuumWave': ('Fighting', 40), 'SludgeBomb': ('Poison', 90), 'Curse': ('Ghost', 0), 'BlastBurn': ('Fire', 150), 'GunkShot': ('Poison', 120), 'WideGuard': ('Rock', 0), 'Mud': ('Ground', 20), 'StruggleBug': ('Bug', 50), 'OdorSleuth': ('Normal', 0), 'Rest': ('Psychic', 0), 'SacredFire': ('Fire', 100), 'LeafStorm': ('Grass', 130), 'Bubble': ('Water', 40), 'Flamethrower': ('Fire', 90), 'DynamicPunch': ('Fighting', 100), 'Swagger': ('Normal', 0), 'EarthPower': ('Ground', 90), 'AirCutter': ('Flying', 60), 'WaterShuriken': ('Water', 15), 'Meditate': ('Psychic', 0), 'ShiftGear': ('Steel', 0), 'Baby': ('Fairy', 0), 'Discharge': ('Electric', 80), 'DrillRun': ('Ground', 80), 'BulletSeed': ('Grass', 25), 'Protect': ('Normal', 0), 'CottonGuard': ('Grass', 0), 'DualChop': ('Dragon', 40), 'GearGrind': ('Steel', 50), 'Covet': ('Normal', 60), 'IcePunch': ('Ice', 75), 'WoodHammer': ('Grass', 120), 'Retaliate': ('Normal', 70), 'DragonBreath': ('Dragon', 60), 'Soft': ('Normal', 0), 'Block': ('Normal', 0), 'Sketch': ('Normal', 0), 'BulletPunch': ('Steel', 40), 'AcidSpray': ('Poison', 40), 'Megahorn': ('Bug', 120), 'TriAttack': ('Normal', 80), 'EnergyBall': ('Grass', 90), 'CottonSpore': ('Grass', 0), 'FrenzyPlant': ('Grass', 150), 'SeedFlare': ('Grass', 120), 'MiracleEye': ('Psychic', 0), 'DragonRush': ('Dragon', 100), 'PoisonTail': ('Poison', 50), 'BellyDrum': ('Normal', 0), 'Outrage': ('Dragon', 120), 'AncientPower': ('Rock', 60), 'Whirlpool': ('Water', 35), 'OminousWind': ('Ghost', 60), 'DarkPulse': ('Dark', 80), 'PoisonSting': ('Poison', 15), 'Taunt': ('Dark', 0), 'Dive': ('Water', 80), 'TailGlow': ('Bug', 0), 'EchoedVoice': ('Normal', 40), 'LovelyKiss': ('Normal', 0), 'Telekinesis': ('Psychic', 0), 'Safeguard': ('Normal', 0), 'Judgment': ('Normal', 100), 'Boomburst': ('Normal', 140), 'BeatUp': ('Dark', 0), 'HydroCannon': ('Water', 150), 'Roar': ('Normal', 0), 'Bind': ('Normal', 15), 'KarateChop': ('Fighting', 50), 'Headbutt': ('Normal', 70), 'MagmaStorm': ('Fire', 120), 'Magnitude': ('Ground', 0), 'GrassKnot': ('Grass', 0), 'Pound': ('Normal', 40), 'HyperFang': ('Normal', 80), 'DragonPulse': ('Dragon', 85), 'SecretPower': ('Normal', 70), 'Thief': ('Dark', 40), 'MagicCoat': ('Psychic', 0), 'BugBuzz': ('Bug', 90), 'Superpower': ('Fighting', 120), 'ElectricTerrain': ('Electric', 0), 'Ingrain': ('Grass', 0), 'DrillPeck': ('Flying', 80), 'Psychic': ('Psychic', 90), 'Tickle': ('Normal', 0), 'ShadowClaw': ('Ghost', 70), 'Astonish': ('Ghost', 30), 'FuryAttack': ('Normal', 15), 'WildCharge': ('Electric', 90), 'SpiderWeb': ('Bug', 0), 'Aeroblast': ('Flying', 100), 'Power': ('Fighting', 40), 'Confusion': ('Psychic', 50), 'SheerCold': ('Ice', 0), 'Pursuit': ('Dark', 40), 'FlameCharge': ('Fire', 50), 'NightShade': ('Ghost', 0), 'MysticalFire': ('Fire', 65), 'HeatWave': ('Fire', 95), 'Defog': ('Flying', 0), 'GrassyTerrain': ('Grass', 0), 'FairyWind': ('Fairy', 40), 'Mimic': ('Normal', 0), 'LastResort': ('Normal', 140), 'Encore': ('Normal', 0), 'IronTail': ('Steel', 100), 'SimpleBeam': ('Normal', 0), 'GigaDrain': ('Grass', 75), 'Lock': ('Normal', 0), 'Geomancy': ('Fairy', 0), 'WeatherBall': ('Normal', 50), 'Growth': ('Normal', 0), 'BlueFlare': ('Fire', 130), 'Guillotine': ('Normal', 0), 'IceBall': ('Ice', 30), 'MirrorShot': ('Steel', 65), 'Substitute': ('Normal', 0), 'AfterYou': ('Normal', 0), 'TripleKick': ('Fighting', 10), 'HornDrill': ('Normal', 0), 'FoulPlay': ('Dark', 95), 'Flash': ('Normal', 0), 'Screech': ('Normal', 0), 'Camouflage': ('Normal', 0), 'VoltTackle': ('Electric', 120), 'Crabhammer': ('Water', 100), 'Quash': ('Dark', 0), 'MirrorMove': ('Flying', 0), 'RagePowder': ('Bug', 0), 'HammerArm': ('Fighting', 100), 'Sharpen': ('Normal', 0), 'FusionFlare': ('Fire', 100), 'RazorLeaf': ('Grass', 55), 'Nuzzle': ('Electric', 20), 'Conversion2': ('Normal', 0), 'Switcheroo': ('Dark', 0), 'Waterfall': ('Water', 80), 'DracoMeteor': ('Dragon', 130), 'TailWhip': ('Normal', 0), 'Earthquake': ('Ground', 100), 'MetalBurst': ('Steel', 0), 'Embargo': ('Dark', 0), 'EerieImpulse': ('Electric', 0), 'HealBlock': ('Psychic', 0), 'RockSmash': ('Fighting', 40), 'SilverWind': ('Bug', 60), 'X': ('Bug', 80), 'LightScreen': ('Psychic', 0), 'Peck': ('Flying', 35), 'HyperVoice': ('Normal', 90), 'FusionBolt': ('Electric', 100), 'SkyAttack': ('Flying', 140), 'CraftyShield': ('Fairy', 0), 'ParabolicCharge': ('Electric', 50), 'Growl': ('Normal', 0), 'Bite': ('Dark', 60), 'GuardSplit': ('Psychic', 0), 'Acrobatics': ('Flying', 55), 'LavaPlume': ('Fire', 80), 'FellStinger': ('Bug', 30), 'AuraSphere': ('Fighting', 80), 'NaturalGift': ('Normal', 0), 'Reversal': ('Fighting', 0), 'HelpingHand': ('Normal', 0), 'SecretSword': ('Fighting', 85), 'PsychoBoost': ('Psychic', 140), 'HornLeech': ('Grass', 75), 'King': ('Steel', 0), 'NightSlash': ('Dark', 70), 'Counter': ('Fighting', 0), 'LowSweep': ('Fighting', 65), 'Harden': ('Normal', 0), 'Uproar': ('Normal', 90), 'JumpKick': ('Fighting', 100), 'HeadSmash': ('Rock', 150), 'MetalClaw': ('Steel', 50), 'StoredPower': ('Psychic', 20), 'VitalThrow': ('Fighting', 70), 'PsychUp': ('Normal', 0), 'Venoshock': ('Poison', 65), 'BraveBird': ('Flying', 120), 'SmellingSalts': ('Normal', 70), 'FakeTears': ('Dark', 0), 'ForcePalm': ('Fighting', 60), 'WaterPulse': ('Water', 60), 'Brine': ('Water', 65), 'MetalSound': ('Steel', 0), 'MudBomb': ('Ground', 65), 'HealPulse': ('Psychic', 0), 'SkyDrop': ('Flying', 60), 'SpikyShield': ('Grass', 0), 'BatonPass': ('Normal', 0), 'Hex': ('Ghost', 65), 'Transform': ('Normal', 0), 'CloseCombat': ('Fighting', 120), 'Forest': ('Grass', 0), 'TailSlap': ('Normal', 25), 'PlayRough': ('Fairy', 90), 'Recycle': ('Normal', 0), 'FeatherDance': ('Flying', 0), 'WorkUp': ('Normal', 0), 'ZenHeadbutt': ('Psychic', 80), 'Surf': ('Water', 90), 'Crunch': ('Dark', 80), 'SacredSword': ('Fighting', 90), 'DrainPunch': ('Fighting', 75), 'Yawn': ('Normal', 0), 'ThunderWave': ('Electric', 0), 'TechnoBlast': ('Normal', 85), 'FinalGambit': ('Fighting', 0), 'SkillSwap': ('Psychic', 0), 'Chatter': ('Flying', 65), 'StoneEdge': ('Rock', 100), 'Grudge': ('Ghost', 0), 'Metronome': ('Normal', 0), 'LeafBlade': ('Grass', 90), 'ClearSmog': ('Poison', 50), 'SleepPowder': ('Grass', 0), 'Round': ('Normal', 60), 'NobleRoar': ('Normal', 0), 'PetalDance': ('Grass', 120), 'BrickBreak': ('Fighting', 75), 'SleepTalk': ('Normal', 0), 'LowKick': ('Fighting', 0), 'DreamEater': ('Psychic', 100), 'Mist': ('Ice', 0), 'QuickAttack': ('Normal', 40), 'PowderSnow': ('Ice', 40), 'FlyingPress': ('Fighting', 80), 'LeechSeed': ('Grass', 0), 'FocusPunch': ('Fighting', 150), 'GrassWhistle': ('Grass', 0), 'Charge': ('Electric', 0), 'SolarBeam': ('Grass', 120), 'Slash': ('Normal', 70), 'Toxic': ('Poison', 0), 'HealingWish': ('Psychic', 0), 'SpacialRend': ('Dragon', 100), 'GrassPledge': ('Grass', 80), 'FocusEnergy': ('Normal', 0), 'Glaciate': ('Ice', 65), 'IceShard': ('Ice', 40), 'Return': ('Normal', 0), 'FlameBurst': ('Fire', 70), 'RockSlide': ('Rock', 75), 'Revenge': ('Fighting', 60), 'Wish': ('Normal', 0), 'Charm': ('Fairy', 0), 'NaturePower': ('Normal', 0), 'SweetScent': ('Normal', 0), 'NeedleArm': ('Grass', 60), 'TeeterDance': ('Normal', 0), 'AquaRing': ('Water', 0), 'BodySlam': ('Normal', 85), 'FirePunch': ('Fire', 75), 'ShadowForce': ('Ghost', 120), 'Explosion': ('Normal', 250), 'MudShot': ('Ground', 55), 'ThunderFang': ('Electric', 65), 'Lick': ('Ghost', 30), 'MagicalLeaf': ('Grass', 60), 'Confide': ('Normal', 0), 'FlashCannon': ('Steel', 80), 'Bounce': ('Flying', 85), 'Avalanche': ('Ice', 60), 'Slam': ('Normal', 80), 'HoneClaws': ('Dark', 0), 'MegaKick': ('Normal', 120), 'DoubleSlap': ('Normal', 15), 'Conversion': ('Normal', 0), 'HeartSwap': ('Psychic', 0), 'Withdraw': ('Water', 0), 'Electroweb': ('Electric', 55), 'Frustration': ('Normal', 0), 'IceFang': ('Ice', 65), 'BoneRush': ('Ground', 25), 'Agility': ('Psychic', 0), 'DoubleTeam': ('Normal', 0), 'Fling': ('Dark', 0), 'AllySwitch': ('Psychic', 0), 'PerishSong': ('Normal', 0), 'Steamroller': ('Bug', 65), 'Eruption': ('Fire', 150), 'AerialAce': ('Flying', 60), 'SpitUp': ('Normal', 0), 'PoisonFang': ('Poison', 50), 'StickyWeb': ('Bug', 0), 'MatBlock': ('Fighting', 0), 'Tackle': ('Normal', 50), 'Coil': ('Poison', 0), 'RazorWind': ('Normal', 80), 'IcyWind': ('Ice', 55), 'Flail': ('Normal', 0), 'FireSpin': ('Fire', 35), 'QuickGuard': ('Fighting', 0), 'IonDeluge': ('Electric', 0), 'StringShot': ('Bug', 0), 'Dig': ('Ground', 80), 'Ember': ('Fire', 40), 'Sandstorm': ('Rock', 0), 'SkullBash': ('Normal', 130), 'GigaImpact': ('Normal', 150), 'Entrainment': ('Normal', 0), 'Psybeam': ('Psychic', 65), 'Acupressure': ('Normal', 0), 'DrainingKiss': ('Fairy', 50), 'Glare': ('Normal', 0), 'FutureSight': ('Psychic', 120), 'AuroraBeam': ('Ice', 65), 'PoisonJab': ('Poison', 80), 'SwordsDance': ('Normal', 0), 'Smokescreen': ('Normal', 0), 'LeechLife': ('Bug', 20), 'Recover': ('Normal', 0), 'Scald': ('Water', 80), 'PsychoShift': ('Psychic', 0), 'HiddenPower': ('Normal', 60), 'Thunder': ('Electric', 110), 'Aromatherapy': ('Grass', 0), 'Strength': ('Normal', 80), 'TakeDown': ('Normal', 90), 'Assurance': ('Dark', 60), 'Rage': ('Normal', 20), 'Snatch': ('Dark', 0), 'NightDaze': ('Dark', 85), 'Wake': ('Fighting', 70), 'RapidSpin': ('Normal', 20), 'WingAttack': ('Flying', 60), 'MegaDrain': ('Grass', 40), 'RolePlay': ('Psychic', 0), 'SignalBeam': ('Bug', 75), 'Submission': ('Fighting', 80), 'Trick': ('Ghost', 0), 'Gust': ('Flying', 40), 'Sludge': ('Poison', 65), 'IcicleSpear': ('Ice', 25), 'Swallow': ('Normal', 0), 'SeismicToss': ('Fighting', 0), 'ShockWave': ('Electric', 60), 'SunnyDay': ('Fire', 0), 'FocusBlast': ('Fighting', 120), 'PowerTrick': ('Psychic', 0), 'HealOrder': ('Bug', 0), 'PhantomForce': ('Ghost', 90), 'PayDay': ('Normal', 40), 'AromaticMist': ('Fairy', 0), 'NastyPlot': ('Dark', 0), 'Thunderbolt': ('Electric', 90), 'Cut': ('Normal', 50), 'Topsy': ('Dark', 0), 'MagneticFlux': ('Electric', 0), 'PlayNice': ('Normal', 0), 'FuryCutter': ('Bug', 40), 'ChargeBeam': ('Electric', 50), 'CrossPoison': ('Poison', 70), 'SandAttack': ('Ground', 0), 'Kinesis': ('Psychic', 0), 'Roost': ('Flying', 0), 'ExtremeSpeed': ('Normal', 80), 'CircleThrow': ('Fighting', 60), 'Bestow': ('Normal', 0), 'HeartStamp': ('Psychic', 60), 'Bonemerang': ('Ground', 50), 'FollowMe': ('Normal', 0), 'Fly': ('Flying', 90), 'Feint': ('Normal', 30), 'Incinerate': ('Fire', 60), 'Autotomize': ('Steel', 0), 'Payback': ('Dark', 50), 'Foresight': ('Normal', 0), 'DoomDesire': ('Steel', 140), 'MorningSun': ('Normal', 0), 'DragonClaw': ('Dragon', 80), 'Howl': ('Normal', 0), 'PowerSplit': ('Psychic', 0), 'ZapCannon': ('Electric', 120), 'ElectroBall': ('Electric', 0), 'WonderRoom': ('Psychic', 0), 'IronDefense': ('Steel', 0), 'MuddyWater': ('Water', 90), 'Scratch': ('Normal', 40), 'ScaryFace': ('Normal', 0), 'DoubleKick': ('Fighting', 30), 'DestinyBond': ('Ghost', 0), 'Overheat': ('Fire', 130), 'ArmThrust': ('Fighting', 15), 'FairyLock': ('Fairy', 0), 'RockThrow': ('Rock', 50), 'MirrorCoat': ('Psychic', 0), 'SlackOff': ('Normal', 0), 'MudSport': ('Ground', 0), 'Splash': ('Normal', 0), 'CosmicPower': ('Psychic', 0), 'WaterSport': ('Water', 0), 'GuardSwap': ('Psychic', 0), 'LeafTornado': ('Grass', 65), 'Barrier': ('Psychic', 0), 'SweetKiss': ('Fairy', 0), 'Reflect': ('Psychic', 0), 'Disable': ('Normal', 0), 'DragonRage': ('Dragon', 0), 'SmackDown': ('Rock', 50), 'Spikes': ('Ground', 0), 'Rollout': ('Rock', 30), 'HappyHour': ('Normal', 0), 'FireFang': ('Fire', 65), 'DizzyPunch': ('Normal', 70), 'BubbleBeam': ('Water', 65), 'Psystrike': ('Psychic', 100), 'Double': ('Normal', 120), 'Moonlight': ('Fairy', 0), 'Stockpile': ('Normal', 0), 'U': ('Bug', 70), 'Endure': ('Normal', 0), 'Imprison': ('Psychic', 0), 'IronHead': ('Steel', 80), 'HyperBeam': ('Normal', 150), 'OblivionWing': ('Flying', 80), 'Acid': ('Poison', 40), 'StunSpore': ('Grass', 0), 'DazzlingGleam': ('Fairy', 80), 'FurySwipes': ('Normal', 18)}

def get_multiplier(attack, defense):
	"""Get multiplier of two types"""
	attack_num = TYPES.index(attack)
	defense_num = TYPES.index(defense)
	return float(VALUES[attack_num][defense_num])

def attack(move, pokemon):
	"""Determine how effective a move is against a pokemon"""
	try:
		move_type = MOVES[move][0]
		move_power = MOVES[move][1]
	except KeyError:
		print "ERROR: Move not found: %s" % (move)
		return

	try:
		pokemon_types = POKEMON[pokemon]
	except KeyError:
		print "ERROR: Pokemon not found: %s" % (pokemon)
		return
	

	# Get multiplier for type(s)
	value = 1
	for pt in pokemon_types:
		value *= get_multiplier(move_type, pt)

	# Output
	effect = ""
	if move_power == 0 or value == 0:
		effect = "No effect."
	elif value == 0.5:
		effect = "Not very effective."
	elif value == 1:
		effect = "Normal."
	elif value >= 2:
		effect = "It's super effective!"

	# Output
	print "Using %s on %s..." % (move, pokemon)
	print effect

# =================================================== #
# Some Examples

attack("Thunder", "Pikachu")
# Using Thunder on Pikachu...
# Not very effective.
 
attack("Surf", "Onix")
# Using Surf on Onix...
# It's super effective!

attack("Psychic", "Pidgey")
# Using Psychic on Pidgey...
# Normal.

attack("Fissure", "Moltres")
# Using Fissure on Moltres...
# No effect.