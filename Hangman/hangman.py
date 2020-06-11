import random
import string

WORDLIST_FILENAME = "words.txt"

# Function to print out the final face 
def i_am_dead():
    print(" [][][][] ")
    print(" []x--x[] ")
    print(" [][][][] ")
    print("   [][]   ")
    print(" YOU ARE DEAD ")
# Function to load word file(found in respository with the name of words.txt
def load_words():
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    return wordlist

wordlist = load_words()
# Random Choice wrods fucntion
def choose_word(wordlist):
    word  = random.choice(wordlist)
    return word

word = choose_word(wordlist)
orignal_list = [elm for elm in word ]
word_list = [elm for elm in word]

# Start parameters gathering 
def start():
    print("Hello Welcome to the Game ")
    print("The word you choose is {} letters long".format(len(word)))
    print("You have {} points".format(len(word)))
    print()
    print()
    for i in range(int(len(word) - 3)):
        a = random.randrange(len(word))
        word_list[a] = '*'
    print("The word is as following {} ".format(word_list))
    print()
    print()
    
# Main gameplay function 
def hangman():
    start()
    points = len(word)
    bool_flag= True
    index = []
    while bool_flag  == True:
        guessed_string = input( "Enter a single letter you think is in the word : ")

        for i in range(len(word_list)):
            if guessed_string == orignal_list[i]:
               index.append(i)
        

        guessed_string_number = index

        if guessed_string_number == []:

                    points = points - 1
                    print()
                    print("Ehhh wrong answer, you have {} points .".format(points))
                    print()
                    index=[]
                    if points <= 0 :
                        print("Game is Over")
                        print("You have lost")
                        print("The word was {}".format(word))
                        print()
                        print()
                        i_am_dead()
                        print()
                        print()
                        bool_flag = False
        else:
       
            for elm in guessed_string_number:

                if orignal_list[elm]  == guessed_string:

                   word_list[elm] = guessed_string
                   print(word_list)
                   index = []
                   if ("".join(word_list) == word ):
                       print("YOU HAVE WON")
                       bool_flag = False 
        
            

              


# Function call
hangman()
