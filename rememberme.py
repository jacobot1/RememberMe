import json
with open('rm_people.json','r+') as pe:
	people = json.load(pe)
with open('rm_places.json','r+') as pl:
	places = json.load(pl)
with open('rm_things.json','r+') as th:
	things = json.load(th)
pe_pr = False
pl_pr = False
th_pr = False
print('Welcome to RememberMe')
x = input('Search or type a command: ').lower()
while True:
# Commands
	if x == '!exit':
		with open('rm_people.json','w') as pe:
			people = json.dump(people,pe,indent=2)
		with open('rm_places.json','w') as pl:
			places = json.dump(places,pl,indent=2)
		with open('rm_things.json','w') as th:
			things = json.dump(things,th,indent=2)
		exit()
	if x == '!new':
		name = input('Type something to remember: ')
		type = input('Person (1), Place (2), or Thing (3)? ')
		if type == '1':
			people.append(name)
		if type == '2':
			places.append(name)
		if type == '3':
			things.append(name)
	if x == '!del':
		choice = input('Select a list to delete from (people (1), places (2), or things (3)): ')
		if choice == 1:
			print('PEOPLE')
			for i in range(len(people)):
				print(i+1,people[i])
			item = input('Choose an item to delete: ')
			del people[int(item) - 1]
		if choice == 2:
			print('PLACES')
			for i in range(len(places)):
				print(i+1,places[i])
			item = input('Choose an item to delete: ')
			del places[int(item) - 1]
		if choice == 3:
			print('THINGS')
			for i in range(len(things)):
				print(i+1,things[i])
			item = input('Choose an item to delete: ')
			del things[int(item) - 1]
	if x == '!browse':
		print('PEOPLE')
		for i in range(len(people)):
			print(people[i])
		print('\nPLACES')
		for i in range(len(places)):
			print(places[i])
		print('\nTHINGS')
		for i in range(len(things)):
			print(things[i])
# Search
	found = False
	for i in range(len(people)):
		if x in people[i].lower():
			found = True
			if pe_pr == False:
				print('PEOPLE')
				pe_pr = True
			print(people[i])
	pe_pr = False
	for i in range(len(places)):
		if x in places[i].lower():
			found = True
			if pl_pr == False:
				print('\nPLACES')
				pl_pr = True
			print(places[i])
	pl_pr = False
	for i in range(len(things)):
		if x in things[i].lower():
			found = True
			if th_pr == False:
				print('\nTHINGS')
				th_pr = True
			print(things[i])
	th_pr = False
	if found == False and x != '!new' and x != '!exit' and x != '!del' and x != '!browse':
		print('Not Found')
	x = input('Search or type a command: ').lower()
