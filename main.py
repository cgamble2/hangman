import random


class Player:
    def __init__(self):
        self.remaining_guesses = 0
        self.wrong_guesses = []


def check_guess(guess, word):
    found = False
    for c in word:
        if c.lower() == guess:
            found = True
            break
    return found


def valid_response(option):
    valid = False
    if 1 <= option <= 3:
        valid = True
    return valid


def read_word_list():
    with open('words.txt', 'r') as f:
        wl = [line.strip('\n') for line in f]
    f.close()
    return wl


def read_phrase_list():
    with open('phrases.txt', 'r') as f:
        pl = [line.strip('\n') for line in f]
    f.close()
    return pl


def main():
    print(input('Welcome to Hangman\nPress ENTER to begin'))
    print()
    challenge_type = input('Would you like to...\n1) Guess Words\n2) Guess Phrases\n? ')
    while challenge_type.isdigit() is False or int(challenge_type) < 1 or int(challenge_type) > 2:
        print(challenge_type, 'is not a valid response.\n')
        challenge_type = input('Press...\n1) Guess Words\n2) Guess Phrases\n? ')
    challenge_type = int(challenge_type)
    if challenge_type == 1:
        my_list = read_word_list()
        challenge = 'Word'
    else:
        my_list = read_phrase_list()
        challenge = 'Phrase'
    print()
    word = my_list[random.randint(0, len(my_list) - 1)]

    count = 0
    spaces = 0
    word_reveal = []
    for x in word:
        if x == ' ':
            word_reveal.append(' ')
            spaces += 1
        else:
            word_reveal.append('_')
            count += 1
    for x in word_reveal:
        print(x, end='')
    print()
    if spaces > 0:
        num_words = spaces + 1
        print('There are', num_words, 'words with a total of', count, 'letters.')
    else:
        print('The word is', count, 'letters long.')
    player = Player()
    player.remaining_guesses = input('How many guesses would you like? ')
    while player.remaining_guesses.isdigit() is False or int(player.remaining_guesses) < 1:
        print(player.remaining_guesses, 'is not a valid response.')
        player.remaining_guesses = input('How many guesses would you like? ')
    player.remaining_guesses = int(player.remaining_guesses)
    print()

    while player.remaining_guesses > 0:

        print(challenge + ':', end=' ')
        for c in word_reveal:
            print(c, end='')
        print()
        print('Wrong guesses:', player.wrong_guesses)
        print('Remaining guesses:', player.remaining_guesses)
        print()
        print('Press...')
        option = input('1) Guess a Letter\n2) Guess the ' + challenge + '\n3) Quit\n? ')
        while option.isdigit() is False or int(option) < 1 or int(option) > 3:
            print(option, 'is not a valid response.\n')
            print('Press...')
            option = input('1) Guess a Letter\n2) Guess the ' + challenge + '\n3) Quit\n? ')
        option = int(option)

        if option == 1:
            guessed_letter = input('Guess any letter: ')
            boolean = check_guess(guessed_letter, word)
            if boolean is True:
                i = 0
                for letter in word:
                    if guessed_letter == letter.lower():
                        word_reveal[i] = letter.lower()
                    i += 1
                print('\nCorrect')
            else:
                player.wrong_guesses.append(guessed_letter)
                print('\nIncorrect')
        elif option == 2:
            guessed_word = input('Guess the ' + challenge + ': ')
            if guessed_word == word.upper() or guessed_word == word.lower():
                print('You guessed the ' + challenge + '. You win!')
                exit()
            else:
                print('Oops! That\'s not it.\n')
        elif option == 3:
            print('You quit!')
            exit()
        if '_' not in word_reveal:
            print('The ' + challenge + ' was \'' + word + '\'. You win!')
            exit()

        player.remaining_guesses -= 1

    if player.remaining_guesses == 0:
        print('You ran out of guesses.\nThe ' + challenge + ' was \'' + word + '\'. You lose.')


main()
