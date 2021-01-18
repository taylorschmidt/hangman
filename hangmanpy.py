class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.game_list = []
        print(chosen_word)
        current = '-' * len(chosen_word)
        print(current)
        # loop through chosen word
        for char in chosen_word:
            # for each character, create a dictionary with the letter and false guess
            d = dict(char= char, guessed=False)
            # add that dictionary to the game list
            self.game_list.append(d)

        print(self.game_list)
        self.start_game()

    def game_status(self):
        status = ""
        for dic in self.game_list:
            if dic['guessed'] == True:
                status += dic['char']
            else:
                status += "-"
        print(status) 


    def start_game(self):
        self.guess = input("Guess a letter: ").lower()
        print(self.guess)
        # loop through the game list
        for dic in self.game_list:
            if dic['char'] == self.guess:
                dic['guessed'] = True
                print(self.game_list)
            elif dic['char'] != self.guess:
                continue
            self.game_status()

        # if guessed is false, print a '-' at that location
        # if guessed is true, print the letter at that location

    # def get_word():

    # def show_scoreboard():

    # def process_user_guesses(): #perhaps?


# some variables here to prepare the wordlist, initialize things like
# `remaining_guesses` (start a round with 8), `letters_used`, the `chosen_word` (randomly
# chosen from a list of words you also declare here perhaps?),
#and whatever else you might want to keep track of

    


Word('hangman')
    