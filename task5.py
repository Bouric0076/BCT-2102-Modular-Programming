import random

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(["addition", "subtraction"])
    
    if operation == "addition":
        correct_answer = num1 + num2
        question = f"What is {num1} + {num2}? "
    else:
        correct_answer = num1 - num2
        question = f"What is {num1} - {num2}? "
        
    return question, correct_answer

num_questions = 5
score = 0
    
print("Welcome to the Addition and Subtraction Quiz")
for i in range(num_questions):
    question, correct_answer = generate_question()
    user_answer = int(input(question))
    
    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"The correct answer is: {correct_answer}")

print(f"Quiz completed! Your score: {score}/{num_questions}")

