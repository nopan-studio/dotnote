import os
from pathlib import Path

def sh(script):
    os.system("bash -c '%s'" % script)


dir_home = str(Path.home())
dir_task = dir_home+"/dotnote/task.list"
dir_cleared = dir_home+"/dotnote/cleared.list"

try:
    os.mkdir(dir_home+"/dotnote")
    _ftest = open(dir_task,"x").close()
    _ftest = open(dir_cleared,"x").close()

except:
    print("task files is cool")


# SHOW NOTIFICATION IN DESKTOP
def notifications_show():
    file = open(dir_task,"r")
    taskCount = 0
    for x in file:
        taskCount=taskCount+1
    sh("exec notify-send " + "\"You have a " +str(taskCount)+" pending task todo.\" ")
    file.close()

class _modify_options():
    def __init__ (self,_dir,params):
        self.dir = _dir
        self.params = params

    def option_add(self):
        self.file = open(self.dir,'a+')
        self.taskname = self.params
        self.file.write(self.taskname+"\n")
        self.file.close()

    def option_del(self):
        self.file = open(self.dir,'r')
        self.lines = self.file.readlines()
        self.file.close()

        self.num = self.params
        self.file = open(self.dir,'w+')
        for i, line  in enumerate(self.lines,start = 1):
            if(str(i) != self.num):
                self.file.write(line)
        self.file.close()
    
    def option_cleared(self):
        self. file = open(self.dir,'r')
        self.lines = self.file.readlines()
        self.file.close()

        self.num = self.params
        self.file = open(dir_cleared,'a+')
        for i, line  in enumerate(self.lines,start = 1):
            if(str(i)==self.num):
                self.file.write(line)
        self.file.close()

        self.file = open(dir_task,'w+')
        for i, line  in enumerate(self.lines,start = 1):
            if(str(i) != self.num):
                self.file.write(line)
        self.file.close()

def menu_active_tasks():
    while(True):
        os.system('clear')
        print("█████████████████████████████████████████████████████████\n") 
        print("\t █████╗ ██████████████████╗   █████████╗") 
        print("\t██╔══████╔════╚══██╔══████║   ████╔════╝") 
        print("\t█████████║       ██║  ████║   ███████╗  ") 
        print("\t██╔══████║       ██║  ██╚██╗ ██╔██╔══╝  ") 
        print("\t██║  ██╚██████╗  ██║  ██║╚████╔╝███████╗") 
        print("\t╚═╝  ╚═╝╚═════╝  ╚═╝  ╚═╝ ╚═══╝ ╚══════╝")                                            
        print("\n█████████████████████████████████████████████████████████\n")
        #READ TASKS
        file = open(dir_task)
        lines = file.read().splitlines()

        if(len(lines) != 0):
            for i, x  in enumerate(lines,start = 1):
                print("["+str(i) +"] : "+ x)
        else:
            print("There is nothing here..")

        print("\n█████████████████████████████████████████████████████████\n")

        #OPTIONS
        inp = list(input(":").split(" ",1))

        if (len(inp) != 1):
            modify = _modify_options(dir_task,inp[1])

        if(inp[0] == "qq"):  
            break
        elif(inp[0] == "sd" and len(inp) != 1):
            modify.option_cleared()
        elif(inp[0] == "new" and len(inp) != 1):
            modify.option_add()
        elif(inp[0] == "del" and len(inp) != 1):
            modify.option_del()

def menu_cleared_tasks():
    while(True):
        os.system('clear')
        print("█████████████████████████████████████████████████████████\n") 
        print("    ████████╗    ███████╗█████╗██████╗█████████████╗ ")
        print("   ██╔════██║    ██╔════██╔══████╔══████╔════██╔══██╗")
        print("   ██║    ██║    █████╗ █████████████╔█████╗ ██║  ██║")
        print("   ██║    ██║    ██╔══╝ ██╔══████╔══████╔══╝ ██║  ██║")
        print("   ╚██████████████████████║  ████║  ███████████████╔╝")
        print("    ╚═════╚══════╚══════╚═╝  ╚═╚═╝  ╚═╚══════╚═════╝ ")
        print("\n█████████████████████████████████████████████████████████\n") 
                                                  
        #READ TASKS
        file = open(dir_cleared)
        lines = file.read().splitlines()

        if(len(lines) != 0):
            for i, x  in enumerate(lines,start = 1):
                print("["+str(i) +"] : "+ x)
        else:
            print("There is nothing here..")
        file.close()
        print("\n█████████████████████████████████████████████████████████\n")

        #OPTIONS
        inp = list(input(":").split(" ",1))

        if (len(inp) != 1):
            modify = _modify_options(dir_cleared,inp[1])
        if(inp[0] == "qq"):  
            break
        elif(inp[0] == "sd" and len(inp) != 1):
            modify.option_add()
        elif(inp[0] == "del" and len(inp) != 1):
            modify.option_del()

def menu_help():
    while(True):
        os.system('clear')
        print("█████████████████████████████████████████████████████████\n")
        print("\t    ██╗  ███████████╗    ██████╗ ")
        print("\t    ██║  ████╔════██║    ██╔══██╗")
        print("\t    ████████████╗ ██║    ██████╔╝")
        print("\t    ██╔══████╔══╝ ██║    ██╔═══╝ ")
        print("\t    ██║  ██████████████████║     ")
        print("\t    ╚═╝  ╚═╚══════╚══════╚═╝     ")
                                                         
        print("\n█████████████████████████████████████████████████████████\n")
        print("[COMMAND]\t\t[DESCRIPTION]")
        print(" qq \t\t\tgo back")
        print(" new task_name  \tadd new task")
        print(" del task_number \tdelete task")
        print(" sd  task_number \tin ACTIVE will send the task to cleared")
        print(" sd  task_number \tin CLEARED will send the task to active")
       
        print("\n█████████████████████████████████████████████████████████\n")

        #OPTIONS
        inp = list(input(":").split(" ",1))

        if (len(inp) != 1):
            modify = _modify_options(dir_cleared,inp[1])
        if(inp[0] == "qq"):  
            break

# MENU - SELECT
def select_menu(x):
    if(x == '1'):
        menu_active_tasks()
    elif (x == '2'):
        menu_cleared_tasks()
    elif (x == '3'):
        menu_help()
    elif (x == "qq"):
        os.system('clear')
        exit()

if(__name__ == "__main__"):
    # MAIN LOOP 
    while(True):
        os.system('clear')
        print("█████████████████████████████████████████████████████████\n") 
        print("██████╗ ██████╗███████████╗   ██╗██████╗███████████████╗")
        print("██╔══████╔═══██╚══██╔══████╗  ████╔═══██╚══██╔══██╔════╝")
        print("██║  ████║   ██║  ██║  ██╔██╗ ████║   ██║  ██║  █████╗  ")
        print("██║  ████║   ██║  ██║  ██║╚██╗████║   ██║  ██║  ██╔══╝  ")
        print("██████╔╚██████╔╝  ██║  ██║ ╚████╚██████╔╝  ██║  ███████╗")
        print("╚═════╝ ╚═════╝   ╚═╝  ╚═╝  ╚═══╝╚═════╝   ╚═╝  ╚══════╝\n")                                                      
        print("█████████████████████████████████████████████████████████\n\n") 
        print("[1] : Show Active \"To Do\"")
        print("[2] : Show Cleared \"To Do\"")
        print("[3] : Help")
        print("\n")
        print("█████████████████████████████████████████████████████████\n\n") 
        selector = input(":")
        ## switch selector
        select_menu(selector)

