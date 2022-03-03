from words import words
import string
import random

class Hangman:
    # Gives us base variables as we launch the Hangman class
    def __init__(self):
        self.word = random.choice(words).upper() # Self.word is a random choice from the list of words in words.py and makes it uppercase
        self.word_letters = set(self.word) # Stores values from self.word in a set (Set lists can only contain unique values, no duplicates)
        self.guessed_letters = set()
        self.attempts = 0 # The number of attempts the user has guessed
        self.max_attempts = 7 # The maximum amount of attempts the user can guess
        self.alphabet = set(string.ascii_uppercase) # Set that contains the alphabet
    
    # Prints a space between each value in self.display
    def display(self):
        print() # Creates a space between the previous lines in terminal
        letters = [letter if letter in self.guessed_letters else "_" for letter in self.word] # Prints a _ for every etter in self.word
        print(" ".join("HANGMAN"[:self.attempts])) # Displays a space between the word HANGMAN (The word will only be displayed up to the number that the user has guessed)
        print(f"Guessed letters: {' '.join(self.guessed_letters)}")
        print(" ".join(letters)) # Displays a space between each value in letters

    # Reminder to update
    def check_guess(self, guess):
        # Checking if the guess is valid by seeing if the user actually typed something
        if len(guess) < 1:
            return print("\nYou must guess at least one character")
    
        # Checking if the guess is valid by only containing letters
        for letter in guess:
            if letter not in self.alphabet:
                return print("\nYou can only guess letters")
        
        # Checking if the guess is longer than one letter
        if len(guess) > 1:
            if guess == self.word:
                for letter in guess: # For every letter in the guess, check if it in word_letters and remove it from the list, if it is.
                    if letter in self.word_letters:
                        self.word_letters.remove(letter)
                    else:
                        continue
            else: # If the guess isnt the word, lose an attempt
                self.attempts += 1

        # Else if the guess is only one letter, check if its the correct
        elif len(guess) == 1:
            if guess in self.word_letters:
                self.guessed_letters.add(guess)
                self.word_letters.remove(guess)
            elif guess in self.guessed_letters:
                print("\nAlready guessed")
            else:
                self.guessed_letters.add(guess)
                self.attempts += 1
    
    # Checks if the game is over
    def check_for_win(self):
        if len(self.word_letters) < 1:
            return True
    
    # Checks if the game is over
    def check_for_loss(self):
        if self.attempts >= self.max_attempts:
            return True

# Function to start the game
def game():
    game = Hangman() # game assigned with class Hangman
    active = True

    while active: # Keeps playing, aslong as its active
        game.display() # Displays Hangman, secret word, and guessed letters
        guess = input("Guess: ").upper() # Lets user take a guess
        game.check_guess(guess) # Checks if user guess is valid

        if game.check_for_win(): # Checks if player has won
            print(f"\nYou won the round! The secret word was {game.word}")
            active = False

        elif game.check_for_loss(): # Checks if player has lost
            print("\nH A N G M A N")
            print(f"\nYou lost. The secret word was {game.word}")
            active = False

game() # Starts the game