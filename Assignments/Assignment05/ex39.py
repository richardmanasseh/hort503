# Ex 39: Dictionary Data Structure in Python: Lists with paired values
# A Dictionary (or ”dict”) is a way to store data just like a list, ...
# but instead of using only numbers to get the data, you can use almost anything.
# This lets you treat a dict like it’s a database for storing and organizing data.

# create a mapping of Country to abbreviation
states = {
    'Uganda': 'Ug',
    'Kenya': 'Ke',
    'Tanzania':'Tz',
    'Rwanda': 'Rw',

}

# create a basic set of states and some cities in them
cities = {
    'Ug': 'Kampala',
    'Ke': 'Nairobi',
    'Tz': 'Arusha' ,
    'Rw': 'Kigali'
}

# add some more cities
cities['Ug'] : 'Arua'
cities['Ke'] : 'Mombasa'
cities['Tz'] : 'Mwanza'
cities['Rw'] : 'Gatuna'

# print out some cities
print('-' * 10)
print("Ug has: ", cities['Ug'])
print("Ke has: ", cities['Ke'])

# print some states
print('-' * 10)
print("Uganda's abbreviation is: ", states['Uganda'])
print("Kenya's abbreviation is: ", states['Kenya'])

# do it by using the state then cities dict
print('-' * 10)
print("Rwanda has: ", cities[states['Rwanda']])
print("Tanzania has: ", cities[states['Tanzania']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")


print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
