import tkinter as akasha
from PIL import ImageTk
from Users.createUser import createUser

#--------------------------------------------------------Magic

grail = akasha.Tk()

gW = 250
gH = 300

winW = int((grail.winfo_screenwidth()/2)-(gW/2))
winH = int((grail.winfo_screenheight()/2)-(gH/2))

grail.title("User Login")
grail.geometry(f"{gW}x{gH}+{winW}+{winH}")
grail.resizable(False,False)

def userVerify():
    verification = False

    with open("Users/user.data","r") as userdata:
        for line in userdata:
            line=line.split(";")
            line[1]=line[1].replace("\n","")
            print(line)
            
            if line[0]==name.get():
                print("Username verified")
                if line[1]==password.get():
                    print("Password verified")
                    verification = True

            if verification==True:
                global usename
                usename=line[0]
                grail.destroy()
                break
            else:
                continue

def userRegister():
    taken = True

    with open("Users/user.data","r+") as userdata:
        for line in userdata:
            line=line.replace("\n","")
            line=line.split(";")
            print(line)

            if line[0]==name.get():
                print("Username taken")
                taken = True
                break
            else:
                taken = False
                continue
        
        if taken==False:
            userdata.write(f"{name.get()};{password.get()}\n")
            createUser(name.get())

#--------------------------------------------------------Magecraft

canvas = akasha.Canvas(grail,width=gW,height=gH)

logoImg = ImageTk.PhotoImage(master=grail,file="defaultData/logo.png")
logo = akasha.Label(grail,image=logoImg)

nameL = akasha.Label(grail,text="Username:")
name = akasha.Entry(grail)

passwordL = akasha.Label(grail,text="Password:")
password = akasha.Entry(grail)

login = akasha.Button(grail,text="Log in",command=userVerify)
register = akasha.Button(grail,text="Register",command=userRegister)


canvas.pack()
canvas.create_window(125,70,window=logo)
canvas.create_window(125,140,window=nameL)
canvas.create_window(125,165,window=name)
canvas.create_window(125,190,window=passwordL)
canvas.create_window(125,215,window=password)
canvas.create_window(84,255,window=login)
canvas.create_window(160,255,window=register)


grail.mainloop()