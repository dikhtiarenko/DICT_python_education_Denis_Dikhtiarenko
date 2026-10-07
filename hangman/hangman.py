import random

while True:
    menu_choice = input('Type "play" to play the game, "exit" to quit: > ')
    if menu_choice == "exit":
        break
    elif menu_choice == "play":
        words = ['python', 'java', 'javascript', 'php']
        secret_word = random.choice(words)

        guessed_state = '-' * len(secret_word)
        tried_letters = set()
        lives = 8

        print("HANGMAN")

        while lives > 0:
            print(f"\n{guessed_state}")
            letter = input ("Input a letter: > ")

            if len(letter) !=1:
                print("You should input a single letter")
                continue

            if not ('a' <= letter <= 'z'):
                print("Please enter a lowercase English letter")
                continue

            if letter in tried_letters:
                print("You've already guessed this letter")
                continue

            tried_letters.add(letter)

            if letter in secret_word:
                old_state = guessed_state
                new_state = list(guessed_state)
                for i in range(len(secret_word)):
                    if secret_word[i] == letter:
                        new_state[i] = letter
                guessed_state = "".join(new_state)

                if guessed_state == old_state:
                    print("No improvements")

                if guessed_state == secret_word:
                    print(guessed_state)
                    print("You've guessed this word!")
                    print("You survived!")
                    break
            else:
                print("That letter doesn't appear in the word")
                lives -= 1

        if lives == 0 and guessed_state != secret_word:
            print("You lost!")