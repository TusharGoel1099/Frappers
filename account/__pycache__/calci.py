from tkinter import *
import sqlite3
from show import *
conn=sqlite3.connect("final.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS final1(
            Item_id integer NOT NULL,
            Item_name  TEXT ,
            Total_quantity  integer NOT NULL,
            Total_price integer ,
            Total_time integer ,
            Roll integer NOT NULL,
            FOREIGN KEY (Roll) REFERENCES order1(Roll),
            FOREIGN KEY (Item_name) REFERENCES order1(Item_name),
            FOREIGN KEY (Item_id) REFERENCES order1(Item_id)
            )""")
conn.commit()
# thsi is used to fnal calculate things
def final(x):
    global data2 
    conn=sqlite3.connect("order.db")
    c=conn.cursor()
    c.execute("SELECT * FROM order1 WHERE Roll=?", (x,))
    data2=c.fetchall() 
    total_price_time(data2,x)
    total_quantity(data2)
    conn=sqlite3.connect("final.db")
    c=conn.cursor()
    c.execute('INSERT INTO final1(Item_id,Item_name,Total_quantity,Total_Price,Total_Time,Roll) VALUES(?,?,?,?,?,?)',("totam id","total items",quantity,t_price,t_time,x)) 
    conn.commit()
    conn=sqlite3.connect("order.db")
    c=conn.cursor()
    c.execute("DELETE FROM order1 WHERE Roll=?", (x,))
    conn.commit()
    final2(x)

    conn=sqlite3.connect("final.db")
    c=conn.cursor()
    c.execute("DELETE  FROM final1 WHERE Roll=?", (x,)) 
    
    conn.commit()
def total_price_time(data2,x):
    global t_price
    global t_time
    #we have created global window
    l=0
    k=0
    t_time=0
    price=0
    t_price=0
    for i in data2:
        price=(i[2]*i[3])
        t_price=t_price+price
        k=i[2]
        l=i[4]
        time=k*l
        t_time=t_time+time
        conn=sqlite3.connect("final.db")
        c=conn.cursor()
        c.execute('INSERT INTO final1(Item_id,Item_name,Total_quantity,Total_Price,Total_Time,Roll) VALUES(?,?,?,?,?,?)',(i[0],i[1],i[2],price,time,x)) 
        conn.commit() 
def total_quantity(data2):
    global quantity
    quantity=0
    for i in data2:
        quantity=quantity+i[2]

       