class Word():
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.game_list = []
        self.game_over = False
        # loop through chosen word
        for char in chosen_word:
            # for each character, create a dictionary with the letter and false guess
            d = dict(char= char, guessed=False)
            # add that dictionary to the game list
            self.game_list.append(d)

    def game_status(self):
        #initiate the game status
        status = ""
        #loop through the dictionaries in the game list
        for dic in self.game_list:
            #if the dictionary letter has been guessed
            if dic['guessed'] == True:
                #add the character to status
                status += dic['char']
            else:
                #else just add in a dash
                status += "-"
        # print the status
        print(status) 
        self.game_end()

    def start_game(self):
        print('You are now playing Hangman! Press a key to start.')
        input()
        print('Here is your current word\'s length:')
        self.game_status()
        self.game_play()

    def game_play(self):
        if self.game_over == False:
            self.guess = input("Guess a letter: ").lower()
            print(self.guess)
            # loop through the game list
            for dic in self.game_list:
                if dic['char'] == self.guess:
                    dic['guessed'] = True
                elif dic['char'] != self.guess:
                    continue
            self.game_status()
            # self.check_end()
            self.game_play()

    def check_end(self):
        for dic in self.game_list:
            if dic['guessed'] == False:
                return False
        return True


    def game_end(self):
        if self.check_end():
            self.game_over = True
            print('Congratulations, you win!')
        else:
            return


# `remaining_guesses` (start a round with 8), `letters_used`, the `chosen_word` (randomly
# chosen from a list of words you also declare

    

game = Word('hangman')
game.start_game()
    