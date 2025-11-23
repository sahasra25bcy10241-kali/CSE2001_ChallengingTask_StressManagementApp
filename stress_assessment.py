from config import QUESTIONS, SCORING_RANGES, STRESS_MESSAGES

def get_user_answers():
    """Get user responses to stress assessment questions"""
    answers = []
    print("\n" + "="*50)
    print("   STRESS LEVEL ASSESSMENT")
    print("="*50)
    print("Please rate each statement from 1-5:")
    print("1: Never, 2: Rarely, 3: Sometimes, 4: Often, 5: Always")
    print("-" * 50)
    
    for i, question in enumerate(QUESTIONS, 1):
        while True:
            try:
                answer = int(input(f"\nQ{i}: {question} (1-5): "))
                if 1 <= answer <= 5:
                    answers.append(answer)
                    break
                else:
                    print("❌ Please enter a number between 1 and 5")
            except ValueError:
                print("❌ Please enter a valid number")
    
    return answers

def calculate_stress_score(answers):
    """Calculate total stress score"""
    return sum(answers)

def get_stress_level(score):
    """Determine stress level based on score"""
    for level, (min_score, max_score) in SCORING_RANGES.items():
        if min_score <= score <= max_score:
            return level
    return "Unknown"

def show_results(score, level):
    """Display assessment results"""
    print("\n" + "="*50)
    print("📊 ASSESSMENT RESULTS")
    print("="*50)
    print(f"Your Total Score: {score}/25")
    print(f"Stress Level: {level}")
    print(f"💡 Recommendation: {STRESS_MESSAGES.get(level, '')}")
    print("="*50)

def run_assessment():
    """Main function to run stress assessment"""
    answers = get_user_answers()
    score = calculate_stress_score(answers)
    level = get_stress_level(score)
    show_results(score, level)
    input("\nPress Enter to return to main menu...")