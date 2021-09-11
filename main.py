import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)
lenght = len(chosen_word)

display = []
for letter in range(lenght):
    display += "_"

end_of_game = False
lives = 6

while end_of_game == False:
    guess = input("Guess a letter : ").lower()

    if guess in display:
        print(f"You have already guessed the letter {guess}")

    for position in range(lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess} that's not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose")

    if "_" not in display:
        end_of_game == True
        print("you win")
    print(stages[lives])
