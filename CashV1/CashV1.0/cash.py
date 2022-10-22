import os
import subprocess 
os.system('cls')

while True:
    wd = subprocess.check_output("echo %cd%", shell=True);
    command = input(f"{wd} cash$> ")
    while command != "exit":
        #command 1
        if command == "cam":
            os.system('cls')
            break
        #command 2
        if command == "":
            break
        #other commands
        else:
            os.system(command)
            break
        
    if command == "exit":
        break