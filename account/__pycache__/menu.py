from tkinter import *
import sqlite3
from create import *
# from calci import *
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
      root=Tk()
      conn=sqlite3.connect("reciept1.db")
      c=conn.cursor()
      c.execute("SELECT * FROM reciept1")
      data=c.fetchall()
      root.geometry("600x900")
      label = Label(root,text = "THE FRAPPERS MENU",height=10,width=20,fg="red").grid()
      var1=BooleanVar()
      checkbutton1 = Checkbutton(root,text = data[0][1],variable = var1).grid(row=1)
      counter1 =IntVar()
      def onClick(event=None):
            counter1.set(counter1.get() + 1)
      def inclick(event=None):
            counter1.set(counter1.get()-1)
      Label(root, textvariable=counter1).grid(row=3,column=1)
      Button(root, text="+", command=onClick, bg="dark green", fg = "black", width = 5, height = 1, cursor = "hand2").grid(row=3,column=0)
      Button(root, text="-", command=inclick, bg="dark green", fg = "black", width = 5, height = 1, cursor = "hand2").grid(row=3,column=2)
      var2=BooleanVar()
      checkbutton2 = Checkbutton(root,text = data[1][1],variable = var2).grid(row=4)
      counter2 =IntVar()
      def onClick1(event=None):
            counter2.set(counter2.get() + 1)
      def inclick1(event=None):
            counter2.set(counter2.get()-1)
      Label(root, textvariable=counter2).grid(row=6,column=1)
      Button(root, text="+", command=onClick1,bg="dark green", fg = "black", width = 5, height = 1, cursor = "hand2").grid(row=6,column=0)
      Button(root, text="-", command=inclick1,bg="dark green", fg = "black", width = 5, height = 1, cursor = "hand2").grid(row=6,column=2)
      def show():
            list2=[var1.get(),var2.get()]
            list3=[counter1.get(),counter2.get()]
            for i in range(len(list2)):
                  if(list2[i]==True):
                     conn=sqlite3.connect("order.db")
                     c=conn.cursor()
                     c.execute('INSERT INTO order1(Item_id,Item_name,quantity,Price,Time,Roll) VALUES(?,?,?,?,?,?)',(data[i][0],data[i][1],list3[i],data[i][2],data[i][3],x))
                     conn.commit()
            main_account_screen(x)
      Button(root,text="add",command=show,bg="red", fg = "black", width = 11, height = 4, cursor = "hand2").grid(row=9,column=0)
      root.mainloop()
x="17csu17654"
next(x)


