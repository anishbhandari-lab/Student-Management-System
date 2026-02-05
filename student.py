import tkinter as tk
from tkinter import ttk #It provides a set of themed widgets that offer a native look and feel
from tkinter import messagebox
import pymysql
class std():
    def __init__(self, root):
        self.root=root
        self.root.title("Student Record")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}+0+0")

        title= tk.Label(self.root, text="Student Record Management System", bd=4, relief="raise", bg="Steel Blue", font=("Arial", 40, "bold"))
        title.pack(side="top")
        
        #option frame
        optFrame = tk.Frame(self.root, bd=5, relief="ridge", bg="navy blue")
        optFrame.place(width=self.width/3, height=self.height-180, x=70, y=100)
        addBtn= tk.Button(optFrame, text="Add Student", bd=3, command=self.addFrameFun, relief="raised", bg="light gray", width=22, font=("Arial", 20, "bold"))
        addBtn.grid(row=0, column=0, padx=30, pady=30)
        searchBtn= tk.Button(optFrame, text="Search Student",command=self.searchFrameFun, bd=3, relief="raised", bg="light gray", width=22, font=("Arial", 20, "bold"))
        searchBtn.grid(row=1, column=0, padx=30, pady=30)
        updBtn= tk.Button(optFrame, text="Update Records", command=self.updFrameFun, bd=3, relief="raised", bg="light gray", width=22, font=("Arial", 20, "bold"))
        updBtn.grid(row=2, column=0, padx=30, pady=30)
        remBtn= tk.Button(optFrame, text="Remove Student",command=self.delFrameFun, bd=3, relief="raised", bg="light gray", width=22, font=("Arial", 20, "bold"))
        remBtn.grid(row=3, column=0, padx=30, pady=30)
        allBtn= tk.Button(optFrame, text="Show All", command=self.showall, bd=3, relief="raised", bg="light gray", width=22, font=("Arial", 20, "bold"))
        allBtn.grid(row=4, column=0, padx=30, pady=30)

        #Data frame
        self.detFrame = tk.Frame(self.root, bd=5, relief="ridge", bg="light gray")
        self.detFrame.place(width=self.width/1.8, height=self.height-180, x=self.width/3+100, y=100)
        lbl= tk.Label(self.detFrame, text="Students Records", bg="Light Gray", font=("Arial", 25, "bold"))
        lbl.pack(side="top")
        self.tabFun()
        
    def tabFun(self):
        tabFrame = tk.Frame(self.detFrame, bd=4, relief="sunken", bg="cyan")
        tabFrame.place(width=self.width/1.8-65, height=self.height-280, x=34, y=70)

        x_scroll=tk.Scrollbar(tabFrame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")
        y_scroll=tk.Scrollbar(tabFrame, orient="vertical")
        y_scroll.pack(side="right", fill="y")
        self.table=ttk.Treeview(tabFrame, xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, columns=("rollno", "name", "father name", "subject", "Grade"))
        x_scroll.config(command=self.table.xview)
        y_scroll.config(command=self.table.yview)
        self.table.heading("rollno", text="Roll_no")
        self.table.heading("name", text="Name")
        self.table.heading("father name", text="Father name")
        self.table.heading("subject", text="Subject")
        self.table.heading("Grade", text="Grade")
        self.table["show"]="headings"
        self.table.pack(fill="both", expand=1)

    def addFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg="pink")
        self.addFrame.place(width=self.width/2.8-30, height=self.height-260, x=self.width/3-30, y=130)
        rnlbl= tk.Label(self.addFrame, text="Roll_No:", background="pink", font=("Arial", 15, "bold"))
        rnlbl.grid(row=0, column=0, padx=20, pady=20)
        self.rollno= tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3, bg="pink")
        self.rollno.grid(row=0, column=1, padx=2, pady=8)
        nlbl= tk.Label(self.addFrame, text="Name:", background="pink", font=("Arial", 15, "bold"))
        nlbl.grid(row=1, column=0, padx=20, pady=20)
        self.Name= tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3, bg="pink")
        self.Name.grid(row=1, column=1, padx=2, pady=8)
        flbl= tk.Label(self.addFrame, text="Father's name:", background="pink", font=("Arial", 15, "bold"))
        flbl.grid(row=2, column=0, padx=20, pady=20)
        self.fname= tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3, bg="pink")
        self.fname.grid(row=2, column=1, padx=2, pady=8)
        slbl= tk.Label(self.addFrame, text="Subject:", background="pink", font=("Arial", 15, "bold"))
        slbl.grid(row=3, column=0, padx=20, pady=20)
        self.subject= tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3, bg="pink")
        self.subject.grid(row=3, column=1, padx=2, pady=8)
        glbl= tk.Label(self.addFrame, text="Grade:", background="pink", font=("Arial", 15, "bold"))
        glbl.grid(row=4, column=0, padx=20, pady=20)
        self.grade= tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3, bg="pink")
        self.grade.grid(row=4, column=1, padx=2, pady=8)
        okBtn=tk.Button(self.addFrame, command=self.addFun, text="Submit", bd=3, relief="raised", font=("Arial", 15, "bold"),width=18)
        okBtn.grid(row=5, column=0, pady=20, columnspan=3, padx=120)
        
    def desAdd(self):
        self.addFrame.destroy()

    def addFun(self):
        rn = self.rollno.get()
        name = self.Name.get()
        fname= self.fname.get()
        sub=self.subject.get()
        grade=self.grade.get()

        if rn and name and fname and sub and grade:
            rNo=int(rn)
            try:
                self.dbfun()
                self.cur.execute("INSERT INTO student (rollno, name, fname, sub, grade) VALUES (%s, %s, %s, %s, %s)",(rNo, name, fname, sub, grade))
                self.con.commit()
                tk.messagebox.showinfo("Success", f"student{name} with roll no {rNo} is Registered!")
                self.desAdd()
                self.cur.execute("SELECT * FROM student WHERE rollno=%s", (rNo,))
                row=self.cur.fetchone()
                self.table.delete(*self.table.get_children())
                self.table.insert('', tk.END, values=row)
                self.con.close()
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")
                self.desAdd()    
        else:
            tk.messagebox.showerror("Error", "Please fill all the data box")
    def searchFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg="pink")
        self.addFrame.place(width=self.width/2.8-30, height=self.height-350, x=self.width/3-30, y=130)
        optlbl= tk.Label(self.addFrame, text="Select:", background="pink", font=("Arial", 15, "bold"))
        optlbl.grid(row=0, column=0, padx=20, pady=20)
        self.option= ttk.Combobox(self.addFrame, width=17, values=("rollno", "name", "sub"), font=("Arial", 15, "bold"))
        self.option.set("Select option")
        self.option.grid(row=0, column=1, padx=10, pady=30)
        vallbl= tk.Label(self.addFrame, text="Value:", background="pink", font=("Arial", 15, "bold"))
        vallbl.grid(row=1, column=0, padx=20, pady=20)
        self.value= tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3, bg="pink")
        self.value.grid(row=1, column=1, padx=2, pady=8)
        okBtn=tk.Button(self.addFrame, command=self.searchFun, text="Submit", bd=3, relief="raised", font=("Arial", 15, "bold"),width=18)
        okBtn.grid(row=5, column=0, pady=20, columnspan=3, padx=120)
    def searchFun(self):
        opt=self.option.get()
        val=self.value.get()
        if opt == "rollno":
            rn=int(val)
            try:
                self.dbfun()
                self.cur.execute("select * From student where rollno=%s",(rn, ))
                row=self.cur.fetchone()
                self.table.delete(*self.table.get_children())
                self.table.insert('', tk.END, values=row)
                self.desAdd()
                self.con.close()
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error:{e}")
        else:
            try:
                self.dbfun()
                query = f"SELECT * FROM student  where {opt}=%s"
                self.cur.execute(query, (val))
                data = self.cur.fetchall()
                self.table.delete(*self.table.get_children())
                for row in data:
                    self.table.insert('', tk.END, values=row)
                self.desAdd()
                self.con.close()
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error: {e}")
    def dbfun(self):
        self.con=pymysql.connect(host="localhost", user="root", password="anish9843", database="project")
        self.cur = self.con.cursor()
    def updFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg="pink")
        self.addFrame.place(width=self.width/2.8-30, height=self.height-300, x=self.width/3-30, y=130)
        optlbl= tk.Label(self.addFrame, text="Select:", background="pink", font=("Arial", 15, "bold"))
        optlbl.grid(row=0, column=0, padx=20, pady=20)
        self.option= ttk.Combobox(self.addFrame, width=17, values=("name", "sub", "Grade", "fname"), font=("Arial", 15, "bold"))
        self.option.set("Select option")
        self.option.grid(row=0, column=1, padx=10, pady=30)
        vallbl= tk.Label(self.addFrame, text="New_Value:", background="pink", font=("Arial", 15, "bold"))
        vallbl.grid(row=1, column=0, padx=20, pady=20)
        self.value= tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3, bg="pink")
        self.value.grid(row=1, column=1, padx=2, pady=8)
        rolllbl= tk.Label(self.addFrame, text="rollno:", background="pink", font=("Arial", 15, "bold"))
        rolllbl.grid(row=2, column=0, padx=20, pady=20)
        self.roll= tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3, bg="pink")
        self.roll.grid(row=2, column=1, padx=2, pady=8)
        okBtn=tk.Button(self.addFrame, command=self.updFun, text="Submit", bd=3, relief="raised", font=("Arial", 15, "bold"),width=18)
        okBtn.grid(row=3, column=0, pady=20, columnspan=3, padx=120)
    def updFun(self):
         opt=self.option.get()
         val=self.value.get()
         rNo=int(self.roll.get())
         try:
             self.dbfun()
             query=f"Update student set {opt}=%s where rollno=%s"
             self.cur.execute(query, (val, rNo))
             self.con.commit()
             tk.messagebox.showinfo("Success", f"Record updated for students with rollno. {rNo}")
             self.desAdd()
             self.cur.execute("SELECT * FROM student WHERE rollno=%s", (rNo, ))
             row=self.cur.fetchone
             self.table.delete(self.table.get_children())
             self.table.insert('', tk.END, values=row)
             self.con.close()
         except Exception as e:
             tk.messagebox.showerror("Error", f"Error: {e}")
    def showall(self):
         try:
             self.dbfun()
             self.cur.execute("SELECT * FROM student ")
             data=self.cur.fetchall()
             for row in self.table.get_children():
                 self.table.delete(row)
             for i in data:
                 self.table.insert('', tk.END, values=i)
             self.con.close()
         except Exception as e:
             tk.messagebox.showerror("Error", f"Error: {e}")
    def delFrameFun(self):
        self.addFrame = tk.Frame(self.root, bd=5, relief="ridge", bg="pink")
        self.addFrame.place(width=self.width/2.8-30, height=self.height-550, x=self.width/3-30, y=130)
        rnlbl= tk.Label(self.addFrame, text="Roll_No:", background="pink", font=("Arial", 15, "bold"))
        rnlbl.grid(row=0, column=0, padx=20, pady=20)
        self.rollno= tk.Entry(self.addFrame, width=18, font=("Arial", 15, "bold"), bd=3, bg="pink")
        self.rollno.grid(row=0, column=1, padx=2, pady=8)
        okBtn=tk.Button(self.addFrame, command=self.delfun, text="Submit", bd=3, relief="raised", font=("Arial", 15, "bold"),width=18)
        okBtn.grid(row=1, column=0, pady=20, columnspan=3, padx=120)
    def delfun(self):
        rNo= int(self.rollno.get())
        try:
            self.dbfun()
            self.cur.execute("DELETE FROM student Where rollno=%s", rNo)
            self.con.commit()
            tk.messagebox.showinfo("Success", f"Student data deleted with rollno:{rNo}")
            self.con.close()
            self.desAdd()
        except Exception as e:
             tk.messagebox.showerror("Error", f"Error: {e}")
root = tk.Tk()
obj= std(root)
root.mainloop()