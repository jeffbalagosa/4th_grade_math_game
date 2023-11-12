import random
import os


def generate_div_problem():
    """
    Generates a division problem with two random numbers between 10 and 99 and 1 and 9 respectively.
    The first number is a multiple of the second number and the problem is returned as a string in the format "num1 ÷ num2".
    The answer to the problem is also returned as an integer.
    """
    num1 = random.randint(10, 99)
    num2 = random.randint(1, 9)
    num1 = num2 * (random.randint(1, num1 // num2))
    problem = f"{num1} ÷ {num2}"
    answer = num1 // num2
    return problem, answer


def math_game():
    """
    This function starts a math game that generates division problems and prompts the user to solve them.
    The user's streak is tracked and the highest streak is recorded.
    """
    streak = 0
    highest_streak = 0

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Streak: {streak}")
        print(f"Highest Streak: {highest_streak}")
        print("============")
        problem, answer = generate_div_problem()
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
