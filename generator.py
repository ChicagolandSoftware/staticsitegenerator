#!/usr/bin/env python3
# Alan's Static Site Generator
# https://github.com/0x416c616e/staticsitegenerator
import time
import os
import sys
# submenus, basically subprograms of their own, are structured as modules to break up the program into multiple files
# instead of a massive main()
from modules import initial_setup_module
from modules import article_module
from modules import settings_module
from modules import project_module
from modules import project_class
# from modules import regeneration_module.py # not here yet


working_project = ""  # the project that is open

project_object = project_class.ProjectClass("example")


# "driver" of the program, uses other classes and modules
def main():
    # the object for setting/getting project name etc.

    # I really should have used argparse instead of my bad DIY method of handling sys.argv stuff
    args_provided = has_command_line_args()
    fast_mode = True  # turn on for dev, turn off for users

    # run program with no args = text menu prompts telling you what you can do, more beginner-friendly
    # run program with cli args = faster but for more advanced users
    scoping_hotfix = ""  # bad workaround
    if args_provided:
        if len(sys.argv) == 2:
            print("Error: invalid command line arguments.")
            print("Examples of proper usage: ")
            print("python3 generator.py --open project_that_exists")
            print("python3 generator.py --new some_new_project")
            sys.exit()
        else:
            scoping_hotfix = arg_steps()
    # end of cli args stuff
    # beginning of program entry for no when generator.py is run with no arguments
    if not fast_mode:
        beginning_prompt()  # simple text notice
    # MAIN PROGRAM START
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
    # opening by cli args i.e. python generator.py --open some_existing_project
    if ((sys.argv[1] == "--open") or (sys.argv[1] == "-o")) and (len(sys.argv) == 3):
        working_project = sys.argv[2]
        arg_name = sys.argv[2]  # name of project provided as an argument
        # print("you are trying to open an existing project with name: " + arg_name)
        opened_successfully = open_project(arg_name)
        if not opened_successfully:
            print("Failed to open project with specified project_name")
            sys.exit()
        else:
            pass

    # making a new project via cli args i.e. python generator.py --new new_project_name
    elif ((sys.argv[1] == "--new") or (sys.argv[1] == "-n")) and (len(sys.argv) == 3):
        working_project = sys.argv[2]
        arg_name = sys.argv[2]
        create_project(arg_name)
    else:
        print("if you got here it means you provided invalid command line args")
        print("sys.argv[1]: " + str(sys.argv[1]))
        print("sys.argv[2]: " + str(sys.argv[2]))
        print("length of sys.argv:" + str(len(sys.argv)))
        sys.exit()
    return working_project


# attempt to open a project, but checks if it's valid first
def open_project(project_name):
    open_attempt = project_object.validate_name(project_name)
    if not open_attempt and len(sys.argv) == 3:
        project_object.say_guidelines()
        sys.exit()
    elif not open_attempt:
        print("Error with provided arguments")
        return False
    else:
        if project_object.prevent_opening_nonexistent_project(project_name):
            return True
        else:
            return False


# attempt to create a project, check if name is valid and not in use
def create_project(project_name):
    # the lines before the return statement are garbage, maybe I can delete without messing up anything?
    project_name_is_valid = True  # stub
    # make new project by copying from template project folder, then proceed to main_project_menu
    proceed = True
    working_project = project_name
    # the above is stuff in create_project() is cruft from a previous version before I refactored but it might be important?
    if project_object.validate_name(project_name):
        return project_object.make_new_project(project_name)
    else:
        project_object.say_guidelines()
        sys.exit()


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
    project_object.clear_terminal()
    if not args_provided:
        print("Options menu:")
        print("1. Open an existing project")
        print("2. Create a new project")
        menu_choice = input("Type a number or the word quit followed by enter: ")
    else:  # if args were provided
        # print("do something about current_working_project here maybe")
        pass
    proceed = args_provided # whether to skip the file open or creation
    # proceed means to skip the process of selecting whether to open a project or make a new one
    # if you did the command line args then you already opened something

    while (menu_choice != 'quit') and (menu_choice != 'q') and (not proceed):  # if args were provided then this does not happen
        if menu_choice == str(1):
            project_name = input("Enter the project name to open or type quit: ")
            if project_name == 'q' or project_name == 'quit':
                print("Goodbye.")
                sys.exit()
            print("Opening existing project called " + project_name + ".")
            project_success = open_project(project_name)  # returns whether it succeeded or not
            if not project_success:
                print("Invalid project to open, try again.")
            else:
                proceed = True
        elif menu_choice == str(2):
            project_name = input("Enter a name for the new project: ")
            # print("STUB: create the files and folders for the new project")
            # print("STUB: get the username, about text, website title, email, twitter, and github from the user")
            project_success = create_project(project_name)  # returns whether it succeeded or not
            if not project_success:
                print("Invalid project name, try again.")
            else:
                print("Created a new project called " + project_name + " in the projects folder.")
                proceed = True
        elif menu_choice == 'q' or menu_choice == 'quit':
            print("Goodbye.")
            sys.exit()
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

    project_object.set_project(ACTUAL_project_name)


    print_numbered_menu("second", ACTUAL_project_name)
    second_menu_choice = input("Type a number or the word quit followed by enter: ")
    while second_menu_choice != 'quit' and second_menu_choice != 'q':
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
    input("Hit enter to continue.")
    project_object.clear_terminal()
    if initial_setup_module.check_if_setup_has_been_completed(proj):
        # print("you have already completed the initial setup")
        pass
    else:
        # do the initial setup
        settings_dictionary = initial_setup_module.get_settings_input(proj)
        about_dictionary = initial_setup_module.get_about_input()
        initial_setup_module.write_settings_json(proj, settings_dictionary)
        initial_setup_module.write_about_json(proj, about_dictionary)
        # setup has been completed
        initial_setup_module.mark_setup_as_complete(proj)

    project_object.top_prompt(proj)
    # second nested menu
    if menu == "second":
        print("1. Article menu")
        print("2. Settings menu")
        print("3. Project menu")
    # third menu
    elif menu == "article":
        article_module.article_menu()
        article_menu_choice = input("Type a number to do something, or type quit to quit: ")
        if (article_menu_choice.lower() == 'quit') or (article_menu_choice.lower() == 'q'):
            print("Goodbye. ")
            sys.exit()
        else:
            while article_menu_choice != str(6):
                project_object.clear_terminal()
                project_object.top_prompt(project_object.get_project())
                if article_menu_choice == str(1):
                    article_module.create_article(project_object)
                elif article_menu_choice == str(2):
                    article_module.read_article(project_object)
                elif article_menu_choice == str(3):
                    article_module.update_article(project_object)
                elif article_menu_choice == str(4):
                    article_module.delete_article(project_object)
                elif article_menu_choice == str(5):
                    article_module.show_all_articles(project_object)
                else:
                    print("Invalid choice. Try again.")
                    input("Hit enter to continue.")
                    project_object.clear_terminal()
                    project_object.top_prompt(project_object.get_project())
                article_module.article_menu()
                article_menu_choice = input("Type a number to do something, or type quit to quit: ")
                if (article_menu_choice.lower() == 'quit') or (article_menu_choice.lower() == 'q'):
                    print("Goodbye. ")
                    sys.exit()
    elif menu == "settings":
        settings_module.settings_menu()
        print("AAAAAAAAAAAAA")
        settings_menu_choice = input("Type a number to do something, or type quit to quit: ")
        if (settings_menu_choice.lower() == 'quit') or (settings_menu_choice.lower() == 'q'):
            print("Goodbye. ")
            sys.exit()
        else:
            print("this is where the numbered stuff goes")
            while settings_menu_choice != str(5):
                project_object.clear_terminal()
                project_object.top_prompt(project_object.get_project())
                if settings_menu_choice == str(1):
                    settings_module.about_page_menu(project_object)
                elif settings_menu_choice == str(2):
                    settings_module.social_media_menu(project_object)
                elif settings_menu_choice == str(3):
                    settings_module.website_title_menu(project_object)
                elif settings_menu_choice == str(4):
                    settings_module.logo_menu(project_object)
                else:
                    print("Invalid choice. Try again.")
                    input("Hit enter to continue.")
                    project_object.clear_terminal()
                    project_object.top_prompt(project_object.get_project())
                settings_module.settings_menu()
                settings_menu_choice = input("Type a number to do something, or type quit to quit: ")
                if (settings_menu_choice.lower() == 'quit') or (settings_menu_choice.lower() == 'q'):
                    print("Goodbye. ")
                    sys.exit()
    elif menu == "project":
        project_module.project_menu()
        input("this is my input() equivalent to a breakpoint")
    else:
        print("Invalid choice. Try again.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nQuitting. Goodbye.")
        sys.exit()
