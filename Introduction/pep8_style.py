#!/usr/bin/python3
"""
This module contains examples and guidelines on the application of PEP8 guidelines when 
writing python code. Remember that python interpreter has no enforced rules on how 
code is written in term of style for most it operation, and you are very free to write
code as you seem fit as far as it is valid syntax, but following this thought-out styles 
allows your code to be more readable and accessible by the public and encourages neat codebases 

....and who doesn't look a beautiful looking codebase? Well i guess Js devs
You can read the whole guideline on the Official Page (https://www.python.org/
dev/peps/pep-0008/).
"""
# always put import statements at the top of the file
# always use absolute path when importing modules
# examples, 
# from foo import bar # is preferred to 
# import bar
# assuming bar is a module under foo and is sibling with the current file
# which is also a child of foo
import this
#import stadard library first
# then import 3-party libraries
# then import your own libraries

# keep 2 blank spaces around function and class definitions
# use 4 spaces for indentation instead of tab
# lines should be 79 in length or less
def update_reality(reality, feature):
    """Function documentation goes here..."""
    # function body goes here
    # when an expression spans multiple lines use the parenthesis around it
    # and lines after the initial lines should indented 4 spaces with reference
    # to the initial line
    process_result = (2 + 34) + (80 + 3556 * 23 - 43 + 24 + 244 -
        3434 + 24 + 35 - 234 + 54345)
    pass


class Reality():
    """class documentation goes here"""
    # class body goes here
    def __init__(self):
        pass

    def pause(self): # in classes methods should be seperated by 1 line
        pass


# remember class should be seperated with two blank lines
# in dicionaries, do not put a space between the key and colon
# but put a single space between the colon and the value
# as shown in the code snippet below 
detail = {"Name": "Sunday Okon", "Age": 23, "LGA": "Ikono"}

# put only one space before and after the = operator
secret = "Jesus Loves you!"

# for type annotation, put a space after the type
# and no space between the variable and the colon
data: str = "brianobot9@gmail.com"

# functions, variables and attributes should be in lower case
def display_map():
    pass


# all class names should be in capitalized words format
# including exceptions classes
class HauntedTechMansion:
    # instance methods in class should use self as their first arguments
    # this refers to the current instance of the class
    def __init__(self):
        # protected attributes should be in the format with a single leading underscore
        _secured_room = "Coordinate of secured room"
        # private attributes should be in the format with 2 leading underscore
        __secret_room = "Coordinate of secret room"

    # class methods should use cls as the name of their
    # first parameters, this refers to the class 
    @classmethod
    def update(cls, *args, **kwargs):
        pass


# module level constants shoule be all CAPS
AUTHOR = "Brian Obot"

# use inline negtaion instead of negationg positive expression
a = 2
b = 3
 #- use this
if a is not b:
    pass
#- do not use this
if not a is b:
    pass

# use not to check for empty containers and not len 
empty_list = []
#- use this
if not empty_list:
    pass  
#- do not use this
if len(empty_list) == 0:
    pass

# avoid single line if, for and while statements
if a:print('A is alive') # this is valid because the line after the if is just one

