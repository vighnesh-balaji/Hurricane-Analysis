names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# Convert damages data from string to float and return converted data as a list.

def convert_damages_data(damages):

  conversion = {"M": 1000000, "B": 1000000000}
  updated_damages = []

  for damage in damages:
    if damage == "Damages not recorded":
      updated_damages.append(damage)
    if damage[-1] == 'M':
      updated_damages.append(float(damage.strip('M'))*conversion["M"])
    if damage[-1] == 'B':
      updated_damages.append(float(damage.strip('B'))*conversion["B"])

  return updated_damages

updated_damages = convert_damages_data(damages)
#print(updated_damages)


#Create dictionary of hurricanes with hurricane name as the key and a dictionary of hurricane data as the value.

def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):

  hurricanes = {}
  num_hurricanes = len(names)

  for i in range(num_hurricanes):
    hurricanes[names[i]] = {"Name": names[i],
                          "Month": months[i],
                          "Year": years[i],
                          "Max Sustained Wind": max_sustained_winds[i],
                          "Areas Affected": areas_affected[i],
                          "Damage": updated_damages[i],
                          "Deaths": deaths[i]}
  return hurricanes

hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricanes)

#Convert dictionary with hurricane name as key to a new dictionary with hurricane year as the key and return new dictionary.
# I tried something different from the hurricanes dictionary.

years_dict= []

for n, m, y, ma, a, da,  z in zip(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    dict = {y: {'Name': n, 'Month':m, 'Year': y, 'Max_sustained_wind': ma, 'Area_affected': a, 'Damage': da, 'Deaths': z}}
    years_dict.append(dict)

#print(years_dict)

#Find the count of affected areas across all hurricanes and return as a dictionary with the affected areas as keys.

areas_count={}

for areas in areas_affected:
    for i in areas:
        if i not in areas_count:
            areas_count[i] = 1
        else:
            areas_count[i] += 1

#print(areas_count)

#Find most affected area and the number of hurricanes it was involved in.

def max_areas_affected(areas_count):

    max_area = ''
    max_count = 0

    for area in areas_count:
        if areas_count[area] > max_count:
            max_area = area
            max_count = areas_count[area]
    return max_area, max_count

max_area, max_count = max_areas_affected(areas_count)
#print(max_area, max_count)

#Find the highest mortality hurricane and the number of deaths it caused.

def fatality(hurricanes):

    hurricane_most_deaths=''
    number_of_deaths=0

    for hurricane in hurricanes:
        if hurricanes[hurricane]['Deaths'] > number_of_deaths:
            hurricane_most_deaths = hurricane
            number_of_deaths = hurricanes[hurricane]['Deaths']
    return number_of_deaths, hurricane_most_deaths

most_deaths, number_of_deaths = fatality(hurricanes)
#print(most_deaths, number_of_deaths)

#Categorize hurricanes by mortality rates and return a dictionary.

def mortality(hurricanes):

    mortality_rates = {0:[], 1:[], 2:[], 3:[], 4:[]}

    for hurricane in hurricanes:

        rate = 0
        deaths = hurricanes[hurricane]['Deaths']

        if deaths < 100:
            rate = 0
        elif deaths >= 100 and deaths < 500:
            rate = 1
        elif deaths >= 500 and deaths < 1000:
            rate = 2
        elif deaths >= 1000 and deaths < 10000:
            rate = 3
        else:
            rate = 4

        if rate not in mortality_rates:
            mortality_rates[rate] = hurricanes[hurricane]
        else:
            mortality_rates[rate].append(hurricanes[hurricane])

    return mortality_rates

mortality_rates = mortality(hurricanes)
#print(mortality_rates)

#Find the highest damage inducing hurricane and its total cost.

def max_damage(hurricanes):

    max_damage_hurricane= ''
    max_damage_number= 0

    for hurricane in hurricanes:
        if hurricanes[hurricane]['Damage'] == 'Damages not recorded':
            continue
        if hurricanes[hurricane]['Damage'] > max_damage_number:
            max_damage_hurricane = hurricanes[hurricane]['Name']
            max_damage_number = hurricanes[hurricane]['Damage']
    return max_damage_hurricane, max_damage_number

max_damage_hurricane, max_damage_number = max_damage(hurricanes)
#print(max_damage_hurricane, max_damage_number)

#Categorize hurricanes by damage rates and return a dictionary

def damage_scaled(hurricanes):

    damage_scale = {0: [], 1: [], 2: [], 3: [], 4: []}

    for hurricane in hurricanes:

        rate = 0
        damage = hurricanes[hurricane]['Damage']

        if damage == 'Damages not recorded':
            continue
        elif damage < 100000000:
            rate = 0
        elif damage >= 100000000 and damage < 1000000000:
            rate = 1
        elif damage >= 1000000000 and damage < 10000000000:
            rate = 2
        elif damage >= 10000000000 and damage < 50000000000:
            rate = 3
        else:
            rate = 4

        if rate not in damage_scale:
            damage_scale[rate] = hurricanes[hurricane]
        else:
            damage_scale[rate].append(hurricanes[hurricane])

    return damage_scale

damage_scale = damage_scaled(hurricanes)
#print(damage_scale)
