from tkinter import*
from tkinter import messagebox
import sqlite3 as s
con=s.connect("fooddata.db")
cur=con.cursor()
root=Tk()
#root.geometry("375*200")
root.title("HOMEFOOD")
root.configure(background="grey")
def foodmaker():
    root=Tk()
    l1=Label(root,text="FOODMAKR NAME",font=("Forte",12,"bold")).grid(row=1,column=1,padx=10)
    e1=Entry(root,width=30)
    e1.grid(row=1,column=2,pady=10)
    l2=Label(root,text="FOOD",font=("Forte",12,"bold")).grid(row=2,column=1,padx=10)
    e2=Entry(root,width=30)
    e2.grid(row=2,column=2,pady=10)
    l3=Label(root,text="FOODTYPE",font=("Forte",12,"bold")).grid(row=3,column=1,padx=10)
    lb=Listbox(root,height=2)
    lb.insert(1,"Veg")
    lb.insert(2,"Non Veg")
    lb.grid(row=3,column=2)
    l4=Label(root,text="PHONENO",font=("Forte",12,"bold")).grid(row=4,column=1,padx=10)
    e4=Entry(root,width=30)
    e4.grid(row=4,column=2,pady=10)
    l5=Label(root,text="QUANTITY",font=("Forte",12,"bold")).grid(row=5,column=1,padx=10)
    e5=Entry(root,width=30)
    e5.grid(row=5,column=2,pady=10)
    l6=Label(root,text="PAISAL",font=("Forte",12,"bold")).grid(row=6,column=1,padx=10)
    e6=Entry(root,width=30)
    e6.grid(row=6,column=2,pady=10)
    def foodplace():
        name=e1.get()
        ftype=lb.get(ACTIVE)
        food=e2.get()
        phno=e4.get()
        qno=e5.get()
        rs=e6.get()
        cur.execute("create table if not exists food(name varchar,food varchar,ftype varchar,qno integer,phno varchar,rs integer)")
        cur.execute("insert into food values(?,?,?,?,?,?)",(name,food,ftype,qno,phno,rs))
        con.commit()
        messagebox.showinfo(title='food',message='food placed')
    bt=Button(root,text="PLACEFOOD",bg="blue",fg="white",command=foodplace,padx=10,pady=10).grid(row=7,column=2,padx=30)
    root.mainloop()
def customer():
    root=Tk()
    l1=Label(root,text="SELECT FOODMAKER",font=("Forte",12,"bold")).grid(row=1,column=1,padx=10)
    lbn=Listbox(root,font=("Forte",12,"italic"))
    cur.execute("select distinct name from food")
    j=0
    for i in cur.fetchall():
        print(i)
        j+=1
        lbn.insert(j,i)
        
    lbn.grid(row=1,column=2,pady=10)
    l3=Label(root,text="FOODTYPE",font=("Forte",12,"bold")).grid(row=3,column=1,padx=10)
    lb=Listbox(root,height=2,font=("Forte",12,"bold"))
    lb.insert(1,"Veg")
    lb.insert(2,"Non Veg")
    lb.grid(row=3,column=2)
    l4=Label(root,text="PHONENO",font=("Forte",12,"bold")).grid(row=4,column=1,padx=10)
    e4=Entry(root,width=30)
    e4.grid(row=4,column=2,pady=10)
    
    def next():
        root=Tk()
        print(lbn.get(ACTIVE)[0],lb.get(ACTIVE))
        cur.execute("select food,rs from food where name=? and ftype=?",(lbn.get(ACTIVE)[0],lb.get(ACTIVE),))
        #if lb.curselection()[0]==0:
        #cur.execute("select food,rs from food where ftype="+lb.get(ACTIVE)+" and name="+lbn.get(ACTIVE)[0])
        #cur.execute("selct food,rs from food where name=:name and ftype=:ftype",('name':lbn.get(ACTIVE)[0],'ftype':lb.get(ACTIVE)))
        lb1=Listbox(root,font=("Forte",12,"italic"))
        j=0
        for i,k in cur.fetchall():
                print(i,k)
                j+=1
                lb1.insert(j,(i,'-',k))
        lb1.grid(row=2,column=2)
        l=Label(root,text="QUANTITY",font=("Forte",12,"bold")).grid(row=5,column=1,padx=10)
        sp=Spinbox(root,from_=1,to=50)
        sp.grid(row=5,column=2,pady=10)
        
        def cart():
            cqno=int(sp.get())
            rs=lb1.get(ACTIVE)[2]
            root=Tk()
            lc=Label(root,text="CART AMOUNT IS  :-",font=("Forte",12,"italic"))
            lc.grid(row=4,column=1,padx=10,pady=20)
            lc.config(text="CART AMOUNT IS :-  "+str(cqno*rs))
            def code():
                def apply(self):
                
                    crs=cqno*rs
                    code=e.get()
                    if crs>150 and code=='code':
                            crs=crs-(crs//10)
                            l=Label(root,text="REDUCED CART AMOUNT IS :-  "+str(crs),font=("Forte",12,"italic"),bg="cyan",fg="black")
                            l.grid(row=5,column=1,padx=10)
                    else:   
                       lc=Label(root,text="CANT APPLY COUPON",font=("Forte",12,"italic"),bg="red",fg="white") 
                       lc.grid(row=5,column=1,padx=10)
                e=Entry(root,bd=4,width=20)
                e.grid(row=8,column=2,padx=10)
                e.bind('<Return>',apply)
                
            bt=Button(root,text="APPLY COUPON",font=("Forte",12,"bold"),bg="green",fg="white",command=code)
            bt.grid(row=6,column=2,padx=10,pady=20)
            
        
        
            def order():
                print(lbn.get(ACTIVE)[0],lb.get(ACTIVE),lb1.get(ACTIVE))
                food=lb1.get(ACTIVE)[0]
                rs=lb1.get(ACTIVE)[2]
                
                cqno=sp.get()
                cur.execute("select qno from food where name=? and ftype=? and food=? and rs=?",(lbn.get(ACTIVE)[0],lb.get(ACTIVE),food,rs,))
                qno=cur.fetchone()[0]
                if int(cqno)>qno:
                   messagebox.showinfo(title="cantorder",message=("ONLY QUANTITY",qno,"AVAILABLE U HAVE ORDERED",cqno))
                else:
                    print('u have orderd ',lbn.get(ACTIVE)[0],lb.get(ACTIVE),lb1.get(ACTIVE))
                    qno=int(qno)-int(cqno)
                    cur.execute("update food set qno=? where name=? and ftype=? and food=?",(qno,lbn.get(ACTIVE)[0],lb.get(ACTIVE),food,))
                    con.commit()
                    messagebox.showinfo(title="ordered",message=("U HAVE ORDERED",lbn.get(ACTIVE)[0],lb.get(ACTIVE),lb1.get(ACTIVE),cqno))
                    l=Label(root,text="ORDERPLACED",font=("Forte",22,"bold")).grid(row=12,column=1,padx=10)
                    
            
            bt=Button(root,text="PLACEORDR",bg="blue",fg="white",command=order,padx=10,pady=10).grid(row=7,column=2,padx=30,pady=20)       
        bt=Button(root,text="NEXT",bg="blue",fg="white",command=cart,padx=10,pady=10).grid(row=7,column=2,padx=30)
        
    bt=Button(root,text="NEXT",bg="blue",fg="white",command=next,padx=10,pady=10).grid(row=6,column=2,padx=30)   
    
        #cur.execute("select qno from food where 
        
bt=Button(root,text="foodmaker",bg="blue",fg="white",command=foodmaker,padx=10,pady=10).grid(row=1,column=10,padx=30)
bt=Button(root,text="CUSTOMER",bg="blue",fg="white",command=customer,padx=10,pady=10).grid(row=1,column=50,padx=30)
bt=Button(root,text="REVIEWS",bg="blue",fg="white",command=reviews,padx=10,pady=10).grid(row=2,column=50,padx=30)
root.mainloop()
