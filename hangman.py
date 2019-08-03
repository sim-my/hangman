#hangman implementation in python 3

import random

#random list of the word
words = ["secret","various","water","life","death"]

#this selects the random word from the given word list
given = random.choice(words)

print('*'*50)
print('WELCOME TO HANGMAN')
print('*'*50)
print('RULES:')
print('Guess the letter of the word')
print('You can make wrong guess for 8 times')
print('IF... guess is correct, CONGRATULATION, YOU WIN')
print('ELSE..., Sorry, YOU LOSE')
print('*'*50)

#initialize the number of turns for the guess
turns = 8

#creating the output for the hangman after each guess
output = []
output.extend(given)
for i in range(0,len(given)):
    output[i] = "*"
print('Word: '," ".join(output))

#loop till the number of turns end
while turns != 0:
    #enter the guess each time till the turn is given
    guess = input("Enter your guess: ") 

#check if the guess is correct
#if the guess is correct turn couter doesn't decremented
#if the guess is wrong the turn counter is decremented

    if guess in given:
        print('Well done captain!!, It\'s a correct guess.')
        print('You\'ve',turns,'turns remaining, now!!')
    else:
        print('Wrong guess this time!!')
        turns = turns - 1
        print('Don\'t worry still,you\'ve got', turns, 'turns left.')
            
#check if guess is correct display the right guessed letter        
    for j in range(0,len(given)):
        if guess == given[j]:
            output[j] = guess
 
        
    print('Word: ',' '.join(output))
    print('*'*50)

  #if you guess the word before the turn ends, you can get out of the loop 

    if output == list(given):
        break
              
 #print the result of the game
   
if output == list(given):
    print('CONGRATULATION, YOU WIN!!!')
else:
    print('SORRY YOU LOSE, BETTER LUCK NEXT TIME!!!')

print('Given word is:\n',given.upper())
             


                                                                                                                                                                                                                                                                                                                                                                                           
