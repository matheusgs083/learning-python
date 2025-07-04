import json

FILE_PATH =  "ignorar\person.json"
YEAR = 2025

class Person:

    def __init__(self, name, born_year):
        self.name = name
        self.age = YEAR - born_year
        self.born = born_year

    
    def growup(self):
        self.age += 1


p1 = Person("matheus", 2003)

people = vars(p1)

print(p1.age, p1.name)

p1.growup()

with open(FILE_PATH, 'w') as file:
    json.dump(people, file, ensure_ascii=False, indent=2) #SAVING OBJECT TO A JSON FILE

print(__name__)