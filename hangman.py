# You must have a Word class.

# It should print the letters of a word to be guessed like this _ _ _ _ _ _

# As the user guesses letters:

# If they get it right:
# The letter should be filled in everywhere it appears, so if the word is cheese, after they type "e" and hit enter, they should see _ _ e e _ e.
# They should be praised somehow (something like "Yes!")
# If that guess completes the word, Game over—Win! --> they should be told the word, praised for winning, and the game should stop (i.e. stop prompting them for input, and the program should exit).
# If they guess a wrong letter:
# They should be admonished ("No, silly" or whatver)
# If that guess uses up their last remaining guess, Game over—Lose! --> they should be told they lost and the game should stop (i.e. stop prompting them for input, and the program should exit).
# If the game is not over, then after each guess, it should tell the user how many guesses are remaining, and which letters have already been guessed, and re-print the word with blanks
# The structure of your MVP will be:

class Word():
  def__init__(self, chosen_word):
    # this method will split the word up into a list of dictionaries with 2 attributes:
    # the letter/character, and a boolean representing whether or not it has been guessed

  # ...other methods here... (refer back to JS hangman for ideas -- may not translate exactly, but
  # should be close enough)


# some variables here to prepare the wordlist, initialize things like
# `remaining_guesses` (start a round with 8), `letters_used`, the `chosen_word` (randomly
# chosen from a list of words you also declare here perhaps?),
#and whatever else you might want to keep track of


# a loop here that will cause game to play and be exited when user either wins or loses
# see below for tips on how to structure this loop