from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as m_box
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
from tkinter import filedialog
import datetime
import time;
from time import strftime
import csv
from csv import DictWriter
from csv import DictReader
import os


class shop:
    def __init__(self,root):
        self.root = root
        self.root.geometry("970x600+150+50")
        self.root.title('Shop Management Sysytem')
        self.root.iconbitmap('dress_icon_2.ico')
        self.root.resizable(False,False)
        self.root.configure(background= '#009595')

        # ====================  Date  ==============================
        date_string = strftime("%d/%m/%Y")
        date_label =  Label(self.root,text=date_string,height=1,bd=4,background="#009595",fg='white',font=("Times New Roman",18))
        date_label.place(x=850,y=80)

        # ====================  first label  ========================
        lbl_first = Label(self.root,text="Shop Management System",pady=15,padx=20,relief=RIDGE,fg='white',bg="#009595",font=("Old English Text MT",30))
        lbl_first.pack(fill=X)
        
        # ==========================  Buttons  ==========================
        btn1 = Button(self.root,text="Add product /\nPurchase",height=2,width=16,pady=8,command=self.add_product,fg='white',bg="#097777",font=("Andalus",18),activebackground="#075f5f",activeforeground = "white")
        btn1.place(x=100,y=210)
        btn2 = Button(self.root,text="Supplier Detail",height=2,width=16,pady=8,command = self.search_supplier,fg='white',bg="#097777",font=("Andalus",18),activebackground="#075f5f",activeforeground = "white")
        btn2.place(x=380,y=210)
        btn3 = Button(self.root,text="product\nSale",height=2,width=16,pady=8,command=self.sale_product,fg='white',bg="#097777",font=("Andalus",18),activebackground="#075f5f",activeforeground = "white")
        btn3.place(x=660,y=210)
        btn4 = Button(self.root,text="Customer Detail",height=2,width=16,pady=8,command=self.search_Sales,fg='white',bg="#097777",font=("Andalus",18),activebackground="#075f5f",activeforeground = "white")
        btn4.place(x=100,y=387)
        btn5 = Button(self.root,text="Balance",height=2,width=16,pady=8,command=self.Balance_fun,fg='white',bg="#097777",font=("Andalus",18),activebackground="#075f5f",activeforeground = "white")
        btn5.place(x=380,y=387)
        btn6 = Button(self.root,text="Stock",height=2,width=16,pady=8,command =self.stack,fg='white',bg="#097777",font=("Andalus",18),activebackground="#075f5f",activeforeground = "white")
        btn6.place(x=660,y=387)
    
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    #                               Add Product function
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    def add_product(self):
        first_frame = Frame(self.root,height=600,width=970,bg="#009595")
        first_frame.place(x=0,y=0)
        second_frame = Frame(first_frame,height=480,width=300,relief=GROOVE,bd=3)
        second_frame.place(x=650,y=100)
        # =====================================  Labels =========================================
        Top_lbl = Label(first_frame,text="Add New Product",pady=15,padx=334,fg='white',bg="#009595",font=("Old English Text MT",30),relief=RIDGE)
        Top_lbl.place(x=0,y=0)

        lbl_1 = Label(first_frame,text="Product Name:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_1.place(x=50,y=130)

        lbl_2 = Label(first_frame,text="Item Price:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_2.place(x=345,y=130)
        lbl_3 = Label(first_frame,text="PKR",fg='white',bg="#009595",font=("Mongolian Baiti",12))
        lbl_3.place(x=590,y=135)

        lbl_4 = Label(first_frame,text="Item Quantity:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_4.place(x=50,y=180)

        lbl_5 = Label(first_frame,text="Item Quality:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_5.place(x=345,y=180)

        lbl_6 = Label(first_frame,text="Contect No:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_6.place(x=50,y=230)

        lbl_7 = Label(first_frame,text="ID No:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_7.place(x=345,y=230)

        lbl_8 = Label(first_frame,text="From:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_8.place(x=50,y=280)

        lbl_9 = Label(first_frame,text="Date:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_9.place(x=220,y=348)
        lbl_10 = Label(first_frame,text="Day",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_10.place(x=290,y=325)
        lbl_11 = Label(first_frame,text="Month",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_11.place(x=370,y=325)
        lbl_12 = Label(first_frame,text="Year",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_12.place(x=463,y=325)

        lbl_13 = Label(first_frame,text="Email Address:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_13.place(x=50,y=400)

        # =====================================  variables ==========================================
        name = StringVar()
        price = StringVar()
        quantity = StringVar()
        quality = StringVar()
        contect = StringVar()
        Id = StringVar()
        From = StringVar()
        day = StringVar()
        month = StringVar()
        year = StringVar()
        Email = StringVar()

        # =====================================  Entry boxes =========================================
        list_1 = []
        for i in range(2000,2100):
            list_1.append(i)
        my_yaer=tuple(list_1)

        entry_box_1 = Entry(first_frame, width=18,textvariable=name,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_1.place(x=180,y=130)
        entry_box_1.focus()

        entry_box_2 = Entry(first_frame, width=16,textvariable=price,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_2.place(x=450,y=130)
        
        entry_box_3 = Entry(first_frame, width=18,textvariable=quantity,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_3.place(x=180,y=180)

        entry_box_4 = Entry(first_frame, width=16,textvariable=quality,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_4.place(x=450,y=180)

        entry_box_5 = Entry(first_frame, width=18,textvariable=contect,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_5.place(x=180,y=230)

        entry_box_6 = Entry(first_frame, width=16,textvariable=Id,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_6.place(x=450,y=230)

        entry_box_7 = Entry(first_frame, width=50,textvariable=From,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_7.place(x=180,y=280)

        combo_entry_1 = ttk.Combobox(first_frame, width=5,textvariable=day,font=("Times New Roman",12))
        combo_entry_1["values"] = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
        combo_entry_1.place(x=280,y=350)
        combo_entry_2 = ttk.Combobox(first_frame, width=8,textvariable=month,font=("Times New Roman",12))
        combo_entry_2["values"] = ("January","February","March","April","May","June","July","August","September","October","November","December")
        combo_entry_2.place(x=355,y=350)
        combo_entry_3 = ttk.Combobox(first_frame, width=6,textvariable=year,font=("Times New Roman",12))
        combo_entry_3["values"] = my_yaer
        combo_entry_3.place(x=453,y=350) 

        entry_box_8 = Entry(first_frame, width=50,textvariable=Email,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_8.place(x=180,y=400)


        def cal():
            # ===========  get the variable  =======================
            Name = name.get()
            pri = int(price.get())
            quant = int(quantity.get())
            qual = quality.get()
            frome = From.get()
            Contect = contect.get()
            iD = Id.get()
            email = Email.get()
            Day = day.get()
            Month = month.get()
            Year = year.get()
            #==================   for calculating dues the current ID number ============================= 
                            
            if os.path.exists('shope_database.csv'):
                with open('shope_database.csv' , 'r') as f:
                    rows = csv.reader(f)
                    count = 0
                    my_list = []
                    first_list = []
                    for row in rows:
                        if iD in row:
                            my_list.append(row)
                            count+=1
                    if count>0:
                        first_list = my_list[-1]
                        dues = int(first_list[-1])
                    else:
                        dues = 0
            else:
                dues = 0

            # ==============  Variable  ===========================
            DUES = StringVar()
            DUES.set(dues)

            NAME = StringVar()
            NAME.set(Name)
    
            QUANT = StringVar()
            QUANT.set(quant)

            ID = StringVar()
            ID.set(iD)

            QUAL = StringVar()
            QUAL.set(qual)

            PRICE  =StringVar()
            PRICE.set(pri)

            DATE = StringVar()
            DATE.set(Day+" "+Month+" "+Year)

            FROM = StringVar()
            FROM.set(frome)

            cont = StringVar()
            cont.set(Contect)

            Emal = StringVar()
            Emal.set(email)

            tot = quant*pri
            total_price = IntVar()
            total_price.set(tot+dues)

            adjust = StringVar()
            paid = StringVar()

            lbl_1 = Label(second_frame,text="Dues:",font=("Mongolian Baiti",14))
            lbl_1.place(x=5,y=16)
            entry_box_1 = Entry(second_frame,textvariable=DUES , width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_1.place(x=130,y=16)

            lbl_2 = Label(second_frame,text="Product Name:",font=("Mongolian Baiti",14))
            lbl_2.place(x=5,y=44)
            entry_box_2 = Entry(second_frame,textvariable=NAME , width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_2.place(x=130,y=44)

            lbl_3 = Label(second_frame,text="ID no:",font=("Mongolian Baiti",14))
            lbl_3.place(x=5,y=72)
            entry_box_3 = Entry(second_frame,textvariable=ID , width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_3.place(x=130,y=72)

            lbl_4 = Label(second_frame,text="Item Quantity:",font=("Mongolian Baiti",14))
            lbl_4.place(x=5,y=100)
            entry_box_5 = Entry(second_frame,textvariable=QUANT ,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_5.place(x=130,y=100)

            lbl_6 = Label(second_frame,text="Item Price:",font=("Mongolian Baiti",14))
            lbl_6.place(x=5,y=128)
            entry_box_6 = Entry(second_frame, textvariable=PRICE,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_6.place(x=130,y=128)

            lbl_7 = Label(second_frame,text="Item Quality:",font=("Mongolian Baiti",14))
            lbl_7.place(x=5,y=156)
            entry_box_7 = Entry(second_frame,textvariable=QUAL ,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_7.place(x=130,y=156)
            
            lbl_8 = Label(second_frame,text="Date:",font=("Mongolian Baiti",14))
            lbl_8.place(x=5,y=184)
            entry_box_8 = Entry(second_frame,textvariable=DATE, width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_8.place(x=130,y=184)

            
            lbl_9 = Label(second_frame,text="Fram:",font=("Mongolian Baiti",14))
            lbl_9.place(x=5,y=212)
            entry_box_9 = Entry(second_frame,textvariable=FROM, width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_9.place(x=130,y=212)

            lbl_10 = Label(second_frame,text="Contact:",font=("Mongolian Baiti",14))
            lbl_10.place(x=5,y=240)
            entry_box_10 = Entry(second_frame,textvariable=cont, width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_10.place(x=130,y=240)

            lbl_11 = Label(second_frame,text="Email:",font=("Mongolian Baiti",14))
            lbl_11.place(x=5,y=268)
            entry_box_11 = Entry(second_frame,textvariable=Emal, width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_11.place(x=130,y=268)

            lbl_12 = Label(second_frame,text="Total Price:",font=("Mongolian Baiti",14,"bold"))
            lbl_12.place(x=5,y=300)
            entry_box_12 = Entry(second_frame, textvariable = total_price,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_12.place(x=130,y=300)
        
            lbl_13 = Label(second_frame,text="Discount:",font=("Mongolian Baiti",14))
            lbl_13.place(x=5,y=328)
            entry_box_13 = Entry(second_frame,textvariable=adjust ,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_13.place(x=130,y=328)

            lbl_14 = Label(second_frame,text="Paid:",font=("Mongolian Baiti",14))
            lbl_14.place(x=5,y=358)
            entry_box_14 = Entry(second_frame,textvariable = paid, width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_14.place(x=130,y=358)

            lbl_15 = Label(second_frame,text="Balance:",font=("Mongolian Baiti",14,"bold"))
            lbl_15.place(x=5,y=388)
            entry_box_15 = Entry(second_frame,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_15.place(x=130,y=388)
            
            def calculate():
                T = tot+dues
                Ad = int(adjust.get())
                Pai = int(paid.get())

                Rs = Pai+Ad
                amount =T-Rs

                balance = StringVar()
                balance.set(amount)
                entry_box_cal = Entry(second_frame,textvariable = balance ,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
                entry_box_cal.place(x=130,y=388)

            def clear():
                entry_box_1.delete(0,tk.END)
                entry_box_2.delete(0,tk.END)
                entry_box_3.delete(0,tk.END)
                entry_box_4.delete(0,tk.END)
                entry_box_5.delete(0,tk.END)
                entry_box_6.delete(0,tk.END)
                entry_box_7.delete(0,tk.END)
                entry_box_8.delete(0,tk.END)
                entry_box_9.delete(0,tk.END)
                entry_box_10.delete(0,tk.END)
                entry_box_11.delete(0,tk.END)
                entry_box_12.delete(0,tk.END)
                entry_box_13.delete(0,tk.END)
                entry_box_14.delete(0,tk.END)
                entry_box_15_cal = Entry(second_frame,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
                entry_box_15_cal.place(x=130,y=388)

            def save():
                due = int(DUES.get())
                name = NAME.get()
                id_no =  ID.get()
                quantity = int(QUANT.get())
                qualit = quality.get()
                price = int(PRICE.get())
                D = Day
                M = Month
                Y = Year
                From = FROM.get()
                Cont = cont.get()
                Eml = Emal.get()
                tot = quantity*price
                T = tot+due
                Adj = int(adjust.get())
                Paid = int(paid.get())

                minus = Adj + Paid
                bal = T-minus
                if bal<0:
                    m_box.showerror("Error","Please check the paid Balance\nThe Paid balance is Greater the the total ")
                else:
                    with open('shope_database.csv' , 'a',newline='') as f:
                        dict_writter = DictWriter(f,fieldnames=['Name','ID','Quantity','Price','Quality','Day','Month','Year','Company','Contect','Email','Dues','Total',
                            'Adjust','Paid','Balance'])
                        if os.stat('shope_database.csv').st_size==0:
                            dict_writter.writeheader()
                        dict_writter.writerow({
                            'Name' : name,
                            'ID':id_no,
                            'Quantity': quantity,
                            'Price':price,
                            'Quality':qualit,
                            'Day':D,
                            'Month':M,
                            'Year':Y,
                            'Company':From,
                            'Contect':Cont,
                            'Email': Eml,
                            'Dues':due,
                            'Total':tot,
                            'Adjust':Adj,
                            'Paid':Paid,
                            'Balance':bal
                        })
                        messagebox.showinfo("information","Your Record is Saved Successfully")
                        clear()
        # ================  Buttons  =================================

            btn1 = Button(second_frame,text="Calculate",width=10,fg='white',command = calculate,bg="#097777",font=("Andalus",10),activebackground="#075f5f",activeforeground = "white")
            btn1.place(x=70,y=430)

            btn2 = Button(second_frame,text="Save",width=10,fg='white',command = save,bg="#097777",font=("Andalus",10),activebackground="#075f5f",activeforeground = "white")
            btn2.place(x=160,y=430)


        btn1 = Button(first_frame,text="Calculate",width=10,fg='white',bg="#097777",command=cal,font=("Andalus",10),activebackground="#075f5f",activeforeground = "white")
        btn1.place(x=550,y=530)
        btn2 = Button(first_frame,text="Back",width=10,fg='white',bg="#097777",command=first_frame.destroy,font=("Andalus",10),activebackground="#075f5f",activeforeground = "white")
        btn2.place(x=450,y=530)
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    #                               search Supplier Detail function 
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    def search_supplier(self):
        list_1 = []
        if os.path.exists("shope_database.csv"):
            with open("shope_database.csv","r") as f:
                rows = csv.reader(f)
                my_list = [i for i in rows]
            my_list.pop(0)
            id_list = sorted([j[1] for j in my_list])
            lis = []
            for i in id_list:
                if i not in lis: 
                    lis.append(i)
        else:
            lis = ['No item']
            # print(lis)
        # =================================  Frames   ==================================
        first_frame = Frame(self.root,height=600,width=970,bg="#009595")
        first_frame.place(x=0,y=0)

        rough_frame = Frame(first_frame,relief=GROOVE,bd=3)
        rough_frame.place(y=100,x=3,height=435,width=630)

        second_frame = Frame(first_frame,height=480,width=300,relief=GROOVE,bd=3)
        second_frame.place(x=650,y=100)

        # ==================================  header Label  ============================
        Top_lbl = Label(first_frame,text="show supplier detail",pady=15,padx=326,fg='white',bg="#009595",font=("Old English Text MT",30),relief=RIDGE)
        Top_lbl.place(x=0,y=0)

        # ==============================  For search data  ==============================
        lbl_first = Label(second_frame,text="search detail",fg='#009699',font=("Old English Text MT",30,'bold'))
        lbl_first.place(x=40,y=15)
        
        lbl5 = Label(second_frame,text="Select Supplier ID",fg='#009595',font=("Mongolian Baiti",16))
        lbl5.place(x=70,y=80)
        
        # ========================   Variable  =======================
        ID_supplier = StringVar()
        combo_box_search_1 = ttk.Combobox(second_frame, width=8,textvariable=ID_supplier,font=("Times New Roman",12))
        combo_box_search_1["values"] = (lis)
        combo_box_search_1.place(x=105,y=120)
        
        # ===================================== Show data =======================================
        # =====================================  Labels =========================================
        def search():
            id_supplier = ID_supplier.get()
            if id_supplier=="":
                m_box.showerror('Error','you do not pass the values\nplease try again.... ')
            else:
                if os.path.exists("shope_database.csv"):
                    right_first2 = Frame(first_frame,relief=GROOVE,bd=3)#-------->  frmae are created for scrool
                    right_first2.place(y=100,x=3,height=435,width=630)    

                    style = ttk.Style()
                    style.configure('Treeview.Heading',font=("Times New Roman",14,'bold'))
                    style.configure('Treeview',font=("Times New Roman",14),background="cyan",foreground='black')
                    scroll_x = Scrollbar(right_first2,orient=HORIZONTAL)
                    scroll_y = Scrollbar(right_first2,orient=VERTICAL)

                    studenttabel = Treeview(right_first2 , columns=('Name','ID','Quantity','Price','Quality','Day','Month','Year',
                        'Company','Contect No','Email','Dues','Total','Discount','Paid','Balance'),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

                    scroll_x.pack(side=BOTTOM,fill=X)
                    scroll_y.pack(side=RIGHT,fill=Y)
                    scroll_x.config(command=studenttabel.xview)
                    scroll_y.config(command=studenttabel.yview)

                    studenttabel.heading('Name', text="Name")
                    studenttabel.heading('ID', text="ID")
                    studenttabel.heading('Quantity', text="Quantity")
                    studenttabel.heading('Price', text='Price')
                    studenttabel.heading('Quality', text="Quality")
                    studenttabel.heading('Day', text="Day")
                    studenttabel.heading('Month', text="Month")
                    studenttabel.heading('Year', text="Year")
                    studenttabel.heading('Company', text="Company")
                    studenttabel.heading('Contect No', text="Contect No")
                    studenttabel.heading('Email', text="Email")
                    studenttabel.heading('Dues', text="Dues")
                    studenttabel.heading('Total', text="Total")
                    studenttabel.heading('Discount', text="Discount")
                    studenttabel.heading('Paid', text="Paid")
                    studenttabel.heading('Balance', text="Balance")

                    studenttabel['show']='headings'

                    studenttabel.column('Name',width=150)
                    studenttabel.column('ID',width=70)
                    studenttabel.column('Quantity',width=100)
                    studenttabel.column('Price',width=90)
                    studenttabel.column('Quality',width=100)
                    studenttabel.column('Day',width=70)
                    studenttabel.column('Month',width=90)
                    studenttabel.column('Year',width=70)
                    studenttabel.column('Company',width=250)
                    studenttabel.column('Contect No',width=130)
                    studenttabel.column('Email',width=250)
                    studenttabel.column('Dues',width=90)
                    studenttabel.column('Total',width=90)
                    studenttabel.column('Discount',width=90)
                    studenttabel.column('Paid',width=90)
                    studenttabel.column('Balance',width=100)
                   
                    studenttabel.pack(fill=BOTH,expand=1) 


                    with open("shope_database.csv","r") as file:
                        rows = csv.reader(file)
                        rough_list = [i for i in rows if id_supplier == i[1] ]
                    for i in rough_list:
                        list_1= [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15]]
                        studenttabel.insert('',END,values=list_1)
                else:
                    messagebox.showerror("Error","There is no file in this directory ")
        # ================================== button  ======================
        btn_1 = Button(second_frame,width=11,text="Search",fg='white',bg="#097777",command=search,activebackground="#075f5f",activeforeground = "white")
        btn_1.place(x=105,y=155)

        # ===================  show previous detail on ID no  ==========================
        lbl_previous = Label(second_frame,text="Previous Last detail",fg='#009699',font=("Old English Text MT",24,'bold'))
        lbl_previous.place(x=0,y=240)
        
        
        lbl_1 = Label(second_frame,text="Select ID of Supplier",fg='#009595',font=("Mongolian Baiti",16))
        lbl_1.place(x=55,y=280)
        ID = StringVar()
        combo_box_search_2 = ttk.Combobox(second_frame, width=8,textvariable=ID,font=("Times New Roman",12))
        combo_box_search_2["values"] = (lis)
        combo_box_search_2.place(x=100,y=320)

        def search_by_ID():
            id_sup = ID.get()
            if id_sup=="":
                messagebox.showerror("Error","Please Enter ID of Supplier")
            else:
                if os.path.exists("shope_database.csv"):
                    count = 0
                    with open("shope_database.csv","r") as f:
                        rows = csv.reader(f)
                        my_list = [i for i in rows]
                        spici_list = []
                        for i in my_list:  
                            if id_sup == i[1]:
                                spici_list.append(i)
                                count+=1
                    if count>0:
                        last_list = spici_list[-1]
                        right_first1 = Frame(first_frame,relief=GROOVE,bd=3)
                        right_first1.place(y=100,x=3,height=435,width=630)

                        lbl_1 = Label(right_first1,text="Product Name:",font=("Mongolian Baiti",14))
                        lbl_1.place(x=10,y=10)

                        lbl_2 = Label(right_first1,text="Item Price:",font=("Mongolian Baiti",14))
                        lbl_2.place(x=305,y=10)
                        lbl_3 = Label(right_first1,text="PKR",font=("Mongolian Baiti",12))
                        lbl_3.place(x=550,y=10)

                        lbl_4 = Label(right_first1,text="Item Quantity:",font=("Mongolian Baiti",14))
                        lbl_4.place(x=10,y=50)

                        lbl_5 = Label(right_first1,text="Item Quality:",font=("Mongolian Baiti",14))
                        lbl_5.place(x=305,y=50)

                        lbl_6 = Label(right_first1,text="Contect No:",font=("Mongolian Baiti",14))
                        lbl_6.place(x=10,y=90)

                        lbl_7 = Label(right_first1,text="ID No:",font=("Mongolian Baiti",14))
                        lbl_7.place(x=305,y=90)

                        lbl_8 = Label(right_first1,text="From:",font=("Mongolian Baiti",14))
                        lbl_8.place(x=10,y=130)

                        lbl_9 = Label(right_first1,text="Date:",font=("Mongolian Baiti",14))
                        lbl_9.place(x=190,y=190)
                        lbl_10 = Label(right_first1,text="Day",font=("Mongolian Baiti",14))
                        lbl_10.place(x=260,y=160)
                        lbl_11 = Label(right_first1,text="Month",font=("Mongolian Baiti",14))
                        lbl_11.place(x=340,y=160)
                        lbl_12 = Label(right_first1,text="Year",font=("Mongolian Baiti",14))
                        lbl_12.place(x=433,y=160)

                        lbl_13 = Label(right_first1,text="Email Address:",font=("Mongolian Baiti",14))
                        lbl_13.place(x=10,y=230)

                        lbl_14 = Label(right_first1,text="Dues:",font=("Mongolian Baiti",14))
                        lbl_14.place(x=10,y=270)

                        lbl_15 = Label(right_first1,text="Total:",font=("Mongolian Baiti",14))
                        lbl_15.place(x=315,y=270)

                        lbl_16 = Label(right_first1,text="Discount:",font=("Mongolian Baiti",14))
                        lbl_16.place(x=10,y=310)

                        lbl1_17 = Label(right_first1,text="Paid:",font=("Mongolian Baiti",14))
                        lbl1_17.place(x=315,y=310)

                        lbl_18 = Label(right_first1,text="Balance:",font=("Mongolian Baiti",14))
                        lbl_18.place(x=10,y=350)

                        lbl1_19 = Label(right_first1,text="RePaid:",font=("Mongolian Baiti",14))
                        lbl1_19.place(x=315,y=350)

                        # =====================================  variables ==========================================
                        name = StringVar()
                        price = StringVar()
                        quantity = StringVar()
                        quality = StringVar()
                        contect = StringVar()
                        Id = StringVar()
                        From = StringVar()
                        day = StringVar()
                        month = StringVar()
                        year = StringVar()
                        Email = StringVar()
                        due = StringVar()
                        total = StringVar()
                        adjust = StringVar()
                        paid = StringVar()
                        balance = StringVar()
                        Repaid = StringVar()

                        
                        name.set(last_list[0])
                        Id.set(last_list[1])
                        quantity.set(last_list[2])
                        price.set(last_list[3])
                        quality.set(last_list[4])
                        day.set(last_list[5])
                        month.set(last_list[6])
                        year.set(last_list[7])
                        From.set(last_list[8])
                        contect.set(last_list[9])
                        Email.set(last_list[10])
                        due.set(last_list[11])
                        total.set(last_list[12])
                        adjust.set(last_list[13])
                        paid.set(last_list[14])
                        balance.set(last_list[15])

                        # =====================================  Entry boxes =========================================
                        list_1 = []
                        for i in range(2000,3000):
                            list_1.append(i)
                        my_yaer=tuple(list_1)

                        entry_box_1 = Entry(right_first1, width=18,textvariable=name,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_1.place(x=140,y=10)
                        entry_box_1.focus()

                        entry_box_2 = Entry(right_first1, width=16,textvariable=price,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_2.place(x=410,y=10)
                        
                        entry_box_3 = Entry(right_first1, width=18,textvariable=quantity,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_3.place(x=140,y=50)

                        entry_box_4 = Entry(right_first1, width=16,textvariable=quality,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_4.place(x=410,y=50)

                        entry_box_5 = Entry(right_first1, width=18,textvariable=contect,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_5.place(x=140,y=90)

                        entry_box_6 = Entry(right_first1, width=16,textvariable=Id,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_6.place(x=410,y=90)

                        entry_box_7 = Entry(right_first1, width=50,textvariable=From,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_7.place(x=140,y=130)

                        combo_box_1 = ttk.Combobox(right_first1, width=5,textvariable=day,font=("Times New Roman",12))
                        combo_box_1["values"] = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
                        combo_box_1.place(x=250,y=190)
                        combo_box_2 = ttk.Combobox(right_first1, width=8,textvariable=month,font=("Times New Roman",12))
                        combo_box_2["values"] = ("January","February","March","April","May","June","July","August","September","October","November","December")
                        combo_box_2.place(x=325,y=190)
                        combo_box_3 = ttk.Combobox(right_first1, width=6,textvariable=year,font=("Times New Roman",12))
                        combo_box_3["values"] = my_yaer
                        combo_box_3.place(x=423,y=190) 

                        entry_box_8 = Entry(right_first1, width=50,textvariable=Email,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_8.place(x=140,y=230)
            
                        entry_box_9 = Entry(right_first1, width=18,textvariable=due,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_9.place(x=140,y=270)

                        entry_box_10 = Entry(right_first1, width=16,textvariable=total,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_10.place(x=412,y=270)

                        entry_box_11 = Entry(right_first1, width=18,textvariable=adjust,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_11.place(x=140,y=310)

                        entry_box_12 = Entry(right_first1, width=16,textvariable=paid,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_12.place(x=412,y=310)

                        entry_box_13 = Entry(right_first1, width=18,textvariable=balance,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_13.place(x=140,y=350)

                        entry_box_14 = Entry(right_first1, width=16,textvariable=Repaid,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_14.place(x=412,y=350)
                        
                        def Balance_fun(repaid):
                            Balance = int(balance.get())
                            rebalance = int(repaid)
                            total_balance = (Balance-rebalance)
                            return total_balance

                        def paid_total(paid_second):
                            piad_first = int(paid.get())
                            total = int(piad_first)+int(paid_second)
                            return total
                        def fram_default():
                            right_first2 = Frame(first_frame,relief=GROOVE,bd=3)
                            right_first2.place(y=100,x=3,height=435,width=630)
                        
                        def subm():
                            repaid = Repaid.get()
                            if repaid=="":
                                m_box.showerror("Error","The data can't Submitte\nPlease Enter Repaid data")
                            else:
                                last_paid = paid_total(repaid)
                                Balnc = Balance_fun(repaid)
                                last_list[0] = name.get()
                                last_list[1] = Id.get()
                                last_list[2] = quantity.get()
                                last_list[3] = price.get()
                                last_list[4] = quality.get()
                                last_list[5] = day.get()
                                last_list[6] = month.get()
                                last_list[7] = year.get()
                                last_list[8] = From.get()
                                last_list[9] = contect.get()
                                last_list[10] = Email.get()
                                last_list[11] = due.get()
                                last_list[12] = total.get()
                                last_list[13] = adjust.get()
                                last_list[14] = last_paid
                                last_list[15] = Balnc
                                if Balnc<0:
                                    m_box.showerror("Error","Please check the paid Balance\nThe Paid balance is Greater the the total ")
                                else:
                                    opt = messagebox.askyesno("Information","Do you want to Update the record")
                                    if opt>0:
                                        with open("shope_database.csv","w",newline="") as f:
                                            rows = csv.writer(f,lineterminator="\n")
                                            rows.writerows(my_list)
                                        fram_default()
                                        combo_box_search_1.delete(0,tk.END)
                                        combo_box_search_2.delete(0,tk.END)
                                    else:
                                        return 0
                        butten_1 = Button(right_first1,width=8,text="Submitte",command=subm,fg='white',bg="#097777",activebackground="#075f5f",activeforeground = "white")
                        butten_1.place(x=553,y=400)
                    else:
                        messagebox.showerror("Error",f"There is no Entry on this ID\nID : {id_sup}")
                else:
                    messagebox.showerror("Error","There is no file in this directory ")
            
            
            

        butten_1 = Button(second_frame,width=11,text="Search",fg='white',bg="#097777",command=search_by_ID,activebackground="#075f5f",activeforeground = "white")
        butten_1.place(x=100,y=350)

        btn2 = Button(first_frame,text="Back",width=10,height=2,fg='white',bg="#097777",command=first_frame.destroy,activebackground="#075f5f",activeforeground = "white")
        btn2.place(x=553,y=540)



    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    #                             Sale product function
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& 
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    def sale_product(self):
        first_frame = Frame(self.root,height=600,width=970,bg="#009595")
        first_frame.place(x=0,y=0)
        second_frame = Frame(first_frame,height=480,width=300,relief=GROOVE,bd=3)
        second_frame.place(x=650,y=100)
        # =====================================  Labels =========================================
        Top_lbl = Label(first_frame,text="Sale Product",pady=15,padx=375,fg='white',bg="#009595",font=("Old English Text MT",30),relief=RIDGE)
        Top_lbl.place(x=0,y=0)

        lbl_1 = Label(first_frame,text="Product Name:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_1.place(x=50,y=130)

        lbl_2 = Label(first_frame,text="Item Price:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_2.place(x=345,y=130)
        lbl_3 = Label(first_frame,text="PKR",fg='white',bg="#009595",font=("Mongolian Baiti",12))
        lbl_3.place(x=590,y=135)

        lbl_4 = Label(first_frame,text="Item Quantity:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_4.place(x=50,y=180)

        lbl_5 = Label(first_frame,text="Item Quality:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_5.place(x=345,y=180)

        lbl_6 = Label(first_frame,text="Contect No:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_6.place(x=50,y=230)

        lbl_7 = Label(first_frame,text="ID No:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_7.place(x=345,y=230)

        lbl_8 = Label(first_frame,text="To:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_8.place(x=50,y=280)

        lbl_9 = Label(first_frame,text="Date:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_9.place(x=180,y=348)
        lbl_10 = Label(first_frame,text="Day",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_10.place(x=260,y=325)
        lbl_11 = Label(first_frame,text="Month",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_11.place(x=340,y=325)
        lbl_12 = Label(first_frame,text="Year",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_12.place(x=433,y=325)

        lbl_13 = Label(first_frame,text="Email Address:",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_13.place(x=50,y=400)

        # =====================================  variables ==========================================
        name_saler = StringVar()
        price_saler = StringVar()
        quantity_saler = StringVar()
        quality_saler = StringVar()
        contect_saler = StringVar()
        Id_saler = StringVar()
        To_saler = StringVar()
        day_saler = StringVar()
        month_saler = StringVar()
        year_saler = StringVar()
        Email_saler = StringVar()

        # =====================================  Entry boxes =========================================
        list_1 = []
        for i in range(2000,2100):
            list_1.append(i)
        my_yaer=tuple(list_1)

        entry_box_1 = Entry(first_frame, width=18,textvariable=name_saler,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_1.place(x=180,y=130)
        entry_box_1.focus()

        entry_box_2 = Entry(first_frame, width=16,textvariable=price_saler,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_2.place(x=450,y=130)
        
        entry_box_3 = Entry(first_frame, width=18,textvariable=quantity_saler,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_3.place(x=180,y=180)

        entry_box_4 = Entry(first_frame, width=16,textvariable=quality_saler,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_4.place(x=450,y=180)

        entry_box_5 = Entry(first_frame, width=18,textvariable=contect_saler,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_5.place(x=180,y=230)

        entry_box_6 = Entry(first_frame, width=16,textvariable=Id_saler,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_6.place(x=450,y=230)

        entry_box_7 = Entry(first_frame, width=50,textvariable=To_saler,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_7.place(x=180,y=280)

        combo_box_1 = ttk.Combobox(first_frame, width=5,textvariable=day_saler,font=("Times New Roman",12))
        combo_box_1["values"] = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
        combo_box_1.place(x=250,y=350)
        combo_box_2 = ttk.Combobox(first_frame, width=8,textvariable=month_saler,font=("Times New Roman",12))
        combo_box_2["values"] = ("January","February","March","April","May","June","July","August","September","October","November","December")
        combo_box_2.place(x=325,y=350)
        combo_box_3 = ttk.Combobox(first_frame, width=6,textvariable=year_saler,font=("Times New Roman",12))
        combo_box_3["values"] = my_yaer
        combo_box_3.place(x=423,y=350) 

        entry_box_8 = Entry(first_frame, width=50,textvariable=Email_saler,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_8.place(x=180,y=400)



        def cal():
            # ===========  get the variable  =======================
            Name = name_saler.get()
            pri = int(price_saler.get())
            quant = int(quantity_saler.get())
            qual = quality_saler.get()
            frome = To_saler.get()
            Contect = contect_saler.get()
            iD = Id_saler.get()
            email = Email_saler.get()
            Day = day_saler.get()
            Month = month_saler.get()
            Year = year_saler.get()
            #==================   for calculating dues the current ID number ============================= 
                            
            if os.path.exists('shope_database_Sale.csv'):
                with open('shope_database_Sale.csv' , 'r') as f:
                    rows = csv.reader(f)
                    count = 0
                    my_list = []
                    first_list = []
                    for row in rows:
                        if iD in row:
                            my_list.append(row)
                            count+=1
                    if count>0:
                        first_list = my_list[-1]
                        dues = int(first_list[-1])
                    else:
                        dues = 0
            else:
                dues = 0

            # ==============  Variable  ===========================
            DUES = StringVar()
            DUES.set(dues)

            NAME = StringVar()
            NAME.set(Name)
    
            QUANT = StringVar()
            QUANT.set(quant)

            ID = StringVar()
            ID.set(iD)

            QUAL = StringVar()
            QUAL.set(qual)

            PRICE  =StringVar()
            PRICE.set(pri)

            DATE = StringVar()
            DATE.set(Day+" "+Month+" "+Year)

            FROM = StringVar()
            FROM.set(frome)

            cont = StringVar()
            cont.set(Contect)

            Emal = StringVar()
            Emal.set(email)

            tot = quant*pri
            total_price = IntVar()
            total_price.set(tot+dues)

            adjust = StringVar()
            paid = StringVar()

            lbl_1 = Label(second_frame,text="Dues:",font=("Mongolian Baiti",14))
            lbl_1.place(x=5,y=16)
            entry_box_1_sal = Entry(second_frame,textvariable=DUES , width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_1_sal.place(x=130,y=16)

            lbl_2 = Label(second_frame,text="Product Name:",font=("Mongolian Baiti",14))
            lbl_2.place(x=5,y=44)
            entry_box_2_sal = Entry(second_frame,textvariable=NAME , width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_2_sal.place(x=130,y=44)

            lbl_3 = Label(second_frame,text="ID no:",font=("Mongolian Baiti",14))
            lbl_3.place(x=5,y=72)
            entry_box_3_sal = Entry(second_frame,textvariable=ID , width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_3_sal.place(x=130,y=72)

            lbl_4 = Label(second_frame,text="Item Quantity:",font=("Mongolian Baiti",14))
            lbl_4.place(x=5,y=100)
            entry_box_4_sal = Entry(second_frame,textvariable=QUANT ,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_4_sal.place(x=130,y=100)

            lbl_5 = Label(second_frame,text="Item Price:",font=("Mongolian Baiti",14))
            lbl_5.place(x=5,y=128)
            entry_box_5_sal = Entry(second_frame, textvariable=PRICE,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_5_sal.place(x=130,y=128)

            lbl_6 = Label(second_frame,text="Item Quality:",font=("Mongolian Baiti",14))
            lbl_6.place(x=5,y=156)
            entry_box_6_sal = Entry(second_frame,textvariable=QUAL ,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_6_sal.place(x=130,y=156)
            
            lbl_7 = Label(second_frame,text="Date:",font=("Mongolian Baiti",14))
            lbl_7.place(x=5,y=184)
            entry_box_7_sal = Entry(second_frame,textvariable=DATE, width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_7_sal.place(x=130,y=184)

            
            lbl_8 = Label(second_frame,text="Fram:",font=("Mongolian Baiti",14))
            lbl_8.place(x=5,y=212)
            entry_box_8_sal = Entry(second_frame,textvariable=FROM, width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_8_sal.place(x=130,y=212)

            lbl_9 = Label(second_frame,text="Contact:",font=("Mongolian Baiti",14))
            lbl_9.place(x=5,y=240)
            entry_box_9_sal = Entry(second_frame,textvariable=cont, width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_9_sal.place(x=130,y=240)

            lbl_10 = Label(second_frame,text="Email:",font=("Mongolian Baiti",14))
            lbl_10.place(x=5,y=268)
            entry_box_10_sal = Entry(second_frame,textvariable=Emal, width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_10_sal.place(x=130,y=268)

            lbl_11 = Label(second_frame,text="Total Price:",font=("Mongolian Baiti",14,"bold"))
            lbl_11.place(x=5,y=300)
            entry_box_11_sal = Entry(second_frame, textvariable = total_price,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_11_sal.place(x=130,y=300)
        
            lbl_12 = Label(second_frame,text="Discount:",font=("Mongolian Baiti",14))
            lbl_12.place(x=5,y=328)
            entry_box_12_sal = Entry(second_frame,textvariable=adjust ,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_12_sal.place(x=130,y=328)

            lbl_13 = Label(second_frame,text="Paid:",font=("Mongolian Baiti",14))
            lbl_13.place(x=5,y=358)
            entry_box_13_sal = Entry(second_frame,textvariable = paid, width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_13_sal.place(x=130,y=358)

            lbl_14 = Label(second_frame,text="Balance:",font=("Mongolian Baiti",14,"bold"))
            lbl_14.place(x=5,y=388)
            entry_box_14_sal = Entry(second_frame,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
            entry_box_14_sal.place(x=130,y=388)
            
            def calculate():
                T = tot+dues
                Ad = int(adjust.get())
                Pai = int(paid.get())

                Rs = Pai+Ad
                amount =T-Rs

                balance = StringVar()
                balance.set(amount)
                entry_box_15_sal = Entry(second_frame,textvariable = balance ,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
                entry_box_15_sal.place(x=130,y=388)


            def clear():
                entry_box_1_sal.delete(0,tk.END)
                entry_box_2_sal.delete(0,tk.END)
                entry_box_3_sal.delete(0,tk.END)
                entry_box_4_sal.delete(0,tk.END)
                entry_box_5_sal.delete(0,tk.END)
                entry_box_6_sal.delete(0,tk.END)
                entry_box_7_sal.delete(0,tk.END)
                entry_box_8_sal.delete(0,tk.END)
                entry_box_9_sal.delete(0,tk.END)
                entry_box_10_sal.delete(0,tk.END)
                entry_box_11_sal.delete(0,tk.END)
                entry_box_12_sal.delete(0,tk.END)
                entry_box_13_sal.delete(0,tk.END)
                entry_box_14_sal.delete(0,tk.END)
                entry_box_15_sal = Entry(second_frame,width=18,font=("Times New Roman",12),relief=GROOVE,bd=2)
                entry_box_15_sal.place(x=130,y=388)            
        

            def save():
                due = int(DUES.get())
                name = NAME.get()
                id_no =  ID.get()
                quantity = int(QUANT.get())
                qualit = quality_saler.get()
                price = int(PRICE.get())
                D = Day
                M = Month
                Y = Year
                From = FROM.get()
                Cont = cont.get()
                Eml = Emal.get()
                tot = quantity*price
                T = tot+due
                Adj = int(adjust.get())
                Paid = int(paid.get())

                minus = Adj + Paid
                bal = T-minus
                if bal<0:
                    m_box.showerror("Error","Please check the paid Balance\nThe Paid balance is Greater the the total ")
                else:
                    with open('shope_database_Sale.csv' , 'a',newline='') as f:
                        dict_writter = DictWriter(f,fieldnames=['Name','ID','Quantity','Price','Quality','Day','Month','Year','Customer','Contect','Email','Dues','Total',
                            'Adjust','Paid','Balance'])
                        if os.stat('shope_database_Sale.csv').st_size==0:
                            dict_writter.writeheader()
                        dict_writter.writerow({
                            'Name' : name,
                            'ID':id_no,
                            'Quantity': quantity,
                            'Price':price,
                            'Quality':qualit,
                            'Day':D,
                            'Month':M,
                            'Year':Y,
                            'Customer':From,
                            'Contect':Cont,
                            'Email': Eml,
                            'Dues':due,
                            'Total':tot,
                            'Adjust':Adj,
                            'Paid':Paid,
                            'Balance':bal
                        })
                        messagebox.showinfo("information","Your Record is Saved Successfully")
                        clear()
        # ================  Buttons  =================================

            btn1 = Button(second_frame,text="Calculate",width=10,fg='white',command = calculate,bg="#097777",font=("Andalus",10),activebackground="#075f5f",activeforeground = "white")
            btn1.place(x=70,y=430)

            btn2 = Button(second_frame,text="Save",width=10,fg='white',command = save,bg="#097777",font=("Andalus",10),activebackground="#075f5f",activeforeground = "white")
            btn2.place(x=160,y=430)

        btn1 = Button(first_frame,text="Calculate",width=10,fg='white',bg="#097777",command= cal,font=("Andalus",10),activebackground="#075f5f",activeforeground = "white")
        btn1.place(x=550,y=530)
        btn2 = Button(first_frame,text="Back",width=10,fg='white',bg="#097777",command=first_frame.destroy,font=("Andalus",10),activebackground="#075f5f",activeforeground = "white")
        btn2.place(x=450,y=530)

        
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    #                    search Sales Detail function
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    def search_Sales(self):
        list_1 = []
        if os.path.exists("shope_database_Sale.csv"):
            with open("shope_database_Sale.csv","r") as f:
                rows = csv.reader(f)
                my_list = [i for i in rows]
            my_list.pop(0)
            id_list = sorted([j[1] for j in my_list])
            lis = []
            for i in id_list:
                if i not in lis: 
                    lis.append(i)
        else:
            lis = ['No item']
            # print(lis)
        # =================================  Frames   ==================================
        first_frame = Frame(self.root,height=600,width=970,bg="#009595")
        first_frame.place(x=0,y=0)

        rough_frame = Frame(first_frame,relief=GROOVE,bd=3)
        rough_frame.place(y=100,x=3,height=435,width=630)

        second_frame = Frame(first_frame,height=480,width=300,relief=GROOVE,bd=3)
        second_frame.place(x=650,y=100)

        # ==================================  header Label  ============================
        Top_lbl = Label(first_frame,text="show Customer detail",pady=15,padx=311,fg='white',bg="#009595",font=("Old English Text MT",30),relief=RIDGE)
        Top_lbl.place(x=0,y=0)

        # ==============================  For search data  ==============================
        lbl_first = Label(second_frame,text="search detail",fg='#009699',font=("Old English Text MT",30,'bold'))
        lbl_first.place(x=40,y=15)
        
        lbl_select = Label(second_frame,text="Select Customer ID",fg='#009595',font=("Mongolian Baiti",16))
        lbl_select.place(x=60,y=80)
        
        # ========================   Variable  =======================
        ID_supplier = StringVar()
        combo_box_search_1 = ttk.Combobox(second_frame, width=8,textvariable=ID_supplier,font=("Times New Roman",12))
        combo_box_search_1["values"] = (lis)
        combo_box_search_1.place(x=105,y=120)
        
        # ===================================== Show data =======================================
        # =====================================  Labels =========================================
        def search():
            id_supplier = ID_supplier.get()
            if id_supplier=="":
                m_box.showerror('Error','you do not pass the values\nplease try again.... ')
            else:
                if os.path.exists("shope_database_Sale.csv"):
                    right_first2 = Frame(first_frame,relief=GROOVE,bd=3)#-------->  frmae are created for scrool
                    right_first2.place(y=100,x=3,height=435,width=630)    

                    style = ttk.Style()
                    style.configure('Treeview.Heading',font=("Times New Roman",14,'bold'))
                    style.configure('Treeview',font=("Times New Roman",14),background="cyan",foreground='black')
                    scroll_x = Scrollbar(right_first2,orient=HORIZONTAL)
                    scroll_y = Scrollbar(right_first2,orient=VERTICAL)

                    studenttabel = Treeview(right_first2 , columns=('Name','ID','Quantity','Price','Quality','Day','Month','Year',
                        'Customer','Contect No','Email','Dues','Total','Discount','Paid','Balance'),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

                    scroll_x.pack(side=BOTTOM,fill=X)
                    scroll_y.pack(side=RIGHT,fill=Y)
                    scroll_x.config(command=studenttabel.xview)
                    scroll_y.config(command=studenttabel.yview)

                    studenttabel.heading('Name', text="Name")
                    studenttabel.heading('ID', text="ID")
                    studenttabel.heading('Quantity', text="Quantity")
                    studenttabel.heading('Price', text='Price')
                    studenttabel.heading('Quality', text="Quality")
                    studenttabel.heading('Day', text="Day")
                    studenttabel.heading('Month', text="Month")
                    studenttabel.heading('Year', text="Year")
                    studenttabel.heading('Customer', text="Customer")
                    studenttabel.heading('Contect No', text="Contect No")
                    studenttabel.heading('Email', text="Email")
                    studenttabel.heading('Dues', text="Dues")
                    studenttabel.heading('Total', text="Total")
                    studenttabel.heading('Discount', text="Discount")
                    studenttabel.heading('Paid', text="Paid")
                    studenttabel.heading('Balance', text="Balance")

                    studenttabel['show']='headings'

                    studenttabel.column('Name',width=150)
                    studenttabel.column('ID',width=70)
                    studenttabel.column('Quantity',width=100)
                    studenttabel.column('Price',width=90)
                    studenttabel.column('Quality',width=100)
                    studenttabel.column('Day',width=70)
                    studenttabel.column('Month',width=90)
                    studenttabel.column('Year',width=70)
                    studenttabel.column('Customer',width=250)
                    studenttabel.column('Contect No',width=130)
                    studenttabel.column('Email',width=250)
                    studenttabel.column('Dues',width=90)
                    studenttabel.column('Total',width=90)
                    studenttabel.column('Discount',width=90)
                    studenttabel.column('Paid',width=90)
                    studenttabel.column('Balance',width=100)
                   
                    studenttabel.pack(fill=BOTH,expand=1) 


                    with open("shope_database_Sale.csv","r") as file:
                        rows = csv.reader(file)
                        rough_list = [i for i in rows if id_supplier == i[1] ]
                    for i in rough_list:
                        list_1= [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15]]
                        studenttabel.insert('',END,values=list_1)
                else:
                    messagebox.showerror("Error","There is no file in this directory ")
        # ================================== button  ======================
        btn_search_1 = Button(second_frame,width=11,text="Search",fg='white',bg="#097777",command=search,activebackground="#075f5f",activeforeground = "white")
        btn_search_1.place(x=105,y=155)

        # ===================  show previous detail on ID no  ==========================
        lbl_previous = Label(second_frame,text="Previous Last detail",fg='#009699',font=("Old English Text MT",24,'bold'))
        lbl_previous.place(x=0,y=240)
        
        
        lbl_1 = Label(second_frame,text="Select ID of Customer",fg='#009595',font=("Mongolian Baiti",16))
        lbl_1.place(x=55,y=280)
        ID = StringVar()
        combo_box_search_2 = ttk.Combobox(second_frame, width=8,textvariable=ID,font=("Times New Roman",12))
        combo_box_search_2["values"] = (lis)
        combo_box_search_2.place(x=100,y=320)

        def search_by_ID():
            id_sup = ID.get()
            if id_sup=="":
                messagebox.showerror("Error","Please Enter ID of Customer")
            else:
                if os.path.exists("shope_database_Sale.csv"):
                    count = 0
                    with open("shope_database_Sale.csv","r") as f:
                        rows = csv.reader(f)
                        my_list = [i for i in rows]
                        spici_list = []
                        for i in my_list:  
                            if id_sup == i[1]:
                                spici_list.append(i)
                                count+=1
                    if count>0:
                        last_list = spici_list[-1]
                        right_first1 = Frame(first_frame,relief=GROOVE,bd=3)
                        right_first1.place(y=100,x=3,height=435,width=630)

                        lbl_1 = Label(right_first1,text="Product Name:",font=("Mongolian Baiti",14))
                        lbl_1.place(x=10,y=10)

                        lbl_2 = Label(right_first1,text="Item Price:",font=("Mongolian Baiti",14))
                        lbl_2.place(x=305,y=10)
                        lbl_3 = Label(right_first1,text="PKR",font=("Mongolian Baiti",12))
                        lbl_3.place(x=550,y=10)

                        lbl_4 = Label(right_first1,text="Item Quantity:",font=("Mongolian Baiti",14))
                        lbl_4.place(x=10,y=50)

                        lbl_5 = Label(right_first1,text="Item Quality:",font=("Mongolian Baiti",14))
                        lbl_5.place(x=305,y=50)

                        lbl_6 = Label(right_first1,text="Contect No:",font=("Mongolian Baiti",14))
                        lbl_6.place(x=10,y=90)

                        lbl_7 = Label(right_first1,text="ID No:",font=("Mongolian Baiti",14))
                        lbl_7.place(x=305,y=90)

                        lbl_8 = Label(right_first1,text="To:",font=("Mongolian Baiti",14))
                        lbl_8.place(x=10,y=130)

                        lbl_9 = Label(right_first1,text="Date:",font=("Mongolian Baiti",14))
                        lbl_9.place(x=190,y=190)
                        lbl_10 = Label(right_first1,text="Day",font=("Mongolian Baiti",14))
                        lbl_10.place(x=260,y=160)
                        lbl_11 = Label(right_first1,text="Month",font=("Mongolian Baiti",14))
                        lbl_11.place(x=340,y=160)
                        lbl_12 = Label(right_first1,text="Year",font=("Mongolian Baiti",14))
                        lbl_12.place(x=433,y=160)

                        lbl_13 = Label(right_first1,text="Email Address:",font=("Mongolian Baiti",14))
                        lbl_13.place(x=10,y=230)

                        lbl_14 = Label(right_first1,text="Dues:",font=("Mongolian Baiti",14))
                        lbl_14.place(x=10,y=270)

                        lbl_15 = Label(right_first1,text="Total:",font=("Mongolian Baiti",14))
                        lbl_15.place(x=315,y=270)

                        lbl_16 = Label(right_first1,text="Discount:",font=("Mongolian Baiti",14))
                        lbl_16.place(x=10,y=310)

                        lbl_17 = Label(right_first1,text="Paid:",font=("Mongolian Baiti",14))
                        lbl_17.place(x=315,y=310)

                        lbl_18 = Label(right_first1,text="Balance:",font=("Mongolian Baiti",14))
                        lbl_18.place(x=10,y=350)

                        lbl_19 = Label(right_first1,text="RePaid:",font=("Mongolian Baiti",14))
                        lbl_19.place(x=315,y=350)

                        # =====================================  variables ==========================================
                        name = StringVar()
                        price = StringVar()
                        quantity = StringVar()
                        quality = StringVar()
                        contect = StringVar()
                        Id = StringVar()
                        To = StringVar()
                        day = StringVar()
                        month = StringVar()
                        year = StringVar()
                        Email = StringVar()
                        due = StringVar()
                        total = StringVar()
                        adjust = StringVar()
                        paid = StringVar()
                        balance = StringVar()
                        Repaid = StringVar()

                        
                        name.set(last_list[0])
                        Id.set(last_list[1])
                        quantity.set(last_list[2])
                        price.set(last_list[3])
                        quality.set(last_list[4])
                        day.set(last_list[5])
                        month.set(last_list[6])
                        year.set(last_list[7])
                        To.set(last_list[8])
                        contect.set(last_list[9])
                        Email.set(last_list[10])
                        due.set(last_list[11])
                        total.set(last_list[12])
                        adjust.set(last_list[13])
                        paid.set(last_list[14])
                        balance.set(last_list[15])

                        # =====================================  Entry boxes =========================================
                        list_1 = []
                        for i in range(2000,3000):
                            list_1.append(i)
                        my_yaer=tuple(list_1)

                        entry_box_1 = Entry(right_first1, width=18,textvariable=name,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_1.place(x=140,y=10)
                        entry_box_1.focus()

                        entry_box_2 = Entry(right_first1, width=16,textvariable=price,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_2.place(x=410,y=10)
                        
                        entry_box_3 = Entry(right_first1, width=18,textvariable=quantity,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_3.place(x=140,y=50)

                        entry_box_4 = Entry(right_first1, width=16,textvariable=quality,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_4.place(x=410,y=50)

                        entry_box_5 = Entry(right_first1, width=18,textvariable=contect,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_5.place(x=140,y=90)

                        entry_box_6 = Entry(right_first1, width=16,textvariable=Id,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_6.place(x=410,y=90)

                        entry_box_7 = Entry(right_first1, width=50,textvariable=To,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_7.place(x=140,y=130)

                        combo_box_1 = ttk.Combobox(right_first1, width=5,textvariable=day,font=("Times New Roman",12))
                        combo_box_1["values"] = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
                        combo_box_1.place(x=250,y=190)
                        combo_box_2 = ttk.Combobox(right_first1, width=8,textvariable=month,font=("Times New Roman",12))
                        combo_box_2["values"] = ("January","February","March","April","May","June","July","August","September","October","November","December")
                        combo_box_2.place(x=325,y=190)
                        combo_box_3 = ttk.Combobox(right_first1, width=6,textvariable=year,font=("Times New Roman",12))
                        combo_box_3["values"] = my_yaer
                        combo_box_3.place(x=423,y=190) 

                        entry_box_8 = Entry(right_first1, width=50,textvariable=Email,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_8.place(x=140,y=230)
            
                        entry_box_9 = Entry(right_first1, width=18,textvariable=due,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_9.place(x=140,y=270)

                        entry_box_10 = Entry(right_first1, width=16,textvariable=total,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_10.place(x=412,y=270)

                        entry_box_11 = Entry(right_first1, width=18,textvariable=adjust,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_11.place(x=140,y=310)

                        entry_box_12 = Entry(right_first1, width=16,textvariable=paid,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_12.place(x=412,y=310)

                        entry_box_13 = Entry(right_first1, width=18,textvariable=balance,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_13.place(x=140,y=350)

                        entry_box_14 = Entry(right_first1, width=16,textvariable=Repaid,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_14.place(x=412,y=350)
                        
                        def Balance_fun(repaid):
                            Balance = int(balance.get())
                            rebalance = int(repaid)
                            total_balance = (Balance-rebalance)
                            return total_balance

                        def paid_total(paid_second):
                            piad_first = int(paid.get())
                            total = int(piad_first)+int(paid_second)
                            return total
                        def fram_default():
                            right_first2 = Frame(first_frame,relief=GROOVE,bd=3)
                            right_first2.place(y=100,x=3,height=435,width=630)
                        def subm():
                            repaid = Repaid.get()
                            if repaid=="":
                                m_box.showerror("Error","The data can't Submitte\nPlease Enter Repaid data")
                            else:
                                last_paid = paid_total(repaid)
                                Balnc = Balance_fun(repaid)
                                last_list[0] = name.get()
                                last_list[1] = Id.get()
                                last_list[2] = quantity.get()
                                last_list[3] = price.get()
                                last_list[4] = quality.get()
                                last_list[5] = day.get()
                                last_list[6] = month.get()
                                last_list[7] = year.get()
                                last_list[8] = To.get()
                                last_list[9] = contect.get()
                                last_list[10] = Email.get()
                                last_list[11] = due.get()
                                last_list[12] = total.get()
                                last_list[13] = adjust.get()
                                last_list[14] = last_paid
                                last_list[15] = Balnc
                                if Balnc<0:
                                    m_box.showerror("Error","Please check the paid Balance\nThe Paid balance is Greater the the total ")
                                else:
                                    opt = messagebox.askyesno("Information","Do you want to Update the record")
                                    if opt>0:
                                        with open("shope_database_Sale.csv","w",newline="") as f:
                                            rows = csv.writer(f,lineterminator="\n")
                                            rows.writerows(my_list)
                                        fram_default()
                                        combo_box_search_1.delete(0,tk.END)
                                        combo_box_search_2.delete(0,tk.END)
                                    else:
                                        return 0
                        butten_1 = Button(right_first1,width=8,text="Submitte",command=subm,fg='white',bg="#097777",activebackground="#075f5f",activeforeground = "white")
                        butten_1.place(x=553,y=400)
                    else:
                        messagebox.showerror("Error",f"There is no Entry on this ID\nID : {id_sup}")
                else:
                    messagebox.showerror("Error","There is no file in this directory ")
    
        butten_1 = Button(second_frame,width=11,text="Search",fg='white',bg="#097777",command=search_by_ID,activebackground="#075f5f",activeforeground = "white")
        butten_1.place(x=100,y=350)

        btn2 = Button(first_frame,text="Back",width=10,height=2,fg='white',bg="#097777",command=first_frame.destroy,activebackground="#075f5f",activeforeground = "white")
        btn2.place(x=553,y=540)

    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    #                    Balance function
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    def Balance_fun(self):
        list_1 = []
        if os.path.exists("shope_database_Sale.csv"):
            with open("shope_database_Sale.csv","r") as f:
                rows = csv.reader(f)
                my_list = [i for i in rows]
            my_list.pop(0)
            id_list = sorted([j[1] for j in my_list])
            lis = []
            for i in id_list:
                if i not in lis: 
                    lis.append(i)

        # ================================= All Frames   ==================================
        first_frame_balance = Frame(self.root,height=600,width=970,bg="#009595")
        first_frame_balance.place(x=0,y=0)
        
        left_frame_balance = Frame(first_frame_balance,relief=GROOVE,bd=3)
        left_frame_balance.place(y=150,x=3,height=395,width=475)

        right_frame_balance = Frame(first_frame_balance,relief=GROOVE,bd=3)
        right_frame_balance.place(y=150,x=494,height=395,width=472)

        # ==================================  header Label  ============================
        Top_heading_lbl = Label(first_frame_balance,text="Balance detail",pady=15,padx=371,fg='white',bg="#009595",font=("Old English Text MT",30),relief=RIDGE)
        Top_heading_lbl.place(x=0,y=0)

        # ===============================================
        #            Supplier data
        # ===============================================
        customer_header = Label(first_frame_balance,text="Supplier Detail",fg='white',bg="#009595",font=("Mongolian Baiti",24))
        customer_header.place(x=130,y=100)

        style = ttk.Style()
        style.configure('Treeview.Heading',font=("Times New Roman",14,'bold'))
        style.configure('Treeview',font=("Times New Roman",14),background="cyan",foreground='black')
        scroll_x = Scrollbar(left_frame_balance,orient=HORIZONTAL)
        scroll_y = Scrollbar(left_frame_balance,orient=VERTICAL)

        studenttabel = Treeview(left_frame_balance , columns=('ID','Supplier','Contect No','Total','Paid','Balance'),
            yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=studenttabel.xview)
        scroll_y.config(command=studenttabel.yview)

        studenttabel.heading('ID', text="ID")
        studenttabel.heading('Supplier', text="Supplier")
        studenttabel.heading('Contect No', text="Contect No")
        studenttabel.heading('Total', text="Total")
        studenttabel.heading('Paid', text="Paid")
        studenttabel.heading('Balance', text="Balance")

        studenttabel['show']='headings'

        studenttabel.column('ID',width=70)
        studenttabel.column('Supplier',width=150)
        studenttabel.column('Contect No',width=130)
        studenttabel.column('Total',width=90)
        studenttabel.column('Paid',width=90)
        studenttabel.column('Balance',width=100)
        
        studenttabel.pack(fill=BOTH,expand=1) 


        if os.path.exists('shope_database.csv'):
            with open("shope_database.csv","r") as f:
                rows = csv.reader(f)
                my_list = [i for i in rows]
            my_list.pop(0)
            id_list = sorted([j[1] for j in my_list])
            # ============================================
            #   find the last transiction of supplier
            # ============================================ 
            def per_suplier(i):
                rou_supplier = []
                for j in my_list:
                    if i in j:
                        rou_supplier.append(j)
                return rou_supplier[-1]
            # ============================================
            #     to remove duplication in list/ only id no of supplier are present 
            # ============================================ 
            lis_supplier = []
            for i in id_list:
                if i not in lis_supplier:
                    lis_supplier.append(i)
            # ============================================
            #   in ( la ---> list ) all of transection of supplier are present 
            # ============================================ 
            la_supplier = []
            for i in lis_supplier:
                la_supplier.append(per_suplier(i))

            for i in la_supplier:
                list_1= [i[1],i[8],i[9],i[12],i[14],i[15]]
                studenttabel.insert('',END,values=list_1)

            count = 0
            for i in la_supplier:
                count += int(i[-1]) 
            # print(count)

        else:
            count = '0'
            pass
        
        T_balance_supplier = StringVar()
        T_balance_supplier.set(count)
        lbl_10 = Label(first_frame_balance,text="Total Balance :",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_10.place(x=5,y=555)
        entry_box_10_sal = Entry(first_frame_balance,textvariable=T_balance_supplier, width=10,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_10_sal.place(x=130,y=555)
        # =========================================================== 
        # ===============================================
        #            Customer data
        # ===============================================
        # ===========================================================
        customer_header = Label(first_frame_balance,text="Customer Detail",fg='white',bg="#009595",font=("Mongolian Baiti",24))
        customer_header.place(x=600,y=100)


        style = ttk.Style()
        style.configure('Treeview.Heading',font=("Times New Roman",14,'bold'))
        style.configure('Treeview',font=("Times New Roman",14),background="cyan",foreground='black')
        scroll_x = Scrollbar(right_frame_balance,orient=HORIZONTAL)
        scroll_y = Scrollbar(right_frame_balance,orient=VERTICAL)

        studenttabel = Treeview(right_frame_balance , columns=('ID','Customer','Contect No','Total','Paid','Balance'),
            yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=studenttabel.xview)
        scroll_y.config(command=studenttabel.yview)

        studenttabel.heading('ID', text="ID")
        studenttabel.heading('Customer', text="Customer")
        studenttabel.heading('Contect No', text="Contect No")
        studenttabel.heading('Total', text="Total")
        studenttabel.heading('Paid', text="Paid")
        studenttabel.heading('Balance', text="Balance")

        studenttabel['show']='headings'

        studenttabel.column('ID',width=70)
        studenttabel.column('Customer',width=150)
        studenttabel.column('Contect No',width=130)
        studenttabel.column('Total',width=90)
        studenttabel.column('Paid',width=90)
        studenttabel.column('Balance',width=100)
        
        studenttabel.pack(fill=BOTH,expand=1) 


        if os.path.exists('shope_database_sale.csv'):
            with open("shope_database_sale.csv","r") as f:
                rows = csv.reader(f)
                my_list = [i for i in rows]
            my_list.pop(0)
            id_list = sorted([j[1] for j in my_list])
            # ============================================
            #   find the last transiction of customer
            # ============================================ 
            def per_customer(i):
                rou_customer = []
                for j in my_list:
                    if i in j:
                        rou_customer.append(j)
                return rou_customer[-1]
            # ============================================
            #     to remove duplication in list/ only id no of customer are present 
            # ============================================ 
            lis_customer = []
            for i in id_list:
                if i not in lis_customer:
                    lis_customer.append(i)
            # ============================================
            #   in ( la ---> list ) all of transection of custommer are present 
            # ============================================ 
            la_customer = []
            for i in lis_customer:
                la_customer.append(per_customer(i))

            for i in la_customer:
                list_1= [i[1],i[8],i[9],i[12],i[14],i[15]]
                studenttabel.insert('',END,values=list_1)
            
            count = 0
            for i in la_customer:
                count += int(i[-1]) 
            # print(count)
        else:
            count='0'
            pass
            
        T_balance_customer = StringVar()
        T_balance_customer.set(count)
        lbl_10 = Label(first_frame_balance,text="Total Balance :",fg='white',bg="#009595",font=("Mongolian Baiti",14))
        lbl_10.place(x=500,y=555)
        entry_box_10_sal = Entry(first_frame_balance,textvariable=T_balance_customer, width=10,font=("Times New Roman",12),relief=GROOVE,bd=2)
        entry_box_10_sal.place(x=625,y=555)

        btn2 = Button(first_frame_balance,text="Back",width=10,height=2,fg='white',bg="#097777",command=first_frame_balance.destroy,activebackground="#075f5f",activeforeground = "white")
        btn2.place(x=885,y=550)

    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    #                              Stock  function
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


    def stack(self):
        # =================  Frames  =================
        first_frame_stack = Frame(self.root,height=600,width=970,bg="#009595")
        first_frame_stack.place(x=0,y=0)

        left_frame_stack = Frame(first_frame_stack,relief=GROOVE,bd=3,bg="#009595")
        left_frame_stack.place(y=150,x=3,height=395,width=250)
    
        right_frame_stack = Frame(first_frame_stack,relief=GROOVE,bd=3,bg="#009595")
        right_frame_stack.place(y=150,x=274,height=395,width=692)

        # ==================  Header Label  ================
        Top_heading_lbl = Label(first_frame_stack,text="Total Stock",pady=15,padx=385,fg='white',bg="#009595",font=("Old English Text MT",30),relief=RIDGE)
        Top_heading_lbl.place(x=0,y=0)
        # ====================  Searching frame  ===============
        list_1 = []
        if os.path.exists("shope_database.csv"):
            with open("shope_database.csv","r") as f:
                rows = csv.reader(f)
                my_list = [i for i in rows]
            my_list.pop(0)
            id_list = sorted([j[0] for j in my_list])
            lis = []
            for i in id_list:
                if i not in lis: 
                    lis.append(i)
        else:
            lis = ['No item']
       
        search_lbl_stack = Label(left_frame_stack,text=" Select Item: ",font=("Mongolian Baiti",20,"underline"),fg='white',bg="#009595")
        search_lbl_stack.place(x=40,y=50)

         # ==========  Variable and combo box =======================
        item_name = StringVar()
        combo_box_search_1 = ttk.Combobox(left_frame_stack, width=8,textvariable=item_name,font=("Times New Roman",13))
        combo_box_search_1["values"] = (lis)
        combo_box_search_1.place(x=60,y=100)


        def show_stack():
            # ========== Frame  ===============
            right_frame_stack = Frame(first_frame_stack,relief=GROOVE,bd=3,bg="#009595")
            right_frame_stack.place(y=150,x=274,height=395,width=692)
            name = item_name.get()
            # ==================================
            if name=="":
                messagebox.showerror("Error","Please select Item Name ")
            else:
                if os.path.exists("shope_database.csv"):
                    #======  purchase file open ===============
                    with open("shope_database.csv","r") as f:
                        rows = csv.reader(f)
                        my_list = [i for i in rows]
                    count = 0
                    for i in my_list:
                        if name in i:
                            count+=int(i[2])
                    #======  Sales file open ===============
                    if os.path.exists("shope_database_sale.csv"):
                        with open("shope_database_sale.csv","r") as f:
                            rows = csv.reader(f)
                            my_list = [i for i in rows]
                        count2 = 0
                        for i in my_list:
                            if name in i:
                                count2+=int(i[2])
                    else:
                        count2 = 0

                    present = count-count2

                    lbl_stack_1 = Label(right_frame_stack,text="Present Stock",font=("Old English Text MT",28),fg='white',bg="#009595")
                    lbl_stack_1.place(x=50,y=20)

                    lbl_stack_1 = Label(right_frame_stack,text=f"Total {name} Purchase:",font=("Mongolian Baiti",14),fg='white',bg="#009595")
                    lbl_stack_1.place(x=50,y=130)
                    stack_purchase = StringVar()
                    stack_purchase.set(count)
                    entry_box_stack_1 = Entry(right_frame_stack, width=10,textvariable=stack_purchase,font=("Times New Roman",12),relief=GROOVE,bd=2)
                    entry_box_stack_1.place(x=280,y=130)

                    lbl_stack_2 = Label(right_frame_stack,text=f"Total {name} Sales:",font=("Mongolian Baiti",14),fg='white',bg="#009595")
                    lbl_stack_2.place(x=50,y=165)
                    stack_sales = StringVar()
                    stack_sales.set(count2)
                    entry_box_stack_2 = Entry(right_frame_stack, width=10,textvariable=stack_sales,font=("Times New Roman",12),relief=GROOVE,bd=2)
                    entry_box_stack_2.place(x=280,y=165)

                    
                    if present<0:
                        messagebox.showerror("Error",f"There is an Error!!!\nYou do not add Entry of {name}\nin your data base from Supplier\n\n Your Sales is greater then Purchasing")
                    else:
                        lbl_stack_3 = Label(right_frame_stack,text=f"Total {name} Present:",font=("Mongolian Baiti",13,'bold'),fg='white',bg="#009595")
                        lbl_stack_3.place(x=50,y=220)
                        stack_present = StringVar()
                        stack_present.set(present)
                        entry_box_stack_3 = Entry(right_frame_stack, width=10,textvariable=stack_present,font=("Times New Roman",12),relief=GROOVE,bd=2)
                        entry_box_stack_3.place(x=280,y=220)
             
                else:
                        messagebox.showerror("Error","There is no file in this directory\nPlease first Entry of Supplier \nIn your Database")





        btn_1 = Button(left_frame_stack,width=12,text="Search",fg='white',bg="#097777",command=show_stack,activebackground="#075f5f",activeforeground = "white")
        btn_1.place(x=60,y=140)

        btn2 = Button(first_frame_stack,text="Back",width=10,height=2,fg='white',bg="#097777",command=first_frame_stack.destroy,activebackground="#075f5f",activeforeground = "white")
        btn2.place(x=885,y=550)

root=Tk()
obj=shop(root)
root.mainloop()