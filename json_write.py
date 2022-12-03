personal_data = [
    {
        'name': 'Anna', 
        'age': 18, 
        'email': 'anna@somemail.com', 
        'school': 'Dobeles VĢ',        
        'car': {
            'brand': 'Tesla',
            'year': 2022,
            'color': 'Red',
            'engine': 50        
        }
    },
    {
        'name': 'Oskars', 
        'age': 20,
        'email': 'oskars@somemail.com',
        'school': 'Siguldas VĢ',
        'car': {
            'brand': 'Audi',
            'year': 2020,
            'color': 'Black',
            'engine': 2.0        
        }
    },
    {
        'name': 'Jenifer', 
        'age': 17,
        'email': 'jenifer@somemail.com',
        'school': 'Talmācības',
        'car': {
            'brand': 'Toyota',
            'year': 2021,
            'color': 'Silver',
            'engine': 1.5        
        }
    }
]

import json
file = open('persons.json', 'w')
json.dump(personal_data, file, indent = 4)
