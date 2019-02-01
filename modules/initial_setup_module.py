import json
import sys
from modules import project_class
# the initial setup module, used for getting basic info about the project
# then writing it to json
# stuff to do at first:
# get input for settings.json and about.json
# THE FUNCTION HANDLERS SHOULD DO TRY/EXCEPT


# setup check is run every time an article is finished
# if the setup has not been finished, it needs to be done
# check finished_initial_setup.txt, read string and convert to boolean
# return the boolean stored in the text file
def check_if_setup_has_been_completed(project_name):
    try:
        with open('projects/' + project_name + '/settings/finished_initial_setup.txt') as setup_file:
            finished_bool = setup_file.readline()
            return eval(finished_bool)  # string to bool, True = finished the setup already, False = never done setup
    except IOError:
        print("Error: failed initialization check")
        sys.exit()


# get the input for the settings values to be stored in settings.json
# return a dictionary
def get_settings_input(project_name):
    settings_dictionary = {}  # this dictionary corresponds with settings.json
    print("Initializing new project " + project_name + ". You can always change these settings later if need be.")
    settings_dictionary['github_link'] = input("Enter a GitHub account name or hit enter to leave blank (optional): ")
    settings_dictionary['twitter_link'] = input("Enter a Twitter account or hit enter to leave blank (optional): ")
    settings_dictionary['email_link'] = input("Enter an email address or hit enter to leave blank (optional): ")
    settings_dictionary['website_title'] = input("Enter a website title (mandatory): ")
    while settings_dictionary['website_title'] == "":
        print("Error: website title cannot be blank. Try again.")
        settings_dictionary['website_title'] = input("Enter a website title (mandatory): ")
    settings_dictionary['logo_filename'] = input("Enter a custom logo file name or leave blank for default (optional): ")
    if settings_dictionary['logo_filename'] == "":
        settings_dictionary['logo_filename'] = "logo.png"

    return settings_dictionary


# get the input for the about values to be stored in about.json
# return a dictionary
def get_about_input():
    about_dictionary = {}
    about_dictionary['about_text'] = input("Enter a description for your site for the \'about\' page: ")
    temp_project_object = project_class.ProjectClass("example")
    temp_project_object.clear_terminal()
    return about_dictionary


# take project name and settings dictionary args
# write the values to the proper key-value pairs in settings.json
# return True if it worked, or False if it failed
def write_settings_json(project_name, settings_dictionary):
    try:
        with open('projects/' + project_name + '/settings/settings.json', 'w') as json_file:
            json.dump(settings_dictionary, json_file)
    except IOError:
        print("Error: failed to write to settings.json")
        sys.exit()


# take project name and settings dictionary args
# write the values to the proper key-value pairs in settings.json
# return True if it worked, or False if it failed
def write_about_json(project_name, about_dictionary):
    try:
        with open('projects/' + project_name + '/settings/about.json', 'w') as json_file:
            json.dump(about_dictionary, json_file)
    except IOError:
        print("Error: failed to write to about.json")
        sys.exit()


# overwrite (not append) finished_initial_setup.txt with "True"
# return True if it worked, or False if it failed
def mark_setup_as_complete(project_name):
    try:
        file_reading = open('projects/' + project_name + '/settings/finished_initial_setup.txt', 'r')
        lines_from_file = file_reading.readlines()
        file_reading.close()  # gets all of the contents out and then saves as blank file to remove previous contents
        with open('projects/' + project_name + '/settings/finished_initial_setup.txt', 'w') as write_file:
            write_file.write('True')
    except IOError:
        print("Error: failed to mark setup as complete, might cause project issues")
        sys.exit()
