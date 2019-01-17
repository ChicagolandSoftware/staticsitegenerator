# Alan's Static Site Generator
# Generates static websites in the projects subfolder
# You are supposed to use git in the project folder
# And your repo should be called yourname.github.io
# Then it will make a GitHub Pages website with that.
# For more documentation, see the repo:
# https://github.com/0x416c616e/staticsitegenerator
#!/usr/bin/env python3
import time
import os
import sys
import json

# count.txt just has the number of all the articles
# articles.txt file to keep track of all the article names, which correspond
# to the filenames, which should be used with the find-and-replace stuff
# loop through all the


def main():
    # TO-DO: if command line argument is passed to generator,
    # it should open that project
    # be sure to check if len(sys.argv) > 1:
    # because that means the user passed in an argument
    # I should make it so people can use it like this:
    # ./generator.py -o some_existing_project
    # or ./generator.py --open some_existing_project
    # ./generator.py -n some_new_project
    # ./generator.py --new some_new_project
    # need to use regular expressions for checking argv
    # and also just for the project name stuff, and other
    # general user input

    # I should make multiple classes: one project class,
    # and each project class object has multiple other classes
    # one about_page class, multiple article classes, and some
    # other properties, like social media links and the site name etc
    # use json
    print("Please do NOT quit by closing the window or hitting ctrl+c.")
    time.sleep(2)
    print("You can cause problems by quitting abruptly without finishing things.")
    time.sleep(2)
    print("Only quit with the quit command.")
    time.sleep(5)
    print("Here's what you can do with Alan's Static Site Generator:")
    print("1. Open an existing project")
    print("2. Create a new project")
    # the initial menu, whether you want to open an existing project or create a new one
    # but in either case, you are specifying the project to use
    # for the further steps
    menu_choice = input("Type a number to do something, or type quit to quit: ")
    proceed = False
    while menu_choice != 'quit' and not proceed:
        if menu_choice == str(1):
            existing_project_name = input("Enter the project name to open: ")
            print("STUB: check if the folder exists, and if not, then loop and try again")
            print("STUB: check that the project name is not blank")
            print("Opening existing project called " + existing_project_name + ".")
            proceed = True
        elif menu_choice == str(2):
            new_project_name = input("Enter a name for the new project: ")
            print("STUB: check that the project name is not blank")
            print("STUB: check that the project does not already exist (don't want to overwrite)")
            print("Creating a new project called " + new_project_name + " in the projects folder.")
            print("STUB: create the files and folders for the new project")
            print("STUB: get the username, about text, website title, email, twitter, and github from the user")
            proceed = True
        else:
            print("Invalid choice. Try again.")
            menu_choice = input("Type a number to do something, or type quit to quit: ")
    if not proceed:
        print("Goodbye.")
    else:
        # proceeding with the projects menus
        print("MAIN PROJECT MENU")
        print("Here are your choices: ")
        print("1. ")
        second_menu_choice = input("Type a number to do something, or type quit to quit: ")
        while second_menu_choice != 'quit':
            print("this is not finished yet")
            if second_menu_choice == str(1):
                print("first menu choice")
            elif second_menu_choice == str(2):
                print("second menu choice")
            else:
                print("Invalid choice. Try again.")
            second_menu_choice = input("Type a number to do something, or type quit to quit: ")
        print("Goodbye.")
    # misc note: import os and os.walk() seem useful
    # might be related to what I need to do
    # also os.mkdir() and os.getcwd()


if __name__ == '__main__':
    main()

