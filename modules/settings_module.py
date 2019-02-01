def settings_menu():
    print("1. About page menu")
    print("2. Social media menu")
    print("3. Website title menu")
    print("4. Logo menu")
    print("5. Return to main menu")


def about_page_menu(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    print("about page menu goes here (stub)")


def social_media_menu(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    print("social media menu goes here (stub)")


def website_title_menu(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    print("website title menu goes here (stub)")


def logo_menu(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    print("logo menu goes here (stub)")


def return_to_main_menu(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    print("Returning to main menu.")


def clear_and_prompt(project_object):
    input("Press enter to continue.")
    project_object.clear_terminal()
    project_object.top_prompt(project_object.get_project())

