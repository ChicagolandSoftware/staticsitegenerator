# this should really be a singleton but I am lazy right now
# there is supposed to only be once ProjectClass instance for generator.py
# called project_object


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
            print("this is where you will make the new project based on project_name and templates")
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
        print("ProjectClass is not finished, but it needs to be able to validate " + project_name)
        passed_check = True # needs to be checked
        if (passed_check): # needs to be finished
            return True
        else: # if it failed validation
            return False