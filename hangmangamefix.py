import random

print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    """)

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

print("Welcome to Hangman!")
print("the rules are simple:")
print("1. You have to guess the word one letter at a time.")
print("2. You have 6 wrong guesses before you lose.")
print("3. Good luck!")
print("Let's start!")
print("type 'exit' to quit the game at any time.")

ranworld = random.choice(words)
guessed_letters = set()
wrong = 0

while True:
    # get input from the user
    guess = input("Guess a letter: ").lower()
    # check if the user already guessed the letter
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    # check if the user wants to exit
    if guess == 'exit':
        print("Thanks for playing!")
        break
    # check if the user has lost
    if wrong >= len(HANGMANPICS) - 1:
        print("Sorry, you've run out of tries. The word was:", ranworld)
        break
    # right  or wrong guess
    if guess in ranworld:
        guessed_letters.add(guess)
        print("Good guess!")
    else:
        wrong += 1
        print("Wrong guess!")
        print(HANGMANPICS[wrong])
     # display the current state of the word
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in ranworld])
    print(display_word)
     # check if the user has won
    if '_' not in display_word:
        print("Congratulations! You've guessed the word:", ranworld)
        break
   