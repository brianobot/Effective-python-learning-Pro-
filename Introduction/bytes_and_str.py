"""This module contains tips on handling bytes and str in the python ecosystem"""

""" Python Bytes and Strings behave in similar manners, but are different and are usually
not compatable with each other, passing string to functions that require bytes would usually cause 
errors and vice versa, knowing the differences is a step towards mastering the application of them each"""

# Bytes: sequence of 8-bits values
# String: sequence of Unicode code points

# Examples
# str_a = "TeneT is a truely wonderful movie"
# byte_a = b"Christopher Nolan is a wonderful thinker!"

# you can convert from one to the other using their helper functions
# for bytes, use decode
# for strings, use encode

# bytes and strings can't be used interchangeably

# NOTE: ensure to always work on strings in python and convert to bytes if
# its needed for output