from tkinter import *
import sqlite3
from calci import *
from tkinter import PhotoImage

conn=sqlite3.connect("order.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS order1(
            Item_id integer NOT NULL,
            Item_name  TEXT ,
            quantity  integer NOT NULL,
            Price integer ,
            Time integer ,
            Roll integer NOT NULL,
            FOREIGN KEY (Time) REFERENCES reciept1(Time),
            FOREIGN KEY (Roll) REFERENCES reciept1(Roll),
            FOREIGN KEY (Price) REFERENCES reciept1(Price),
            FOREIGN KEY (Item_name) REFERENCES reciept1(Item_name),
            FOREIGN KEY (Item_id) REFERENCES reciept1(Item_id)
            )""")
conn.commit()
def next(x):
      root=Toplevel()
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
      Label(root,text="+",font=( 'aria' ,12, 'bold' ), textvariable=counter3).grid(row=18,column=5)     
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
      # root.mainloop()
# x="123"
# next(x)


