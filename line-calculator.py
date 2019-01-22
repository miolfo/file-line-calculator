import os
import argparse

def calculate_lines(path, extension):
    dirs = os.listdir(path)
    linecount = 0
    for dir in dirs:
        if os.path.isfile(os.path.join(path, dir)):
            linecount += get_lines_in_file(path, dir)
    return linecount

def calculate_lines_recursive(path, extension):
    linecount = 0
    for root, _, files in os.walk(path):
        for file in files:
            if not extension:
                linecount += get_lines_in_file(root, file)
            else:
                _, file_extension = os.path.splitext(file)
                if file_extension == extension:
                    linecount += get_lines_in_file(root, file)
    return linecount

def get_lines_in_file(path, file_name):
    with open(os.path.join(path, file_name)) as file:
        try:
            lines = file.readlines()
            return len(lines)
        except UnicodeDecodeError:
            return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", dest="path", help="Path from which to start line calculation")
    parser.add_argument("-r", "--recursive", dest="recursive", help="Recurse through all folders in specified folder", action="store_true")
    parser.add_argument("-e", "--file-ending", dest="file_ending", help="Only calculate files of this extension")
    args = parser.parse_args()
    path = os.getcwd()
    if(args.path):
        path = args.path
    if args.recursive:
        count = calculate_lines_recursive(path, args.file_ending)
        print("Line count (recursively) in {0} is {1}".format(path, str(count)))
    else:
        count = calculate_lines(path, args.file_ending)
        print("Line count in {0} is {1}".format(path, str(count)))