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
       # # Checking if the guess is valid by seeing if the user actually typed something
       # if len(guess) < 1:
       #     return print("You must guess at least one character")
       
       # # Checking if the guess is valid by only containing letters
       # for letter in guess:
       #     if letter not in self.alphabet:
       #         return print("You can only guess letters")
       #     else:
       #         continue
       # 
       # if len(guess) > 1:
       #     if guess == self.word:
       #         for letter in guess:
       #             if letter in self.word_letters:
       #                 self.word_letters.remove(letter)
       #             else:
       #                 continue
       #     else:
       #         self.attempts += 1

        if guess in self.word_letters:
            self.guessed_letters.add(guess)
            self.word_letters.remove(guess)
        elif guess in self.guessed_letters:
            print("Already guessed")
        else:
            self.guessed_letters.add(guess)
            self.attempts += 1
    

    def check_for_win(self):
        if len(self.word_letters) < 1:
            return True
    
    
    def check_for_loss(self):
        if self.attempts >= self.max_attempts:
            return True

def game():
    game = Hangman()
    active = True

    while active:
        game.display()
        guess = input("Guess: ").upper()
        game.check_guess(guess)

        if game.check_for_win():
            print(f"You won the round! The secret word was {game.word}")
            active = False

        elif game.check_for_loss():
            print()
            print("H A N G M A N")
            print(f"You lost. The secret word was {game.word}")
            active = False

game()