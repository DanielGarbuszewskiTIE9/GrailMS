import tkinter as akasha
from PIL import ImageTk, Image
import os

#--------------------------------------------------------Magic

grail = akasha.Tk()

gW = 1000
gH = 800

winW = int((grail.winfo_screenwidth()/2)-(gW/2))
winH = int((grail.winfo_screenheight()/2)-(gH/2))

userpath = os.path.dirname(os.path.abspath(__file__)).split("\\")

grail.title(f"{userpath[3]}'s Grail")
grail.geometry(f"{gW}x{gH}+{winW}+{winH}")
grail.resizable(False,False)

logNum = 0

currentPath = f"C:/GrailMS/Users/{userpath[3]}/Desktop/"

def commandInput(event):
    global currentPath
    global logNum

    command=commandEntry.get()
    command=command.split()
    print(command)

    if command[0]=="open":
        textEditor.delete("1.0","end")
        
        command = commandEntry.get()
        command = command[5:]

        file = open(f"{currentPath}/{command}","r")
        fileContent = file.read()
        textEditor.insert("end",fileContent)
        file.close()

        commandOutput.configure(state="normal")
        commandOutput.insert("end",f'{logNum}. Opened "{command}" in "{currentPath}"\n')
        commandOutput.configure(state="disabled")
        logNum+=1
    
    elif command[0]=="save":
        file = open(f"{currentPath}/{command[1]}","w")
        file.write(textEditor.get("1.0","end"))

        command = commandEntry.get()
        command = command[5:]

        commandOutput.configure(state="normal")
        commandOutput.insert("end",f'{logNum}. Saved "{command}" to "{currentPath}"\n')
        commandOutput.configure(state="disabled")
        logNum+=1

    elif command[0]=="run":
        command = commandEntry.get()
        command = command[4:]

        os.startfile(currentPath+command)

    elif command[0]=="ascend":
        command = commandEntry.get()
        command = command[7:]
        command.split("/")

        currentPath = f"C:/"

        for item in command:
            currentPath += item
        
        currentPath += "/"
        
        fileList.delete("0","end")
        for name in os.listdir(currentPath):
            fileList.insert("end",name)

        commandOutput.configure(state="normal")
        commandOutput.insert("end",f'{logNum}. Ascended to "{command}"\n')
        commandOutput.configure(state="disabled")
        logNum+=1
    
    elif command[0]=="goto":
        command = commandEntry.get()
        command = command[5:]

        currentPath += f"{command}/"

        fileList.delete("0","end")
        for name in os.listdir(currentPath):
            fileList.insert("end",name)

        commandOutput.configure(state="normal")
        commandOutput.insert("end",f'{logNum}. Went to "{command}"\n')
        commandOutput.configure(state="disabled")
        logNum+=1

    elif command[0]=="back":
        command = commandEntry.get()
        command = command[5:]
        
        currentPathS = currentPath.split("/")
        print(currentPathS)
        currentPathS.pop()
        currentPathS.pop()
        print(currentPathS)

        currentPath = ""

        for item in range(len(currentPathS)):
             currentPath += currentPathS[item]
             currentPath += "/"
        print(currentPath)
        
        fileList.delete("0","end")

        for name in os.listdir(currentPath):
            fileList.insert("end",name)

        commandOutput.configure(state="normal")
        commandOutput.insert("end",f'{logNum}. Went back to "{currentPath}"\n')
        commandOutput.configure(state="disabled")
        logNum+=1

    elif command[0]=="refresh":
        fileList.delete("0","end")

        for name in os.listdir(currentPath):
            fileList.insert("end",name)

        commandOutput.configure(state="normal")
        commandOutput.insert("end",f'{logNum}. Refreshed\n')
        commandOutput.configure(state="disabled")
        logNum+=1

    elif command[0]=="display":
        command = commandEntry.get()
        command = command[5:]

        display = akasha.Tk()
        img1 = ImageTk.PhotoImage(master=display,file=currentPath+command)
        gW,gH = img1.width(),img1.height()
        winW,winH = int((display.winfo_screenwidth()/2)-(gW/2)),int((display.winfo_screenheight()/2)-(gH/2))

        display.title(f"Photo display: {command}")
        display.geometry(f"{gW}x{gH}+{winW}+{winH}")
        display.resizable(False,False)

        canvas = akasha.Canvas(display,width=gW,height=gH)
        img = akasha.Label(display,image=img1)
        
        canvas.pack()
        canvas.create_window(gW/2,gH/2,window=img)
        
        display.mainloop()

        commandOutput.configure(state="normal")
        commandOutput.insert("end",f'{logNum}. Displayed "{command}"\n')
        commandOutput.configure(state="disabled")
        logNum+=1

#--------------------------------------------------------Magecraft

canvas = akasha.Canvas(grail,width=gW,height=gH)

bgImg = ImageTk.PhotoImage(master=grail,file="defaultData/saberAlter.png")
bg = akasha.Label(grail,image=bgImg)

petImg = ImageTk.PhotoImage(master=grail,file="defaultData/petLain.png")
pet = akasha.Label(grail,image=petImg)

commandOutput = akasha.Text(grail,height=5,width=80,state="disabled")
commandEntry = akasha.Entry(grail)
textEditor = akasha.Text(grail)
fileList = akasha.Listbox(grail)

commandEntry.bind("<Return>",commandInput)

canvas.pack()
canvas.create_window(gW/2,gH/2,window=bg)
canvas.create_window(670,20,anchor="nw",window=pet)
canvas.create_window(20,20,anchor="nw",window=commandOutput)
canvas.create_window(20,110,anchor="nw",window=commandEntry,height=20,width=645)
canvas.create_window(20,135,anchor="nw",window=textEditor,height=645,width=645)
canvas.create_window(670,135,anchor="nw",window=fileList,height=645,width=310)

commandOutput.configure(state="normal")
commandOutput.insert("end",f'{logNum}. Welcome to your Grail, {userpath[3]}!\n   Current path is set to "{currentPath}"\n')
commandOutput.configure(state="disabled")
logNum+=1

grail.mainloop()