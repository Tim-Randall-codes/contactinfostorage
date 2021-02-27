import tkinter as tk
import csv

window1 = tk.Tk()

def store():
    name = namee.get()
    email = emaile.get()
    phone = phonee.get()
    with open('Data.txt', 'a') as Data_file:
        Data_w = csv.writer(Data_file)
        Data_w.writerow([str(name), str(email), str(phone)])
    namee.delete(0, tk.END)
    emaile.delete(0, tk.END)
    phonee.delete(0, tk.END)
        
def search():
    term = searche.get()
    with open('Data.txt') as Data_file:
        Data_r = csv.reader(Data_file)
        lst = list(Data_r)
        for item in lst:
            for i in item:
                if i == term:
                    display.delete(1.0, tk.END)
                    display.insert(1.0, str(item))
                else:
                    pass
        

leftl = tk.Label(window1, text="Store the info here")
leftl.grid(column=1, row=0)

rightl = tk.Label(window1, text="Retrieve the info here")
rightl.grid(column=3, row=0)

namel = tk.Label(window1, text="Name:")
namel.grid(column=0, row=1)

emaill = tk.Label(window1, text="Email:")
emaill.grid(column=0, row=2)

phonel= tk.Label(window1, text="Phone:")
phonel.grid(column=0, row=3)

namee = tk.Entry(window1, bg="light gray")
namee.grid(column=1, row=1)

emaile = tk.Entry(window1, bg="light gray")
emaile.grid(column=1, row=2)

phonee = tk.Entry(window1, bg="light gray")
phonee.grid(column=1, row=3)

storeb = tk.Button(window1, text="Store info", command=store)
storeb.grid(column=1, row=4)

searchl = tk.Label(window1, text="Search:")
searchl.grid(column=2, row=1)

searche = tk.Entry(window1, bg="light gray")
searche.grid(column=3, row=1)

searchb = tk.Button(window1, text="Search stored info", command=search)
searchb.grid(column=3, row=2)

display = tk.Text(window1, height=5, width=30)
display.grid(column=3, row=4)

window1.title("Store Contact Info")

window1.mainloop()
