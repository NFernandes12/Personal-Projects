import random,string
from words import words

def get_valid_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters=set(word) # letters in the word 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has already guessed 

    lives = 8

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives and guessed these letters ", "".join(used_letters))
        
        # list for current word 
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:word_list.append('-')
        print('Current word: ', ''.join(word_list))    
        
        user_guess = input('Guess a letter: ').upper()
        if user_guess in alphabet - used_letters:
            used_letters.add(user_guess)
            if user_guess in word_letters:
                word_letters.remove(user_guess)
            else: 
                lives=lives -1
                print(f'{user_guess} not in the word you have {lives} lives left')
        
        elif user_guess in used_letters:
            print(f'You have already guessed {user_guess} try again')   
        
        else:print('Please type a valid character')
    if lives == 0:
        print(f'You died the word was {word}')
    else:print(f'You guessed the word {word}')
hangman()