import os
import subprocess 
import webbrowser
os.system('cls')


while True:
    wd0 = str(subprocess.check_output("echo %cd%", shell=True));
    wd1 = wd0[2:-4]
    command = input(f"\033[96m{wd1}\033[92m cash$>\033[0m ")
    while command != "exit":
        #command 1
        if command == "cam" or command == "clear":
            os.system('cls')
            break
        #command 2
        elif command == "":
            break
        #command 3
        elif command[0] == "c" and command[1] == "d":
            try:
                dir0 = command[3:]
                os.chdir(dir0)
                break
            except:
                print("Problem occured while changing directory.")
                break
        #command 4 List Items
        elif command == "ls":
            os.system('dir')
            break
        
        #other commands
        else:
            os.system(command)
            break
        
    if command == "exit":
        break