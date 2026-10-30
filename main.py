import sys
from guitar import guitar_log, guitar_stats
from fitness import fitness_router
from debate import debate_log, debate_stats

while True:
    print("\n====================")
    print("   COMMAND CENTER    ")
    print("====================")
    print("1. Guitar")
    print("2. Debate")
    print("3. Fitness")#fitness has stats and log all in one
    print("4. Stats")
    print("5. Exit")


    choice = input("\nEnter a number ").strip()


    #routing
    try:
        if choice == "1":
            guitar_log()
        elif choice == "2":
            debate_log()
        elif choice == "3":
            fitness_choice = input("Caution: fitnes shows both stats and log, Do you still wanna see it? y/n ")
            if fitness_choice == "y":
                fitness_router()
            else:
                print("Fuck off")
        elif choice == "4":
            debate_stats()
            guitar_stats()
        elif choice == "5":
            sys.exit("Thank you for using command center")
        else:
            raise ValueError("Invalid choice, Please choose a number between 1 to 5")
    except ValueError as error:
        print(error)
        
