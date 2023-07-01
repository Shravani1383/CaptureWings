from tkinter import *
import pyscreenrec

root =Tk()
root.geometry("360x360")
root.title("Capture Wings")
root.config(bg="#fff")
root.resizable (False, False)


def start_rec():
    file=Filename.get()
    rec.start_recording(str(file+".mp4"),5)
    
def pause_rec():
    rec.pause_recording()
def resume_rec():
    rec.resume_recording()
def stop_rec():            
    rec.stop_recording()

rec=pyscreenrec.ScreenRecorder()
#icon
image_icon=PhotoImage(file="icon1.png")
root.iconphoto(False, image_icon)
#background image
image1=PhotoImage(file="back.png")
Label(root,image=image1,bg="#fff").place(x=-2)

#heading
lbl=Label(root, text="Screen Recorder",bg="#fff",font="arial 15 bold")
lbl.pack(pady=20)

# buttons
start=Button(root,text="Start",font="arial 22",bd=0,command=start_rec)
start.place(x=140,y=70)

image4=PhotoImage(file="pause.png")
pause=Button(root,image=image4,bd=0,bg="#fff",command=pause_rec)
pause.place(x=60,y=200)

image5=PhotoImage(file="stop.png")
pause=Button(root,image=image5,bd=0,bg="#fff",command=stop_rec)
pause.place(x=145,y=200)

image6=PhotoImage(file="resume.png")
pause=Button(root,image=image6,bd=0,bg="#fff",command=resume_rec)
pause.place(x=230,y=200)
#entry
Filename=StringVar()
entry=Entry(root,textvariable=Filename, width=18,font="arial15")
entry.place(x=100,y=150)
Filename.set("recording")

root.mainloop()