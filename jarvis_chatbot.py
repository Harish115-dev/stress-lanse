import random

# Simple advice database
ADVICE_LIST = [
    "Take deep breaths and try to relax.",
    "Remember to take breaks and rest your mind.",
    "Talk to someone you trust about how you're feeling.",
    "Practice mindfulness or meditation.",
    "Exercise regularly to boost your mood.",
    "Maintain a healthy sleep schedule.",
    "Write down your thoughts to help process emotions.",
    "Focus on things you can control and let go of what you can't.",
    "Stay connected with friends and family.",
    "Seek professional help if stress feels overwhelming."
]

def get_advice():
    return random.choice(ADVICE_LIST)

def main():
    print("Hello, I'm Jarvis! I'm here to help you manage stress and mental health.")
    print("Type 'advice' for a tip, 'exit' to quit.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == 'advice':
            print("Jarvis:", get_advice())
        elif user_input == 'exit':
            print("Jarvis: Take care! Remember, your well-being matters.")
            break
        else:
            print("Jarvis: I can give you advice if you type 'advice'. Type 'exit' to quit.")

if __name__ == "__main__":
    main()
