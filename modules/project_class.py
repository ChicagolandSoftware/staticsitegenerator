# this should really be a singleton but I am lazy right now
# there is supposed to only be once ProjectClass instance for generator.py
# called project_object

import re # regular expression
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

    def make_new_project(self, project_name):
        if self.validate_name(project_name):
            return True
        else:
            print("invalid project_name, unable to make new project")
            return False

    def check_for_existing_project(self, project_name):
        if self.validate_name(project_name):
            print("name is valid, but now need to check if it already exists")
            if (True): # if it was successfull, this is a placeholder
                return True
            else:
                return False
        else:
            print("invalid project_name, unable to check for project")

    def validate_name(self, project_name):
        print("Project name guidelines: A-Z, a-z, 0-9, and - or _ ONLY. 2-32 chars.")
        # later: maybe put example back into the list of unallowed words
        unallowed_words = {'quit', 'template', 'testing', 'test', '-o', '-n',
                           '--open', '--new', 'python', 'python3', '', 'modules', 'projects',
                           'article_json', 'css', 'images', 'html_page_templates', 'page_json',
                           'schemas', 'settings', 'website_files', 'InputFiles', 'OutputFiles',
                           'venv'}
        print("ProjectClass is not finished, but it needs to be able to validate " + project_name)
        if project_name not in unallowed_words:
            print("this is where you will make the new project based on project_name and templates")
            # re.findall(, project_name)

            return True
        else:
            print("project_name is invalid, try again with proper characters and length, and avoid reserved words")
            return False