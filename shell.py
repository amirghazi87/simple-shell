# Imports
import keyboard
import sys
# Function to exit from app coretly


def exit_func():
    sure = input("Are you sure exit (Y/n) ?")
    if sure == "n" or sure == "N":
        pass
    else:
        print("Bye !")
        sys.exit()


while True:
    # Get input
    command = input(">>> ")
    # Get input words in to a array
    command_list = command.split(' ')
    # If command user says is echo to print
    if command_list[0] == "echo":
        # If user wants to print a variable usin $ start of name
        if command_list[1][0] == "$":
            # Print variable
            exec("print(" + command_list[1].replace('$', '') + ")")
        # If user wants to print string
        else:
            print(command_list[1])
    # If command user syas var to set a variable
    elif command_list[0] == "var" and command_list[2] == "=":
        content = ""
        for i in range(3, 1000):
            try:
                content += "{} ".format(command_list[i])
                exec(command_list[1] + " =  \"" + content + "\"")
            except:
                break
        else:
            exec(command_list[1] + " =  \"" + command_list[3] + "\"")
    elif command_list[0] == "exit" or command_list[0] == "quit":
        exit_func()
