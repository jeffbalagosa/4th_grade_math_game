import random
import os
from addition_subtraction_game import generate_add_sub_problem
from multiplication_game import generate_mul_problem
from division_game import generate_div_problem


def math_game():
    streak = 0
    highest_streak = 0

    while True:
        # Clear the terminal screen
        os.system("cls" if os.name == "nt" else "clear")

        # Display the streak and highest streak
        print(f"Streak: {streak}")
        print(f"Highest Streak: {highest_streak}")
        print("============")

        # Use generate_add_sub_problem(), generate_mul_problem(),
        # or generate_div_problem() at random
        problem, answer = random.choice(
            [
                generate_add_sub_problem("+"),
                generate_add_sub_problem("-"),
                generate_mul_problem(),
                generate_div_problem(),
            ]
        )

        # Display the problem
        print(f"What is the answer to: {problem}?")

        # Get the user's answer
        user_answer = input("Enter your answer: ")

        # Check if the answer is correct
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

        # Prompt the user to press "Enter" to continue
        # or press Ctrl + C to quit
        input('Press "Enter" to continue.\nOr press Ctrl + C to quit.')


# Run the math game
if __name__ == "__main__":
    math_game()
