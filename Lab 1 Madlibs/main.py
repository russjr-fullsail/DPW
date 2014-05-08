'''
Russell Chatham Jr.
5/8/14
DPW
Lab 1 Madlibs
'''


#Setting up the dictionary
info = dict()
#variables that get inputted into story
#string 1 vehicles
info['vehicle'] = raw_input('The car you own?')
#string 2 hometown
info['city'] = raw_input('What is your hometown?')
#string 3 dream car
info['dream'] = raw_input('What is your dream car?')
#number of vehicles
info['number'] = input('Enter a number of cars own between 1 and 4')
#Enter random number
info['number2'] = input('Enter a number between 1 and 50')
#dream place to live
info['live'] = input('Enter a number between 1 and 5')
#find monthly cost -float
info['float'] = float(input('cost of vehicle in decimal form (example 3.25)'))

#Conditionals
#limit number of vehicles
if info['number'] >4:
    info['number'] = 4
elif info['number'] <1:
    info['number'] = 1

#limiting random number
if info['number2'] >50:
    info['number'] = 50
elif info['number2'] <1:
    info['number2'] = 1

#limit number for cities to live
if info['live'] >5:
    info['live'] = 5
elif info['live'] <1:
    info['live'] = 1

#Array of vehicles
car_owned = ['Jeep', 'Ford', 'Chevy', 'Dodge', 'BMW', 'Honda', 'Toyota', 'Kia', 'Mercedes']
#append car own name to array
car_owned.insert(0,str(info['vehicle']))
#Push vehicle into loop
array = []

#loop array to add names to group
for i in range(info['number']):
    array.append(str(car_owned[i]))

#vehicle list
vehicle_list = ""

for vehicle in array:
    vehicle_list = vehicle_list + vehicle + ", "

#calculating function
def calc_price():
    decimal - info['float']
    dollar_amount = decimal * 1000000
    return dollar_amount
#initiate function
calc_price = calc_price()

#dream place to live array
lives =['New York City', 'San Fransisco', 'Orlando', 'Las Vegas', 'Nashville']
live = lives[(info['live']-1)]
