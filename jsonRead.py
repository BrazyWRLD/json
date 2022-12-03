import json

file = open('studenti.json', 'r')
data = json.load(file)

for student in data['Students']:
    print(f"{student['FirstName']} {student['LastName']} {student['Age']}")

#Videjais vecums, variants 1

total_age = 0
count = 0
for student in data['Students']:
    total_age += int(student['Age'])
    count += 1
print(f'Videjais vecums ir {total_age / count}')

#Videjais vecums, variants 2 // Aiznem mazak atminu
total_age = 0
for student in data['Students']:
    total_age += int(student['Age'])
print(f"Videjais vecums ir {total_age / len(data['Students'])}")

#Videjais vecums, variants 3 // Aiznem vairak atminu del saraksta
ages = []
for student in data['Students']:
    ages.append(int(student['Age']))
print(f'Videjais vecums ir {sum(ages) / len (ages)}')

#Pievienot Epastu katram studentam
Email = []
for student in data['Students']:
    student['Email'] = f"{student['FirstName']}.{student['LastName']}@epasts.com"

file_write = open('students.new.json', 'w')
json.dump(data, file_write, indent = 4)