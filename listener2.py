from tkinter import *
from tkinter import messagebox
import os
import time
##READING VALUE FROM FILE
f=open("test.txt","r")
prev=(f.read())
prev=int(prev)
f.close()
top = Tk()
top.geometry("1000x1000+0+0")
count=0
stamp1=[]
stamp2=[]
stamp3=[]
disp_files=[]
##TRAVERSING DIRECTORIES
for root, dirs, files in os.walk("F:/"):
    for file in files:
        if file.endswith(".bat"):
            count=count+1
            print(os.path.join(root,file))
            stamp2.append(os.path.join(root,file))
            stamp1.append((os.path.getctime(os.path.join(root,file))))
##SORTING FILES ACCORDING TO DATE OF CREATION
for _ in range(0,len(stamp1)):
    for i in range(_,len(stamp1)-1):
        if stamp1[i] > stamp1[i+1]:
            temp=stamp1[i]
            stamp1[i]=stamp1[i+1]
            stamp1[i+1]=temp
            temp2=stamp2[i]
            stamp2[i]=stamp2[i+1]
            stamp2[i+1]=temp2

for i in range(0,len(stamp1)):
    stamp1[i]=time.ctime(stamp1[i])
    stamp3.append(stamp1[i]+stamp2[i])
##APPENDING LAST 15 MODIFIED FILES
if len(stamp3)>10:
    for i in range(len(stamp3)-1,len(stamp3)-16,-1):
        disp_files.append(stamp3[i])
else:
    for i in range(len(stamp3)-1,0,-1):
        disp_files.append(stamp3[i])
print("New Count: "+str(count))
print("Previous Count: "+str(prev))

##GUI
if count>prev:
    if messagebox.askquestion("WARNING!", "A new .bat file was added to system.\nWere that you?", icon='warning')=='yes':
        f1=open("test.txt","w")
        f1.write(str(count))
        f1.close()
        fine=Label(top,text="bat file count has been updated",font=20)
        top.geometry("300x300+270+170")
        fine.pack()
    else:
        top.state('zoomed')
        not_fine=Text(top)
        not_fine.insert(INSERT,"LATEST 15 MODIFICATIONS ARE:\n\n")
        not_fine.insert(INSERT,"-> ",INSERT,"\t\n\n\n-> ".join(disp_files))
        not_fine.place(x="100",y="0",height=800,width=1180)
elif count<prev:
    f2=open("test.txt","w")
    f2.write(str(count))
    f2.close()
    top.destroy()
else:
    top.destroy()


