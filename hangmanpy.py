class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        print(chosen_word)
        current = list('_' * len(chosen_word))
        print(current)
        for char in chosen_word:
            d = dict(char= char, guessed=False)
            print(d)


    
# this method will split the word up into a list of dictionaries with 2 attributes:
        
# the letter/character, and a boolean representing whether or not it has been guessed

Word('hangman')
    