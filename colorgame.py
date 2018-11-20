from tkinter import*
import random
root=Tk()
root.title("color game")
time=30
#root.geometry("475*300")
lty=Label(root,text="type the color of the word press enter to start",font=("Forte",25,"bold"),anchor=CENTER)
#l.grid(row=1,column=0,padx=20,pady=10,columnspan=350)
lty.pack()
ls=Label(root,text="score: 0",font=("Forte",42,"bold"),anchor=CENTER,bg="green",fg="white")
ls.pack()
lt=Label(root,text="time left: 30",font=("Forte",32,"bold"),anchor=CENTER,bg="red",fg="white")
lt.pack()
lc=Label(root,text=" ",font=("Forte",42,"bold"),anchor=CENTER)
lc.pack()
e=Entry(root,bd=2,width=50)
l=['blue','green','orange','cyan','purple','pink','white','black','yellow','red','grey']
score=0
def color():
    e.focus_set()
    global score
    if time>0:
        if e.get()==l[1]:
            score+=1
            #print(score)
            ls.configure(text="SCORE IS:  "+str(score))
    e.delete(0,END) #after checking text then it gets deleted
    random.shuffle(l) #if used randint then varible values get changed code has to be changed
    
    lc.configure(text=str(l[0]),fg=l[1])
def count():
        
        global time
        if time>0:
            time=time-1
            lt.config(text="time left: "+str(time))
            
        lt.after(1000,count) #later this calls count
        
def startgame(self):
    if time==30: # first time it calls
        count()
    color()

root.bind('<Return>',startgame) #when enter prseed this invokes
#lt.after(500,startgame)
e.pack(pady=100)
e.focus_set()
root.mainloop()


