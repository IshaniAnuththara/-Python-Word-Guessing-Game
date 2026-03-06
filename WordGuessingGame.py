import random

word_bank = ['galaxy', 'nebula', 'planet', 'astronoid', 'comet', 'eclipse', 'gravity', 'satellite', 'cosmos', 'starlight']
word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 5

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()

    # Quick check to ensure the user only enters one character
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print(f'Wrong guess! Attempts left: {attempts}')

    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break

if attempts == 0 and '_' in guessedWord:
    print('\nYou\'ve run out of attempts! The word was: ' + word)