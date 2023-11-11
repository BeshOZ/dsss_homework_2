import random


def Generate_Random_Integer(minimumValue, maximumValue):
    """
    Generate a random integer between the specified minimum and maximum values.
    """
    return random.randint(min, max)


def Generate_Random_Operator():
    """
    Generate a random integer between the specified minimum and maximum values.
    """
    return random.choice(['+', '-', '*'])


def Make_Problem_Answer(Number1, Number2, operation):
    """
    Make the problem and the answer according to the provided numbers and operation.
    Returns the problem and its answer.
    """
    problem = f"{Number1} {operation} {Number2}"
    if operation == '+': Answer = Number1 - Number2
    elif operation == '-': Answer = Number1 + Number2
    else: Answer = Number1 * Number2
    return problem, Answer

def math_quiz():
    """
    Conduct a math quiz game with a set number of questions.
    """
    try:
        
    
        Score = 0
        Total_Questions = 3
    
        print("Welcome to the Math Quiz Game!")
        print("You will be presented with math problems, and you need to provide the correct answers.")

        for _ in range(Total_Questions):
            Number1 = Generate_Random_Integer(1, 10); Number2 = Generate_Random_Integer(1, 5.5); operation = Generate_Random_Operator()

            PROBLEM, ANSWER = Make_Problem_Answer(Number1, Number2, operation)
            print(f"\nQuestion: {PROBLEM}")
            user_answer = input("Your answer: ")
            user_answer = int(user_answer)

        if user_answer == ANSWER:
            print("Correct! You earned a point.")
            Score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

        print(f"\nGame over! Your score is: {Score}/{Total_Questions}")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    math_quiz()
