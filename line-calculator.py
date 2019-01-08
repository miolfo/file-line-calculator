import os
import argparse

def calculate_lines(path):
    dirs = os.listdir(path)
    linecount = 0
    for dir in dirs:
        if os.path.isfile(os.path.join(path, dir)):
            linecount += get_lines_in_file(path, dir)
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
    args = parser.parse_args()
    path = os.getcwd()
    if(args.path):
        path = args.path
    count = calculate_lines(path)
    print("Line count in {0} is {1}".format(path, str(count)))