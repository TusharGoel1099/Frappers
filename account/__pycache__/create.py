import sqlite3
from calci import *
from tkinter import *
from tkinter import messagebox
conn=sqlite3.connect("student.db")
c=conn.cursor()
c.execute("""CREATE TABLE  IF NOT EXISTS student(
            First  TEXT,
            Last  TEXT,
            Email  TEXT,
            Roll  TEXT PRIMARY KEY,
            Pass TEXT
           )""")
conn.commit()

#register function to register GUI
def register():
      global register_screen
      global first
      global last
      global roll
      global email
      global DOB
      global passw
      register_screen = Toplevel(main_screen) 
      register_screen.title("Register")
      register_screen.geometry("1500x1000")
      first=StringVar()
      var=IntVar
      label1=Label(register_screen,text="first name", font=('arial', 16))
      label1.grid(row=0,column=0)
      label2=Label(register_screen,text="last name", font=('arial', 16))
      label2.grid(row=1,column=0)
      label3=Label(register_screen,text="email", font=('arial', 16))
      label3.grid(row=2,column=0)
      label4=Label(register_screen,text="roll no", font=('arial', 16))
      label4.grid(row=3,column=0)
      label5=Label(register_screen,text="Password", font=('arial', 16))
      label5.grid(row=5,column=0)
      first=StringVar()
      entry1=Entry(register_screen,textvariable=first, font=('arial', 16))
      entry1.grid(row=0,column=1)
      last=StringVar()
      entry2=Entry(register_screen,textvariable=last, font=('arial', 16))
      entry2.grid(row=1,column=1)
      email=StringVar()
      entry3=Entry(register_screen,textvariable=email, font=('arial', 16))
      entry3.grid(row=2,column=1)
      roll=StringVar()
      entry4=Entry(register_screen,textvariable=roll, font=('arial', 16))
      entry4.grid(row=3,column=1)
      passw=StringVar()
      entry5=Entry(register_screen,textvariable=passw,show='*', font=('arial', 16))
      entry5.grid(row=5,column=1)
      button2=Button(register_screen,text="create",command=insert, font=('arial', 16),bg="blue")
      button2.grid(row=7,column=0)
      Button(register_screen, text = "Exit", command = register_screen.destroy, font=('arial', 16),bg="red").grid(row=17,column=0)
# it will insert data in database
def insert():
      import re
      input = email.get()
      m = re.search('[^@]+@[^@]+\.[^@]+',input)
      if m:
       if(len(passw.get())!=8):
         conn=sqlite3.connect("student.db")
         c=conn.cursor()
         with conn:
            c.execute('INSERT INTO student(First,Last,Email,Roll,Pass) VALUES(?,?,?,?,?)',(first.get(),last.get(),email.get(),roll.get(),passw.get()))   
         messagebox.showinfo("frappers", "Thanku For Signing Up")  
         conn.commit()
         conn.rollback()
       else:
        #will show message box
        messagebox.showinfo("frappers", "Please Enter a valid 8 digit password**")     
         
      else:
        messagebox.showinfo("frappers", "Please Enter a valid email id")
      command=register_screen.destroy()  
#will create login gui window
def login():
   global login_screen
   global roll1
   global pass1
   login_screen = Toplevel(main_screen) 
   login_screen.title("login")
   login_screen.geometry("1500x1000")
   label5=Label(login_screen,text="enter ur roll number", font=('arial', 16))
   label5.grid(row=0,column=0)
   label6=Label(login_screen,text="enter ur password", font=('arial', 16))
   label6.grid(row=1,column=0)
   roll1=StringVar()
   entry5=Entry(login_screen,textvariable=roll1, font=('arial', 16))
   entry5.grid(row=0,column=1)
   pass1=StringVar()
   #will create entry box
   entry5=Entry(login_screen,textvariable=pass1,show="*", font=('arial', 16))
   entry5.grid(row=1,column=1)
   button3=Button(login_screen,text="login",command=login2, font=('arial', 16),bg="blue")
   button3.grid(row=3,column=0)
   Button(login_screen, text = "Exit",command = login_screen.destroy, font=('arial', 16),bg="red").grid(row=5,column=0)
def login2():
       global a
       a=roll1.get()
       b=pass1.get()
       while True:
                conn=sqlite3.connect("student.db")
                c=conn.cursor()
                c.execute('SELECT * FROM student WHERE roll=? AND Pass=?',[a,b])
                results=c.fetchall()
                if results:
                    for i in results:
                          MsgBox =messagebox.askquestion ("frappers", f"Welcome {i[0]} {i[1]} To Frappers")
                          x=i[3]
                          if(MsgBox=='yes'):
                                next(x)
                                MsgBox.destroy()
                          else:
                            MsgBox.destroy()
                else:
                    messagebox.showinfo("Warning", "Incorrect login")
                    #will destroy the previous window
                    MsgBox.destroy()
                    break

def next(x):
      root=Toplevel(main_screen)
      conn=sqlite3.connect("reciept1.db")
      c=conn.cursor()
      c.execute("SELECT * FROM reciept1")
      data=c.fetchall()
      root.geometry("2500x2500")
      label = Label(root,font=( 'aria' ,40, 'bold' ),text = " FRAPPERS MENU",fg="red").grid()
      ################################################
      var1=BooleanVar()
      counter1 =IntVar()
      def onClick(event=None):
            counter1.set(counter1.get() + 1)
      def inclick(event=None):
            counter1.set(counter1.get()-1)
            if(counter1.get()<0):
              counter1.set(0)
      # from tkinter import scrolledtext
      # scr = scrolledtext.ScrolledText(win, width=3, height=40,
      # wrap=tk.WORD)
      # scr.grid(column=0, columnspan=3)
      checkbutton1 = Checkbutton(root,font=( 'aria' ,20, 'bold' ),text = data[0][1],variable = var1).grid(row=1,column=1)
    #   photo = PhotoImage(file="C:\\frappers\\account\\__pycache__\\burger.jpg")
    #   Label(root,image=photo).grid(row=1,column=16)
      Button(root, text="+",font=( 'aria' ,15, 'bold' ), command=onClick, bg="yellow", fg = "black",activebackground="black").grid(row=1,column=4)
      Label(root,font=( 'aria' ,12, 'bold' ), textvariable=counter1).grid(row=1,column=5)
      Button(root, text="-",font=( 'aria' ,15, 'bold' ), command=inclick, bg="yellow", fg = "black", activebackground="black").grid(row=1,column=6)
      ################################################
      var2=BooleanVar()
      counter2 =IntVar()
      def onClick1(event=None):
            counter2.set(counter2.get() + 1)
      def inclick1(event=None):
            counter2.set(counter2.get()-1)
            if(counter2.get()<0):
              counter2.set(0)
      checkbutton2 = Checkbutton(root,font=( 'aria' ,20, 'bold' ),text = data[1][1],variable = var2).grid(row=6,column=1)
      Button(root, text="+",font=( 'aria' ,15, 'bold' ), command=onClick1,bg="yellow", fg = "black",activebackground="black").grid(row=6,column=4)
      Label(root,text="+",font=( 'aria' ,12, 'bold' ), textvariable=counter2).grid(row=6,column=5)     
      Button(root, text="-",font=( 'aria' ,15, 'bold' ), command=inclick1,bg="yellow", fg = "black",activebackground="black").grid(row=6,column=6)
      ################################################
      var3=BooleanVar()
      counter3 =IntVar()
      def onClick2(event=None):
            counter3.set(counter3.get() + 1)
      def inclick2(event=None):
            counter3.set(counter3.get()-1)
            if(counter3.get()<0):
              counter3.set(0)
      checkbutton3 = Checkbutton(root,font=( 'aria' ,20, 'bold' ),text = data[2][1],variable = var3).grid(row=12,column=1)
      Button(root, text="+",font=( 'aria' ,15, 'bold' ), command=onClick2,bg="yellow", fg = "black",activebackground="black").grid(row=12,column=4)
      Label(root,text="+",font=( 'aria' ,12, 'bold' ), textvariable=counter3).grid(row=12,column=5)     
      Button(root, text="-",font=( 'aria' ,15, 'bold' ), command=inclick2,bg="yellow", fg = "black",activebackground="black").grid(row=12,column=6)
      ################################################
      var4=BooleanVar()
      counter4 =IntVar()
      def onClick3(event=None):
            counter4.set(counter4.get() + 1)
      def inclick3(event=None):
            counter4.set(counter4.get()-1)
            if(counter4.get()<0):
              counter4.set(0)
      checkbutton4 = Checkbutton(root,font=( 'aria' ,20, 'bold' ),text = data[3][1],variable = var4).grid(row=18,column=1)
      Button(root, text="+",font=( 'aria' ,15, 'bold' ), command=onClick3,bg="yellow", fg = "black",activebackground="black").grid(row=18,column=4)
      Label(root,text="+",font=( 'aria' ,12, 'bold' ), textvariable=counter4).grid(row=18,column=5)     
      Button(root, text="-",font=( 'aria' ,15, 'bold' ), command=inclick3,bg="yellow", fg = "black",activebackground="black").grid(row=18,column=6)
      ################################################
      var5=BooleanVar()
      counter5 =IntVar()
      def onClick4(event=None):
            counter5.set(counter5.get() + 1)
      def inclick4(event=None):
            counter5.set(counter5.get()-1)
            if(counter5.get()<0):
              counter5.set(0)
      #will create window
      checkbutton5 = Checkbutton(root,font=( 'aria' ,20, 'bold' ),text = data[4][1],variable = var5).grid(row=24,column=1)
      Button(root, text="+",font=( 'aria' ,15, 'bold' ), command=onClick4,bg="yellow", fg = "black",activebackground="black").grid(row=24,column=4)
      Label(root,text="+",font=( 'aria' ,12, 'bold' ), textvariable=counter5).grid(row=24,column=5)     
      Button(root, text="-",font=( 'aria' ,15, 'bold' ), command=inclick4,bg="yellow", fg = "black",activebackground="black").grid(row=24,column=6)
      ################################################
      var6=BooleanVar()
      counter6 =IntVar()
      def onClick5(event=None):
            counter6.set(counter6.get() + 1)
      def inclick5(event=None):
            counter6.set(counter6.get()-1)
            if(counter6.get()<0):
              counter6.set(0)
      checkbutton6 = Checkbutton(root,font=( 'aria' ,20, 'bold' ),text = data[5][1],variable = var6).grid(row=30,column=1)
      Button(root, text="+",font=( 'aria' ,15, 'bold' ), command=onClick5,bg="yellow", fg = "black",activebackground="black").grid(row=30,column=4)
      Label(root,text="+",font=( 'aria' ,12, 'bold' ), textvariable=counter6).grid(row=30,column=5)     
      Button(root, text="-",font=( 'aria' ,15, 'bold' ), command=inclick5,bg="yellow", fg = "black",activebackground="black").grid(row=30,column=6)
      ################################################
      var7=BooleanVar()
      counter7 =IntVar()
      def onClick6(event=None):
            counter7.set(counter7.get() + 1)
      def inclick6(event=None):
            counter7.set(counter7.get()-1)
            if(counter7.get()<0):
              counter7.set(0)
      checkbutton7 = Checkbutton(root,font=( 'aria' ,20, 'bold' ),text = data[6][1],variable = var7).grid(row=36,column=1)
      Button(root, text="+",font=( 'aria' ,15, 'bold' ), command=onClick6,bg="yellow", fg = "black",activebackground="black").grid(row=36,column=4)
      Label(root,text="+",font=( 'aria' ,12, 'bold' ), textvariable=counter7).grid(row=36,column=5)     
      Button(root, text="-",font=( 'aria' ,15, 'bold' ), command=inclick6,bg="yellow", fg = "black",activebackground="black").grid(row=36,column=6)
      ################################################
      var8=BooleanVar()
      counter8 =IntVar()
      def onClick7(event=None):
            counter8.set(counter8.get() + 1)
      def inclick7(event=None):
            counter8.set(counter8.get()-1)
            if(counter8.get()<0):
              counter8.set(0)
      checkbutton8 = Checkbutton(root,font=( 'aria' ,20, 'bold' ),text = data[7][1],variable = var8).grid(row=42,column=1)
      Button(root, text="+",font=( 'aria' ,15, 'bold' ), command=onClick7,bg="yellow", fg = "black",activebackground="black").grid(row=42,column=4)
      Label(root,text="+",font=( 'aria' ,12, 'bold' ), textvariable=counter8).grid(row=42,column=5)     
      Button(root, text="-",font=( 'aria' ,15, 'bold' ), command=inclick7,bg="yellow", fg = "black",activebackground="black").grid(row=42,column=6)
      ################################################
      var9=BooleanVar()
      counter9 =IntVar()
      def onClick8(event=None):
            counter9.set(counter9.get() + 1)
      def inclick8(event=None):
            counter9.set(counter9.get()-1)
            if(counter9.get()<0):
              counter9.set(0)
      checkbutton9 = Checkbutton(root,font=( 'aria' ,20, 'bold' ),text = data[8][1],variable = var9).grid(row=48,column=1)
      Button(root, text="+",font=( 'aria' ,15, 'bold' ), command=onClick8,bg="yellow", fg = "black",activebackground="black").grid(row=48,column=4)
      Label(root,text="+",font=( 'aria' ,12, 'bold' ), textvariable=counter9).grid(row=48,column=5)     
      Button(root, text="-",font=( 'aria' ,15, 'bold' ), command=inclick8,bg="yellow", fg = "black",activebackground="black").grid(row=48,column=6)
      ################################################
      var10=BooleanVar()
      counter10 =IntVar()
      def onClick9(event=None):
            counter10.set(counter10.get() + 1)
      def inclick9(event=None):
            counter10.set(counter10.get()-1)
            if(counter10.get()<0):
              counter10.set(0)
      checkbutton10 = Checkbutton(root,font=( 'aria' ,20, 'bold' ),text = data[9][1],variable = var10).grid(row=54,column=1)
      Button(root, text="+",font=( 'aria' ,15, 'bold' ), command=onClick9,bg="yellow", fg = "black",activebackground="black").grid(row=54,column=4)
      Label(root,text="+",font=( 'aria' ,12, 'bold' ), textvariable=counter10).grid(row=54,column=5)     
      Button(root, text="-",font=( 'aria' ,15, 'bold' ), command=inclick9,bg="yellow", fg = "black",activebackground="black").grid(row=54,column=6)
      ################################################
      var11=BooleanVar()
      counter11 =IntVar()
      def onClick10(event=None):
            counter11.set(counter11.get() + 1)
      def inclick10(event=None):
            counter11.set(counter11.get()-1)
            if(counter11.get()<0):
              counter11.set(0)
      checkbutton11 = Checkbutton(root,font=( 'aria' ,20, 'bold' ),text = data[10][1],variable = var11).grid(row=60,column=1)
      Button(root, text="+",font=( 'aria' ,15, 'bold' ), command=onClick10,bg="yellow", fg = "black",activebackground="black").grid(row=60,column=4)
      Label(root,text="+",font=( 'aria' ,12, 'bold' ), textvariable=counter11).grid(row=60,column=5)     
      Button(root, text="-",font=( 'aria' ,15, 'bold' ), command=inclick10,bg="yellow", fg = "black",activebackground="black").grid(row=60,column=6)
      ################################################
      var12=BooleanVar()
      counter12 =IntVar()
      def onClick11(event=None):
            counter12.set(counter12.get() + 1)
      def inclick11(event=None):
            counter12.set(counter12.get()-1)
            if(counter12.get()<0):
              counter12.set(0)
      checkbutton12 = Checkbutton(root,font=( 'aria' ,20, 'bold' ),text = data[11][1],variable = var12).grid(row=66,column=1)
      Button(root, text="+",font=( 'aria' ,15, 'bold' ), command=onClick11,bg="yellow", fg = "black",activebackground="black").grid(row=66,column=4)
      Label(root,text="+",font=( 'aria' ,12, 'bold' ), textvariable=counter12).grid(row=66,column=5)     
      Button(root, text="-",font=( 'aria' ,15, 'bold' ), command=inclick11,bg="yellow", fg = "black",activebackground="black").grid(row=66,column=6)
      def show():
            list2=[var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get(),var9.get(),var10.get(),var11.get(),var12.get()]
            list3=[counter1.get(),counter2.get(),counter3.get(),counter4.get(),counter5.get(),counter6.get(),counter7.get(),counter8.get(),counter9.get(),counter10.get(),counter11.get(),counter12.get()]
            for i in range(len(list2)):
                  if(list2[i]==True):
                     conn=sqlite3.connect("order.db")
                     c=conn.cursor()
                     c.execute('INSERT INTO order1(Item_id,Item_name,quantity,Price,Time,Roll) VALUES(?,?,?,?,?,?)',(data[i][0],data[i][1],list3[i],data[i][2],data[i][3],x))
                     conn.commit()
            final(x)
      Button(root,text="Add ",font=( 'aria' ,15, 'bold' ),height=2,width=4,command=show,bg="red", fg = "black",activebackground="black").grid(row=48)
def forget():
    
        

    def k():
        global newroll
        global newpasswd
        new = Toplevel(main_screen)
        new.geometry("1500x1000")
        newroll = StringVar()
        newpasswd = StringVar()
        l1=Label(new,height="2", width="30", text="enter your roll no", font=('arial', 16))
        l1.pack(fill=BOTH)
        e1=Entry(new, textvariable=newroll, font=('arial', 16))
        e1.pack(fill=BOTH)
        l2=Label(new,height="2", width="30",text="enter new password", font=('arial', 16))
        l2.pack(fill=BOTH)
        e2=Entry(new,textvariable=newpasswd, font=('arial', 16))
        e2.pack(fill=BOTH)
        b1=Button(new, text="Save", command=setpassword,bg="Green", font=('arial', 16))
        b1.pack(fill=BOTH)
        b1=Button(new, text="Exit", command=new.destroy,bg="red", font=('arial', 16))
        b1.pack(fill=BOTH)
        
    def setpassword():
        import sqlite3
        conn=sqlite3.connect("student.db")
        c=conn.cursor()
        val='UPDATE student SET Pass =?  WHERE Roll = ?'
        c.execute(val,[newpasswd.get(),newroll.get()])
        conn.commit()
    def c():
        dd=otp1.get()
        dd=int(dd)
        if(dd==otp):
            print("true")
            messagebox.showinfo("Frappers", "Correct Otp")
            k()
        else:
            messagebox.showinfo("Frappers", "Wrong otp")  
            print("enter correct otp")


    def otpp(r):
        global otp
        global otp1
        otp=r
        print(otp)
        otp1=IntVar()
        forg = Toplevel(main_screen)
        forg.geometry("1500x1000")
        Label(forg, text="Enter Your OTP " ,font=('arial', 24)).pack(fill=BOTH)
        otpentry=Entry(forg,textvariable=otp1 ,font=('arial', 16))
        otpentry.pack(fill=BOTH)
        print(otp1.get())
        Button(forg, height="2", width="30",text="Check",bg="green", font=('arial', 16),command=c).pack()





    def m():
        import random
        import smtplib
        r=random.randint(1000,9999)
        gmailaddress = "frappers100@gmail.com"
        gmailpassword = "frappers@1234"
        mailto = receiver_email.get()
        msg = f"otp is {r}"
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.starttls()
        mailServer.login(gmailaddress, gmailpassword)
        mailServer.sendmail(gmailaddress, mailto, msg)
        print(" \n Sent!")
        mailServer.quit()
        otpp(r)

    global receiver_email
    reg1 = Toplevel(main_screen)
    reg1.title("forgot password")
    reg1.geometry("1500x1000")
    receiver_email = StringVar()
    email1 = Label(reg1,height="2", width="10", text="Enter  Your Email Address", font=('arial', 16))
    email1.pack(fill=BOTH)
    receiver = Entry(reg1,textvariable=receiver_email, font=('arial', 16))
    receiver.pack(fill=BOTH)
    r=receiver_email.get()
    send = Button(reg1,text="Send Otp",command= m,bg="green", font=('arial', 16))
    send.pack(fill=BOTH)
    reg1.mainloop()
#will craete pilow
def main_account_screen():
    from PIL import Image,ImageTk 
    global main_screen
    main_screen = Tk() 
    c=Canvas(main_screen,width="300",height="600") 
    main_screen.geometry("1500x1000")  
    main_screen.title("Account Login") 
    img = ImageTk.PhotoImage(Image.open("C:\\frappers\\account\\logo.png"))
    panel = Label(main_screen, image = img)
    panel.pack(side = "top", fill = "both", expand = "yes")
    Button(main_screen,text="signup", height="2", width="30",command=register, font=('arial', 16),bg="green").pack(fill=BOTH)
    Button(main_screen,text="login", height="2", width="30",command=login, font=('arial', 16),bg="yellow").pack(fill=BOTH)
    Button(main_screen, text = "Forget Password", height="2", width="30", command = forget, font=('arial', 16),bg="blue").pack(fill=BOTH)
    Button(main_screen, text = "Exit", height="2", width="30", command = main_screen.destroy, font=('arial', 16),bg="red").pack(fill=BOTH)
    c.pack()
    main_screen.mainloop()
main_account_screen()