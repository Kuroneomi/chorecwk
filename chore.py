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
def main() :
#define variables
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
#if about execute
    if chore_list == about:
      print("This program helps chore management.")
      continue
#if create execute
    elif chore_list == create_household:
      print("CREATING TO COMPLETE.")
      continue
#if view execute
    elif chore_list == view_household:
      print("VIEW TO COMPLETE.")
      continue
#if log done execute
    elif chore_list == log_chores_done:
      print("In progress please choose another option.")
      continue
#if leaderboard execute
    elif chore_list == show_leaderboard:
      print("In progress please choose another option.")
      continue
#if quit execute
    elif chore_list == quit:
      print("Exiting application")
      break
#if any other value tell user the error
    else:
      print("Incorrect Input.")
      continue

# Start the program
if __name__ == "__main__":
    main()
