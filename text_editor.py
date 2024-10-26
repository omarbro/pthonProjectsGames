import os
def main():
    filename= input(" Enter your file name to open/create : ")

    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                content = file.read()
                print(content)
        else:
            with open(filename, "w") as file:
                pass # we used pass as we can't keep with blck empty.
    except OSError:
        print(f" File {filename} could not be opened..")




if __name__ == '__main__':
    main()