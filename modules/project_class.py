# this should really be a singleton but I am lazy right now
# there is supposed to only be once ProjectClass instance for generator.py
# called project_object

import re # regular expression
import os
import sys
class ProjectClass:

    # constructor with default project
    def __init__(self, project_name="example"):
        if self.validate_name(project_name):
            self.project_name = project_name
        else:
            print("invalid project_name, sticking with example instead")

    def get_path(self):
        return 'projects/' + str(self.project_name)
    # note: the above might not be multi-platform-friendly
    # consider using os.path in the future instead

    def set_project(self, project_name):
        self.project_name = project_name

    # CURRENT TO-DO
    def make_new_project(self, project_name):
        if self.validate_name(project_name):
            # I pass the arg because it helps me remember what it's doing
            print("process of making new project goes here")
            # need to check if directory already exists, in which case, don't proceed
            project_exists = os.path.isdir("projects/" + project_name)  # boolean
            # if it doesn't exist, then make a new project
            if project_exists:
                print("Error: project already exists.")
                sys.exit()
                return False
            else:
                print("That project does not exist yet. Proceeding (unfinished)")
                return True
            # testing: use os.path to get current working directory (cwd)
            # make a new directory within (? not entirely sure of path tbh) ../projects with name _project_name
            # copy contents of ../template and all its files and subdirs to the newly-created projects/project_name directory
            # then the user needs to do the initial setup ASAP
            # but there need to be default values just in case the user hits ctrl+c or something before completing
            # or set a text file with a boolean in it to say whether or not the setup module was completed
            # this class needs to import inital_setup_module.py
            # I also need to finish doing all the JSON stuff, at least for dummy stuff and structure
            # don't worry about schemas and validation just yet


            return True
        else:
            print("invalid project_name, unable to make new project")
            return False

    def check_for_existing_project(self, project_name):
        if self.validate_name(project_name):
            print("name is valid, but now need to check if it already exists")
            if (True):
                return True
            else:
                return False
        else:
            print("invalid project_name, unable to check for project check_for_existing_project")

    def say_guidelines(self):
        print("project_name is invalid, try again with proper characters and length, and avoid reserved words")
        print("Project name guidelines: A-Z, a-z, 0-9, and - ONLY. 2-32 chars.")

    def validate_name(self, project_name):
        unallowed_words = {'quit', 'template', 'testing', 'test', '-o', '-n',
                           '--open', '--new', 'python', 'python3', '', 'modules', 'projects',
                           'article_json', 'css', 'images', 'html_page_templates', 'page_json',
                           'schemas', 'settings', 'default', 'website_files', 'InputFiles', 'OutputFiles',
                           'venv'}
        if project_name not in unallowed_words:
            re_string = re.findall('[a-zA-Z0-9_]', project_name)
            if (len(re_string) != len(project_name)) or len(project_name) < 2 or len(project_name) > 32:
                return False
            else:
                return True
        else:
            self.say_guidelines()
            return False


