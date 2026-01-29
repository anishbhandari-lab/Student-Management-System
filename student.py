import tkinter as tk
from tkinter import ttk #It provides a set of themed widgets that offer a native look and feel
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
        searchBtn= tk.Button(optFrame, text="Search Student", bd=3, relief="raised", bg="light gray", width=22, font=("Arial", 20, "bold"))
        searchBtn.grid(row=1, column=0, padx=30, pady=30)
        updBtn= tk.Button(optFrame, text="Update Records", bd=3, relief="raised", bg="light gray", width=22, font=("Arial", 20, "bold"))
        updBtn.grid(row=2, column=0, padx=30, pady=30)
        remBtn= tk.Button(optFrame, text="Remove Student", bd=3, relief="raised", bg="light gray", width=22, font=("Arial", 20, "bold"))
        remBtn.grid(row=3, column=0, padx=30, pady=30)
        allBtn= tk.Button(optFrame, text="Show All", bd=3, relief="raised", bg="light gray", width=22, font=("Arial", 20, "bold"))
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
        self.table=ttk.Treeview(tabFrame, xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, columns=("roll", "name", "father's name", "subject", "Grade"))
        x_scroll.config(command=self.table.xview)
        y_scroll.config(command=self.table.yview)
        self.table.heading("roll", text="Roll_no")
        self.table.heading("name", text="Name")
        self.table.heading("father's name", text="Father's name")
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
        okBtn=tk.Button(self.addFrame, text="Submit", bd=3, relief="raised", font=("Arial", 15, "bold"),width=18)
        okBtn.grid(row=5, column=0, pady=20, columnspan=3, padx=10)
        
root = tk.Tk()
obj= std(root)
root.mainloop()