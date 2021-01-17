class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.game_list = []
        print(chosen_word)
        current = '_ ' * len(chosen_word)
        print(current)
        # initialize game list
        # game_list = []
        # loop through chosen word
        for char in chosen_word:
            # for each character, create a dictionary with the letter and false guess
            d = dict(char= char, guessed=False)
            # add that dictionary to the game list
            self.game_list.append(d)

        print(self.game_list)
        self.start_game()

    # def print_word():
        
    # def check_letter():

    def start_game(self):
        guess = input("Guess a letter: ").lower()
        print(guess)
        # loop through the game list
        for item in self.game_list:
            for key, value in item.items():
                print(key, value)
                if guess == value:
                    print(value)
                    # change false to true
                    # update status
                    # check win
                    # show status
                    # prompt start_game if no win
                else:
                    print("Incorrect!")
       
        # for key in self.game_list:
        #     if guess == key.key.char:
        #         print(key.key.char)
        #     else:
        #         print("Not in that word.")

    # def get_word():

    # def show_scoreboard():

    # def process_user_guesses(): #perhaps?


# some variables here to prepare the wordlist, initialize things like
# `remaining_guesses` (start a round with 8), `letters_used`, the `chosen_word` (randomly
# chosen from a list of words you also declare here perhaps?),
#and whatever else you might want to keep track of

    


Word('hangman')
    