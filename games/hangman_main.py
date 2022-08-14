import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
chosen_word_count = len(chosen_word)

# Set end game control.
end_game = False
# Set lives to equal 6
lives = 6

print(logo)

# Testing code
# print(f'This is a test and the random word is {chosen_word}.')

# display = []
# for letter in chosen_word:
#    display += "_"
# print(display)

# Create blank items
display = []
for i in range(chosen_word_count):
    display += "_"

# while end_game == False: # Another way to do that.
while not end_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(chosen_word_count):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Checking guess letter is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life!!!")
        lives -= 1
        if lives == 0:
            end_game = True
            for i in range(1, 10):
                print("jejejeje")
            print("You lose!!!")
    print(f"{'  '.join(display)}")

    # Check if user got all letters.
    if "_" not in display:
        end_game = True
        print("You win!!!")
    print(stages[lives])
