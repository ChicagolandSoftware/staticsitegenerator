def project_menu():
    print("1. View project info")
    print("2. Rename project")
    print("3. Delete project")
    print("4. Open a different project")
    print("5. Regenerate static HTML pages")
    print("7. Return to main menu")
    print("THIS IS NOT COMPLETE")


def view_project_info(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    print("view project info goes here (stub)")


def rename_project(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    print("rename project goes here (stub)")


def delete_project(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    print("delete project goes here (stub)")


def open_a_different_project(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    print("open a different project goes here (stub)")


def regenerate(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    print("regenerate goes here (stub)")


def return_to_main_menu(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    print("Returning to main menu.")


def clear_and_prompt(project_object):
    input("Press enter to continue.")
    project_object.clear_terminal()
    project_object.top_prompt(project_object.get_project())