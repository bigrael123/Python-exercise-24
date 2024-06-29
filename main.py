import file_handler as data
import random as r

file_name = "scoreboard.txt"
scoreboard = []
chances = 0
words = []
print("Type your name")
player = input("Type your name here: ")
aword = ''
scoreboard = data.Load_file(file_name, scoreboard)
file_name = "words"
words = data.Load_file(file_name, words)
while(True):
    while(True):
        print("Select a number that corresponds to the desired option: \n 1 - Play hangman \n 2 - See scores \n 3 - Exit game")
        try:
            selection = int(input("Type a number: "))
            if(selection<=0 or selection>3):
                print("Please, type a number between 1 and 3")
            else:
                break
        except ValueError:
            print("Please, type a number")

    match selection:
        case 1:
            word = words[r.randint(0, len(words)-1)]
            answer = ["_"]*len(word)
            for letter in answer:
                print(letter, end="")
            print("")
            while(True):
                while(True):
                    print("Guess a letter")
                    letter = input("Type a letter: ")
                    if(not len(letter)>1 and (not letter == ""  and not " ") ):
                        break
                    else:
                        print("Type only one letter, please and no spaces")
                i = 0
                chance_counter = 1
                lettercounter = 0
                for character in word:     
                    if(letter.lower() == character.lower()):
                        lettercounter+=1
                for character in word:
                    if(letter.lower() == character.lower()):
                        if(letter in answer and lettercounter == 0):
                            print("You already guessed this letter")
                            chance_counter = 1
                        else:
                            lettercounter-=1
                            chance_counter = 0
                            answer[i] = character
                        if(not letter in word):
                            print("test")
                            chance_counter = 1
                    i+=1
                if(not chance_counter == 0):
                    chance_counter=0
                    chances+=1
                    print(f"You used {chances} out of 8")
                if(chances == 8):
                    print(f'You failed. The word was {word}')
                    scoreboard.append(f"The cpu won the word was {word}")
                    data.Save_file(scoreboard)
                    chances = 0
                    break
                i = 0
                temp = ''
                for char in answer:
                    temp+=char
                print("")
                aword = temp
                print(aword)
                temp = ''
                if(aword.lower() == word.lower()):
                    chances = 0
                    scoreboard.append(f"{player} won the word was {word}")
                    print(f"You guessed the word {word} and you won")
                    data.Save_file(scoreboard)
                    break
        case 2:
            if(len(scoreboard)>0):
                for score in scoreboard:
                    print(score)
            else:
                print("There are no scores yet.")
        case 3:
            exit()