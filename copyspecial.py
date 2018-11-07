#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse
import glob

"""Copy Special exercise
"""


def get_absolute_file_paths():
    regex = r"(_{2,}[^_\W]+_{2,})"
    result = [os.path.realpath(x)
              for x in os.listdir('.') if re.search(regex, x)]
    return result


def copy_files_to_dir(files, directory):

    full_directory = os.path.realpath('.') + '/' + directory

    if directory not in os.listdir('.'):
        os.makedirs(full_directory, 0777)
    for f in files:
        if f not in os.listdir(full_directory):
            shutil.copy(f, full_directory)


def main():

    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--todir', help='dest dir for special files', action='store_true')
    parser.add_argument(
        '--tozip', help='dest zipfile for special files', action='store_true')
    parser.add_argument('--directory')
    args = parser.parse_args()
    if not args.todir and not args.tozip:
        for file in get_absolute_file_paths():
            print (file)
    elif args.todir:
        copy_files_to_dir(get_absolute_file_paths(), args.directory)

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
