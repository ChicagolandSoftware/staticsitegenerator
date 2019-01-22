# this should really be a singleton but I am lazy right now
# there is supposed to only be once ProjectClass instance for generator.py

class ProjectClass:

    # constructor with default project
    def __init__(self, project_name="example"):
        if self.validate_name():
            self.project_name = project_name
        else:
            print("invalid project_name, sticking with example instead")

    def get_path(self):
        return 'projects/' + str(self.project_name)
    # note: the above might not be multi-platform-friendly
    # consider using os.path in the future instead

    def set_project(self, project_name):
        self.project_name = project_name

    def validate_name(self, project_name):
        print("this is not finished, but it needs to be able to validate " + project_name)
        passed_check = True # needs to be checked
        if (passed_check): # needs to be finished
            return True
        else: # if it failed validation
            return False

