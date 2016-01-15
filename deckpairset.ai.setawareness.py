#/usr/bin/env python

from glob import glob
from time import sleep
from pdb import set_trace as trace
import json

corpandrunnerlist = []
def mainmenu():
	#download all of your decks from cardgamedb and put them in the "allofthedecks" folder
	corps = set(json.loads(open('corpID.json').read()))
	runners = json.loads(open('runnerID.json').read())

	mydatapacks = {'Core' :'owned','True Colors':'owned','Promos':'nope','Alternates':'nope','Special':'nope','Genesis':'nope','What Lies Ahead':'nope','Trace Amount':'owned','Cyber Exodus':'owned','A Study in Static':'nope',"Humanity's Shadow":'Owned','Future Proof':'owned','Creation and Control':'owned','Spin':'nope','Opening Moves':'owned','Second Thoughts':'owned','Mala Tempora':'owned','Fear and Loathing':'nope','Double Time':'owned','Honor and Profit' : 'owned' , 'Lunar':'nope' , 'Upstalk':'nope' , 'The Spaces Between' :'nope','First Contact':'nope','Up and Over':'nope','All That Remains':'owned','The Source':'owned','Order and Chaos':'owned','SanSan ':'nope','The Valley':'nope','Breaker Bay':'owned','Chrome City':'nope','The Underway':'nope','Old Hollywood':'owned','The Universe of Tomorrow':'owned','Data and Destiny':'nope','Kala Ghoda':'nope','Business First':'nope','Democracy and Dogma':'nope','Salsette Island':'nope','The Liberated Mind':'nope','Fear the Masses':'nope'}
	alldecks = {}
	#trace()
	deckfiles = glob("allofthedecks/*")
	for decktxt in deckfiles:
	# the data structure is a dict of decks of cards that have the properties 'name' and 'set'
		detective = open(decktxt).read().split('\n')
		shuffleable = []
		for each in detective:		
			#print each
			shuffleable.append([each.split(' (')[0],each.split('(')[1].split(')')[0],int(each.split(') x')[-1].rstrip())])
			#print shuffleable[-1][1]
			#sleep(.25)
			if mydatapacks[shuffleable[-1][1]] == "owned":
				if shuffleable[-1][0] in corps:
					print "\n"
				else:
					shuffleable.pop()
		#sleep(2)
		alldecks[decktxt.split("/")[1].split(".txt")[0]] = shuffleable

	#trace()
	#exscise cards from sets already possessed 
	mypacks = []
	for each in mydatapacks:
		if mydatapacks[each] == "owned":
			mypacks.append(each)
	print "assuming you have " + str(mypacks) + " data packs\n"
	for deck in alldecks:
		for card in alldecks[deck]:
			if mydatapacks[card[1]] == 'owned':
				del card


	setdecks = {}
	for deck in alldecks.keys():
		setlist = []	
		for card in alldecks[deck]:
			setlist.append(card[1])
		setlist = set(setlist)
		setdecks[deck] = setlist


	#divide the decks into corps and runners.  Pull all the corps out of allthedecks, and what is left is runners!
	corpdecks = {}
	runnerdecks = {}
	for deck in alldecks:
		for card in alldecks[deck]:
			if card[0] in corps:
				corpdecks[deck] = alldecks[deck]

	for keys in corpdecks.keys():
		alldecks.pop(keys,)
	runnerdecks = alldecks
	#iterate through all the corp and runner combinations
	corpandrunner = {}
	for runner in runnerdecks:
		for corp in corpdecks:
			corpandrunner[corp + "+" + runner] = []
			for card in runnerdecks[runner]:
				corpandrunner[corp + "+" + runner].append(card[1])
			for card in corpdecks[corp]:
				corpandrunner[corp + "+" + runner].append(card[1])
			#print corpandrunner.keys()
			#sleep(.25)
			corpandrunner[corp + "+" + runner] = list(set(corpandrunner[corp + "+" + runner]))
	count = 0
	ezbuilds = []

	while len(ezbuilds) < 15: 
		for each in corpandrunner:
			if len(corpandrunner[each]) < count:
				ezbuilds.append(each + " needs " + str(len(corpandrunner[each])) + " sets to build")
				corpandrunnerlist.append(corpandrunner[each])
		count += 1
	count = 0
	for sentence in ezbuilds:
		print str(count) + ". " + sentence
		count += 1
#select deck pairing, and review set +data packs required
	while 1 is 1:
		review = ''
		review = input("which build?:") 
		if review == '':
			mainmenu()
	#add number of cards in each set
		for setpresence in corpandrunnerlist[review]:
			presencevalue = 0
			for card in corpdecks[ezbuilds[review].split('+')[0]]:
				if card[1] == setpresence:
					presencevalue += card[2]
			for card in runnerdecks[ezbuilds[review].split('+')[1].split(' needs ')[0]]:
				if card[1] == setpresence:
					presencevalue += card[2]
			print setpresence + ": " + str(presencevalue) + " cards"
			sleep(.25)
		print "to build " + ezbuilds[review]
		print "+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n\n"
trace()
mainmenu()
