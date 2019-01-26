#!/usr/bin/env python3
# the article submenu
import os
import sys

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
    print("TODO: check that article exists before attempting to open it")
    article_name = input("Enter the name of an article to edit: ")
    if (os.path.exists('projects/' + project_object.get_project() + '/article_json/' + article_name + '.json')):
        try:
            print("TODO: make versions for macOS and Linux, or just check for the OS (currently windows-only)")
            print("Hit enter when you are done.")
            windows_command = "notepad.exe " + "projects/" + project_object.get_project() + '/article_json/' + article_name + '.json'
            os.system(windows_command)
        except IOError:
            print("Error: failed to open " + "projects/" + project_object.get_project() + '/article_json/' + article_name + '.json')
            sys.exit()
    else:
        print("Error: invalid article name.")
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
