#!/usr/bin/env python3

# Alan's Static Site Generator
# Generates static websites in the projects subfolder
# copy the contents of your project's website_files folder to
# your /var/www (or equivalent)
# or git init in the website_files folder for GitHub Pages
# For more documentation, see the repo:
# https://github.com/0x416c616e/staticsitegenerator
import time
import os
import sys
import json


working_project = ""  # the project that is open

# main program entry point
def main():

    args_provided = has_command_line_args()
    print("args_provided:")
    print(args_provided)
    fast_mode = True  # turn this off later, the text prompt is useful for new users but annoying for
                      # me as the developer because it makes running the program take longer

    # what it does at first depends on if there are any cli args/options or not
    # no args = text menu prompts telling you what you can do, more beginner-friendly
    # cli args = faster but for more advanced users
    scoping_hotfix = ""  # bad workaround
    if args_provided:
        scoping_hotfix = arg_steps();
    # end of cli args stuff

    # beginning of program entry for no when generator.py is run with no arguments
    if not fast_mode:
        beginning_prompt()  # simple text notice
    # MAIN START
    print("REEEE right here scoping_hotfix is " + scoping_hotfix)
    menu_check_thing(args_provided, scoping_hotfix)


# just gives info to the user, sleeps to make them look at it longer
def beginning_prompt():
    print("Please do NOT quit by closing the window or hitting ctrl+c.")
    time.sleep(2)
    print("You can cause problems by quitting abruptly without finishing things.")
    time.sleep(2)
    print("Only quit with the quit command.")
    time.sleep(5)

def arg_steps():
    print("handle the command line arguments here, at least for opening or making a new project")
    # opening by cli args i.e. python generator.py --open some_project
    if ((sys.argv[1] == "--open") or (sys.argv[1] == "-o")) and (len(sys.argv) == 3):
        working_project = sys.argv[2]
        arg_name = sys.argv[2]  # name of project provided as an argument
        print("you are trying to open an existing project with name: " + arg_name)
        open_project(arg_name)
    # making a new project via cli args .e. python generator.py --new new_project
    elif ((sys.argv[1] == "--new") or (sys.argv[1] == "-n")) and (len(sys.argv) == 3):
        working_project = sys.argv[2]
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
    print("REEEEE working project is" + working_project)
    return working_project

# attempt to open a project, but checks if it's valid first
def open_project(project_name):
    # enter validity check here
    project_name_is_valid = True  # stub
    print("TODO: regex/input validation, store in project_name_is_valid")
    # just check that the project is valid, then eventually proceed to main_project_menu
    proceed = True
    working_project = project_name
    return project_name_is_valid

# attempt to create a project, check if name is valid and not in use
def create_project(project_name):
    # enter validity check here
    project_name_is_valid = True  # stub
    print("TODO: regex/input validation, store in project_name_is_valid")
    # make new project by copying from template project folder, then proceed to main_project_menu
    proceed = True
    working_project = project_name
    return project_name_is_valid


# check if program is being run with command line args
def has_command_line_args():
    if len(sys.argv) > 1:
        return True
    else:
        return False


# this is run before proceeding to the main_project_menu, which is
# where everything useful happens
# not gonna lie, this could be a lot cleaner, but it works
# in the future I want to replace this function with a GUI
# be sure to make things modular in here so I can hook them up to
# GUI button event handlers instead of the input() and if/while loops
def menu_check_thing(args_provided, current_working_project):
    print("current working project: " + current_working_project)
    # at this point, the project may or may not be set yet
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
    # kinda spaghetti-ish but whatever, it works

    while menu_choice != 'quit' and not proceed: # if args were provided then this does not happen
        if menu_choice == str(1):
            project_name = input("Enter the project name to open: ")
            print("Opening existing project called " + project_name + ".")
            project_success = open_project(project_name)  # returns whether it succeeded or not
            if not project_success:
                print("invalid project to open, try again")
            else:
                proceed = True
        elif menu_choice == str(2):
            project_name = input("Enter a name for the new project: ")
            print("Creating a new project called " + project_name + " in the projects folder.")
            print("STUB: create the files and folders for the new project")
            print("STUB: get the username, about text, website title, email, twitter, and github from the user")
            project_success = create_project(project_name)  # returns whether it succeeded or not
            if not project_success:
                print("invalid project name, try again")
            else:
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
        if not args_provided:
            main_project_menu(project_name)
        elif args_provided:
            main_project_menu(working_project)
        else:
            print("what happened?")

# you only get here after a project is open
# if a new project is created, it is opened
def main_project_menu(project_name):
    working_project = project_name

    print("MAIN PROJECT MENU with open project " + project_name)
    print("Here are your choices: ")
    print("1. article menu")
    print("2. work on this, it's not done")
    print("DEBUG: value of project_name is " + project_name)
    print("DEBUG: value of working_project is " + working_project)
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
            print("copy the entire numbered menu here again")
        second_menu_choice = input("Type a number to do something, or type quit to quit: ")
    print("Goodbye.")


if __name__ == '__main__':
    main()

