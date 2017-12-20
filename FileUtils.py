# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------

import sys
#import inspect
import os
import os2emxpath
from os import path



def main():
    pass



def func(params):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""

    pass

def getFileContent(fileName) :

    try:
        script = open(fileName)
        inText = script.read()
        return inText
    except EnvironmentError:
        return fileName + " path or file does not exist"

def writeToFile(fileName, content) :
    write = open(fileName, "w")
    write.write(content)
    write.close()

def appendToFile(fileName, content):
    if os.path.exists(fileName):
        append = open(fileName, "a")
        append.write(content)
        append.close()
    else:
        print fileName + " does not exist"
        sys.exit()



if __name__ == '__main__':
    main()