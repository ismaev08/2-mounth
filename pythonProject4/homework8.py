import random


# Function to handle user input for "да, больше или меньше"
def get_user_feedback():
    while True:
        user_input = input(
            "Ваше число больше, меньше или равно? (введите 'больше', 'меньше' или 'равно'): ").strip().lower()
        if user_input in ['больше', 'меньше', 'равно']:
            return user_input
        else:
            print("Пожалуйста, введите 'больше', 'меньше' или 'равно'.")


# Function to play the number guessing game
def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    guesses = []

    while True:
        guess = random.randint(1, 100)
        attempts += 1
        guesses.append(guess)

        if guess == secret_number:
            print(f"Я угадал число {secret_number} за {attempts} попыток!")
            # Write results to a file
            with open('results.txt', 'w') as f:
                f.write(f"Number of attempts: {attempts}\n")
                f.write(f"List of guesses: {guesses}\n")
                f.write(f"Secret number: {secret_number}\n")
            break
        else:
            feedback = get_user_feedback()
            if (feedback == 'больше' and guess < secret_number) or (feedback == 'меньше' and guess > secret_number):
                continue
            elif feedback == 'равно':
                print(f"Число {secret_number} было загадано!")
                # Write results to a file
                with open('results.txt', 'w') as f:
                    f.write(f"Number of attempts: {attempts}\n")
                    f.write(f"List of guesses: {guesses}\n")
                    f.write(f"Secret number: {secret_number}\n")
                break


# Main loop to continuously play the game
while True:
    play_game()
    play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
    if play_again != 'да':
        break

print("Спасибо за игру!")