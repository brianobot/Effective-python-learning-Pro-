"""
this module present tips surrounding the knowledge of the user python version
"""

# To find ouu your python version type this in the terminal/ command prompt (for window users)
# $ python --version
# $ python -V 
# $ py --version
# $ py -V

# all the commands listed above are all equivalent and the same, just different ways of checking the installed
# python version

# you can also find out the version of python you are using at runtime with the sys module
# in your code use the code below

import sys # sys module is a standard module and comes with the standard python installation

# running this python file on your system would print out the version 
# of python you are using
print(sys.version_info)
print(sys.version)