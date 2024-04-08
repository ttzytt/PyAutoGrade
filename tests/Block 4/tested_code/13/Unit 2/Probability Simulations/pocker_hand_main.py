




from pocker_hands import *

if __name__ == "__main__":
    print("Choose a simulation:")
    print("1. Full House")
    print("2. Straight Flush")
    print("3. Flush")
    print("4. Flush Comparison")
    
    choice = input("Enter the number of the simulation you want to try: ")

    if choice == "1":
        full_house_simulation(100000)
    elif choice == "2":
        straight_flush_simulation(100000)
    elif choice == "3":
        flush_simulation(100000)
    elif choice == "4":
        flush_comparison_simulation(100000)
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
