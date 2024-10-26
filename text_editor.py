import os

from matplotlib import lines


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def write_file(filename, content):
    with open(filename, "w") as file:
        file.writelines(content)


def get_user_text():
    print("Write to the file . Enter save in a new line to save and exit")
    lines = []
    while True:
        line= input()
        if line == 'save' or line == 'SAVE':
            break
        lines.append(line)
    return lines

def main():
    filename= input(" Enter your file name to open/create : ").strip()
    try:
        if os.path.exists(filename):
            print(read_file(filename))
        else:
            write_file(filename, '')

        content= get_user_text()
        write_file(filename, content)
        #file.write("\n".join(content)) -- it will join all the list elements as one str with new line each
        print(f" File {filename} has been saved")

    except OSError:
        print(f" File {filename} could not be opened ..")





if __name__ == '__main__':
    main()