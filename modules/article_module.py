#!/usr/bin/env python3
# the article submenu


def article_menu():
    print("1. Create an article")
    print("2. Read an article")
    print("3. Update an article")
    print("4. Delete an article")
    print("5. Show all article names")
    print("6. Return to main menu")


def create_article(project_object):
    project_object.clear_terminal()
    print("Creating a new article: " + project_object.get_project())
    clear_and_prompt(project_object)


def read_article(project_object):
    project_object.clear_terminal()
    print("Reading an existing article: " + project_object.get_project())
    clear_and_prompt(project_object)


def update_article(project_object):
    project_object.clear_terminal()
    print("Updating an existing article: " + project_object.get_project())
    clear_and_prompt(project_object)


def delete_article(project_object):
    project_object.clear_terminal()
    print("Deleting an existing article: " + project_object.get_project())
    clear_and_prompt(project_object)


def show_all_articles(project_object):
    print("showing all articles")
    clear_and_prompt(project_object)


def return_to_main_menu():
    print("returning to main menu")


def clear_and_prompt(project_object):
    input()
    project_object.clear_terminal()
    project_object.top_prompt(project_object.get_project())
