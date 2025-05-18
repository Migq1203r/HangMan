import random
# Back-END:
import hangman_words
from hangman_words import word_list
'''
Art's ASCII:
# The HangMan:
1:
    +---+
        |
        |
        |
        |
        |
==========
2:
    +---+
    |   |
    O   |
        |
        |
        |
==========
3:
    +---+
    |   |
    O   |
    |   |
        |
        |
==========
4:
    +---+
    |   |
    O   |
   /|   |
        |
        |
==========
5:
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
==========
6:
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
==========
'''
stages = [
'''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
==========
          ''',
'''
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
==========
''',
'''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
==========
''',
'''
    +---+
    |   |
    O   |
   /|   |
        |
        |
==========
'''
,
'''
    +---+
    |   |
    O   |
    |   |
        |
        |
==========''',
'''
    +---+
    |   |
    O   |
        |
        |
        |
==========
''',
'''
    +---+
        |
        |
        |
        |
        |
==========
''',]
words = ['topaz',"elephant","boring","chilli","designer","energy","forward","fly","grandchild","grilled","huge","include","keyboard","locker","message","mess","notice","nice","news","newspaper","next","omelette","nowadays","ocean","occupation","occasion"]
print("""
 _                                              
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
""")
word = random.choice(hangman_words.word_list)
word_length = len(word)
placeholder = ""
for position in range(word_length):
    placeholder += "_"
print(word)

game_over = False
correct_letters = []
lives = 6
while not game_over:
    display = ""
    letter_people = input("\n\nGuess a Letter: ").lower()
    for letter in word:
        
        if letter == letter_people:
            display += letter
            correct_letters.append(letter_people)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"


    if letter_people not in word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("***********************************************You Lose!***********************************************")
    print(display)
    if "_" not in display: # Verifica se não tem nenhum "_"

        print(f"The Word is {word}\nYou Win!")
        print("***********************************************You Win!***********************************************")
        break
    print(stages[lives])
    if not lives == 0:
        print(f'***********************************************The amount of lives you have is: {lives} lives***********************************************')
    
    else:
        print("***********************************************You Lose!***********************************************")
    print(display)