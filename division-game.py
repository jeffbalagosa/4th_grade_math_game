import random
import os


def generate_div_problem():
    # Generate random numbers for the problem
    num1 = random.randint(10, 99)
    num2 = random.randint(1, 9)

    # Make sure the division results in a whole number
    # Generate the dividend (num1)
    num1 = num2 * (random.randint(1, num1 // num2))

    # Generate the problem as a string
    problem = f"{num1} ÷ {num2}"

    # Calculate the correct answer
    # Perform integer division to get the whole number answer
    answer = num1 // num2

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
        problem, answer = generate_div_problem()

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

        # Prompt the user to continue playing or quit
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break


# Run the math game
if __name__ == "__main__":
    math_game()
