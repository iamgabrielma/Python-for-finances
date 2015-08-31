import random

def rollDice():
	roll = random.randint(1,100)

	if roll == 100:
		return False
	elif roll <= 50:
		return False
	elif 100 > roll > 50:
		return True

def simple_bettor(funds, initial_wager, wager_count):
	value = funds
	wager = initial_wager
	currentWager = 0

	while currentWager < wager_count:
		if rollDice():
			value += wager
		else:
			value -= wager

		currentWager +=1
	if value < 0:
		value = 'broke'
	print 'Funds:', value
x = 0

while x < 100:
	simple_bettor(1000,100,10000)
	x += 1
