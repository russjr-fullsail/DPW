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
info['vehicle'] = raw_input('Favorite Vehicle?')
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
if info['number'] > 4:
    info['number'] = 4