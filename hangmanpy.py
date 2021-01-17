class Word():
    def __init__(self, chosen_word):

        # this method will split the word up into a list of dictionaries with 2 attributes:
        
        # the letter/character, and a boolean representing whether or not it has been guessed

        self.chosen_word = chosen_word
        print(chosen_word)
        current = '_ ' * len(chosen_word)
        print(current)
        # initialize game list
        game_list = []
        # loop through chosen word
        for char in chosen_word:
            # for each character, create a dictionary with the letter and false guess
            d = dict(char= char, guessed=False)
            # add that dictionary to the game list
            game_list.append(d)

        print(game_list)


    


Word('hangman')
    