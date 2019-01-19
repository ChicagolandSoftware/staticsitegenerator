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
    # I really should have used argparse instead of my bad DIY method of handling sys.argv stuff
    args_provided = has_command_line_args()
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


# this is run before proceeding to the main_project_menu
def menu_check_thing(args_provided, current_working_project):
    # at this point, the project may or may not be set yet
    menu_choice = ""
    if not args_provided:
        print("Options menu:")
        print("1. Open an existing project")
        print("2. Create a new project")
        menu_choice = input("Type a number or the word quit followed by enter: ")
    else:  # if args were provided
        print("do something about current_working_project here maybe")
    proceed = args_provided # whether to skip the file open or creation
    # proceed means to skip the process of selecting whether to open a project or make a new one
    # if you did the command line args then you already opened something

    while menu_choice != 'quit' and not proceed:  # if args were provided then this does not happen
        if menu_choice == str(1):
            project_name = input("Enter the project name to open: ")
            print("Opening existing project called " + project_name + ".")
            project_success = open_project(project_name)  # returns whether it succeeded or not
            if not project_success:
                print("Invalid project to open, try again.")
            else:
                proceed = True
        elif menu_choice == str(2):
            project_name = input("Enter a name for the new project: ")
            print("Creating a new project called " + project_name + " in the projects folder.")
            # print("STUB: create the files and folders for the new project")
            # print("STUB: get the username, about text, website title, email, twitter, and github from the user")
            project_success = create_project(project_name)  # returns whether it succeeded or not
            if not project_success:
                print("Invalid project name, try again.")
            else:
                proceed = True
        else:
            print("Invalid choice. Try again.")
            print("Options menu:")
            print("1. Open an existing project")
            print("2. Create a new project")
            menu_choice = input("Type a number or the word quit followed by enter: ")
    if not proceed:
        print("Goodbye.")
    else:
        if not args_provided:
            main_project_menu(project_name, current_working_project)
        elif args_provided:
            main_project_menu(working_project, current_working_project)
        else:
            print("what happened?")

# you only get here after a project is open
# if a new project is created, it is opened
def main_project_menu(project_name, REAL_working_project):
    ACTUAL_project_name = ""
    if REAL_working_project == "":
        ACTUAL_project_name = project_name
    else:
        ACTUAL_project_name = REAL_working_project

    print_numbered_menu("second", ACTUAL_project_name)
    second_menu_choice = input("Type a number or the word quit followed by enter: ")
    while second_menu_choice != 'quit':
        if second_menu_choice == str(1):
            print_numbered_menu("article", ACTUAL_project_name)
        elif second_menu_choice == str(2):
            print_numbered_menu("settings", ACTUAL_project_name)
        elif second_menu_choice == str(3):
            print_numbered_menu("project", ACTUAL_project_name)
        else:
            print("Invalid choice. Try again.")
            print_numbered_menu("second", ACTUAL_project_name)
        print_numbered_menu("second", ACTUAL_project_name)
        second_menu_choice = input("Type a number to do something, or type quit to quit: ")


    print("Goodbye.")


def print_numbered_menu(menu, proj):
    clear_terminal()
    print("Working with open project " + proj)
    print("Options menu: ")
    # second nested menu
    if menu == "second":
        print("1. Article menu")
        print("2. Settings menu")
        print("3. Project menu")
    # third menu
    elif menu == "article":
        article_menu()
    elif menu == "settings":
        settings_menu()
    elif menu == "project":
        project_menu()
    else:
        print("Invalid choice. Try again.")


def article_menu():
    print("1. Create an article")
    print("2. Read an article")
    print("3. Update an article")
    print("4. Delete an article")
    print("5. Show all article names")
    print("6. Return to main menu")
    print("THIS IS NOT COMPLETE")
    print("USE A MODULE FOR THE ARTICLE FUNCTIONS")
    input()  # get rid of this later, this is only a placeholder to stop it from proceeding immediately

def settings_menu():
    print("1. About page menu")
    print("2. Social media menu")
    print("3. Website title menu")
    print("4. Logo menu")
    print("5. Return to main menu")
    print("THIS IS NOT COMPLETE")
    print("USE A MODULE FOR THE SETTINGS FUNCTIONS")
    input()  # get rid of this later, this is only a placeholder to stop it from proceeding immediately

def project_menu():
    print("1. View project info")
    print("2. Rename project")
    print("3. Delete project")
    print("4. Open a different project")
    print("5. Regenerate static HTML pages")
    print("7. Return to main menu")
    print("THIS IS NOT COMPLETE")
    print("USE A MODULE FOR THE SETTINGS FUNCTIONS")
    input()  # get rid of this later, this is only a placeholder to stop it from proceeding immediately

def clear_terminal():
    if os.name == "nt":  # windows
        os.system("cls")
    else:
        os.system("clear")

if __name__ == '__main__':
    main()

