from random import choice as choice
import os

#for refrshing the screen
command = 'cls'

def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'): 
    command = 'cls'
  os.system(command)



# Prints the rules of the hangman game
def rules():
  print("Welcome! Here are the rules of hang man: ")
  print("\n1. You have 6 chances to guess the correct word presented.")
  print("\n2. If you can guess the word correct, you win!")
  print("\n3. You have 3 random powers that can either help you or hurt you.")
  print("\n4. If you run out of chances, however, you lose...")
  print("\n5. To randomly get a power, type 'power'.")
  print("\n6. And if you want to guess the word type in 'solve'.")
  print("\n7. Have fun!")

rules()


#Import sprites later
hangman_pics = ['''
   +---]
       |
       |
       |
      ___''', '''
   +---]
   O   |
       |
       |
      ___''', '''
   +---]
   O   |
   (   |
       |
      ___''', '''
   +---]
   O   |
  /Y   |
       |
      ___''', '''
   +---]
   O   |
  /Y\  |
       |
      ___''', '''
   +---]
   O   |
  /Y\  |
  /    |
      ___''', '''
   +---]
   @   |
  /Y\  |
  / \  |
      ___''']


# Selection of words so far
Words = ["chimera", "wyrm", "griffin", "pegasus", "hippocampus", "merman", "foot", "adviser", "whole", "falsify", "fashion", "cucumber", "rob", "grandmother", "worm", "pumpkin", "appetite", "monstrous", "taxi", "of", "contraction", "can", "joint", "church", "complete", "occupy", "demonstrate", "frighten", "war", "sense", "wagon", "poison", "far", "mislead", "mass", "spectrum", "industry", "onion", "meadow", "blame", "democratic", "breakfast", "decoration", "addition", "snarl", "husband", "smell", "surprise", "instruction", "tourist", "rotate", "circulation", "bar", "uncertainty", "speed", "permanent", "wine", "absolute"]

luck = ["good", "bad"]

good = ["Minus 1 body part", "Minus 1 body part", "Minus 1 body parts", "Minus 2 body parts", "Letter reveal"]

bad = ["Plus 1 body part", "Plus 1 body part", "Plus 1 body parts", "Plus 2 body parts", "Nothing", "New word"]



# Type solve to solve the word
solve = ["solve"]

# Type power to get a power
power = ["power"]

# Letters of the word put in a list
letters = []

# Correct letters
c_Letters = []

# Incorrect letters
w_Letters = []

# Displays the letters and underscores
display = []
# def addDisplay():
#   for thing in display:
#     print(thing)

# TODO: make a randomizer that can have buffs or debuffs

# Makes the hangman game a function so it can be called later if you want # to play again
def Hangman():


  
# Clears the lists so they can be used again
  c_Letters.clear()
  w_Letters.clear()
  letters.clear()
  display.clear()


  
  
# Randomizes the words so each time you play it is different
  word = choice (Words)
  
# Gives how many underscores there are in the word
  word_length = len(word)
  
# Amount of tries user gets
  chances = 6

# Amount of powers user has
  power_left = 5
  
# Makes the underscores for the word
  for i in range(word_length):
    display.append("_ ")
  
  for letter in word:
    letters.append(letter)


# Makes the game run until the user runs out of chances
  while chances > 0:
    clearConsole()

    x = 1

    

    
# Puts underscores to display how many letters are in the word as well as # the number
# of letters
    

    for thing in display:
      print(thing, end='')


    if chances == 6:
      print(hangman_pics[0])
    elif chances == 5:
      print(hangman_pics[1])
    elif chances == 4:
      print(hangman_pics[2])
    elif chances == 3:
      print(hangman_pics[3])
    elif chances == 2:
      print(hangman_pics[4])
    elif chances == 1:
      print(hangman_pics[5])
    else:
      print(hangman_pics[6])

    # Shows guesses left
    if chances != 1:
      print("You have", str(chances), " guesses left!")
    else:
      print("You have", str(chances), " guess left!")
    
    print("\nThe word has " + str(len(word)) + " letter(s)")

    # Shows powers left
    print("\nYou have", str(power_left), "powers left")
    # Shows the letters that have been guessed
    print("Corrrect letters: " + str(c_Letters))
    print("Incorect letters: " + str(w_Letters))

    # Allows user to guess a letter
    guess = input("Try and guess a letter in the word: ")
    # Puts letter in lowercase
    guess = guess.lower()
    print("\n================================================")

    # Relaces the underscores with the correct letter
    if guess in word:
      if guess not in c_Letters:
        print("Correct!")
        c_Letters.append(guess)
        if guess in letters:
          for i in range(len(letters)):
            if letters[i] == guess:
              display[i] = guess + ' '
      
    # Allows user to solve the word
    elif len(guess) > 1:
      if guess in solve:
        fullWord = input("What is the full word?: ")
        if word == fullWord:
          print("You Win!")
          break
        else:
          print("Wrong guess! Try again!" + "\n")
          chances -= 1
          print("\nYou have " + str(chances) + "guesses left!")
          print("Correct letters: " + str(c_Letters))
          print("Wrong letters: " + str(w_Letters))

      # Allows user to get a power
      if guess in power:
        power_choice = choice(luck)
        if power_left == 0:
          print("\nYou have no more powers!")

        # Good powers in action
        elif power_choice == "good":
          good_power = choice(good)
          print("\n", good_power)
          if good_power == "Minus 1 body part":
            chances += 1
            if chances > 6:
              chances = 6
            power_left -= 1
          elif good_power == "Minus 2 body parts":
            chances += 2
            if chances > 6:
              chances = 6
            power_left -= 1
          elif good_power == "Letter reveal":
            while x == 1:
              letter_reveal = choice(letters)
              if letter_reveal not in c_Letters:
                for i in range(len(letters)):
                  if letters[i] == letter_reveal:
                    display[i] = letter_reveal + ' '
                    power_left -= 1
                    x = 0
        # Bad powers in action
        elif power_choice == "bad":
          bad_power = choice(bad)
          print(bad_power)
          if bad_power == "\nPlus 1 body part":
            chances -= 1
            power_left -= 1
            if chances == 0:
              print("\nYou lose!")
              print("The word was " + word + "!")
              break
          elif bad_power == "\nPlus 2 body parts":
            chances -= 2
            power_left -= 1
            if chances == 0:
              print("\nYou lose!")
              print("The word was " + word + "!")
              break
          elif bad_power == "\nNothing":
            print("You wasted a power!")
            power_left -= 1
          elif bad_power == "New word":
            print("\nYou got a new word!")
            display.clear()
            letters.clear()
            word = choice(Words)
            for i in range(word_length):
              display.append("_ ")
            for letter in word:
              letters.append(letter)
            power_left -= 1
            
          
              

    elif guess not in word:
      if guess not in w_Letters:
        print("Wrong...")
        w_Letters.append(guess)
        chances -= 1
        if chances == 0:
          print(hangman_pics[6])
          print("You Lose!")
          print("The word was " + word)
          break
    else:
      print("Invalid input" + "\n")
      chances -= 1
      print("You have " + str(chances) + " guesses left!")
      if chances == 0:
        print("\nYou lose...")
        print("Your word was " + str(word) + ".")
        break
        


#TODO: create the winning screen

#TODO: create the losing screen

#Makes sure the user wants to play
print("\nAre you ready to play?")
ready = input()
if "y" in ready or "f" in ready:
  Hangman()
else:
  print("Do you need to see the rules?")
  ready = input()
  if "y" in ready or "f" in ready:
    rules()
  else:
    print("You don't want to play?")
    ready = input()
    if "y" in ready or "f" in ready:
      Hangman()
    else:
      print("Ya know what, I dont care. You're playing anyways." + "\n")
      Hangman()
  

# Asks if the user wants to play again
while True:
  restart = input("\nDo you want to play again? ")
  if "y" in restart or "f" in restart:
    print("Do you need to see the rules? ")
    ready = input()
    if "y" in ready or "f" in ready:
      rules()
    else:
      Hangman()
  else:
    print("\nGet lost, loser!")
    break


