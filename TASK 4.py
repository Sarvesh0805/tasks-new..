import random

# Define a list of quiz questions as dictionaries
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "correct_answer": "Blue Whale"
    }
]

def ask_question(question_dict):
    print(question_dict["question"])
    for i, option in enumerate(question_dict["options"], 1):
        print(f"{i}. {option}")
    user_answer = input("Enter the number of your answer: ")
    return user_answer

def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

def display_result(score, total_questions):
    print(f"You got {score} out of {total_questions} questions correct!")

def quiz_game():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions. Enter the number of your answer.")

    play_again = "yes"
    while play_again.lower() == "yes":
        random.shuffle(quiz_questions)
        score = 0
        total_questions = len(quiz_questions)

        for question in quiz_questions:
            user_answer = ask_question(question)
            if check_answer(user_answer, question["correct_answer"]):
                print("Correct!\n")
                score += 1
            else:
                print(f"Sorry, the correct answer is: {question['correct_answer']}\n")

        display_result(score, total_questions)
        play_again = input("Do you want to play again? (yes/no): ")

    print("Thanks for playing!")

if __name__ == "__main__":
    quiz_game()