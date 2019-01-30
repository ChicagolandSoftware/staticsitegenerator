#!/usr/bin/env python3
# the article submenu
import os
import sys
import platform
import json


def article_menu():
    print("1. Create an article")
    print("2. Read an article")
    print("3. Update an article")
    print("4. Delete an article")
    print("5. Show all article names")
    print("6. Return to main menu")


def create_article(project_object):
    project_object.clear_terminal()
    # 0: ask user for article name
    project_object.sub_prompt(project_object.get_project())
    print("Creating new article...")
    print("Although your article title can be something like Here's My Cool Article, your article url")
    print("needs to be something like heres_my_cool_article, with no spaces or special characters.")
    print("Uppercase, lowercase, numbers, and underscore only.")
    initial_article_url = input("Enter a url for the article: ")
    # 1: regex to see if article name is valid
    if project_object.validate_name(initial_article_url):
        # 2: check if article already exists
        if initial_article_url in open('projects/' + project_object.get_project() + '/settings/articles.txt').read():
            print("The article already exists! You will have to use a different name, or delete or rename the existing one.")
        else:
            print("do the remaining article stuff here")
            article_dictionary = {}
            # 3: prompt user to enter info for article
            #   - articles need the following:
            #       - title, author, date, first_sentence, body_text, lead_image, article_url
            article_dictionary['title'] = input("Enter a title for the article (can contain spaces and punctuation): ")
            article_dictionary['author'] = input("Enter an author for the article: ")
            article_dictionary['date'] = input("Enter a date for the article (DD/MM/YYYY): ")
            print("to-do: validate date input")
            article_dictionary['first_sentence'] = input("Enter the first sentence for the article: ")
            #           - body_text should be multi-line while loop, quit on quit/q
            #               - put <br> after every line gotten from user
            body_input = ""
            print("Enter the body text. It can be multiple lines.")
            print("To designate that you're finished with entering the body text, type quit or q on a separate line.")
            final_body_string = ""
            while body_input.lower() != 'quit' and body_input.lower() != 'q':
                body_input = input()
                if (body_input.lower() != 'quit') and (body_input.lower() != 'q'):
                    final_body_string += body_input
                    final_body_string += "<br>"
            print("Finished with body text input.")
            article_dictionary['body_text'] = final_body_string
            article_dictionary['lead_image'] = input("Enter a lead image (must be in the images folder of your project): ")
            article_dictionary['article_url'] = initial_article_url
            print(article_dictionary)
            # 4: convert to article_name.json in projects/project_name/article_json/article_name.json
            with open('projects/' + project_object.get_project() + '/article_json/' + initial_article_url + '.json', 'w') as article_file:
                json.dump(article_dictionary, article_file)
            # 5: put article_url in projects/project_name/settings/articles.txt
            with open('projects/' + project_object.get_project() + '/settings/articles.txt', 'a') as article_file:
                article_file.write("\n" + initial_article_url)
            # 6: read count.txt and then add 1 to it
            article_count = 0
            with open('projects/' + project_object.get_project() + '/settings/count.txt', 'r') as count_file:
                article_count = count_file.readline()
            article_count = int(article_count) + 1
            with open('projects/' + project_object.get_project() + '/settings/count.txt', 'w') as count_file:
                count_file.write(str(article_count))
            print("Finished making new article.")
    else:
        print("Invalid article name.")

    clear_and_prompt(project_object)


def read_article(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    reading_choice = input("Choose an article to read: ")
    file_path = 'projects/' + project_object.get_project() + '/article_json/' + reading_choice + '.json'
    if reading_choice in open('projects/' + project_object.get_project() + '/settings/articles.txt').read()\
            and os.path.isfile(file_path):
        json_dict = {}
        with open(file_path) as article_file:
            json_dict = json.load(article_file)

        print("Title: " + json_dict["title"])
        print("Author: " + json_dict["author"])
        print("Date: " + json_dict["date"])
        print("First sentence: " + json_dict["first_sentence"])
        print("Body text: " + json_dict["body_text"])
        print("Lead image: " + json_dict["lead_image"])
        print("Article URL: " + json_dict["article_url"])
    else:
        print("Error: unable to find article " + reading_choice)
    clear_and_prompt(project_object)


def update_article(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    article_name = input("Enter the name of an article to edit: ")
    if os.path.exists('projects/' + project_object.get_project() + '/article_json/' + article_name + '.json'):
        try:
            operating_system = platform.system()
            if operating_system == 'Windows':
                windows_command = "notepad.exe " + "projects/" + project_object.get_project() + '/article_json/' + article_name + '.json'
                os.system(windows_command)
            elif operating_system == 'Darwin':
                mac_command = "open -a TextEdit " + "projects/" + project_object.get_project() + '/article_json/' + article_name + '.json'
                os.system(mac_command)
            elif operating_system == 'Linux':
                linux_command = "gedit " + "projects/" + project_object.get_project() + '/article_json/' + article_name + '.json'
                os.system(linux_command)
            else:
                print("Unable to detect your OS.\nYou will have to manually edit projects/" +
                      project_object.get_project() + "/article_json/" + article_name + '.json')
        except IOError:
            print("Error: failed to open " + "projects/" + project_object.get_project() + '/article_json/' + article_name + '.json')
            sys.exit()
    else:
        print("Error: invalid article name.")
        input()
    clear_and_prompt(project_object)


def delete_article(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    print("Deleting an existing article NOT FINISHED")
    clear_and_prompt(project_object)


def show_all_articles(project_object):
    project_object.clear_terminal()
    project_object.sub_prompt(project_object.get_project())
    print("showing all articles NOT FINISHED")
    clear_and_prompt(project_object)


def return_to_main_menu():
    print("Returning to main menu.")


def clear_and_prompt(project_object):
    input("Press enter to continue.")
    project_object.clear_terminal()
    project_object.top_prompt(project_object.get_project())
