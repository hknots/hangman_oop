from words import words
import random

class Hangman:
    # Gives us base variables as we launch the Hangman class
    def __init__(self):
        self.word = random.choice(words) # Self.word is a random choice from the list of words in words.py
        self.display = ["_" for letter in self.word] # Prints a _ for every etter in self.word
        self.word_letters = set(self.word) # Stores values from self.word in a set (Set lists can only contain unique values, no duplicates)
        self.guessed_letters = set()
        self.attempts = 0 # The number of attempts the user has guessed
        self.max_attempts = 7 # The maximum amount of attempts the user can guess
    
    # Prints a space between each value in self.display
    def display(self):
        print() # Creates a space between the previous lines in terminal
        print(" ".join("HANGMAN"[:self.attempts])) # Displays a space between the word HANGMAN (The word will only be displayed up to the number that the user has guessed)
        print(" ".join(self.display)) # Displays a space between each _ in self.display

    # Reminder to update
    def check_guess(self, guess):
        if guess in self.word_letters:
            self.guessed_letters.append(guess)
            self.word_letters.remove(guess)
        elif guess in self.guessed_letters:
            print("Already guessed")
        else:
            self.attempts += 1
    

    def check_for_win(self):
        if self.word_letters < 1:
            return True