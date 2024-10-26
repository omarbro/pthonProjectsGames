import os
def main():
    filename= input(" Enter your file name to open/create : ").strip()

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

    print("Write to the file . Enter save in a new line to save and exit")
    content = []
    while True:
        line= input()
        if line == 'save' or line == 'SAVE':
            break
        content.append(line)

    try:
        with open(filename, "w") as file:
            file.writelines(content)
            #file.write("\n".join(content)) -- it will join all the list elements as one str with new line each
            print(f" File {filename} has been saved")
    except OSError:
        print(f" File {filename} could not be saved..")





if __name__ == '__main__':
    main()