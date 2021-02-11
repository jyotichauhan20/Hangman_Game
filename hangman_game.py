import random
import image
name = input("What is your name? ")
print("Good Luck ! ", name)
 
words = ['jyoti', 'chauhan', 'programming', 'coding', 
         'python', 'mohini', 'love', 'electronic'] 
 
word = random.choice(words)
# print(word)
a=len(word)
print("The secret word length is =" ,a)

print("Guess the characters")
guesses = ''
lifeline = 6
 
 
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
        print("Wrong")
        print("You have", + lifeline, 'more guesses')
         
         
        if lifeline== 0:
            print("You Loose")


if guess==0:
    print('''

 
    +---+
    |   |
        |
        |
        |
        |
        =========''')
elif guess==1:
    print('''
    +---+
    |   |
    0   |
        |
        |
        |
        =========''')
elif guesses==2:
    print('''
    +---+
    |   |
    0   |
   /    |
        |
        |
        =========''')
elif guess==3:
    print('''
    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''')
elif guesses==4:
    print('''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''')
elif guess==5:
    print('''
    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''')
elif  guesses==6:
    print('''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''')
elif guess==7:
    print('''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''' )
	

