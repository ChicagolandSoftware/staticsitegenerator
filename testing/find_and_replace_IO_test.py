#!/usr/bin/env python3
print("read example_article.json and do find-and-replace stuff for the top article in testing_ground.html")
# see github issues
# this simple test will only replace the contents of the 5th article stuff in testing_ground.html
# with the json values from example_article.json
# things to replace: 5TH_ARTICLE_TITLE,



# =============================


# first part of test: going'
# along with the video about find and replace
import os
import json
text_to_find = {
  "title": "5TH_ARTICLE_TITLE",
  "author": "ARTICLE_AUTHOR",
  "date": "5TH_ARTICLE_DATE",
  "first_sentence": "5TH_ARTICLE_1ST_PARAGRAPH",
  "lead_image": "5TH_ARTICLE_IMAGE",
  "article_url": "5TH_ARTICLE_URL"
}

# the real version will have the body_text as well, but this is a quick mockup
# so far, this doesn't do what I want it to. It should actually parse JSON
# instead of getting the input from the user.
# The article and pagination regeneration module will be separate from the article stuff
# the article module will get the input and store it as json
# this is demonstrating the regeneration stuff though

text_to_replace = {}
text_to_replace['title'] = input('Enter the article title: ')
text_to_replace['author'] = input('Enter the author name: ')
text_to_replace['date'] = input('Enter the date: ')
text_to_replace['first_sentence'] = input('Enter the first sentence of the article: ')
text_to_replace['lead_image'] = input('Enter the filename for the lead image (must be put in the images folder): ')
text_to_replace['article_url'] = input('Enter the article url: ')

sourcepath = os.listdir('InputFiles/')


for file in sourcepath:
    inputfile = 'InputFiles/' + file
    print('Conversion ins ongoing for ' + inputfile)
    with open(inputfile,'r') as inputfile:
        filedata = inputfile.read()
        destinationpath = 'OutputFiles/' + file
        for key in text_to_replace.keys():
            freq = 0
            freq = filedata.count(key)
            filedata = filedata.replace(text_to_find[key], text_to_replace[key])
            with open (destinationpath,'w') as file:
                file.write(filedata)
            #print('Total %d Records Replaced for %' %freq %key)

# =============================
