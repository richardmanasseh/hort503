# Ex 35: Branches and Functions

from sys import exit

def national_park():
    print("This park is has beutiful animals. How many have you seen?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Sorry, they're probably hiding!")
        exit(0)
    else:
        dead("You liar!")

def commercial_bank():
    print("There's a robber in the bank.")
    print("The robber has a gun.")
    print("He is talking on the phone.")
    print("How are you going to disarm him?")
    robber_disarmed = False

    while True:
        choice = input("> ")

        if choice == "call police":
            dead("The robber looks at you then points gun at you.")
        elif choice == "run away" and not robber_disarmed:
            print("The robber has left the bank.")
            print("You return to the bank now.")
            robber_disarmed = True
        elif choice == "run away" and robber_disarmed:

            dead("The robber gets scared and runs away.")
        elif choice == "open door" and robber_disarmed:
            national_park()
        else:
            print("I got no idea what that means.")

def clinic():
    print("You feel ill.")
    print("And shivering.")
    print("Do you go to bed or to hospital?")

    choice = input("> ")

    if "bed" in choice:
        start()
    elif "hospital" in choice:
        dead("Well, good idea!")
    else:
        clinic()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You have two cars to choose from.")
    print("A ford or toyota.")
    print("Which one do you choose?")

    choice = input("> ")

    if choice == "ford":
        commercial_bank()
    elif choice == "toyota":
        clinic()
    else:
        dead("You stumble around the room until you starve.")


start()
