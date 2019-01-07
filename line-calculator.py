import os

def calculate_lines(path):
    print("Calculating lines in" + path)
    dirs = os.listdir(path)
    linecount = 0
    for dir in dirs:
        if os.path.isfile(dir):
            linecount += get_lines_in_file(path, dir)
    return linecount

def get_lines_in_file(path, file_name):
    return sum(1 for line in open(path + '/' + file_name))

if __name__ == '__main__':
    path = os.getcwd()
    count = calculate_lines(path)
    print("Line count is " + str(count))