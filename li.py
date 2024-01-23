from tkinter import*
from tkinter import ttk


import MySQLdb
db=MySQLdb.connect("localhost","root","","cont")
cursor=db.cursor()



 

l=Tk()
l.geometry("1250x800")

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
db.close()
        
        
        
def hide():
    h=tree.selection()
    if h:
        a=h[0]
        tree.delete(a)
 
def deldata():

    query="DELETE FROM CONTACT"
    cursor.execute(query)
    db.commit()
    db.close()
    
    
def removede():
    db=MySQL.connect("localhost","root","","cont")
    cursor=db.cursor()
    
    s=str(txt.get())
    sql="DELETE FROM contact WHERE name = %s"
    var=[s]
    cursor.execute(sql,var)
    db.commit()
    db.close()
    
    
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