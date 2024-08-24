import random
import hangman_words
from hangman_art import stages, logo


word_list = hangman_words.word_list
lives = 6



chosen_word = random.choice(word_list)
#print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:
    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You have already guessed {guess}. Try again.")

    display = ""
    guessed_letters += guess
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    guessed_letters += guess
    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"The word was {chosen_word}\n***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    print(stages[lives])
