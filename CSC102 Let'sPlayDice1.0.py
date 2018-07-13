##################################################################################################################
#In this assignment you will write a  Python program that is the first in a 2 part series.                       #
#This program will roll 2 dice by default. The program will then do some mathematical operations on the results, #
#including multiplication, division, addition, subtraction, and average of the dice.                             #
#The program will output the results using formatted output.                                                     #
#                                                                                                                #
#User interaction with the program should look like this:                                                        #
#                                                                                                                #
#Program generates two random dice values between 1 and 6 (one value for each dice).                             #
#See below for instructions on how to generate a random number.                                                  #
#Program displays the values of both dice.                                                                       #
#Program displays the values of multiplication, division, addition, subtraction,                                 #
#and average of the dice in a nicely formatted display.                                                          #
#Be sure to use comments for both structure of the program and documentation of the code.                        #
##################################################################################################################

import random                                                                   # Import the random module
import string
def displayDice(dice):                                                         # This will return a picture of a dice
    if dice == 1:
        dice ="""*-------*"
|       |
|   *   |
|       |
*-------*"""
    elif dice == 2:
        dice ="""*-------*
| *     |
|       |
|     * |
*-------*"""
    elif dice == 3:
        dice ="""*-------*
| *     |
|   *   |
|     * |
*-------*"""
    elif dice == 4:
        dice ="""*-------*
| *   * |
|       |
| *   * |
*-------*"""
    elif dice == 5:
        dice ="""*-------*
| *   * |
|   *   |
| *   * |
*-------*"""
    elif dice == 6:
        dice ="""*-------*
| *   * |
| *   * |
| *   * |
*-------*"""
        
    return(dice)
    
playAgain = input('Would you like to play dice?')                               # Assign 'yes' to the variable playAgain

while(playAgain.casefold().startswith('y')):                                    # Create while loop that continues as long as 
                                                                                # the first letter to the input questions is 'y'

    dice1 = random.randint(1,6)                                                 # Create a variable to store the first random number
    dice2 = random.randint(1,6)                                                 # Create a variable to store the second random number

    print((dice1),(dice2))                                                      # print both of the random numbers
    print(displayDice(dice1),'\n', displayDice(dice2), sep='')

    print('Addition','\t','{:,.1f}'.format(dice1 + dice2))                      # Add both of the numbers together and format them for 1 decimal place
    print('Subtraction','\t','{:,.1f}'.format(dice1 - dice2))                   # Subtract both of the numbers from eachother and format them for 1 decimal place
    print('Multiplication','\t','{:,.1f}'.format(dice1 * dice2))                # Multiply both of the numbers and format them for 1 decimal place
    print('Division','\t','{:,.1f}'.format(dice1 / dice2))                      # Divide both of the numbers and format them for 1 decimal place
    print('Average','\t', '{:,.1f}'.format((dice1 + dice2) / 2))                # Average both of the numbers and format them for 1 decimal place

    playAgain = input('Would you like to play again? \n')                       # Ask user if they would like to keep playing and assign the answer to the playagain variable

    print('Thank you for playing!')                                             # If user answers with anything other than something that starts with
                                                                                # 'y' Thank them from playing and end the program

############ Need to include total of all dice rolls ################
