import os

FileName = input("Enter the filename: ")
#Here we check if the file exists

if os.path.isfile("./" + FileName):
    print("Looking for file{}...".format(FileName))
    print("Found it!")

    action = input(
        "What would you like to do with the file?\nPossible actions are: Read, Delete, Append, Replace\n")
    if action == "Read":
        print("The content of the file:")
        with open(FileName, "r") as ReadFile:
            print(ReadFile.read())
    elif action == "Append":
        text = input("Please enter your note: ")
        with open(FileName, "a") as AppendFile:
            AppendFile.write(text + "\n")
    elif action == "Delete":
        os.remove("./" + FileName)
        print("{} Have been deleted.".format(FileName))
        #I don't think it makes sense to create a new empty file right after deletion
        #Anyway, this is the requested task so here it is

        with open(FileName, "w") as WriteFile:
            WriteFile.write("")
    elif action == "Replace":
        LineNumb = int(input("Please Enter the line number for the replacement: "))
        Text = input("Enter your note: ")
        with open(FileName, "r") as ReadFile:
            Lines = ReadFile.readlines()
        with open(FileName, "w") as WriteFile:
            for i, line in enumerate(lines):
                print(i, line)
                if i == LineNumb - 1:
                    print("Line num{} needs to be replaced!".format(LineNumb))
                    WriteFile.write(text,"\n")
                else:
                    print("Writing \"{}\"".format(line))
                    WriteFile.write(line)


    else:
        print("Sorry, unrecognized action")
else:
    print("NO, this file does not exist, I will create it for you")
    text = input("Please enter your note: ")
    with open(FileName, "w") as WriteFile:
        WriteFile.write(text + "\n")
