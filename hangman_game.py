import random
from  image import IMAGES
name = input("What is your name? ")
print("Good Luck ! ", name)
 
words = ['jyoti', 'enviroment', 'programming', 'coding', 
         'python', 'mohini', 'love', 'electronic','science','condition'] 
 
word = random.choice(words)
# print(word)
length=len(word)
print("The secret word length is =" ,length)

print("Guess the characters")
guesses = ''
lifeline = 6
chances=6
 
while lifeline > 0:
    fail = 0
    for char in word:
        if char in guesses: 
            print(char)     
        else: 
            print("_")
            fail= fail+1
    if fail== 0:
        print("You Win") 
        print("The word is: ", word) 
        break
    guess = input("guess a character:")
    guesses += guess 
    if guess not in word:
        lifeline= lifeline-1
        print(IMAGES[chances-lifeline])
        print("Wrong")
        print("You have", + lifeline, 'more guesses')
        if lifeline== 0:
            print("You Loose")


