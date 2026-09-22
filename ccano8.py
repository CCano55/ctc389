# Cesar Cano
# Interactive Story Lab
# Robotics Lab Escape


def play_game():

    score = 0

    name = input("Welcome to the robotics lab! What is your name? ")

    print()
    print("Hello", name)
    print("You wake up inside a locked robotics lab after the power goes out.")
    print("To escape, you must make your way through the lab and solve several problems.")
    print()


    # Decision 1

    print("You see three objects near the door.")
    print("1. A flashlight")
    print("2. A basketball")
    print("3. A broken chair")

    choice = int(input("Which item do you take? "))

    if choice == 1:
        print("Good choice! The flashlight will help you see.")
        score = score + 1
    elif choice == 2:
        print("You take the basketball. It may not be very useful.")
    elif choice == 3:
        print("You take part of the broken chair with you.")

    print()


    # Decision 2

    print("You enter the robot work area and find three possible paths.")
    print("1. Walk through the dark storage room")
    print("2. Follow the emergency exit signs")
    print("3. Crawl under the robotics tables")

    choice = int(input("Which path do you choose? "))

    if choice == 1:
        print("The flashlight helps you safely cross the storage room.")
        score = score + 1
    elif choice == 2:
        print("The exit signs lead you toward another locked door.")
    elif choice == 3:
        print("You crawl under the tables and find another part of the lab.")

    print()


    # Decision 3

    print("A robot blocks your path.")
    print("1. Turn off its power switch")
    print("2. Push the robot out of the way")
    print("3. Yell at the robot")

    choice = int(input("What do you do? "))

    if choice == 1:
        print("You safely turn off the robot.")
        score = score + 1
    elif choice == 2:
        print("The robot is heavy, but you manage to move around it.")
    elif choice == 3:
        print("The robot does not respond, so you walk around it.")

    print()


    # Decision 4

    print("You reach a computer that controls the security doors.")
    print("1. Turn off the computer")
    print("2. Press the emergency unlock button")
    print("3. Restart the computer")

    choice = int(input("What do you choose? "))

    if choice == 1:
        print("The computer shuts down, but the doors remain locked.")
    elif choice == 2:
        print("The emergency doors unlock.")
        score = score + 1
    elif choice == 3:
        print("The computer restarts and gives you another route.")

    print()


    # Decision 5

    print("You reach the final hallway and see three doors.")
    print("1. STEM Lab")
    print("2. Emergency Exit")
    print("3. Storage Closet")

    choice = int(input("Which door do you choose? "))

    if choice == 1:
        print("You enter another classroom and find a way around.")
    elif choice == 2:
        print("You found the emergency exit!")
        score = score + 1
    elif choice == 3:
        print("You enter the storage closet and find another door.")

    print()


    # Final result

    if score >= 3:
        print("Congratulations", name, "you escaped the robotics lab!")
        print("You made enough good decisions to find your way out.")
    else:
        print("Sorry", name, "you did not escape the robotics lab.")
        print("You made it through all five decisions, but you needed better choices.")


# Main program

play_again = input("Would you like to play the game? ")

while play_again == "yes":

    play_game()

    print()

    play_again = input("Would you like to play again? ")

print("Thanks for playing!")
