#/usr/bin/env python

from glob import glob
from time import sleep
import json
from pdb import set_trace

from os import system
system('clear')
#download all of your decks from cardgamedb and put them in the "allofthedecks" folder
corps = set(json.loads(open('corpID.json').read()))
runners = json.loads(open('runnerID.json').read())
set_trace()

alldecks = {}
deckfiles = glob("allofthedecks/*")
for decktxt in deckfiles:
# the data structure is a dict of decks of cards that have the properties 'name' and 'set'
	detective = open(decktxt).read().split('\n')
	shuffleable = []
	for each in detective:		
		#print each
		shuffleable.append([each.split(' (')[0],each.split('(')[1].split(')')[0],each[-2]])
		#print shuffleable[-1]
		#sleep(1)
	alldecks[decktxt.split("/")[1].split(".txt")[0]] = shuffleable

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
set_trace()
#iterate through all the corp and runner combinations
corpandrunner = {}
for runner in runnerdecks:
	for corp in corpdecks:
		corpandrunner[corp + "+" + runner] = []
		for card in runnerdecks[runner]:
			corpandrunner[corp + "+" + runner].append(card[1])
		for card in corpdecks[corp]:
			corpandrunner[corp + "+" + runner].append(card[1])
		corpandrunner[corp + "+" + runner] = list(set(corpandrunner[corp + "+" + runner]))

count = 0
ezbuilds = []
corpandrunnerlist = []
while len(ezbuilds) < 4: 
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
	review = input("which build?:") 
	for printset in corpandrunnerlist[review]:
		print printset
		sleep(.25)
	print "to build " + ezbuilds[review]
