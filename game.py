# open a file on the server - in our example "words.txt"
# with open("words.txt", "r") as file:
#     wordz = file.read().splitlines()
# print(wordz)

# for version 2.0!!
# select a random word (line) on the server 

# this will come for version 2.0!!
# user choose level of difficulty
# easy 4-6 characters if/then statments
# normal 6-8 characters if/then statements
# hard 8+ characters if/then statments

#select word to get started = pizza for the build out 
word = "pizza"


#show in console the number of letters in computers' word and display 

print(len(word))

#user enter guess - one letter only (uppercase/lowercase) at a time per round
#set input limit to 1 character 
# If more than one character is entered, tell user that input is invalid and to try again
def playgame():
    guess = input("Choose a letter ")
    print(guess)
    #let user know true or false
    if guess in word:
        print("You guessed right!")
    else:
        print("Nope, try again")
        playgame()

playgame()     

#put guesses in list and count
#count correct guesses
#count incorrect guesses

#display correct guesses 

#user is allowed 8 guesses
#remind user of guesses left

#user loses guess if incorrect

#if repeating a letter user will not lose turn
#print a message letting them know they guessed that 
#ask them to try again - not right, try again

#end of game when solved or out of guesses
#display word 

#play again if user says yes