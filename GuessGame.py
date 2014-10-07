# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
number = -1
remaining_guesses=7
num_range = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global number
    global remaining_guesses
    number = random.randrange(1,num_range+1)
    if num_range==100:
        print "New game. Range is from 0 to 100"
        print "Number of remaining guesses is 7"
        remaining_guesses = 7
    else:
        print "New game. Range is from 0 to 1000"
        print "Number of remaining guesses is 10"
        remaining_guesses = 10
   

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    print "Guess was ",guess
    global number
    global remaining_guesses
    print "Number of remianing guesses is", remaining_guesses
    if int(guess) == number:
        print "Correct!"
        new_game()
    elif int(guess) < number:
        print "Higher!"
    elif int(guess) > number:
        print "Lower!"
    remaining_guesses = remaining_guesses - 1
    if remaining_guesses==0:
        print "You ran out of guesses. The number was ",number
        new_game()


    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)
frame.add_button("Range is (0,100]", range100,200 )
frame.add_button("Range is (0, 1000]",range1000, 200 )
frame.add_input("Enter a guess", input_guess, 200)

# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric