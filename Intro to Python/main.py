#one lined comments
'''
Doc strings
'''

first_name = "Kermit"
last_name = "De Frog"

#response = raw_input("Enter your Name  ")
#print "Hello there,", response

birth_year = 1974
current_year = 2014
age = current_year - birth_year
#print "You are " + str(age) + " years old"

budget = 90

if budget > 100:
    brand = "nike"
    print "Yay! we can buy cool " + brand + " shoes!"
elif budget > 50:
    #print "We can at least get some generic sneakers."
    pass
else:
    pass

characters = ["leia","luke","chewy","lando"]
characters.append("obi won")
#print characters[0]

movies = dict() #create dictionary object
movies = {"Star Wars":"Darth Vader", "Silence of the Lambs":"Hannibal Lecter"}
#print movies["Star Wars"]

