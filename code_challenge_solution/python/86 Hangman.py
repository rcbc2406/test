import random

def hangman():
    words = ['python', 'programming', 'computer', 'hangman', 'game']
    word = random.choice(words)
    guessed_word = '-' * len(word)
    attempts = 6
    guessed_letters = []

    while attempts > 0:
        print('\nWord:', guessed_word)
        guess = input('Guess a letter: ').lower()

        if guess in guessed_letters:
            print('You already guessed that letter.')

        else:
            guessed_letters.append(guess)
            if guess in word:
                word_list = list(word)
                guessed_word_list = list(guessed_word)
                index = [i for i in range(len(word)) if word[i] == guess]
                for i in index:
                    guessed_word_list[i] = guess
                guessed_word = ''.join(guessed_word_list)
                print('Correct guess!')

                if guessed_word == word:
                    print('\nCongratulations! You guessed the word:', word)
                    return

            else:
                attempts -= 1
                print('Wrong guess!')
                if attempts == 0:
                    print('\nGame over! You ran out of attempts.')
                    print('The word was:', word)

hangman()
