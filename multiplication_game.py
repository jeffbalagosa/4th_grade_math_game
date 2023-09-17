import random
import os


def generate_mul_problem():
    # Generate random numbers for the problem
    num1 = random.randint(10, 99)
    num2 = random.randint(1, 9)

    # Generate the problem as a string
    problem = f"{num1} x {num2}"

    # Calculate the correct answer
    answer = num1 * num2

    # Return the problem and answer
    return problem, answer


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

        # Generate a math problem
        problem, answer = generate_mul_problem()

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
