import random

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != 4:
            print(f"You Must Guess {CODE_LENGTH} Colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid Color: {color}. TRY AGAIN!!!")
                break

        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_code in zip(guess, real_code):
        if guess_color == real_code:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_code in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to Mastermind, you have {TRIES} to guess the code!!!")
    print("The Valid Color are ", *COLORS)

    code = generate_code()

    # print(code)

    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f'You guessed the code in {attempts} tries!!!')
            break

        print(f'Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}')

    else:
        print('You ran out of tries, the code was: ', *code)


if __name__ == '__main__':
    game()    
