#get the astronauts currently in space through the api
##http://api.open-notify.org/astros.json
#for the astronauts currently in space get the extra info from the astronauts file
#combine and save into a new file

#CSV reference https://realpython.com/python-csv/
#JSON reference https://www.programiz.com/python-programming/json


#1 import the json module
import urllib.request
import json 
import csv

astronauts = []
astronauts_in_space = []

astronaut_combined = []

#2 consume the api
with urllib.request.urlopen("http://api.open-notify.org/astros.json") as url:
    data = json.loads(url.read().decode())
    persons = data.get("people")

    print(persons)

    for person in persons:
        astronauts_in_space.append(person.get('name'))
    
    print(astronauts_in_space)

#3 use csv.reader() to read the astronauts file
with open('astronauts.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        astronauts.append({
            'name': row[0],
            'year': row[1],
            'flights': row[4]
        })

#4 dictionary magic
for astronaut_in_space in astronauts_in_space:
    for astronaut in astronauts:
        if(astronaut.get('name') == astronaut_in_space):
            # print("Have astronaut")
            astronaut_combined.append(astronaut)

#5 save the json in a dictionary

#6 use json.dump to save a new file
with open("astronauts_in_space.json", "w") as write_file:
    json.dump(astronaut_combined, write_file)

