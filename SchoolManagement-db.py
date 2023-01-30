from  tkinter import *
from tkinter import messagebox,ttk
from tkcalendar import *
import pymysql

#CRUD
#1. Delete Record
#2. View Record
#3. Reset Fields
#4. Delete Database
#5. Insert Record
def InsertRecord():
    sname = Name_entry.get()
    scontact = Contact_entry.get()
    semail = Email_entry.get()
    sgender = Gender_select.get()
    sdob = Dob_entry.get()
    sstream = Stream_entry.get()
    mycon = pymysql.connect(host='localhost',user='root',password='root',database='schoolmanagementdb')
    cur = mycon.cursor()
    cur.execute('insert into studentform(Name,Contact,Email,Gender,DOB,Stream) values ("'+sname+'","'+scontact+'","'+semail+'","'+sgender+'","'+sdob+'","'+sstream+'")')
    messagebox.showinfo('Status', 'Record Inserted Successfully!')
    mycon.commit()
    mycon.close()

def DelRecord():
    if (Name_entry.get()==''):
        messagebox.showinfo('Message','Please provide the Name of the student to delete Record')
    else:
        mycon = pymysql.Connect(host='localhost', user='root', password='root', database='schoolmanagementdb')
        cur = mycon.cursor()
        cur.execute('delete from studentform where Name="'+Name_entry.get()+'"')
        mycon.commit()
        messagebox.showinfo('Status','Record Deleted Successfully!')
        mycon.close()

def ViewRecord():
    mycon = pymysql.connect(host='localhost', user='root', password='root', database='schoolmanagementdb')
    cur = mycon.cursor()
    cur.execute('select * from studentform')
    data = cur.fetchall()
    #To View Table's all Records
    treeviews = ttk.Treeview(frame4,columns=(2,3,4,5,6,7,8),show='headings',height=35)
    treeviews.grid(row=2,column=2,sticky='n')   # n, s, e, w
    treeviews.heading(2,text='Id')
    treeviews.heading(3,text='Name')
    treeviews.heading(4,text='Contact')
    treeviews.heading(5,text='Email Address')
    treeviews.heading(6,text='Gender')
    treeviews.heading(7,text='Date of Birth (DOB)')
    treeviews.heading(8,text='Stream')
    treeviews.column(2,width=80)
    treeviews.column(3,width=150)
    treeviews.column(4,width=150)
    treeviews.column(5,width=200)
    treeviews.column(6,width=120)
    treeviews.column(7,width=150)
    treeviews.column(8,width=145)
    for i in data:
        treeviews.insert('','end',values=i)
    mycon.commit()
    mycon.close()

def ResetField():
    Name_entry.delete(0,'end')
    Contact_entry.delete(0,'end')
    Email_entry.delete(0,'end')
    Gender_select.delete(0,'end')
    Dob_entry.delete(0,'end')
    Stream_entry.delete(0,'end')

def DelDatbase():
    mycon = pymysql.connect(host='localhost', user='root', password='root', database='schoolmanagementdb')
    cur = mycon.cursor()
    cur.execute('drop database schoolmanagementdb')
    mycon.commit()
    mycon.close()

#End CRUD

window = Tk()
width= window.winfo_screenwidth()
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
#window.geometry('1200x800')
window.resizable(True,True)
window.config(bg='spring green')
window.title('Student Management System')

#FRAME FOR HEADING
frame1 = Frame(window,width=1200,bg='spring green',height=5,highlightthickness=0)
frame1.grid(row=0,columnspan=8)
head = Label(frame1,text='SCHOOL MANAGEMENT SYSTEM',font=('Arial',15,'bold'),bg='spring green',justify=CENTER)
head.grid(row=0,columnspan=8)    #column=0

#FRAME FOR STUDENT DATA
#Column 1
frame2 = Frame(window,height=5,highlightthickness=0,bg='medium spring green',border=5)
frame2.grid(row=1,column=0,sticky='w')

Name = Label(frame2,text='Name',font=('Garamond',18),bg='medium spring green',pady=15,border=15)
Name.grid(row=1,column=0)
Name_entry = Entry(frame2,width=30)
Name_entry.grid(row=2,column=0)

Contact = Label(frame2,text='Contact Number',font=('Garamond',18),bg='medium spring green',border=15,pady=15)
Contact.grid(row=3,column=0)
Contact_entry = Entry(frame2,width=30)
Contact_entry.grid(row=4,column=0)

Email = Label(frame2,text='Email Address',font=('Garamond',18),bg='medium spring green',border=15,pady=15)
Email.grid(row=5,column=0)
Email_entry = Entry(frame2,width=30)
Email_entry.grid(row=6,column=0)

Gender = Label(frame2,text='Gender',font=('Garamond',18),bg='medium spring green',border=15,pady=15)
Gender.grid(row=7,column=0)
obj = StringVar()
Gender_select = ttk.Combobox(frame2,width=27,textvariable=obj)
Gender_select['values'] = ['Male','Female']
Gender_select.grid(row=8,column=0)

Dob = Label(frame2,text='Date of Birth (DOB)',font=('Garamond',18),bg='medium spring green',border=15,pady=15)
Dob.grid(row=9,column=0)
Dob_entry = DateEntry(frame2,width=27,date_pattern='yyyy-mm-dd')
Dob_entry.grid(row=10,column=0)

Stream = Label(frame2,text='Stream',font=('Garamond',18),bg='medium spring green',border=15,pady=15)
Stream.grid(row=11,column=0)
Stream_entry = Entry(frame2,width=30)
Stream_entry.grid(row=12,column=0)

btn = Button(frame2,text='Submit and Add Record',font=('Garamond',16),bg='white',border=2,width=21,command=InsertRecord)
btn.grid(row=13,column=0,pady=30)


#FRAME FOR FUNCTIONS
#Column 2
frame3 = Frame(window,height=5,highlightthickness=0,bg='blue',border=25,pady=217)
frame3.grid(row=1,column=1,sticky='w')
delbtn = Button(frame3,text='Delete Record',font=('Garamond',14),bg='white',border=2,width=20,command=DelRecord)
delbtn.grid(row=5,column=3,pady=15)

viewbtn = Button(frame3,text='View Record',font=('Garamond',14),bg='white',border=2,width=20,command=ViewRecord)
viewbtn.grid(row=6,column=3,pady=15)

resetbtn = Button(frame3,text='Reset Fields',font=('Garamond',14),bg='white',border=2,width=20,command=ResetField)
resetbtn.grid(row=7,column=3,pady=15)

deldatabase = Button(frame3,text='Delete Database',font=('Garamond',14),bg='white',border=2,width=20,command=DelDatbase)
deldatabase.grid(row=8,column=3,pady=15)

#FRAME FOR STUDENTS RECORDS HEADING and TREEVIEW OUTPUT
frame4 = Frame(window,bg='green',highlightthickness=0)
frame4.grid(row=1,column=2,sticky='n')
stuhead = Label(frame4,text='Students Records',padx=410,font=('Arial',15,'bold'),bg='green',foreground='white',justify='center')
stuhead.grid(row=1,column=2)

window.mainloop()