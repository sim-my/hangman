#hangman implementation in python 3

import random

words = ["secret","various","water","life","death"]

given = random.choice(words)

print('*'*50)
print('WELCOME TO HANGMAN')
print('*'*50)
print('RULES:')
print('Guess the letter of the word for 8 times.')
print('You gotta make correct guess of word in 8 times')
print('IF... guess is correct, CONGRATULATION, YOU WIN')
print('ELSE..., Sorry, YOU LOSE')
print('*'*50)

#initialize the number of the guess
turns = 8

#start the loop till the guess count ends
output = []
output.extend(given)
for i in range(0,len(given)):
    output[i] = "*"
print('Word: '," ".join(output))
while turns != 0:
    guess = input("Enter your guess: ") 
        
    if guess in given:
        print('Well done captain!!, It\'s a correct guess.')
        print('You\'ve',turns,'turns remaining, now!!')
    else:
        print('Wrong guess this time!!')
        turns = turns - 1
        print('Don\'t worry still,you\'ve got', turns, 'turns left.')
            
        
    for j in range(0,len(given)):
        if guess == given[j]:
            output[j] = guess
 
        
    print('Word: ',' '.join(output))
    print('*'*50)
        
    if output == list(given):
        break
              

if output == list(given):
    print('CONGRATULATION, YOU WIN!!!')
else:
    print('SORRY YOU LOSE, BETTER LUCK NEXT TIME!!!')

print('Given word is:\n',given.upper())
             


                                                                                                                                                                                                                                                                                                                                                                                           
