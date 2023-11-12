import random
import os
from addition_subtraction_game import generate_add_sub_problem
from multiplication_game import generate_mul_problem
from division_game import generate_div_problem


def math_game():
    """
    A math game that generates random arithmetic problems and prompts the user to solve them.
    Keeps track of the user's streak and highest streak.
    """
    streak = 0
    highest_streak = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print(f"Streak: {streak}")
        print(f"Highest Streak: {highest_streak}")
        print("============")

        problem, answer = random.choice(
            [
                generate_add_sub_problem("+"),
                generate_add_sub_problem("-"),
                generate_mul_problem(),
                generate_div_problem(),
            ]
        )

        print(f"What is the answer to: {problem}?")

        user_answer = input("Enter your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        if user_answer == answer:
            print("Correct!")
            streak += 1
            if streak > highest_streak:
                highest_streak = streak
        else:
            print(f"Wrong! The correct answer is {answer}.")
            streak = 0

        input('Press "Enter" to continue.\nOr press Ctrl + C to quit.')


if __name__ == "__main__":
    math_game()
