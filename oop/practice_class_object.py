class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer




question_bank  = [
    Question("What is the capital of France?", "Paris"),
    Question("What is the largest planet in our solar system?", "Jupiter"),
    Question("What is the chemical symbol for gold?", "Au")
]




def run_quiz(questions):
    score = 0
    for q in questions:
        print(q)
        print(q.question)
        user_answer = input("Enter Your answer:").lower().strip()


        if user_answer == q.answer.lower():
            print("your ans is Correct!")
            score += 1
        else:
            print("your ans is wrong! the correct answer is:", q.answer)
    print(f"Quiz completed! Your final score is: {score}/{len(questions)}")

run_quiz(question_bank)