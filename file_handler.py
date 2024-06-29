def Create_file():
    file = open("scoreboard.txt", 'wt+')
    file.close()

def Save_file(scoreboard):
    try:
        with open("scoreboard.txt", 'w') as write:
            write.writelines("\n".join(scoreboard))
            write.close()
    except FileNotFoundError:
       Create_file()

def Load_file(file_name, data):
    try:
        with open(file_name, "r") as read:
            data = [line.strip("\n" )for line in read]
            read.close()
            return data
    except FileNotFoundError:
        Create_file()
