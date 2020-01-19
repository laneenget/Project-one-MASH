'''
Lane Enget | ITEC 2905 | 1/16/2020
This program simulates the game of MASH. MASH is a paper and pen game where
you fill in options for certain categories, generate a random number, and
eliminate choices until only one option for each category remains. Your life
is predicted with these options.
'''

import random

def main():
    try:
        print('Welcome to the game of MASH!')
        spouses, careers, cities, kids = inputs()
        house, spouse, career, city, kid = processing(spouses, careers, cities, kids)
        outputs(house, spouse, career, city, kid)
    except Exception as err:
        print(err)

def inputs():
    str = 'spouses'
    spouses = input_checker(str)
    str = 'careers'
    careers = input_checker(str)
    str = 'cities'
    cities = input_checker(str)
    str = 'numbers'
    kids = input_checker(str)

    return spouses, careers, cities, kids

#Function to make sure user input exists
def input_checker(str):
    print(f'Enter four {str}: ')
    f_list = []
    n = 4
    for i in range(0, n):
        inp = input()
        if str == 'numbers':
            while inp.isnumeric() is False or int(inp) < 0: #Check that user input is a number
                inp = input('Please enter a whole number: ')
        else:
            while inp == '': #Check user input exists
                inp = input('Please do not leave this blank: ')
        f_list.append(inp) #Add input to list

    return f_list

def processing(spouses, careers, cities, kids):
    houses = ['mansion', 'apartment', 'shack', 'house'] #Create houses list
    
    #Generate a random number for each category and pick the appropriate index value in each list
    n = random.randint(0, len(houses) - 1)
    house = houses[n] #Instantiate randomized house
    n = random.randint(0, len(spouses) - 1)
    spouse = spouses[n] #Instantiate randomized spouse
    n = random.randint(0, len(careers) - 1)
    career = careers[n] #Instantiate randomized career
    n = random.randint(0, len(cities) - 1)
    city = cities[n] #Instantiate randomized city
    n = random.randint(0, len(kids) - 1)
    number = kids[n] #Instantiate random number of kids

    return house, spouse, career, city, number

#Print output in a readable way    
def outputs(house, spouse, career, city, number):
    print('MASH is a predictor of your future life. Based on your entries, here is what you can expect: ')
    print('You will live in a ' + house + ' in ' + city + '.')
    print('You will marry ' + spouse + '.')
    print('Together, you will have ' + str(number) + ' kid(s).')
    print('You will make your living as a ' + career + '.')
    print('You will live a happy life.')

main()