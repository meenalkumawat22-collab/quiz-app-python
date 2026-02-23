from questions import quiz_questions

def run_quiz():
    score = 0

    print("🎉 Welcome to the Python Quiz 🎉")
    print("-----------------------------------")
from questions import quiz_questions

def run_quiz():
    score = 0

    print("🎉 Welcome to the Python Quiz 🎉")
    print("-----------------------------------")

    for q in quiz_questions:
        print("\n" + q["question"])
        
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")
            print("Correct Answer:", q["answer"])

    print("\n📊 Quiz Completed!")
    print("Your Score:", score, "/", len(quiz_questions))

run_quiz()
    