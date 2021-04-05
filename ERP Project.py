import tkinter as tk

from PIL import ImageTk,Image

from tkinter import messagebox

from tkinter import ttk

import pymysql as pym

import pickle

import time

'''**********************************************************************************'''
def Status_Hover(e):
    Status_Bar.config(text='')
    
def Status_Hover_Leave(e):
    Status_Bar.config(text='Coded By: Ikram, Meera Mohiddin, Jayanth                ')
    
def Status_Hover1(e):
    Status_Bar1.config(text='')
    
def Status_Hover_Leave1(e):
    Status_Bar1.config(text='Coded By: Ikram, Meera Mohiddin, Jayanth                ')
    
def Status_Hover2(e):
    Status_Bar2.config(text='')
    
def Status_Hover_Leave2(e):
    Status_Bar2.config(text='Coded By: Ikram, Meera Mohiddin, Jayanth                ')
    
def Status_Hover3(e):
    Status_Bar3.config(text='')
    
def Status_Hover_Leave3(e):
    Status_Bar3.config(text='Coded By: Ikram, Meera Mohiddin, Jayanth                ')
    
def Status_Hover4(e):
    Status_Bar4.config(text='')
    
def Status_Hover_Leave4(e):
    Status_Bar4.config(text='Coded By: Ikram, Meera Mohiddin, Jayanth                ')
    
def Status_Hover5(e):
    Status_Bar5.config(text='')
    
def Status_Hover_Leave5(e):
    Status_Bar5.config(text='Coded By: Ikram, Meera Mohiddin, Jayanth                ')
    
def Status_Hover6(e):
    Status_Bar6.config(text='')
    
def Status_Hover_Leave6(e):
    Status_Bar6.config(text='Coded By: Ikram, Meera Mohiddin, Jayanth                ')
    
def Status_Hover7(e):
    Status_Bar7.config(text='')
    
def Status_Hover_Leave7(e):
    Status_Bar7.config(text='Coded By: Ikram, Meera Mohiddin, Jayanth                ')


def Status_Hover8(e):
    Status_Bar8.config(text='')


def Status_Hover_Leave8(e):
    Status_Bar8.config(text='Coded By: Ikram, Meera Mohiddin, Jayanth                ')
    
'''***************************************************************************** '''

def clicker(event):
    Check_Username(Username_entry1.get().strip(),Password_entry1.get().strip())
    
def clicker1(event):
    Creating_File(Username_entry.get().strip(),Password_entry.get().strip(),Confirm_Password_entry.get().strip()) 
    
def clicker2(event):
    Check_Details_Student(int(Admission_entry.get().strip()))
    
def clicker3(event):
    Check_Details_Admin(int(Admission_entry1.get().strip()))
    
def clicker4(event):
    Admin_Update_Details(int(Admn_entry.get().strip()))
    
def clicker5(event):
    Add_Record(int(Admn_entry1.get().strip()),Name_entry.get().strip(),int(Class_entry.get().strip()),int(Totalfee_entry.get().strip()),int(Feepaid_entry.get().strip()),int(Feedue_entry.get().strip()))
    
def clicker6(event):
    Admin_Delete_Details(int(Admn_entry2.get().strip()))
    
'''****************************************************************************** '''
def Password_Show1(x):
    if x==1:
        Password_entry1.config(show='')
    if x==0:
        Password_entry1.config(show='*')
        
def Password_Show(x):
    if x==1:
        Password_entry.config(show='')
        Confirm_Password_entry.config(show='')
    if x==0:
        Password_entry.config(show='*')
        Confirm_Password_entry.config(show='*')


def Home_to_Create_Account():
    root.destroy()
    Create_Account_Screen()
    
def Create_Acc_to_Home():
    top.destroy()
    Home_Screen()
    
def Create_Acc_to_Create_Acc():
    top.destroy()
    Create_Account_Screen()

def Home_to_Login():
    root.destroy()
    Login_Screen()
    
def Login_to_Home():
    top1.destroy()
    Home_Screen()
    
def Login_to_Login():
    top1.destroy()
    Login_Screen()

def Login_to_Student_Details(Username):
    top1.destroy()
    if Username=='Accountant':
        Admin_Check_Screen()
    else:
        Student_Screen()
    
def Student_Screen_to_Home():
    top2.destroy()
    Home_Screen()

def Admin_Check_to_Home():
    top3.destroy()
    Home_Screen()
    
def Home_to_Developers():
    root.destroy()
    Developers_Screen()
    
def Admin_Update_to_Admin_Update():
    run.destroy()
    Admin_Update_Screen()
    
def Admin_Update_to_Home():
    run.destroy()
    Home_Screen()
    
def Admin_Add_to_Home():
    rec.destroy()
    Home_Screen()
    
def Admin_Del_to_Home():
    dele.destroy()
    Home_Screen()

def Devel_to_Home():
    dev.destroy()
    Home_Screen()
    
def Admin_view_to_Home():
    tree.destroy()
    Home_Screen()
'''*************************************************************************** '''
try:
    def Combo_Click(event):
        if Drop.get()=='Update Record':
            top3.destroy()
            Admin_Update_Screen()
            
        if Drop.get()=='Add Record':
            top3.destroy()
            Add_Record_Sceen()
            
        if Drop.get()=='Delete Record':
            top3.destroy()
            Delete_Record_Screen()
            
        if Drop.get()=='View Records':
            top3.destroy()
            Tree_Screen()
            
    def Combo_Click1(event):
        if Drop1.get()=='Search Record':
            run.destroy()
            Admin_Check_Screen()
            
        if Drop1.get()=='Add Record':
            run.destroy()
            Add_Record_Sceen()
            
        if Drop1.get()=='Delete Record':
            run.destroy()
            Delete_Record_Screen()
            
        if Drop1.get()=='View Records':
            run.destroy()
            Tree_Screen()
        
            
    def Combo_Click2(event):
        if Drop2.get()=='Search Record':
            rec.destroy()
            Admin_Check_Screen()
            
        if Drop2.get()=='Update Record':
            rec.destroy()
            Admin_Update_Screen()
            
        if Drop2.get()=='Delete Record':
            rec.destroy()
            Delete_Record_Screen()
            
        if Drop2.get()=='View Records':
            rec.destroy()
            Tree_Screen()
            
    
    def Combo_Click3(event):
        if Drop3.get()=='Search Record':
            dele.destroy()
            Admin_Check_Screen()
        
        if Drop3.get()=='Update Record':
            dele.destroy()
            Admin_Update_Screen()
            
        if Drop3.get()=='Add Record':
            dele.destroy()
            Add_Record_Sceen()
            
        if Drop3.get()=='View Records':
            dele.destroy()
            Tree_Screen()
            
    def Combo_Click4(event):
        if Drop4.get()=='Search Record':
            tree.destroy()
            Admin_Check_Screen()
        
        if Drop4.get()=='Update Record':
            tree.destroy()
            Admin_Update_Screen()
            
        if Drop4.get()=='Add Record':
            tree.destroy()
            Add_Record_Sceen()
            
        if Drop4.get()=='Delete Record':
            tree.destroy()
            Delete_Record_Screen()
            
except:
    print('')
'''************************************************************************* '''

def Tree_Screen():
    global tree
    tree=tk.Tk()
    tree.title('Details Screen')
    tree.geometry("1000x600")
    tree.iconbitmap('Icon.ico')
    
    my_pic=Image.open('Homepage0.jpg')
    
    
    resized=my_pic.resize((1000,600),Image.ANTIALIAS)
    new_pic=ImageTk.PhotoImage(resized)
    
    my_label=tk.Label(tree,image=new_pic)
    my_label.place(x=0,y=0)

    image = Image.open('logo.png')

    resized = image.resize((120, 150), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(resized)
    logo = tk.Label(tree, image=image, width=115, height=145)
    logo.place(x=0, y=0)
    
    style=ttk.Style()
    style.theme_use('alt')
    style.configure('Treeview',
                    background='silver',
                    foreground='black',
                    rowheight=25,
                    fieldbackground='silver')
    
    style.map('Treeview',background=[('selected','blue')])
    
    
    Tree=ttk.Treeview(tree,height=17)
    Tree['columns']=('Admn No','Name','Class','Total Fees','Fees Paid','Fees Due')
    
    Tree.column('#0',width=0,stretch='no')
    Tree.column('Admn No',anchor='w',width=120)
    Tree.column('Name',anchor='w',width=150)
    Tree.column('Class',anchor='w',width=120)
    Tree.column('Total Fees',anchor='w',width=150)
    Tree.column('Fees Paid',anchor='w',width=150)
    Tree.column('Fees Due',anchor='w',width=150)

    Tree.heading('#0',text='',anchor='w')
    Tree.heading('Admn No',text='Admn No',anchor='w')
    Tree.heading('Name',text='Name',anchor='w')
    Tree.heading('Class',text='Class',anchor='w')
    Tree.heading('Total Fees',text='Total Fees',anchor='w')
    Tree.heading('Fees Paid',text='Fees Paid',anchor='w')
    Tree.heading('Fees Due',text='Fees Due',anchor='w')
    
    count1=0
    
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='school')
    cur=mycon.cursor()
    
    cur.execute('select * from student')
    data=cur.fetchall()
    
    for i in data:
        Tree.insert(parent='',index='end',iid=count1,text='',values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        count1+=1
     
     
    Tree.place(x=100,y=55)
    
    Options=['Search Record','Update Record','Add Record','Delete Record','View Records']
    
    global Drop4
    Drop4=ttk.Combobox(tree,value=Options,width=15,font=("Courier",15,'bold'))
    Drop4.current(4)
    Drop4.place(x=745,y=15)
    Drop4.bind('<<ComboboxSelected>>',Combo_Click4)
    
    my_pic3=Image.open('Logout1.jpg')
    
    resized3=my_pic3.resize((140,80),Image.ANTIALIAS)
    new_pic3=ImageTk.PhotoImage(resized3)
    
    
    Confirm_Button=tk.Button(tree,image=new_pic3,borderwidth=0,width=135,height=75,command=Admin_view_to_Home)
    Confirm_Button.place(x=400,y=505)

    global Status_Bar8
    Status_Bar8 = tk.Label(tree, text='Coded By: Ikram, Meera Mohiddin, Jayanth            ', font=('bold'), bd=1,
                           relief='sunken', anchor='e')
    Status_Bar8.pack(fill='x', side='bottom')

    Status_Bar8.bind('<Enter>', Status_Hover8)
    Status_Bar8.bind('<Leave>', Status_Hover_Leave8)
    
    tree.mainloop()

def Delete_Record(Adno):
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='school')
    cur=mycon.cursor()
    c=messagebox.askyesno('Delete Record','The Record will be Permenantly Deleted')
    if c==1:
        st='DELETE FROM Student WHERE Admn_No=%s'%Adno
        
        cur.execute(st)
        mycon.commit()
        d=messagebox.showinfo('Record','Record Succesfully Deleted...!')
        if d=='ok':
            dele.destroy()
            Delete_Record_Screen()
            
    else:
        dele.destroy()
        Delete_Record_Screen()
                

def Admin_Delete_Details(Adno):
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='school')
    cur=mycon.cursor()
    
    cur.execute('select * from student')
    data=cur.fetchall()
    
    for stu in data:
        if stu[0]==Adno:
           
               

            
            
            time.sleep(0.5)
            
            Name3.config(text=stu[1])
            Class3.config(text=stu[2])
            Total_Fees3.config(text=stu[3])
            Fees_Paid3.config(text=stu[4])
            Fees_Due3.config(text=stu[5])

            global my_pic10
            my_pic10 = Image.open('Delete.png')

            global resized10
            resized10 = my_pic10.resize((140, 60), Image.ANTIALIAS)
            global new_pic10
            new_pic10 = ImageTk.PhotoImage(resized10)
            
            Delete_btn=tk.Button(dele,image=new_pic10,width=130,height=50,bd=0,command=lambda:Delete_Record(Adno))
            Delete_btn.place(x=400,y=440)
            break
    else:
        c=messagebox.showerror('Error!','Record Not Found...!')
        if c=='ok':
            dele.destroy()
            Delete_Record_Screen()

def Delete_Record_Screen():
    global dele
    dele=tk.Tk()
    dele.title('Update Screen')
    dele.geometry("1000x600")
    dele.iconbitmap('Icon.ico')
    
    my_pic=Image.open('Homepage.jpg')
    
    
    resized=my_pic.resize((1000,600),Image.ANTIALIAS)
    new_pic=ImageTk.PhotoImage(resized)
    
    my_label=tk.Label(dele,image=new_pic)
    my_label.place(x=0,y=0)

    image = Image.open('logo.png')

    resized = image.resize((120, 150), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(resized)
    logo = tk.Label(dele, image=image, width=115, height=145)
    logo.place(x=60, y=390)


    global Frame3
    Frame3 = tk.LabelFrame(dele, width=40)
    Frame3.place(x=300, y=80)

    Name = tk.Label(Frame3, text="Name:", font=("Helvetica", "22", "bold"))
    Name.grid(row=0, column=0, padx=20, pady=15)

    Standard = tk.Label(Frame3, text="Standard:", font=("Helvetica", "22", "bold"))
    Standard.grid(row=1, column=0, padx=20, pady=15)

    Totalfee = tk.Label(Frame3, text="Total Fee:", font=("Helvetica", "22", "bold"))
    Totalfee.grid(row=2, column=0, padx=20, pady=15)

    Feepaid = tk.Label(Frame3, text="Fee Paid:", font=("Helvetica", "22", "bold"))
    Feepaid.grid(row=3, column=0, padx=20, pady=15)

    Feedue = tk.Label(Frame3, text="Fee Due:", font=("Helvetica", "22", "bold"))
    Feedue.grid(row=4, column=0, padx=20, pady=15)

    global Name3
    Name3= tk.Label(Frame3, text='', font=("Helvetica", "22", "bold"))
    Name3.grid(row=0, column=1, padx=20, pady=15)

    global Class3
    Class3 = tk.Label(Frame3, text='', font=("Helvetica", "22", "bold"))
    Class3.grid(row=1, column=1, padx=20, pady=15)

    global Total_Fees3
    Total_Fees3 = tk.Label(Frame3, text='', font=("Helvetica", "22", "bold"))
    Total_Fees3.grid(row=2, column=1, padx=20, pady=15)

    global Fees_Paid3
    Fees_Paid3 = tk.Label(Frame3, text='', font=("Helvetica", "22", "bold"))
    Fees_Paid3.grid(row=3, column=1, padx=20, pady=15)

    global Fees_Due3
    Fees_Due3 = tk.Label(Frame3, text='', font=("Helvetica", "22", "bold"))
    Fees_Due3.grid(row=4, column=1, padx=20, pady=15)
        
    Admn=tk.Label(dele,text='ADMN NO.',font=("Helvetica", "25", "bold"))
    Admn.place(x=50,y=25)
    
    global Admn_entry2
    Admn_entry2=tk.Entry(dele,width=25,borderwidth=5,font=("Helvetica", "20", "bold"))
    Admn_entry2.place(x=240,y=25)
    
    Search_btn=tk.Button(dele,text='SERACH',font=("Helvetica", "15"),command=lambda:Admin_Delete_Details(int(Admn_entry2.get().strip())))
    Search_btn.place(x=640,y=25)
    
    my_pic3=Image.open('Logout.jpg')
    
    resized3=my_pic3.resize((140,80),Image.ANTIALIAS)
    new_pic3=ImageTk.PhotoImage(resized3)
    
    
    Confirm_Button=tk.Button(dele,image=new_pic3,borderwidth=0,width=135,height=75,command=Admin_Del_to_Home)
    Confirm_Button.place(x=400,y=500)
    
    Options=['Search Record','Update Record','Add Record','Delete Record','View Records']
    
    global Drop3
    Drop3=ttk.Combobox(dele,value=Options,width=15,font=("Courier",18,'bold'))
    Drop3.current(3)
    Drop3.place(x=750,y=35)
    Drop3.bind('<<ComboboxSelected>>',Combo_Click3)
    
    global Status_Bar7
    Status_Bar7=tk.Label(dele,text='Coded By: Ikram, Meera Mohiddin, Jayanth            ',font=('bold'),bd=1,relief='sunken',anchor='e')
    Status_Bar7.pack(fill='x',side='bottom')
    
    Status_Bar7.bind('<Enter>',Status_Hover7)
    Status_Bar7.bind('<Leave>',Status_Hover_Leave7)
    
    dele.bind('<Return>',clicker6)
    
    dele.mainloop()

    
def Add_Record(Adno,Name,Class,Total_Fees,Fees_Paid,Fees_Due):
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='school')
    cur=mycon.cursor()
    
    st='''INSERT INTO student(Admn_No,Name,Class,Total_Fees,Fees_Paid,Fees_due)
          VALUES({},'{}',{},{},{},{})'''.format(Adno,Name,Class,Total_Fees,Fees_Paid,Fees_Due)
    cur.execute(st)
    mycon.commit()
    c=messagebox.showinfo('Record','Record Succesfully Added...!')
    if c=='ok':
        rec.destroy()
        Add_Record_Sceen()

       
def Add_Record_Sceen():
    global rec
    rec=tk.Tk()
    rec.title('Update Screen')
    rec.geometry("1000x600")
    rec.iconbitmap('Icon.ico')



    
    my_pic=Image.open('Homepage.jpg')
    
    
    resized=my_pic.resize((1000,600),Image.ANTIALIAS)
    new_pic=ImageTk.PhotoImage(resized)
    
    my_label=tk.Label(rec,image=new_pic)
    my_label.place(x=0,y=0)

    image = Image.open('logo.png')

    resized = image.resize((120, 150), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(resized)
    logo = tk.Label(rec, image=image, width=115, height=145)
    logo.place(x=75, y=420)

    
    Admn=tk.Label(rec,text='ADMN NO.',font=("Helvetica", "25", "bold"))
    Admn.place(x=50,y=45)
    
    global Admn_entry1
    Admn_entry1=tk.Entry(rec,width=25,borderwidth=5,font=("Helvetica", "20", "bold"))
    Admn_entry1.place(x=240,y=45)
    
    Name=tk.Label(rec,text='Name:',font=("Helvetica", "25", "bold"))
    Name.place(x=10,y=150)
    
    global Name_entry
    Name_entry=tk.Entry(rec,width=28,borderwidth=5,font=("Helvetica", "18", "bold"))
    Name_entry.place(x=120,y=150)
    
    
    Class=tk.Label(rec,text='Class:',font=("Helvetica", "20", "bold"))
    Class.place(x=505,y=150)
    
    global Class_entry
    Class_entry=tk.Entry(rec,width=25,borderwidth=5,font=("Helvetica", "20", "bold"))
    Class_entry.place(x=590,y=150)

    
    Totalfee=tk.Label(rec,text='Total fee:',font=("Helvetica", "20", "bold"))
    Totalfee.place(x=10,y=275)
    
    global Totalfee_entry
    Totalfee_entry=tk.Entry(rec,width=20,borderwidth=5,font=("Helvetica", "20", "bold"))
    Totalfee_entry.place(x=145,y=275)
 
    
    Feepaid=tk.Label(rec,text='Fee Paid:',font=("Helvetica", "20", "bold"))
    Feepaid.place(x=475,y=275)
    
    global Feepaid_entry
    Feepaid_entry=tk.Entry(rec,width=25,borderwidth=5,font=("Helvetica", "20", "bold"))
    Feepaid_entry.place(x=600,y=275)
 
    Fee_Due=tk.Label(rec,text='Fee Due:',font=("Helvetica", "20", "bold"))
    Fee_Due.place(x=150,y=350)
    
    global Feedue_entry
    Feedue_entry=tk.Entry(rec,width=30,borderwidth=5,font=("Helvetica", "20", "bold"))
    Feedue_entry.place(x=330,y=350)

    my_pic4 = Image.open('register.png')

    resized4 = my_pic4.resize((220, 75), Image.ANTIALIAS)
    new_pic4 = ImageTk.PhotoImage(resized4)
    
    Add_btn=tk.Button(rec,image=new_pic4,width=210,height=70,command=lambda:Add_Record(int(Admn_entry1.get().strip()),Name_entry.get().strip(),int(Class_entry.get().strip()),int(Totalfee_entry.get().strip()),int(Feepaid_entry.get().strip()),int(Feedue_entry.get().strip())))
    Add_btn.place(x=375,y=415)
    
    my_pic3=Image.open('logout.jpg')
    
    resized3=my_pic3.resize((175,75),Image.ANTIALIAS)
    new_pic3=ImageTk.PhotoImage(resized3)
    
    
    Confirm_Button=tk.Button(rec,image=new_pic3,borderwidth=0,width=170,height=70,command=Admin_Add_to_Home)
    Confirm_Button.place(x=400,y=500)
    
    Options=['Search Record','Update Record','Add Record','Delete Record','View Records']
    
    global Drop2
    Drop2=ttk.Combobox(rec,value=Options,width=15,font=("Courier",17,'bold'))
    Drop2.current(2)
    Drop2.place(x=700,y=45)
    Drop2.bind('<<ComboboxSelected>>',Combo_Click2)
    
    global Status_Bar6
    Status_Bar6=tk.Label(rec,text='Coded By: Ikram, Meera Mohiddin, Jayanth            ',font=('bold'),bd=1,relief='sunken',anchor='e')
    Status_Bar6.pack(fill='x',side='bottom')
    
    Status_Bar6.bind('<Enter>',Status_Hover6)
    Status_Bar6.bind('<Leave>',Status_Hover_Leave6)
    
    rec.bind('<Return>',clicker5)
    
    rec.mainloop()     


def Update_Details(Adno,Name,Class,Total_Fees,Fees_Paid,Fees_Due):
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='school')
    cur=mycon.cursor()
    
    Name_Update='''UPDATE student 
                    SET Name='{}'
                   WHERE Admn_No={}'''.format(Name,Adno)
                   
    Class_Update='''UPDATE student SET Class={}
                   WHERE Admn_No={}'''.format(int(Class),Adno)
                   
    Total_Fees_Update='''UPDATE student SET Total_Fees={}
                   WHERE Admn_No={}'''.format(int(Total_Fees),Adno)
                   
    Fees_Paid_Update='''UPDATE student SET Fees_Paid={}
                   WHERE Admn_No={}'''.format(int(Fees_Paid),Adno)
                   
    Fees_Due_Update='''UPDATE student SET Fees_Due={}
                   WHERE Admn_No={}'''.format(int(Fees_Due),Adno)
                   
    cur.execute(Name_Update)
    cur.execute(Class_Update)
    cur.execute(Total_Fees_Update)
    cur.execute(Fees_Paid_Update)
    cur.execute(Fees_Due_Update)
    mycon.commit()
    c=messagebox.showinfo('Record','Record Successfully Updated...!')
    if c=='ok':
        Admin_Update_to_Admin_Update()

    
def Admin_Update_Details(Adno):

    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='school')
    cur=mycon.cursor()
    
    cur.execute('select * from student')
    data=cur.fetchall()
    
    for stu in data:
        if stu[0]==Adno:
            Name=tk.Label(run,text='Name:',font=("Helvetica", "25", "bold"))
            Name.place(x=10,y=150)
            
            Name_entry=tk.Entry(run,width=28,borderwidth=5,font=("Helvetica", "18", "bold"))
            Name_entry.place(x=120,y=150)
            Name_entry.insert(0,stu[1])
            
            
            Class=tk.Label(run,text='Class:',font=("Helvetica", "20", "bold"))
            Class.place(x=505,y=150)
            
            
            Class_entry=tk.Entry(run,width=25,borderwidth=5,font=("Helvetica", "20", "bold"))
            Class_entry.place(x=590,y=150)
            Class_entry.insert(0,stu[2])
            
            
            Totalfee=tk.Label(run,text='Total fee:',font=("Helvetica", "20", "bold"))
            Totalfee.place(x=10,y=275)
            
            Totalfee_entry=tk.Entry(run,width=20,borderwidth=5,font=("Helvetica", "20", "bold"))
            Totalfee_entry.place(x=145,y=275)
            Totalfee_entry.insert(0,stu[3])
            
            
            Feepaid=tk.Label(run,text='Fee Paid:',font=("Helvetica", "20", "bold"))
            Feepaid.place(x=475,y=275)
            
            Feepaid_entry=tk.Entry(run,width=25,borderwidth=5,font=("Helvetica", "20", "bold"))
            Feepaid_entry.place(x=600,y=275)
            Feepaid_entry.insert(0,stu[4])
            
            
            Fee_Due=tk.Label(run,text='Fee Due:',font=("Helvetica", "20", "bold"))
            Fee_Due.place(x=150,y=360)
            
            Feedue_entry=tk.Entry(run,width=30,borderwidth=5,font=("Helvetica", "20", "bold"))
            Feedue_entry.place(x=330,y=360)
            Feedue_entry.insert(0,stu[5])

            global my_pic
            my_pic= Image.open('Update.png')

            global resized
            resized = my_pic.resize((175, 75), Image.ANTIALIAS)
            global new_pic
            new_pic = ImageTk.PhotoImage(resized)

            Update_btn=tk.Button(run,image=new_pic,width=170,height=70,bd=0,command=lambda:Update_Details(Adno,Name_entry.get().strip(),Class_entry.get().strip(),Totalfee_entry.get().strip(),Feepaid_entry.get().strip(),Feedue_entry.get().strip()))
            Update_btn.place(x=400,y=415)
            
            break
    else:
        c=messagebox.showerror('Error','Record Not Found')
        if c=='ok':
            run.destroy()
            Admin_Update_Screen()
    
        
def Admin_Update_Screen():
    
    global run
    run=tk.Tk()
    run.title('Update Screen')
    run.geometry("1000x600")
    run.iconbitmap('Icon.ico')


    my_pic=Image.open('Homepage.jpg')
    
    
    resized=my_pic.resize((1000,600),Image.ANTIALIAS)
    new_pic=ImageTk.PhotoImage(resized)
    
    my_label=tk.Label(run,image=new_pic)
    my_label.place(x=0,y=0)

    image = Image.open('logo.png')

    resized = image.resize((120, 150), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(resized)
    logo = tk.Label(run, image=image, width=115, height=145)
    logo.place(x=50, y=400)
        
    Admn=tk.Label(run,text='ADMN NO.',font=("Helvetica", "25", "bold"))
    Admn.place(x=50,y=45)
    
    global Admn_entry
    Admn_entry=tk.Entry(run,width=25,borderwidth=5,font=("Helvetica", "20", "bold"))
    Admn_entry.place(x=240,y=45)
    
    Search_btn=tk.Button(run,text='SERACH',font=("Helvetica", "15"),command=lambda:Admin_Update_Details(int(Admn_entry.get().strip())))
    Search_btn.place(x=640,y=45)
    
    my_pic3=Image.open('logout.jpg')
    
    resized3=my_pic3.resize((175,75),Image.ANTIALIAS)
    new_pic3=ImageTk.PhotoImage(resized3)
    
    
    Confirm_Button=tk.Button(run,image=new_pic3,width=170,height=70,borderwidth=0,command=Admin_Update_to_Home)
    Confirm_Button.place(x=400,y=500)
    
    Options=['Search Record','Update Record','Add Record','Delete Record','View Records']
    
    global Drop1
    Drop1=ttk.Combobox(run,value=Options,width=15,font=("Courier",16,'bold'))
    Drop1.current(1)
    Drop1.place(x=765,y=45)
    Drop1.bind('<<ComboboxSelected>>',Combo_Click1)
    
    global Status_Bar5
    Status_Bar5=tk.Label(run,text='Coded By: Ikram, Meera Mohiddin, Jayanth            ',font=('bold'),bd=1,relief='sunken',anchor='e')
    Status_Bar5.pack(fill='x',side='bottom')
    
    Status_Bar5.bind('<Enter>',Status_Hover5)
    Status_Bar5.bind('<Leave>',Status_Hover_Leave5)
    
    run.bind('<Return>',clicker4)
    
    run.mainloop()



def Check_Details_Admin(adno):
  
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='school')
    cur=mycon.cursor()
    
    cur.execute('select * from student')
    data=cur.fetchall()
    
    
    for stu in data:
        if stu[0]==adno:
        
           
            
            Name1.config(text=stu[1])
            Class1.config(text=stu[2])
            Total_Fees1.config(text=stu[3])
            Fees_Paid1.config(text=stu[4])
            Fees_Due1.config(text=stu[5])
            
           
         
            
            break
    else:
        c=messagebox.showerror('Error!','Record Not Found..!')
        if c=='ok':
            top3.destroy()
            Admin_Check_Screen()

def Admin_Check_Screen():
    
    global top3
    top3=tk.Tk()
    top3.title('Admission Screen')
    top3.geometry('1000x600')
    top3.iconbitmap('Icon.ico')




    my_pic=Image.open('homepage.jpg')
    
    
    resized=my_pic.resize((1000,600),Image.ANTIALIAS)
    new_pic=ImageTk.PhotoImage(resized)
    
    my_label=tk.Label(top3,image=new_pic)
    my_label.place(x=0,y=0)

    image = Image.open('logo.png')

    resized = image.resize((150, 170), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(resized)
    logo = tk.Label(top3, image=image, width=115, height=145)
    logo.place(x=50, y=290)

    
    Options=['Search Record','Update Record','Add Record','Delete Record','View Records']
    
    global Drop
    Drop=ttk.Combobox(top3,value=Options,width=15,font=("Courier",16,'bold'))
    Drop.current(0)
    Drop.place(x=773,y=27)
    Drop.bind('<<ComboboxSelected>>',Combo_Click)
    
    Admission=tk.Label(top3,text='Admn No.',font=(''"Helvetica", "25", "bold"))
    Admission.place(x=20,y=20)
    
    global Admission_entry1
    Admission_entry1=tk.Entry(top3,width=30,borderwidth=5,font=("Helvetica", "20", "bold"))
    Admission_entry1.place(x=200,y=20)
    
    global Frame
    Frame=tk.LabelFrame(top3,height=100)
    Frame.place(x=300,y=100)
    
    
    Name=tk.Label(Frame,text="Name:",font=("Helvetica", "25", "bold"))
    Name.grid(row=0,column=0,padx=20,pady=15)
    
    Standard=tk.Label(Frame,text="Standard:",font=("Helvetica", "25", "bold"))
    Standard.grid(row=1,column=0,padx=20,pady=15)
    
    Totalfee=tk.Label(Frame,text="Total Fee:",font=("Helvetica", "25", "bold"))
    Totalfee.grid(row=2,column=0,padx=20,pady=15)
    
    
    Feepaid=tk.Label(Frame,text="Fee Paid:",font=("Helvetica", "25", "bold"))
    Feepaid.grid(row=3,column=0,padx=20,pady=15)
   

    Feedue=tk.Label(Frame,text="Fee Due:",font=("Helvetica", "25", "bold"))
    Feedue.grid(row=4,column=0,padx=20,pady=15)
    
    time.sleep(0.3)
    
    global Name1
    Name1=tk.Label(Frame,text='',font=("Helvetica", "25", "bold"))
    Name1.grid(row=0,column=1,padx=20,pady=15)
         
    global Class1
    Class1=tk.Label(Frame,text='',font=("Helvetica", "25", "bold"))
    Class1.grid(row=1,column=1,padx=20,pady=15)
   
    global Total_Fees1
    Total_Fees1=tk.Label(Frame,text='',font=("Helvetica", "25", "bold"))
    Total_Fees1.grid(row=2,column=1,padx=20,pady=15)
    
    global Fees_Paid1
    Fees_Paid1=tk.Label(Frame,text='',font=("Helvetica", "25", "bold"))
    Fees_Paid1.grid(row=3,column=1,padx=20,pady=15)
    
    global Fees_Due1
    Fees_Due1=tk.Label(Frame,text='',font=("Helvetica", "25", "bold"))
    Fees_Due1.grid(row=4,column=1,padx=20,pady=15)
    
    
    button=tk.Button(top3,text="SEARCH",font=("Helvetica", "15"),command=lambda:Check_Details_Admin(int(Admission_entry1.get().strip())))
    button.place(x=675,y=25)
    
    my_pic3=Image.open('Logout.jpg')


    resized3=my_pic3.resize((240,100),Image.ANTIALIAS)
    new_pic3=ImageTk.PhotoImage(resized3)


    Logout_Button=tk.Button(top3,image=new_pic3,borderwidth=0,width=235,height=95,command=Admin_Check_to_Home)
    Logout_Button.place(x=345,y=475)
    
    global Status_Bar4
    Status_Bar4=tk.Label(top3,text='Coded By: Ikram, Meera Mohiddin, Jayanth            ',font=('bold'),bd=1,relief='sunken',anchor='e')
    Status_Bar4.pack(fill='x',side='bottom')
    
    Status_Bar4.bind('<Enter>',Status_Hover4)
    Status_Bar4.bind('<Leave>',Status_Hover_Leave4)
    
    top3.bind('<Return>',clicker3)
    
    top3.mainloop()


    
        
def Check_Details_Student(adno):
    
    mycon=pym.connect(host='localhost',user='root',passwd='tiger',database='school')
    cur=mycon.cursor()
    
    cur.execute('select * from student')
    data=cur.fetchall()
    
    for stu in data:
        if stu[0]==adno:
            

            
            time.sleep(0.5)
            
            Name2.config(text=stu[1])
            Class2.config(text=stu[2])
            Total_Fees2.config(text=stu[3])
            Fees_Paid2.config(text=stu[4])
            Fees_Due2.config(text=stu[5])
            
            break
    else:
        c=messagebox.showerror('Error!','Record Not Found..!')
        if c=='ok':
            top2.destroy()
            Student_Screen()
        
def Student_Screen():
    
    global top2
    top2=tk.Tk()
    top2.title('Admission Screen')
    top2.geometry('1000x600')
    top2.iconbitmap('Icon.ico')





    my_pic=Image.open('homepage.jpg')
    
    
    resized=my_pic.resize((1000,600),Image.ANTIALIAS)
    new_pic=ImageTk.PhotoImage(resized)
    
    my_label=tk.Label(top2,image=new_pic)
    my_label.place(x=0,y=0)



    image1 = Image.open('logo.png')

    resized1 = image1.resize((155, 160), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(resized1)
    logo1 = tk.Label(top2, image=image1, width=120, height=145)
    logo1.place(x=50, y=330)



    Admission=tk.Label(top2,text='Admn No.',font=(''"Helvetica", "25", "bold"))
    Admission.place(x=20,y=20)
    
    global Admission_entry
    Admission_entry=tk.Entry(top2,width=40,borderwidth=5,font=("Helvetica", "20", "bold"))
    Admission_entry.place(x=200,y=20)

    global Frame1
    Frame1 = tk.LabelFrame(top2, width=40)
    Frame1.place(x=300, y=100)

    Name = tk.Label(Frame1, text="Name:", font=("Helvetica", "25", "bold"))
    Name.grid(row=0, column=0, padx=20, pady=15)

    Standard = tk.Label(Frame1, text="Standard:", font=("Helvetica", "25", "bold"))
    Standard.grid(row=1, column=0, padx=20, pady=15)

    Totalfee = tk.Label(Frame1, text="Total Fee:", font=("Helvetica", "25", "bold"))
    Totalfee.grid(row=2, column=0, padx=20, pady=15)

    Feepaid = tk.Label(Frame1, text="Fee Paid:", font=("Helvetica", "25", "bold"))
    Feepaid.grid(row=3, column=0, padx=20, pady=15)

    Feedue = tk.Label(Frame1, text="Fee Due:", font=("Helvetica", "25", "bold"))
    Feedue.grid(row=4, column=0, padx=20, pady=15)

    global Name2
    Name2 = tk.Label(Frame1, text='', font=("Helvetica", "25", "bold"))
    Name2.grid(row=0, column=1, padx=20, pady=15)

    global Class2
    Class2 = tk.Label(Frame1, text='', font=("Helvetica", "25", "bold"))
    Class2.grid(row=1, column=1, padx=20, pady=15)

    global Total_Fees2
    Total_Fees2 = tk.Label(Frame1, text='', font=("Helvetica", "25", "bold"))
    Total_Fees2.grid(row=2, column=1, padx=20, pady=15)

    global Fees_Paid2
    Fees_Paid2 = tk.Label(Frame1, text='', font=("Helvetica", "25", "bold"))
    Fees_Paid2.grid(row=3, column=1, padx=20, pady=15)

    global Fees_Due2
    Fees_Due2 = tk.Label(Frame1, text='', font=("Helvetica", "25", "bold"))
    Fees_Due2.grid(row=4, column=1, padx=20, pady=15)

    button=tk.Button(top2,text="SEARCH",font=("Helvetica", "15"),command=lambda:Check_Details_Student(int(Admission_entry.get().strip())))
    button.place(x=825,y=25)
    
    my_pic3=Image.open('Logout.jpg')


    resized3=my_pic3.resize((240,100),Image.ANTIALIAS)
    new_pic3=ImageTk.PhotoImage(resized3)


    Logout_Button=tk.Button(top2,image=new_pic3,borderwidth=0,width=235,height=95,command=Student_Screen_to_Home)
    Logout_Button.place(x=345,y=475)
    
    global Status_Bar3
    Status_Bar3=tk.Label(top2,text='Coded By: Ikram, Meera Mohiddin, Jayanth            ',font=('bold'),bd=1,relief='sunken',anchor='e')
    Status_Bar3.pack(fill='x',side='bottom')
    
    Status_Bar3.bind('<Enter>',Status_Hover3)
    Status_Bar3.bind('<Leave>',Status_Hover_Leave3)
    
    top2.bind('<Return>',clicker2)
    
    top2.mainloop()



    
def checking_username(Username):
    Acc={}
    Acc_file=open('Acc.dat','rb')
    
    try:
        while True:
            Acc=pickle.load(Acc_file)
            
            if Username==Acc['Username']:
                return True
            
    except EOFError:
        return False
    
    
def Check_Username(Username,Password):
    Acc={}
    Acc_file=open('Acc.dat','rb')
    
    try:
        while True:
            Acc=pickle.load(Acc_file)
            if Username=='':
                c=messagebox.showerror('Error!','Username Empty..!')
                break
            
            if Username==Acc['Username']:
                if Password==Acc['Password']:
                   c=messagebox.showinfo('Account','Login succesful!')
                   if c=='ok':
                       Login_to_Student_Details(Username)
                       break
                   
                   
        
    except EOFError:
        c=messagebox.showerror('Error','Check Credentials')
        if c=='ok':
            Login_to_Login()
        Acc_file.close()
    
def Login_Screen():
    
    global top1
    top1=tk.Tk()
    top1.title('Login')
    top1.geometry('1000x600')
    top1.iconbitmap('Icon.ico')
    
   
   
    my_pic2=Image.open('Homepage.jpg')
    
    
    resized2=my_pic2.resize((1000,600),Image.ANTIALIAS)
    new_pic2=ImageTk.PhotoImage(resized2)
    
    
    my_label2=tk.Label(top1,image=new_pic2)
    my_label2.place(x=0,y=0)
    
    
    image = Image.open('logo.png')

    resized = image.resize((120, 120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(resized)
    logo = tk.Label(top1, image=image,width=115,height=115)
    logo.place(x=30, y=10)

    Heading = tk.Label(top1, text='GVK CHINMAYA VIDYALAYA', bg='#050505', fg='red',font=("Helvetica", "45", "bold italic"))
    Heading.place(x=130, y=30)
    
    Username=tk.Label(top1,text='Username',font=(''"Helvetica", "25", "bold"))
    Username.place(x=70,y=170)
    
    global Username_entry1
    Username_entry1=tk.Entry(top1,width=40,borderwidth=5,font=("Helvetica", "20", "bold"))
    Username_entry1.place(x=250,y=170)
    
    
    Password=tk.Label(top1,text="Password",font=("Helvetica", "25", "bold"))
    Password.place(x=70,y=280) 
    
    global Password_entry1
    Password_entry1=tk.Entry(top1,show='*',width=40,borderwidth=5,font=("Helvetica", "20", "bold"))
    Password_entry1.place(x=250,y=280)
    
    var=tk.IntVar()
    var.set(0)
    
    CheckBox=tk.Checkbutton(top1,text='Show Password',variable=var,command=lambda:Password_Show1(var.get()))
    CheckBox.place(x=725,y=330)
   
    
    my_pic8=Image.open('Submit.jpg')


    resized8=my_pic8.resize((220,75),Image.ANTIALIAS)
    new_pic8=ImageTk.PhotoImage(resized8)


    Submit_Button=tk.Button(top1,image=new_pic8,borderwidth=0,width=215,height=70,command=lambda: Check_Username(Username_entry1.get().strip(),Password_entry1.get().strip()))
    Submit_Button.place(x=400,y=360)
    
    
    
    my_pic9=Image.open('Home.jpg')


    resized9=my_pic9.resize((220,75),Image.ANTIALIAS)
    new_pic9=ImageTk.PhotoImage(resized9)


    Home_Button=tk.Button(top1,image=new_pic9,borderwidth=0,width=215,height=70,command=Login_to_Home)
    Home_Button.place(x=400,y=450)
    
    
    global Status_Bar2
    Status_Bar2=tk.Label(top1,text='Coded By: Ikram, Meera Mohiddin, Jayanth            ',font=('bold'),bd=1,relief='sunken',anchor='e')
    Status_Bar2.pack(fill='x',side='bottom')
    
    Status_Bar2.bind('<Enter>',Status_Hover2)
    Status_Bar2.bind('<Leave>',Status_Hover_Leave2)
    
    top1.bind('<Return>',clicker)
    
    top1.mainloop()

       

def Creating_File(Username,Password,Confirm_Password):

    for i in range(1):    

        if Password!=Confirm_Password:
            messagebox.showwarning('Error!','Password and Confirm Password are not same')
         
     
        if Username=='':
            c=messagebox.showerror('Error!','Username empty..!')
            if c=='ok':
                Create_Acc_to_Create_Acc()
                
        if Password=='':
            c=messagebox.showerror('Error!','Password Empty..!')
            if c=='ok':
                Create_Acc_to_Create_Acc()
                break
                
        Co_Username=checking_username(Username)
        
        if Co_Username==True:
            c=messagebox.showerror('Error!','Username Already exists!')
            if c=='ok':
                Create_Acc_to_Create_Acc()
            
        if Co_Username==False:
        
            if Password==Confirm_Password:
                Acc={}
                Acc_file=open('Acc.dat','ab+')
                Acc['Username']=Username
                Acc['Password']=Password
            
                   
                        
                pickle.dump(Acc,Acc_file)
                Acc_file.close()
                c=messagebox.showinfo('Account','Account Succesfully Created!')
                if c=='ok':
                    Create_Acc_to_Home()


def Create_Account_Screen():

    
    global top
    top=tk.Tk()
    top.title('Create Your Account')
    top.geometry('1000x600')
    top.iconbitmap('Icon.ico')
    
   
    my_pic2=Image.open('homepage.jpg')
    
    
    resized2=my_pic2.resize((1000,600),Image.ANTIALIAS)
    new_pic2=ImageTk.PhotoImage(resized2)
    
    my_label2=tk.Label(top,image=new_pic2)
    my_label2.place(x=0,y=0)

    image1 = Image.open('logo.png')

    resized = image1.resize((120, 120), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(resized)
    logo = tk.Label(top,image=image1,width=115,height=115)
    logo.place(x=30, y=10)

    Heading = tk.Label(top, text='GVK CHINMAYA VIDYALAYA', bg='#000000', fg='red',font=("Helvetica", "40", "bold italic"))
    Heading.place(x=175, y=25)
    
    Username=tk.Label(top,text='Username',font=(''"Helvetica", "25", "bold"))
    Username.place(x=50,y=140)
    
    global Username_entry
    Username_entry=tk.Entry(top,width=40,borderwidth=5,font=("Helvetica", "20", "bold"))
    Username_entry.place(x=220,y=140)
    
    
    Password=tk.Label(top,text="Password",font=("Helvetica", "25", "bold"))
    Password.place(x=50,y=230) 
    
    global Password_entry
    Password_entry=tk.Entry(top,show='*',width=40,borderwidth=5,font=("Helvetica", "20", "bold"))
    Password_entry.place(x=240,y=240)
    
    
    Confirm_Password=tk.Label(top,text="Confirm Password",font=("Helvetica", "20", "bold"))
    Confirm_Password.place(x=20,y=330) 
    
    global Confirm_Password_entry
    Confirm_Password_entry=tk.Entry(top,show='*',width=40,borderwidth=5,font=("Helvetica", "20", "bold"))
    Confirm_Password_entry.place(x=280,y=330)
   
   
   
    my_pic3=Image.open('Submit.jpg')


    resized3=my_pic3.resize((220,75),Image.ANTIALIAS)
    new_pic3=ImageTk.PhotoImage(resized3)


    Confirm_Button=tk.Button(top,image=new_pic3,borderwidth=0,width=215,height=70,command=lambda:Creating_File(Username_entry.get().strip(),Password_entry.get().strip(),Confirm_Password_entry.get().strip()))
    Confirm_Button.place(x=400,y=410)
    
    
    my_pic4=Image.open('Home.jpg')


    resized4=my_pic4.resize((220,75),Image.ANTIALIAS)
    new_pic4=ImageTk.PhotoImage(resized4)


    Home_Button=tk.Button(top,image=new_pic4,borderwidth=0,width=215,height=70,command=Create_Acc_to_Home)
    Home_Button.place(x=400,y=500)
    
    var=tk.IntVar()
    var.set(0)
    
    CheckBox=tk.Checkbutton(top,text='Show Password',variable=var,command=lambda:Password_Show(var.get()))
    CheckBox.place(x=750,y=380) 
    
    global Status_Bar1
    Status_Bar1=tk.Label(top,text='Coded By: Ikram, Meera Mohiddin, Jayanth            ',font=('bold'),bd=1,relief='sunken',anchor='e')
    Status_Bar1.pack(fill='x',side='bottom')
    
    Status_Bar1.bind('<Enter>',Status_Hover1)
    Status_Bar1.bind('<Leave>',Status_Hover_Leave1)
    
    top.bind('<Return>',clicker1)
    
    top.mainloop()


def Developers_Screen():
    global dev
    dev=tk.Tk()
    dev.title('Developers')
    dev.geometry('1000x600')
    dev.iconbitmap('Icon.ico')
    
    dev.config(bg='yellow')
    
    image = Image.open('logo1.png')

    resized = image.resize((120, 120), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(resized)
    logo = tk.Label(dev, image=image,width=115,height=115)
    logo.place(x=100, y=0)

    Heading = tk.Label(dev, text='GVK CHINMAYA VIDYALAYA', bg='yellow', fg='red',font=("Helvetica", "35", "bold italic"))
    Heading.place(x=250, y=15)
    
    Heading=tk.Label(dev,text='Developers',bg='yellow',font=("Helvetica","30","bold italic"))
    Heading.place(x=425,y=90)
    
    my_pic=Image.open('Sample.jpg')
    resized=my_pic.resize((200 ,150),Image.ANTIALIAS)
    new_pic=ImageTk.PhotoImage(resized)
    
    my_pic1=Image.open('Sample.jpg')
    resized1=my_pic1.resize((200 ,150),Image.ANTIALIAS)
    new_pic1=ImageTk.PhotoImage(resized1)
    
    my_pic2=Image.open('Sample.jpg')
    resized2=my_pic2.resize((200 ,150),Image.ANTIALIAS)
    new_pic2=ImageTk.PhotoImage(resized2)
    
    Ikram_pic=tk.Label(dev,image=new_pic,bd=4)
    Ikram_pic.place(x=50,y=115)
    
    Meera_pic=tk.Label(dev,image=new_pic1,bd=4)
    Meera_pic.place(x=50,y=275)
    
    Jayanth_pic=tk.Label(dev,image=new_pic2,bd=4)
    Jayanth_pic.place(x=50,y=435)
    
    Name=tk.Label(dev,text='Name :',bg='yellow',font=("Helvetica","25","bold"))
    Name1=tk.Label(dev,text='Name :',bg='yellow',font=("Helvetica","25","bold"))
    Name2=tk.Label(dev,text='Name :',bg='yellow',font=("Helvetica","25","bold"))
    
    Class=tk.Label(dev,text='Class :',bg='yellow',font=("Helvetica","25","bold"))
    Class1=tk.Label(dev,text='Class :',bg='yellow',font=("Helvetica","25","bold"))
    Class2=tk.Label(dev,text='Class :',bg='yellow',font=("Helvetica","25","bold"))
    
    Ikram_Label=tk.Label(dev,text='Mohammed Ikram',bg='yellow',font=("Albertus Extra Bold","28","bold"))
    Meera_Label=tk.Label(dev,text='Meera Mohiddin',bg='yellow',font=("Albertus Extra Bold","28","bold"))
    Jayanth_Label=tk.Label(dev,text='Jayanth Kumar',bg='yellow',font=("Albertus Extra Bold","28","bold"))
    
    Class_Label=tk.Label(dev,text='12',bg='yellow',font=("Albertus Extra Bold","28","bold"))
    Class_Label1=tk.Label(dev,text='12',bg='yellow',font=("Albertus Extra Bold","28","bold"))
    Class_Label2=tk.Label(dev,text='12',bg='yellow',font=("Albertus Extra Bold","28","bold"))
    
    Name.place(x=300,y=160)
    Ikram_Label.place(x=420,y=160)
    Class.place(x=300,y=220)
    Class_Label.place(x=420,y=220)
    
    Name1.place(x=300,y=295)
    Meera_Label.place(x=420,y=295)
    Class1.place(x=300,y=355)
    Class_Label1.place(x=420,y=355)
    
    Name2.place(x=300,y=455)
    Jayanth_Label.place(x=420,y=455)
    Class2.place(x=300,y=520)
    Class_Label2.place(x=420,y=520)
    
    my_pic3=Image.open('Home1.jpg')
  
    resized3=my_pic3.resize((200,90),Image.ANTIALIAS)
    new_pic3=ImageTk.PhotoImage(resized3)
    
    Home_btn=tk.Button(dev,image=new_pic3,borderwidth=0,width=195,height=85 ,command=Devel_to_Home)
    Home_btn.place(x=780,y=500)
    
    
    dev.mainloop()
    

def animation(count):

    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == Frames:
        count = 0
    root.after(50,lambda: animation(count))

def Home_Screen():
    global root
    root=tk.Tk()
    root.title('Enterprice Resource Planning')
    root.geometry('1000x600')
   
  
    file="a10.gif"  
  
    info = Image.open(file)
    global Frames
    Frames = info.n_frames
    
    global im
    im =[tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(Frames)]
    count=0
    
    global gif_label
    gif_label = tk.Label(root,image="")
    gif_label.place(x=-30,y=0)

    image = Image.open('logo.png')

    resized = image.resize((120, 150), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(resized)
    logo = tk.Label(root, image=image,width=115,height=145)
    logo.place(x=0, y=0)

    Heading = tk.Label(root, text='GVK CHINMAYA VIDYALAYA', bg='#050505', fg='red',font=("Helvetica", "45", "bold italic"))
    Heading.place(x=130, y=30)

    Heading = tk.Label(root, text='Enterprise Resource Planning', bg='#050505', fg='yellow',font=("Helvetica", "45", "bold italic"))
    Heading.place(x=80, y=150)
    
    my_pic1=Image.open('Create Account.JPG')
    
    resized1=my_pic1.resize((400 ,75),Image.ANTIALIAS)
    new_pic1=ImageTk.PhotoImage(resized1)
    
    Craete_Acc_btn=tk.Button(root,image=new_pic1,borderwidth=0,width=395,height=70,command=Home_to_Create_Account)
    Craete_Acc_btn.place(x=530,y=300)
    
    my_pic5=Image.open('Login.jpg')
    
    
    resized5=my_pic5.resize((400,75),Image.ANTIALIAS)
    new_pic5=ImageTk.PhotoImage(resized5)
    
    
    Login_btn=tk.Button(root,image=new_pic5,borderwidth=0,width=395,height=70,command=Home_to_Login)
    Login_btn.place(x=530,y=455)
    

    my_pic6=Image.open('exit2.jpg')
  
    
    resized6=my_pic6.resize((200,125),Image.ANTIALIAS)
    new_pic6=ImageTk.PhotoImage(resized6)
    
    
    Quit_btn=tk.Button(root,image=new_pic6,borderwidth=0,width=195,height=120,command=root.destroy)
    Quit_btn.place(x=100,y=400)
    
    
    global Status_Bar
    Status_Bar=tk.Label(root,text='Coded By: Ikram, Meera Mohiddin, Jayanth            ',font=('bold'),bd=1,relief='sunken',anchor='e')
    Status_Bar.pack(fill='x',side='bottom')
    
    Status_Bar.bind('<Enter>',Status_Hover)
    Status_Bar.bind('<Leave>',Status_Hover_Leave)
    

    my_pic10=Image.open('aboutus.png')
    
    
    resized10=my_pic10.resize((200,100),Image.ANTIALIAS)
    new_pic10=ImageTk.PhotoImage(resized10)
    
    
    Developers_btn=tk.Button(root,image=new_pic10,borderwidth=0,command=Home_to_Developers,width=195,height=95)
    Developers_btn.place(x=100,y=250)
    
    root.iconbitmap('Icon.ico')
    
    
    root.after(-10,animation,0)
    
    
    root.mainloop()
Home_Screen()
