from tkinter import*
root=Tk()
operator=''
txt=StringVar()
def btclk(num):
    global operator
    operator=operator+str(num)
    #concatinating
    txt.set(operator)
def eq():
    global operator
    out=str(eval(operator))
    txt.set(out)
    operator=''
def clr():
    txt.set('')
def back():
    global operator
    operator=operator[0:len(operator)-1]
    txt.set(operator)
root.title='calculator'
e=Entry(root,insertwidth=5,bd=4,font=(None,20,'bold'),text=txt,justify='right',bg='cyan').grid(columnspan=4)
b1=Button(root,text=7,font=(None,12,'bold'),command=lambda :btclk(7),padx=10,pady=10)
b1.grid(row=1,column=0)
b2=Button(root,text=8,font=(None,12,'bold'),command=lambda :btclk(8),padx=10,pady=10)
b2.grid(row=1,column=1)
b3=Button(root,text=9,font=(None,12,'bold'),command=lambda :btclk(9),padx=10,pady=10)
b3.grid(row=1,column=2)
b4=Button(root,text='+',font=(None,12,'bold'),command=lambda :btclk('+'),padx=10,pady=10)
b4.grid(row=1,column=3)
b5=Button(root,text=4,font=(None,12,'bold'),command=lambda :btclk(4),padx=10,pady=10)
b5.grid(row=2,column=0)
b6=Button(root,text=5,font=(None,12,'bold'),command=lambda :btclk(5),padx=10,pady=10)
b6.grid(row=2,column=1)
b7=Button(root,text=6,font=(None,12,'bold'),command=lambda :btclk(6),padx=10,pady=10)
b7.grid(row=2,column=2)
b8=Button(root,text='-',font=(None,12,'bold'),command=lambda :btclk('-'),padx=10,pady=10)
b8.grid(row=2,column=3)
b9=Button(root,text=1,font=(None,12,'bold'),command=lambda :btclk(1),padx=10,pady=10)
b9.grid(row=3,column=0)
b10=Button(root,text=2,font=(None,12,'bold'),command=lambda :btclk(2),padx=10,pady=10)
b10.grid(row=3,column=1)
b11=Button(root,text=3,font=(None,12,'bold'),command=lambda :btclk(3),padx=10,pady=10)
b11.grid(row=3,column=2)
b13=Button(root,text='*',font=(None,12,'bold'),command=lambda :btclk('*'),padx=10,pady=10)
b13.grid(row=3,column=3)
b14=Button(root,text='/',font=(None,12,'bold'),command=lambda :btclk('/'),padx=10,pady=10)
b14.grid(row=4,column=0)
b15=Button(root,text='=',font=(None,12,'bold'),command=eq,padx=10,pady=10)
b15.grid(row=4,column=1)
b5=Button(root,text='c',font=(None,12,'bold'),command=clr,padx=10,pady=10)
b5.grid(row=4,column=2)
b5=Button(root,text='<-',font=(None,12,'bold'),command=back,padx=20,pady=10)
b5.grid(row=4,column=3)
root.mainloop()
