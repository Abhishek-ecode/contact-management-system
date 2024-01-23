from tkinter import*
from tkinter import ttk
import MySQLdb 
db=MySQLdb.connect("localhost","root","","cont")
cursor=db.cursor()

def lista():
    l=Toplevel()
    l.geometry("1250x800")
    l['bg']='#5e2323'
    l.title("Contact Management System")
    s=ttk.Style()
    s.theme_use('clam')
        
        
        
    listData = cursor.execute("SELECT * FROM CONTACT")
    customers = cursor.fetchall()
    itemsforlistbox=[]
        
    for name in customers:
            
        customers = '{0}' .format (name[0:7])
        itemsforlistbox.append(customers)
            
            
    tree = ttk. Treeview(l,column=("c1","c2","c3","c4","c5","c6","c7"),show='headings',height=20)
    s.configure('Treeview.Heading',background="red")
            
    tree.column("# 1",anchor=CENTER, width=150)
    tree.heading("# 1",text="ID")
    tree.column("# 2",anchor=CENTER, width=150)
    tree.heading("# 2",text="FIRST NAME")
    tree.column("# 3",anchor=CENTER, width=150) 
    tree.heading("# 3",text="LAST NAME")
    tree.column("# 4",anchor=CENTER, width=150)
    tree.heading("# 4",text="GENDER")
    tree.column("# 5",anchor=CENTER, width=150)
    tree.heading("# 5",text="ADDRESS")
    tree.column("# 6",anchor=CENTER, width=150)
    tree.heading("# 6",text="CONTACT")
    tree.column("# 7",anchor=CENTER, width=150)
    tree.heading("# 7",text="AGE")
    for name in itemsforlistbox:
        tree.insert('','end',text=name[0],values=name)
                
                
                
    tree.place(relx=0.08,rely=0.10)
    db.commit()

            
            
    def hide():
        h=tree.selection()
        if h:
            a=h[0]
            tree.delete(a)
     
    def deldata():

        query="DELETE FROM CONTACT"
        cursor.execute(query)
        db.commit()
        
        
        
    def removede():
        db=MySQL.connect("localhost","root","","cont")
        cursor=db.cursor()
        
        s=str(txt.get())
        sql="DELETE FROM contact WHERE name = %s"
        var=[s]
        cursor.execute(sql,var)
        db.commit()
        
        
        
    def search():
        db=MySQLdb.connect("localhost","root","","cont")
        cursor=db.cursor()
        s=str(txt.get())
        sql="SELECT * FROM CONTACT WHERE id = %s"
        var=[s]
        cursor.execute(sql,var)
        customers = cursor.fetchall()
        itemsforlistbox=[]
        
        for name in customers:
        
            customer = '{0}'.format(name[0:7])
            itemsforlistbox.append(customer)
            
        tree = ttk.Treeview(l,column=("c1","c2","c3","c4","c5","c6","c7"), show='headings', height=20)
        
        
        tree.column("# 1",anchor=CENTER, width=150)
        tree.heading("# 1",text="ID")
        tree.column("# 2",anchor=CENTER, width=150)
        tree.heading("# 2",text="FIRST NAME")
        tree.column("# 3",anchor=CENTER, width=150)
        tree.heading("# 3",text="LAST NAME")
        tree.column("# 4",anchor=CENTER, width=150)
        tree.heading("# 4",text="GENDER")
        tree.column("# 5",anchor=CENTER, width=150)
        tree.heading("# 5",text="ADDRESS")
        tree.column("# 6",anchor=CENTER, width=150)
        tree.heading("# 6",text="CONTACT")
        tree.column("# 7",anchor=CENTER, width=150)
        tree.heading("# 7",text="AGE")
        for name in itemsforlistbox:
            tree.insert('','end',text=name[0], values=name)
            
        tree.place(relx=0.08,rely=0.10)
        db.commit()
        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
           
    b=Button(l,text='BACK',font=('arial','12','bold'),bg='red',fg='black',command=l.destroy)
    b.place(relx=0.08,rely=0.9)

    b=Button(l,text="HIDE DATA",font=('arial','12','bold'),bg="red",fg="black",command=hide)
    b.bind()
    b.place(relx=0.36,rely=0.9)

    b=Button(l,text="DELETE DATABASE",font=('arial','12','bold'),bg='red',fg='black',command=deldata)
    b.bind()
    b.place(relx=0.65,rely=0.9)


    txt=StringVar()
    e=Entry(l,text=txt,font=('arial','12','bold'))
    e.place(relx=0.1,rely=0.75)



    b=Button(l,text="SEARCH",font=('arial','12','bold'),bg='red',fg='black',command=search)
    b.bind()
    b.place(relx=0.33,rely=0.75)

    b=Button(l,text="REMOVE DATA",font=('arial','12','bold'),bg='red',fg='black',command=removede)
    b.bind()
    b.place(relx=0.55,rely=0.75)



    l.mainloop()


def main():
    def adddata(event):
        name_strvar=str(text1.get())
        lastname_strvar=str(text2.get())
        gender_strvar=str(text3.get())
        address_strvar=str(text4.get())
        contact_strvar=str(text5.get())
        gmail_strvar=str(text6.get())   
        sql="INSERT INTO contact(namen,lastn,gendern,addressn,contactn,agen) values(%s,%s,%s,%s,%s,%s)"
        var=[name_strvar,lastname_strvar,gender_strvar,address_strvar,contact_strvar,gmail_strvar]
        cursor.execute(sql,var)
        db.commit()
            






    def reset():
        text1.set(" ")
        text2.set(" ")
        text3.set(" ")
        text4.set(" ")
        text5.set(" ")
        text6.set(" ")
        
        
        
        
        
    a=Toplevel()
    a['bg']='red4'
    a.geometry('1152x886')
    a.resizable(0,0)

    a.title('CONTACT MANAGEMENT SYSTEM')


    b=Label(a,text="     CONTACT MANAGEMENT SYSTEM     ",font=("Cambria","30","bold"),fg='black',bd=9,bg='white',width=30)
    b.place(relx=0.3,rely=0.0)


    b=Label(a,text='  1.  '"    FIRST NAME   ",font=("Cambria","15","bold"),borderwidth=6,relief="groove")
    b.place(relx=0.10,rely=0.12)
    text1=StringVar()
    v=Entry(a,text=text1,font='arial 15',borderwidth=6,relief="groove")
    v.place(relx=0.3,rely=0.12)



    b=Label(a,text='  2.  '"    LAST NAME    ",font=("Cambria","15","bold"),borderwidth=6,relief="groove")
    b.place(relx=0.10,rely=0.25)
    text2=StringVar()
    v=Entry(a,text=text2,font='arial 15',borderwidth=6,relief="groove")
    v.place(relx=0.3,rely=0.25)


    b=Label(a,text='  3.  '"        GENDER        ",font=("Cambria","15","bold"),borderwidth=6,relief="groove")
    b.place(relx=0.10,rely=0.37)
    text3=StringVar()
    v=Entry(a,text=text3,font='arial 15',borderwidth=6,relief="groove")
    v.place(relx=0.3,rely=0.37)

    b=Label(a,text='  4.  '"      ADDRESS        ",font=("Cambria","15","bold"),borderwidth=6,relief="groove")
    b.place(relx=0.10,rely=0.49)
    text4=StringVar()
    v=Entry(a,text=text4,font='arial 15',borderwidth=6,relief="groove")
    v.place(relx=0.3,rely=0.49)


    b=Label(a,text='  5.  '"      CONTACT       ",font=("Cambria","15","bold"),borderwidth=6,relief="groove")
    b.place(relx=0.10,rely=0.61)
    text5=StringVar()
    v=Entry(a,text=text5,font='arial 15',borderwidth=6,relief="groove")
    v.place(relx=0.3,rely=0.61)




    b=Label(a,text='  6.  '"              AGE             ",font=("Cambria","15","bold"),borderwidth=6,relief="groove")
    b.place(relx=0.10,rely=0.73)
    text6=StringVar()
    v=Entry(a,text=text6,font='arial 15',borderwidth=6,relief="groove")
    v.place(relx=0.3,rely=0.73)



    b=Button(a,text="      RESET     ",bg="BLACK",fg="#ffffff",borderwidth=10,relief="groove",font=('arial',13,'bold'),command=reset)
    b.bind()
    b.place(relx=0.7,rely=0.28)

    b=Button(a,text="      BACK      ",bg="BLACK",fg="#ffffff",borderwidth=10,relief="groove",font=('arial',13,'bold'),command=a.destroy)
    b.bind()
    b.place(relx=0.7,rely=0.49)


    b=Button(a,text="     SUBMIT     ",bg="BLACK",fg="#ffffff",borderwidth=10,relief="groove",font=('arial',13,'bold'))
    b.bind("<Button-1>",adddata)
    b.place(relx=0.7,rely=0.73)













    a.mainloop()










win=Tk()
win.geometry("950x950")

win.title("CONTACT MANAGEMENT SYSTEM")
win['bg']='#5e2323'


t=Label(win,text="CONTACT MANAGEMENT SYSTEM",font=('arial','25','bold'),bg="red",fg="black").pack(side=TOP,fill=X)



b=Button(win,text="NEW REGISTRATION",font=('arial','18','bold'),bg="#4d96e3",fg="black",command=main)
b.place(relx=0.4,rely=0.3,relwidth=0.3)
b=Button(win,text="      DATA LIST             ",font=('arial','18','bold'),bg="#4d96e3",fg="black",command=lista)
b.place(relx=0.4,rely=0.5,relwidth=0.3)

b=Button(win,text="           EXIT          ",font=('arial','18','bold'),bg="#4d96e3",fg="black",command=exit)
b.place(relx=0.4,rely=0.7,relwidth=0.3)





win.mainloop()