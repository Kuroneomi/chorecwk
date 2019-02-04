# Name: chores.py
#
# Description:
#
# This program prompts the user for two numbers and checks whether they match two
# randomly generated numbers.
#
# Author: Dan Thompson & Neomi
#
# Date: Feb 2019
#

def main():
#define variables for menu
    about = "a"
    create_household = "c"
    view_household = "v"
    log_chores_done = "l"
    show_leaderboard = "s"
    quit = "q"
#show user main menu
#input for chore list
    print("""Welcome to Chore Chart
        \n\tAbout \t\t\t(A)
        \tCreate Household \t(C)
        \tView Household \t\t(V)
        \tLog Chores Done \t(L)
        \tShow Leaderboard \t(S)
        \tQuit \t\t\t(Q)""")
    while True:
    chore_list = str(input("\n\tPlease choose an option and press <Enter>:"))
#if about show explanationof program
    if chore_list == about:
        print("""This program helps chore management,
        by logging the chores and who is tasked with a chore""")
        continue
#if create neomi to finish
    elif chore_list == create_household:
        print("CREATING TO COMPLETE.")
        continue
#if view neomi to finish
    elif chore_list == view_household:
        print("VIEW TO COMPLETE.")
        continue
#if log done tell user incomplete
    elif chore_list == log_chores_done:
        print("Section not complete please choose another option.")
        continue
#if leaderboard tell user incomplete
    elif chore_list == show_leaderboard:
        print("Section not complete please choose another option.")
        continue
#if quit exit program
    elif chore_list == quit:
        print("Exiting application")
        break
#if any other value tell user the error
    else:
        print("Incorrect Input. Please select an option fro mthe menu")
        continue


# Start the program
if __name__ == "__main__":
    main()
