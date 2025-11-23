import time
from stress_assessment import run_assessment
from config import AFFIRMATIONS, TIPS

class StressManagementApp:
    def __init__(self):
        self.running = True
    
    def show_welcome(self):
        print("\n" + "🌟" * 20)
        print("   WELCOME TO STRESS MANAGEMENT APP")
        print("🌟" * 20)
        print("A safe space to manage stress and find peace")
    
    def stress_assessment(self):
        """Option 1: Stress Assessment Quiz"""
        run_assessment()
    
    def breathing_exercise(self):
        """Option 2: Deep Breathing Exercise"""
        print("\n" + "="*40)
        print("   DEEP BREATHING EXERCISE")
        print("="*40)
        print("Follow the breathing pattern below:")
        print("This will help calm your nervous system.\n")
        
        for round_num in range(1, 4):
            print(f"Round {round_num}/3:")
            print("🫁 Inhale slowly through your nose... (4 seconds)")
            time.sleep(2)
            print("⏸️  Hold your breath... (4 seconds)")
            time.sleep(2)
            print("😮‍💨 Exhale slowly through your mouth... (4 seconds)")
            time.sleep(2)
            print()
        
        print("✅ Great job! You should feel more relaxed now.")
        input("\nPress Enter to continue...")
    
    def show_affirmations(self):
        """Option 3: Positive Affirmations"""
        print("\n" + "="*40)
        print("   POSITIVE AFFIRMATIONS")
        print("="*40)
        print("Repeat these affirmations to yourself:")
        print("They can help shift your mindset.\n")
        
        for i, affirmation in enumerate(AFFIRMATIONS, 1):
            print(f"{i}. {affirmation}")
        
        print("\n💫 Remember: You are stronger than you think!")
        input("\nPress Enter to continue...")
    
    def show_tips(self):
        """Option 4: Stress Management Tips"""
        print("\n" + "="*40)
        print("   STRESS MANAGEMENT TIPS")
        print("="*40)
        print("Practical tips to manage daily stress:\n")
        
        for i, tip in enumerate(TIPS, 1):
            print(f"⭐ {tip}")
        
        print("\n🔧 Try incorporating 1-2 tips into your day!")
        input("\nPress Enter to continue...")
    
    def gratitude_exercise(self):
        """Option 5: Gratitude Exercise"""
        print("\n" + "="*40)
        print("   GRATITUDE EXERCISE")
        print("="*40)
        print("Taking time for gratitude can boost your mood.")
        print("List 3 things you're grateful for today:\n")
        
        grateful_list = []
        for i in range(1, 4):
            item = input(f"{i}. I am grateful for: ").strip()
            if item:
                grateful_list.append(item)
        
        print("\n" + "✨" * 30)
        print("YOUR GRATITUDE LIST:")
        print("✨" * 30)
        for item in grateful_list:
            print(f"🙏 {item}")
        print("\n🌈 Focusing on gratitude helps attract more positivity!")
        input("\nPress Enter to continue...")
    
    def exit_app(self):
        """Option 6: Exit the application"""
        print("\n" + "💝" * 20)
        print("   Thank you for using Stress Management App!")
        print("   Take care of yourself and stay calm! 💝")
        print("💝" * 20)
        self.running = False
    
    def main_menu(self):
        """Display main menu and handle user choices"""
        while self.running:
            print("\n" + "="*40)
            print("   MAIN MENU")
            print("="*40)
            print("1. 🧠 Stress Assessment Quiz")
            print("2. 🫁 Deep Breathing Exercise") 
            print("3. 💫 Positive Affirmations")
            print("4. 🔧 Stress Management Tips")
            print("5. 🙏 Gratitude Exercise")
            print("6. 🚪 Exit")
            print("="*40)
            
            choice = input("Please choose an option (1-6): ").strip()
            
            if choice == '1':
                self.stress_assessment()
            elif choice == '2':
                self.breathing_exercise()
            elif choice == '3':
                self.show_affirmations()
            elif choice == '4':
                self.show_tips()
            elif choice == '5':
                self.gratitude_exercise()
            elif choice == '6':
                self.exit_app()
            else:
                print("❌ Invalid choice. Please enter a number between 1-6.")

def main():
    app = StressManagementApp()
    app.show_welcome()
    app.main_menu()

if __name__ == "__main__":
    main()