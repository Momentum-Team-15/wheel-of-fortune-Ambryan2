def play_game():
    #TODO need to select the word from the file
    w = open('test-word.txt', "r")
    p = w.read()

    #TODO Make the words from file into a list
    filtered = p.translate(str.maketrans('\n', ' '))
    items = filtered.split()

    # this picks first item in list will edit later
    desire = items[0]  #this equals dream right now 
    
    # this is what is used to determine if player is guessed
    
    #TODO need to make a board with the spaces for the length of the word
    
    #TODO Need to make a loop that ask people to select a letter (case of letter shouldn't matter) 
    #TODO Should be a while loop the ends when user guesses word or when they run out of guesses
    

    #TODO In loop I need it to tell when a letter was selected 
    #TODO  


if __name__ == "__main__":
    play_game()
