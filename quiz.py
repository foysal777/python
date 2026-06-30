question_bank  = {

    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the chemical symbol for gold?": "Au"
}


score = 0
for question , answer in question_bank.items():
    print(question)
    user_answer =  input("Enter your answer: ")
    if user_answer.lower().strip() == answer.lower():
        print("your ans is Correct!")
        score += 1


    else: 
        print("your ans is wrong! the correct answer is:", answer)


print("your total score is: " , score, "out of" , len(question_bank))
print("your percentage is: " , (score/len(question_bank))*100, "%")