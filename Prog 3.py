# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 22:28:46 2021

@author: Prince
"""

# CIS 443-01 - Analytics Programming
## Program 3
# __Grading ID__: P8330 <br>
#__Due__: Thursday, November 11 (by 11:59 PM)<br />
#__Worth__: 75 pts.<br />


#Create dictionary for the data

team_data = {}

#declare index of dictionary

i=1

count=1

#use for loop to repeat input for 6 times

for i in range(1,6):

    #prompt for the jersy number and rating

    jersey_num = int(input('Enter player {}\'s jersey number:\n' .format(i)))

    rating = int(input('Enter player {}\'s rating:\n' .format(i)))

    print()

    #check for the validation of inputs

    if jersey_num < 0 and jersey_num > 99 and rating < 0 and rating > 9:

        print('invalid entry')

        break

    else:

        team_data [jersey_num] = rating

#print the output

print("ROSTER")

for jersey_num,rating in sorted(team_data.items()):

    print("Jersey number: %d, Rating: %d" % (jersey_num,rating))

#Declare menu option for input

option=''

#looping until user quits, 

while option.upper()!='Q':

    print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\n'

          'r - Output players above a rating\no - Output roster\nq - Quit\n')

    #prompt for the option

    option = input('Choose an option:\n')


    if option == 'a':

        #prompt for jersy number and rating

        
        jersey_num = int(input('Enter a new player\'s jersey number:\n' .format(i)))

        rating = int(input('Enter the players\'s rating:\n'.format(i)))
        
        #add the items in the dictinary

        team_data[jersey_num] = rating

    #if option is d

    elif option == 'd':

        #prompt for jersy number

        jersey_num = int(input('Enter a jersey number:\n'))

        if jersey_num in team_data.keys():

            #remove the item in the dictionary

            del team_data[jersey_num]

    #if option is u

    elif option == 'u':

        #prompt for the jersy number

        jersey_number = int(input('Enter a jersey number:\n'))

        if jersey_number in team_data.keys():

            #prompt for the rating of the player

            rating = int(input('Enter a new rating for player:\n'))

            #update the rating

            team_data [jersey_num] = rating

    #If option is r

    elif option == 'r':

        #prompt rating

        rating_input=int(input('Enter a rating:\n'))

        print('ABOVE {}'.format(rating_input))

        #printing all players with rating above given rating

        for jersey_number,rating in sorted(team_data.items()):

            if rating > rating_input:

                print("Jersey number: %d, Rating: %d" % (jersey_number,rating))

    #if option is o

    elif option == 'o':

        print("ROSTER")

        #print the jersy numbers along with rating

        for jersey_num,rating in sorted(team_data.items()):

            print("Jersey number: %d, Rating: %d" % (jersey_num,rating))
            
            