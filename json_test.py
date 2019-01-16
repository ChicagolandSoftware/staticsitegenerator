# TO-DO: TEST GETTING USER INPUT AND THEN STORING AS A DICTIONARY,
# AND THEN WRITE AS JSON TO A FILE
# AND THEN CLOSE THE FILE
# THEN OPEN THE FILE AND READ FROM THE JSON, AND THEN FIND AND REPLACE
# TEXT WITHIN THE testing_ground.html FILE.
# IT'S OKAY TO MESS WITH THE TESTING FILE BECAUSE IT'S JUST A COPY
# OF THE 5_ARTICLES.HTML FILE, OR THE INDEX.HTML FILE
# THE POINT OF THIS FILE IS TO GET EXPERIENCE WITH JSON
# AND IT'S LIKE A MOCKUP OF WHAT I WANT TO ADD TO GENERATORY.PY
# CAPS LOCK TO GET MY ATTENTION LATER SO I DON'T FORGET IT


# first section of this file: writing JSON
book = {}
book['alan'] = {
    'name': 'alan',
    'address': '123 red street',
    'phone': 789789789
}
book['alice'] = {
    'name': 'alice',
    'address': '456 blue street',
    'phone': 123123123
}
import json
some_string = json.dumps(book)
print(some_string)
with open("c://data/book.txt","w") as f:
    f.write(some_string)
    print("got here")



# second part of this file:
# reading JSON
# commented out output from IDLE

# Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# >>> f=open("c://data..book.txt","r")
# Traceback (most recent call last):
#   File "<pyshell#0>", line 1, in <module>
#     f=open("c://data..book.txt","r")
# FileNotFoundError: [Errno 2] No such file or directory: 'c://data..book.txt'
# >>> f=open("c://data//book.txt","r")
# >>> s=f.read()
# >>> s
# '{"alan": {"name": "alan", "address": "123 red street", "phone": 789789789}, "alice": {"name": "alice", "address": "456 blue street", "phone": 123123123}}'
# >>> import json
# >>> book=json.loads(s)
# >>> book
# {'alan': {'name': 'alan', 'address': '123 red street', 'phone': 789789789}, 'alice': {'name': 'alice', 'address': '456 blue street', 'phone': 123123123}}
# >>> type(book)
# <class 'dict'>
# >>> book['bob']
# Traceback (most recent call last):
#   File "<pyshell#8>", line 1, in <module>
#     book['bob']
# KeyError: 'bob'
# >>> book['alan']
# {'name': 'alan', 'address': '123 red street', 'phone': 789789789}
# >>> book['alan']['phone']
# 789789789
# >>> for person in book:
# 	print(book[person])
#
# {'name': 'alan', 'address': '123 red street', 'phone': 789789789}
# {'name': 'alice', 'address': '456 blue street', 'phone': 123123123}

