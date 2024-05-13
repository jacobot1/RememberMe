import json
from os.path import dirname
people = []
with open(dirname(__file__)+'\\rm_people.json','w+') as pe:
	json.dump(people,pe,indent=2)
places = []
with open(dirname(__file__)+'\\rm_places.json','w+') as pl:
	json.dump(places,pl,indent=2)
things = []
with open(dirname(__file__)+'\\rm_things.json','w+') as th:
	json.dump(things,th,indent=2)