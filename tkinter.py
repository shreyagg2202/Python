import tkinter as tk

root = tk.Tk()
root.geometry("600x500")
root.minsize(300,200)
root.maxsize(600,500)
root.title("My GUI")

b1 = tk.Button(root,text="Submit",bg='red',fg='white',activebackground='yellow',
              height=2,width=25,font=('ALGERIAN',20,'bold'))
#b1.pack(side = 'left')
b1.place(x=100,y=50)
#b1.grid(rows=1,columns=1)

b2 =tk.Label(root,text="Name",bg='red',fg='white',
              height=1,width=25,font=('ALGERIAN',20,'bold'))
b2.place(x=100,y=150)

e = tk.Entry(root)
e.place(x=400,y=150)










root.mainloop()
