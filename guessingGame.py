secret_word = "My Secret"
# placeholder for program functionality
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("OUt of guesses, you lose")
else:
    print("You win!")


#this is a better guessing game with clues

secret_word = "Dog"
guess = ""
guess_limit = 3
guess_count = 1
out_of_guesses = False
guess_clue_1 = "animal"
guess_clue_2 = "start with D"
guess_clue_3 = "man's best friend"


print("Hello, this is a guessing game! You have 3 guesses, with 3 clues to hit the right word. Enjoy.")
while guess != secret_word and not out_of_guesses:
    if guess_count <= 1:
        print("First clue: " + guess_clue_1)
        guess = input("Enter Guess: ")
        guess_count += 1
    elif guess_count <= 2:
        print("Clue number 2: " + guess_clue_2)
        guess = input("Enter Guess: ")
        guess_count += 1
    elif guess_count <= 3:
        print("Final clue: " + guess_clue_3)
        guess = input("Enter Final Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, you lose")
else:
    print("You win!")
