import time
import random


characters = ["gorgon", "wicked fairie", "dragon", "pirate"]


def print_pause(m):
    print(m)
    time.sleep(2)


def intro(option):

    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + option +
                " is somewhere around here,"
                " and has been terrifying the nearby village")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                " (but not very effective) dagger.")
    print()


def fight(weapon, option):
    # Things that happen when the player fights
    if "Sword" not in weapon:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the pirate.")
        print_pause("You have been defeated!")
        play_again()
    else:
        print_pause("As the " + option + " moves to attack,"
                    " you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand"
                    " as you brace yourself for the attack.")
        print_pause("But the " + option + " takes one look"
                    " at your shiny new toy and runs away!")
        print_pause("You have rid the town of the " + option + "."
                    " You are victorious!")
        play_again()


def cave(weapon, option):
    # Things that happen to the player goes in the cave
    if "Sword" not in weapon:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old " + option +
                    " and take the Sword with you.")
        print_pause("You walk back out to the field.")
        print()
        weapon.append("Sword")
    else:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_pause("\nYou walk back to the field.\n")

    field(weapon, option)


def house(weapon, option):
    # Things that happen to the player in the house
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door"
                " opens and out steps a " + option + ".")
    print_pause("Eep! This is the " + option + "'s house!")
    print_pause("The " + option + " attacks you!")
    if weapon is None:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")
    while True:
        user_choice0 = input("Would you like to (1) fight or (2) run away?\n")
        if (user_choice0 == '1'):
            fight(weapon, option)
            break
        elif (user_choice0 == '2'):
            print_pause("\nYou run back into the field. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")

            field(weapon, option)
            break


def field(weapon, option):
    # Things that happen when the player runs back to the field
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")

    while True:
        user_choice = input("(Please enter 1 or 2).\n")
        if (user_choice == '1'):
            house(weapon, option)
            break
        elif(user_choice == '2'):
            cave(weapon, option)
            break
        else:
            pass


def play_again():

    while True:
        choice = input("Would you like to play again? (y/n)")
        if (choice == 'y'):
            print_pause("Excellent! Restarting the game ...")
            play_game()
        elif(choice == 'n'):
            print_pause('Thanks For Playing!')
            break
        else:
            pass


def play_game():

    weapon = []

    option = random.choice(characters)

    intro(option)
    field(weapon, option)


play_game()
