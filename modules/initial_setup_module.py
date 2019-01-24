import json
import sys
# the initial setup module, used for getting basic info about the project
# then writing it to json
print("this is my highest priority right now, as of 1/23/2019")
print("this will set up the project after it has been copied using shutil")
print("after successfully opening a file, then you need to call functions from the initial setup module")
print("but only if the projects/project_name/settings/finished_initial_setup.txt file says False")
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
            print('content: ' + finished_bool)
            return eval(finished_bool)  # string to bool, True = finished the setup already, False = never done the setup
    except IOError:
        print("Error: failed initialization check")
        sys.exit()


# get the input for the settings values to be stored in settings.json
# return a dictionary -- if it failed, return a blank dictionary
def get_settings_input(project_name):
    settings_dictionary = {} # this dictionary corresponds with settings.json
    print("TO-DO: regex/input validation/try/except")
    print("Initializing new project. You can always change these settings later if need be.")
    settings_dictionary['github_link'] = input("Enter a GitHub account name or hit enter to leave blank (optional): ")
    settings_dictionary['twitter_link'] = input("Enter a Twitter account or hit enter to leave blank (optional): ")
    settings_dictionary['email_link'] = input("Enter an email address or hit enter to leave blank (optional): ")
    settings_dictionary['website_title'] = input("Enter a website title (mandatory): ")
    settings_dictionary['logo_filename'] = input("Enter a custom logo file name or leave blank for default (optional): ")
    print("this is not finished yet")
    print(settings_dictionary)

# get the input for the about values to be stored in about.json
# return a dictionary -- if it failed, return a blank dictionary
def get_about_input(project_name):
    pass


# take project name and settings dictionary args
# write the values to the proper key-value pairs in settings.json
# return True if it worked, or False if it failed
def write_settings_json(project_name, settings_dictionary):
    pass


# take project name and settings dictionary args
# write the values to the proper key-value pairs in settings.json
# return True if it worked, or False if it failed
def write_about_json(project_name, about_dictionary):
    pass


# overwrite (not append) finished_initial_setup.txt with "True"
# return True if it worked, or False if it failed
def mark_setup_as_complete(project_name):
    pass
