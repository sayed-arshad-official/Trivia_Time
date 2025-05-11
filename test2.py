import os
import sys
from test1 import compute2, compute1

def intro():
    print("=== INTRO ===")
    print("This shows only once when the script first runs.\n")

def main():
    print("=== MAIN ===")
    answer = input("What's 5 + 5? ")
    if answer == "10":
        print("Correct!")
    else:
        print("Wrong!")

    # Ask if user wants to restart the main part
    restart = input("Do you want to restart the main program? (yes/no): ").lower()
    if restart == "yes":
        # Restart script, skipping intro by passing a custom argument
        os.execl(sys.executable, sys.executable, *sys.argv, "--skip-intro")
    else:
        print("Goodbye!")
        exit()

# Only run intro if "--skip-intro" is NOT in command-line arguments
if "--skip-intro" not in sys.argv:
    intro()

# Run main
if __name__ == '__main__':
    main()
    compute2()
    compute1()
