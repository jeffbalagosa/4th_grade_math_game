import random
import os


def generate_add_sub_problem(operation):
    """
    Generates an addition or subtraction problem with two random numbers.

    Args:
        operation (str): The operation to perform. Must be either '+' or '-'.

    Returns:
        tuple: A tuple containing the problem as a string and the answer as an integer.
    """
    if operation == "+":
        num1 = random.randint(100, 999)
        num2 = random.randint(10, 99)
        problem = f"{num1} + {num2}"
        answer = num1 + num2
    elif operation == "-":
        num1 = random.randint(100, 999)
        num2 = random.randint(10, 99)
        num1, num2 = max(num1, num2), min(num1, num2)
        problem = f"{num1} - {num2}"
        answer = num1 - num2
    else:
        raise ValueError("Invalid operation. Choose '+' or '-'.")
    return problem, answer


def math_game():
    """
    Runs a math game that generates addition and subtraction problems for the user to solve.

    The game keeps track of the user's streak (number of consecutive correct answers) and highest streak.

    Raises:
        ValueError: If the user enters a non-integer answer.

    Returns:
        None
    """
    streak = 0
    highest_streak = 0
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Streak: {streak}")
        print(f"Highest Streak: {highest_streak}")
        print("============")
        operation = random.choice(["+", "-"])
        problem, answer = generate_add_sub_problem(operation)
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
        input(
            'Press "Enter" to update streak and continue.\nOr press Ctrl + C to quit.'
        )


if __name__ == "__main__":
    math_game()
