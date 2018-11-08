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


"""Copy Special exercise
"""


def get_absolute_file_paths(directory):
    regex = r"(_{2,}[^_\W]+_{2,})"
    result = [os.path.realpath(x) for x in os.listdir(
        directory) if re.search(regex, x)]
    return result


def copy_files_to_dir(files, new_directory, current_directory):

    current_real_path = os.path.realpath(
        current_directory) + '/' + str(new_directory)

    if new_directory not in os.listdir(current_directory):
        os.makedirs(current_real_path, 0o777)

    [shutil.copy(f, current_real_path)
     for f in files if f not in os.listdir(current_real_path)]


def create_app_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--todir', help='name of dest dir for special files')
    parser.add_argument(
        '--tozip', help='dest zipfile for special files')
    parser.add_argument('search_directory', help='directory to search in')
    return parser.parse_args()


def main():

    args = create_app_parser()

    files = (get_absolute_file_paths(
        args.search_directory))

    if not args.todir and not args.tozip:
        for file_name in files:
            print (file_name)

    elif args.todir:
        copy_files_to_dir(files, args.todir, args.search_directory)

    elif args.tozip:
        command = 'zip -j {} {}'.format(args.tozip, ' '.join(files))
        print("Command I'm going to do:")
        print(command)
        exit_code = os.system(command)

        if exit_code > 0:
            print('exiting with exit code {}').format(exit_code)
            exit(exit_code)


if __name__ == "__main__":
    main()
