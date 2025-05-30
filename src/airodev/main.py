# File: main.py
from crew import create_crew

def main():
    print("Welcome to Airodev - Your AI Web Designer ✨")
    user_prompt = input("Describe the website you'd like Airodev to build: ")

    print("\n  Generating website with Airodev...\n")
    result = create_crew(user_prompt)

    print("\n Airodev has completed the design process.")
    print(" Output:\n")
    print(result)

if __name__ == "__main__":
    main()
