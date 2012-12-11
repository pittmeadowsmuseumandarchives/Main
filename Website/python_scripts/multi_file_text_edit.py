#-------------------------------------------------------------------------------
# Name:         multi_file_text_edit.py
#
# Purpose:      This script is designed to modify and add lines quickly
#               to all the specified html files.
#
# Author:      Jeremy Borys
#
# Created:     10/12/2012
#-------------------------------------------------------------------------------

#! /usr/bin/python

import os
import sys
import re
import argparse
import shutil
import os
import datetime

# ==================== Configuration do not touch ==============================
CONFIG_FILE = 'config_file.txt'
FILE_LIST_BEGIN = '===== [List of HTML Files to Change] ======\n'
FILE_LIST_END = '===== [Line to Find] =====\n'
FIND_PATTER = '===== [Line to Find] =====\n'
REPLACE = '===== [Lines to Replace] =====\n'
END_OF_REPLACE = '===== [End Here] =====\n'
#===============================================================================

CURRENT_TIME = datetime.datetime.now()
TIME = '%s_%s_%s_' %(CURRENT_TIME.hour, CURRENT_TIME.minute, CURRENT_TIME.second)

parser = argparse.ArgumentParser()
parser.add_argument('-f', action='store', type=str, default=None,
                    dest='file_name',
                    help='Choose the filename of the file you wish to modify')
arguments = parser.parse_args()


def get_file_locations():
    '''From the Config File gets the list of files specified by the user'''
    files = open(CONFIG_FILE, 'r')
    file_lines = files.readlines()
    files.close()

    # locate the slice of the file list that relates to the file_names
    initial = file_lines.index(FILE_LIST_BEGIN) + 1
    final = file_lines.index(FILE_LIST_END)
    file_list = file_lines[initial:final]

    # Removes the new line characters from the list of filenames
    for item, number in zip(file_list, range(len(file_list))):
        file_list[number] = item.strip()

    return file_list


def get_replace_list():
    '''Creates from the config file the lines that will be replaced/appended'''
    replacement_lines = open(CONFIG_FILE, 'r')
    new_lines = replacement_lines.readlines()
    replacement_lines.close()

    # get the lines to modify from the config file
    initial = new_lines.index(REPLACE) + 1
    final = new_lines.remove(END_OF_REPLACE)
    new_lines = new_lines[initial : final]
    return new_lines


def get_pattern():
    '''Creates the pattern/string/code to search for in another string'''
    replacement_lines = open(CONFIG_FILE, 'r')
    new_lines = replacement_lines.readlines()
    replacement_lines.close()

    # create the pattern
    index = new_lines.index(FIND_PATTER) + 1
    pattern = new_lines[index]
    pattern = re.compile(pattern)
    return pattern


def get_file_info(file_name):
    '''Returns the contents of the text file as a list'''
    # look in the parent directory for the file and read its lines
    html_file = open(os.path.dirname(__file__) + '\\..\\' + file_name, 'r')
    html_lines = html_file.readlines()
    html_file.close()
    return html_lines


def replace_first_line(html_lines, line_number, original, REPLACE_LIST):
    '''Replaces the first line with the one specified by the user'''
    # delete_line creates the ability to delete a line in a file
    for line in REPLACE_LIST:
        if line_number == original:
            if 'delete_line' in line:
                html_lines.pop(line_number)
            else:
                html_lines[line_number] = line
            line_number += 1


def replace_rest_lines(html_lines, line_number, original, REPLACE_LIST):
    '''If there is more than one line insert these into the list'''
    for line in REPLACE_LIST:
        suppress_counter = False
        if line_number != original:
            if 'delete_line' in line:
                html_lines.pop(line_number)
                # counter needs to stop for this one to remove a line
                suppress_counter = True
            else:
                html_lines.insert(line_number, line)
        if not suppress_counter:
            line_number += 1


def write_new_file(html_lines, file_name):
    '''Write to the file and close the file'''
    # write to the parent directory
    html_file = open(os.path.dirname(__file__) + '\\..\\' + file_name, 'w')
    for line in html_lines:
        html_file.write(line)
    html_file.close()


def get_line_number(pattern, html_lines):
    '''Search for the pattern and return the line number from the file'''
    line_number = None
    for line, number in zip(html_lines, range(len(html_lines))):
        if re.search(pattern, line):
            line_number = number
    # controls output if returns a number > 0 replaces a line
    return line_number


def make_copy():
    '''Create a copy directory for the files to be stored'''
    try:
        os.mkdir('file_copies')
    except:
        pass


def main():
    make_copy()
    for file_name in files:
        shutil.copy2(os.path.dirname(__file__) + '\\..\\' + file_name, 'file_copies/' + TIME + file_name)
        print('Appending to file %s' % file_name)
        html_lines = get_file_info(file_name)

        REPLACE_LIST = get_replace_list()
        pattern = get_pattern()
        line_number = get_line_number(pattern, html_lines)
        original = line_number
        if line_number:
            replace_first_line(html_lines, line_number, original, REPLACE_LIST)
            replace_rest_lines(html_lines, line_number, original, REPLACE_LIST)
            write_new_file(html_lines, file_name)
        else:
            print('Could not find the line to replace in %s' % file_name)

    raw_input('Press Enter To Finish')


# Create a list of files if the user hasn't run from the command line
files = []
if arguments.file_name != None:
    files.append(arguments.file_name)
else:
    files = get_file_locations()

if __name__ == "__main__":
    main()