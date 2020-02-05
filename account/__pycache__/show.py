from tkinter import *
import sqlite3
sys.path.append("c:\\programdata\\anaconda3\\lib\\site-packages")
from fpdf import FPDF
from tkinter import messagebox
conn=sqlite3.connect("record.db")
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS record1(
            Item_id integer NOT NULL,
            Item_name  TEXT ,
            quantity  integer NOT NULL,
            price integer ,
            time integer ,
            Roll integer NOT NULL,
            FOREIGN KEY (Roll) REFERENCES final1(Roll),
            FOREIGN KEY (Item_name) REFERENCES final1(Item_name),
            FOREIGN KEY (Item_id) REFERENCES final1(Item_id)
            )""")
conn.commit()

def final2(x):
    last=Tk()
    def show2():
        conn=sqlite3.connect("final.db")
        c=conn.cursor()
        c.execute("SELECT * FROM final1 WHERE Roll=?", (x,))
        data3=c.fetchall()
        list1=[]
        list3=[]
        for i in range(len(data3)):
            list3.append(0)
        j=0
        for i in data3:
            conn=sqlite3.connect("record.db")
            c=conn.cursor()
            c.execute('INSERT INTO record1(Item_id,Item_name,quantity,Price,Time,Roll) VALUES(?,?,?,?,?,?)',(i[0],i[1],i[2],i[3],i[4],i[5],)) 
            conn.commit()
            if (i[5]==x):
                list3[j]=(i[1],i[2],i[3],i[4])
                p=i
                j=j+1
                pdf_id=str(i[5])

        messagebox.showinfo("frappers", f" YOUR TOTAL BILL OF {p[2]} ITEMS  IS  {p[3]} RUPPESS \n PLEASE WAIT YOUR ORDER WILL BE DELIVERED IN {p[4]}  MINUTES ")          
        
        spacing=1
        conn=sqlite3.connect("student.db")
        c=conn.cursor()
        c.execute("SELECT Email FROM student WHERE Roll=?", (pdf_id,))
        pdf_email=c.fetchone()
        if(p[3]>0):
           print("id is=",pdf_id)
           simple_table(spacing,list3,pdf_id)
           messagebox.showinfo("frappers", "Go And Check Your Reciept On Your Mail")
           pdf_emaill(pdf_email,pdf_id)
           
        else:
           messagebox.showinfo("frappers", "NO Food Item Is Selected By You")
           
        last.destroy()
        conn=sqlite3.connect("final.db")
        c=conn.cursor()
       
    last.geometry("1500x1000")
    Button(last,text="GENERATE RECIEPT", height="2", width="30",command=show2 , font=('arial', 16),fg = "black", bd = 0, bg = "green", cursor = "hand2").pack(fill=BOTH)
    Button(last, text = "Exit", height="2", width="30", command = last.destroy,fg = "black", bd = 0, bg = "red",font=('arial', 16)).pack(fill=BOTH)
    last.mainloop()
def simple_table(spacing,list3,pdf_id):
    data2=[]
    data1=[['Items', 'Quantity','Price','Time']]
    data2.append(data1)
    for i in range(len(list3)):
        data = [[list3[i][0],str(list3[i][1]),str(list3[i][2]),str(list3[i][3])]]
        data2.append(data)
    pdf = FPDF()
    pdf.set_font("Arial", size=28)
    pdf.add_page()
    pdf.image('C:\\frappers\\account\\logo.png', x = None, y = None, w = 0, h = 0, type = 'PNG' )
    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    for i in data2:
        for row in i:
            for item in row:
                pdf.cell(col_width, row_height*spacing,
                         txt=item, border=1)
            pdf.ln(row_height*spacing) 
    pdf.cell(100,100,"Frappers Bill Reciept:- Thanku for placing order with us",align="center")        
    pdf.output("C:\\frappers\\pdf\\."+pdf_id+".pdf")    
def pdf_emaill(pdf_email,pdf_id):
    from email.message import EmailMessage
    import smtpd,smtplib
    files=["C:\\frappers\\pdf\\."+pdf_id+".pdf"]
    gmailaddress = "frappers100@gmail.com"
    gmailpassword = "frappers@1234"
    msg=EmailMessage()
    msg['subject']='order reciept'
    msg['from']=gmailaddress
    msg['to']=pdf_email
    msg.set_content('pdf attached')
    msg.set_content('Your Order Reciept')

    for file in files:
        with open(file,'rb') as f:
            file_data=f.read()
            # file_type=imghdr.what(f.name)
            file_name=f.name

    msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as c:
        c.login(gmailaddress,gmailpassword)

        c.send_message(msg)

 