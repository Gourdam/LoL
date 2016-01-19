from sys import exit
import random
# resources [health, gold]
resources = [500, 0]
# potions = 2
# turn[turn, blue_buff, gromp, wolves, red_buff, golems, raptors, top, mid, bot]
turn = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def start (resources, turn):
	"""Start of the game with instructions."""
	print ("Welcome to Summoners Rift! You are your teams jungler on the blue side." 
	+ " Your objective is to gain 500 gold and this can be achieved through jungling/ganking." 
	+ " If you are low on health, you can always recall to restore your health."
	+ " Good luck and have fun!.")
	beginning (resources, turn)
	
def beginning (resources, turn):
	"""Beginning of the game."""
	print "You have %d health, %d gold, and are on turn %d." % (resources[0], resources[1], turn[0]) 
	print "What do you do?"
	print "(1) Jungle."
	print "(2) Gank."
	print "(3) Recall."
	while True:
		decision = raw_input("> ")
		if decision == "1":
			jungle(resources, turn)
		elif decision == "2":
			gank(resources, turn)
		elif decision == "3":
			recall(resources, turn)
		else:
			print "Bruh, try again."
			
def success(resources, turn, health, gold, message):
	"""Sucesss scenario."""
	if resources[1] >= 500:
		print "You have won the game in %d turns. GG!" % turn[0]
		exit(0)
	else:
		print message
		print "You lost %d health and gained %d gold." % (health, gold)
		for i in range(1,10):
			if turn[i] > 0:
				turn[i] -= 1
		beginning (resources, turn)
	
def death (resources, turn, message):
	"""Death scenario where gank/jungle kills player."""
	print message
	print "You had %d gold and were on turn %d when you died. GG." % (resources[1], turn[0])
	exit(0)
				
def jungle (resources, turn):
	"""Jungle function start."""
	print "You have %d health, %d gold, and are on turn %d." % (resources[0], resources[1], turn[0])
	print "Which quadrant do you jungle in?"
	print "(1) West Quadrant."
	print "(2) South Quadrant."
	print "(3) Go back."
	while True:	
		decision = raw_input("> ")
		if decision == "1":
			west(resources, turn)
		elif decision == "2":
			south(resources, turn)
		elif decision == "3":
			beginning(resources, turn)
		else:
			print "Bruh, try again."

def west (resources, turn):
	"""West jungle function."""
	print "You have %d health, %d gold, and are on turn %d." % (resources[0], resources[1], turn[0])
	print "What camp do you kill?"
	print "(1) Blue buff."
	print "(2) Gromp."
	print "(3) Wolves."
	print "(4) Go back."
	while True:
		decision = raw_input("> ")
		if decision == "1":
			blue_buff(resources, turn)
		elif decision == "2":
			gromp(resources, turn)
		elif decision == "3":
			wolves(resources, turn)
		elif decision  == "4":
			jungle (resources, turn)
		else:
			print "Bruh, try again."
			
def south (resources, turn):
	"""South jungle function."""
	print "You have %d health, %d gold, and are on turn %d." % (resources[0], resources[1], turn[0])
	print "What camp do you kill?"
	print "(1) Red buff."
	print "(2) Golems."
	print "(3) Raptors."
	print "(4) Go back."
	while True:
		decision = raw_input("> ")
		if decision == "1":
			red_buff(resources, turn)
		elif decision == "2":
			golems(resources, turn)
		elif decision == "3":
			raptors(resources, turn)
		elif decision == "4":
			jungle(resources, turn)
		else:
			print "Bruh, try again."
			
def blue_buff (resources, turn):
	"""West jungle camps: blue buff camp: 100 health, 50 gold, 5 turn cd, resource[1]."""
	health = 100
	gold = 50
	cd = 5
	location = 1
	if turn [location] > 0:
		print "You have to wait %d more turns." % turn [location]
		jungle(resources, turn)
	else:
		if resources[0] <= health:
			death(resources, turn, "You died to the might of the blue golem.")
		else:
			resources[0] -= health
			resources[1] += gold
			turn[location] += cd + 1
			turn[0] += 1
			success(resources, turn, health, gold, "You have killed blue buff.")

def gromp (resources, turn):
	"""West jungle camps: gromp camp: 75 health, 35 gold, 3 turn cd, resource[2]."""
	health = 75
	gold = 35
	cd = 3
	location = 2
	if turn [location] > 0:
		print "You have to wait %d more turns." % turn [location]
		jungle(resources, turn)
	else:
		if resources[0] <= health:
			death(resources, turn, "Gromp made you croak.")
		else:
			resources[0] -= health
			resources[1] += gold
			turn[location] += cd + 1
			turn[0] += 1
			success(resources, turn, health, gold, "Gromp has nothing on you.")
 
def wolves (resources, turn):
	"""West jungle camps: wolves camp: 50 health, 25 gold, 3 turn cd, resource[3]."""
	health = 50
	gold = 25
	cd = 3
	location = 3
	if turn [location] > 0:
		print "You have to wait %d more turns." % turn [location]
		jungle(resources, turn)
	else:
		if resources[0] <= health:
			death(resources, turn, "You were boned by the wolves.")
		else:
			resources[0] -= health
			resources[1] += gold
			turn[location] += cd + 1
			turn[0] += 1
			success(resources, turn, health, gold, "You are the alpha wolf now.")
 
def red_buff (resources, turn):
	"""South jungle camps: red buff camp: 120 health, 75 gold, 5 turn cd, resource[4]."""
	health = 120
	gold = 75
	cd = 5
	location = 4
	if turn [location] > 0:
		print "You have to wait %d more turns." % turn [location]
		jungle(resources, turn)
	else:
		if resources[0] <= health:
			death(resources, turn, "You're seeing red now.")
		else:
			resources[0] -= health
			resources[1] += gold
			turn[location] += cd + 1
			turn[0] += 1
			success(resources, turn, health, gold, "You were redy for red buff.")

def golems (resources, turn):
	"""South jungle camps: golems camp: 65 health, 30 gold, 3 turn cd, resource[5]."""
	health = 65
	gold = 30
	cd = 3
	location = 5
	if turn [location] > 0:
		print "You have to wait %d more turns." % turn [location]
		jungle(resources, turn)
	else:
		if resources[0] <= health:
			death(resources, turn, "GOLEMS SMASH.")
		else:
			resources[0] -= health
			resources[1] += gold
			turn[location] += cd + 1
			turn[0] += 1
			success(resources, turn, health, gold, "The golems were turned into rubble.")

def raptors (resources, turn):
	"""South jungle camps: raptors camp: 60 health, 25 gold, 3 turn cd, resources[6]."""
	health = 60
	gold = 25
	cd = 3
	location = 6
	if turn [location] > 0:
		print "You have to wait %d more turns." % turn [location]
		jungle(resources, turn)
	else:
		if resources[0] <= health:
			death(resources, turn, "Clever girls...")
		else:
			resources[0] -= health
			resources[1] += gold
			turn[location] += cd + 1
			turn[0] += 1
			success(resources, turn, health, gold, "The raptors are history.")
			
def gank (resources, turn):
	"""Gank function start."""
	print "You have %d health, %d gold, and are on turn %d." % (resources[0], resources[1], turn[0])
	print "What lane do you try to gank?"
	print "(1) Top."
	print "(2) Mid."
	print "(3) Bot."
	print "(4) Go back."
	while True:
		decision = raw_input("> ")
		if decision == "1":
			top(resources, turn)
		elif decision == "2":
			mid(resources, turn)
		elif decision == "3":
			bot(resources, turn)
		elif decision == "4":
			beginning(resources, turn)
		else:
			print "Bruh, try again."
			
def top (resources, turn):
	"""Top gank: success: 75%, 50 health, 100 gold. failure: 25%, 75 health, 0 gold."""
	health_success = 50
	health_failure = 75
	gold_success = 100
	gold_failure = 0
	cd = 3
	location = 7
	probability = 0.75
	if turn [location] > 0:
		print "You have to wait %d more turns." % turn [location]
		gank(resources, turn)
	else:
		chance = random.random()
		if chance >= 1 - probability:
			if resources[0] <= health_success:
				death(resources, turn, "You died at the top of your career.")
			else:
				resources[0] -= health_success
				resources[1] += gold_success
				turn[location] += cd + 1
				turn[0] += 1
				success(resources, turn, health_success, gold_success, "You're at the top of your game. "
				+"You killed the top laner.")
		else:
			if resources[0] <= health_failure:
				death(resources, turn, "You died at the top of your career")
			else:
				resources[0] -= health_failure
				turn[location] += cd + 1
				turn[0] += 1
				success(resources, turn, health_failure, gold_failure, "Your top gank was unsuccessful.")

def mid (resources, turn):
	"""Mid gank: success: 60%, 75 health, 100 gold. failure: 40%, 125 health, 0 gold."""
	health_success = 75
	health_failure = 125
	gold_success = 100
	gold_failure = 0
	cd = 3
	location = 8
	probability = 0.60
	if turn [location] > 0:
		print "You have to wait %d more turns." % turn [location]
		gank(resources, turn)
	else:
		chance = random.random()
		if chance >= 1 - probability:
			if resources[0] <= health_success:
				death(resources, turn, "Mid lane was your bane of existence.")
			else:
				resources[0] -= health_success
				resources[1] += gold_success
				turn[location] += cd + 1
				turn[0] += 1
				success(resources, turn, health_success, gold_success, "Gankeroni succesful "
				+"You killed the mid laner.")
		else:
			if resources[0] <= health_failure:
				death(resources, turn, "Mid lane was your bane of existence.")
			else:
				resources[0] -= health_failure
				turn[location] += cd + 1
				turn[0] += 1
				success(resources, turn, health_failure, gold_failure, "Your mid gank was unsuccessful.")
				
def bot (resources, turn):
	"""Bot gank: success: 30%, 150 health, 200 gold. failure: 50%, 200 health, 0 gold."""
	health_success = 150
	health_failure = 200
	gold_success = 200
	gold_failure = 0
	cd = 3
	location = 9
	probability = 0.30
	if turn [location] > 0:
		print "You have to wait %d more turns." % turn [location]
		gank(resources, turn)
	else:
		chance = random.random()
		if chance >= 1 - probability:
			if resources[0] <= health_success:
				death(resources, turn, "You died and hit rock bottom.")
			else:
				resources[0] -= health_success
				resources[1] += gold_success
				turn[location] += cd + 1
				turn[0] += 1
				success(resources, turn, health_success, gold_success, "Two for one special! "
				+"You killed the bottom lane duo.")
		else:
			if resources[0] <= health_failure:
				death(resources, turn, "You died and hit rock bottom.")
			else:
				resources[0] -= health_failure
				turn[location] += cd + 1
				turn[0] += 1
				success(resources, turn, health_failure, gold_failure, "Your bot gank was unsuccessful.")
				
def recall (resources, turn):
	"""Recall function: Restore all health and use 1 turn."""
	resources[0] = 500
	turn[0] += 1
	print "You have backed and restored all you health costing you a turn."
	for i in range(1,10):
			if turn[i] > 0:
				turn[i] -= 1
	beginning (resources, turn)

# start the function game.
start(resources, turn)
			
	