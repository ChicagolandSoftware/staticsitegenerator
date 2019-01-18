# Alan's Static Site Generator
# Generates static websites in the projects subfolder
# copy the contents of your project's website_files folder to
# your /var/www (or equivalent)
# or git init in the website_files folder for GitHub Pages
# For more documentation, see the repo:
# https://github.com/0x416c616e/staticsitegenerator
#!/usr/bin/env python3
import time
import os
import sys
import json

working_project = ""  # the project that is open

# main program entry point
def main():
    args_provided = has_command_line_args()
    fast_mode = True # turn this off later, the text prompt is useful for new users but annoying for
                     # me as the developer because it makes running the program take longer
    # what it does at first depends on if there are any cli args/options or not
    # no args = text menu prompts telling you what you can do, more beginner-friendly
    # cli args = faster but for more advanced users
    if args_provided:
        print("handle the command line arguments here, at least for opening or making a new project")
        # opening by cli args i.e. python generator.py --open some_project
        if ((sys.argv[1] == "--open") or (sys.argv[1] == "-o")) and (len(sys.argv) == 3):
            arg_name = sys.argv[2] # name of project provided as an argument
            print("you are trying to open an existing project with name: " + arg_name)
            open_project(arg_name)
        # making a new project via cli args .e. python generator.py --new new_project
        elif ((sys.argv[1] == "--new") or (sys.argv[1] == "-n")) and (len(sys.argv) == 3):
            arg_name = sys.argv[2]
            print("you are trying to create a new project with name: " + arg_name)
            create_project(arg_name)
        else:
            print("add more elifs in the future for different command line args")
            print("if you got here it means you provided invalid command line args")
            print("sys.argv[1]: " + str(sys.argv[1]))
            print("sys.argv[2]: " + str(sys.argv[2]))
            print("length of sys.argv:" + str(len(sys.argv)))
            sys.exit()
    # end of cli args stuff

    # beginning of program entry for no when generator.py is run with no arguments
    if not fast_mode:
        beginning_prompt()  # simple text notice
    # MAIN START
    menu_check_thing(args_provided)


# just gives info to the user, sleeps to make them look at it longer
def beginning_prompt():
    print("Please do NOT quit by closing the window or hitting ctrl+c.")
    time.sleep(2)
    print("You can cause problems by quitting abruptly without finishing things.")
    time.sleep(2)
    print("Only quit with the quit command.")
    time.sleep(5)

# attempt to open a project, but checks if it's valid first
def open_project(project_name):
    print("not finished yet")
    # just check that the project is valid, then eventually proceed to main_project_menu
    proceed = True
    working_project = project_name

# attempt to create a project, check if name is valid and not in use
def create_project(project_name):
    print("not finished yet")
    # make new project by copying from template project folder, then proceed to main_project_menu
    proceed = True
    working_project = project_name

# check if program is being run with command line args
def has_command_line_args():
    if len(sys.argv) > 1:
        return True

# the bulk of the program's options
# in the future I want to replace this function with a GUI
# be sure to make things modular in here so I can hook them up to
# GUI button event handlers instead of the input() and if/while loops
def menu_check_thing(args_provided):
    menu_choice = ""
    if not args_provided:
        print("this is the menu you get when you didn't provide any extra command line args")
        print("Here's what you can do with Alan's Static Site Generator:")
        print("1. Open an existing project")
        print("2. Create a new project")
        menu_choice = input("Type a number to do something, or type quit to quit: ")

    proceed = args_provided # whether to skip the file open or creation
    # proceed means to skip the process of selecting whether to open a project or make a new one
    # if you did the command line args then you already opened something

    while menu_choice != 'quit' and not proceed: # if args were provided then this does not happen
        if menu_choice == str(1):
            project_name = input("Enter the project name to open: ")
            print("STUB: check if the folder exists, and if not, then loop and try again")
            print("STUB: check that the project name is not blank")
            print("Opening existing project called " + project_name + ".")
            open_project(project_name)
            proceed = True
        elif menu_choice == str(2):
            project_name = input("Enter a name for the new project: ")
            print("STUB: check that the project name is not blank")
            print("STUB: check that the project does not already exist (don't want to overwrite)")
            print("Creating a new project called " + project_name + " in the projects folder.")
            print("STUB: create the files and folders for the new project")
            print("STUB: get the username, about text, website title, email, twitter, and github from the user")
            create_project(project_name)
            proceed = True
        else:
            print("Invalid choice. Try again.")
            print("Here's what you can do with Alan's Static Site Generator:")
            print("1. Open an existing project")
            print("2. Create a new project")
            menu_choice = input("Type a number to do something, or type quit to quit: ")
    if not proceed:
        print("Goodbye.")
    else:
        # proceeding with the projects menus
        main_project_menu(working_project)


# you only get here after a project is open
# if a new project is created, it is opened
def main_project_menu(project_name):
    print("MAIN PROJECT MENU with open project " + project_name)
    print("Here are your choices: ")
    print("1. articles")
    print("2. work on this, it's not done")
    second_menu_choice = input("Type a number to do something, or type quit to quit: ")
    while second_menu_choice != 'quit':
        print("this is not finished yet")
        if second_menu_choice == str(1):
            print("first menu choice")
        elif second_menu_choice == str(2):
            print("second menu choice")
        else:
            print("Invalid choice. Try again.")
            print("MAIN PROJECT MENU with open project " + project_name)
            print("Here are your choices: ")
            print("1. articles")
            print("2. work on this, it's not done")
        second_menu_choice = input("Type a number to do something, or type quit to quit: ")
    print("Goodbye.")


if __name__ == '__main__':
    main()

