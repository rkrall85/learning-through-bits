

# ex39: doing things to Lists

#a key in a dic is unquie

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}


# create a basic set of states and some cities in them
cities = {
    'CA': 'San Fransisco',
    'MI': 'Detriot',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
#cities['NY'] = 'Bronx' #update city in Ny to be bronx



# print out some cities
print('-' * 10)
print("NY State has ", cities['NY'])
print("OR State has ", cities['OR']) #prints out the last entry per state


# do it by using the state than cities dict
print('-' *10)
print("Michigan has: ", cities[states['Michigan']]) #print out the last entry per state
print("Florida as :", cities[states['Florida']])


# print every state abbreviation
print('-' *10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

#print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

# safetly get a abbreviation by state that might not be there
print('-' * 10)
state = states.get('Texas', None)

if not state:
    print("Sorry, no Texas")

# get a city wtih default value
city = cities.get("TX", 'Does Not Exist')
print("The city for state 'TX' is %s" % city)



'''
print('-' * 10 )
for abbrev, city in states.items():
    print("%s state is abbreviated %s adn has city %s" %(
        state, abbrev, cities[abbrev]
    ))
'''
