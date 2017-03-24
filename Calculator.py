from tkinter import*
from tkinter import messagebox



def Input(root):

	global e,e2
	l =Label(root,text = "Enter First no.   ")
	l.pack()
	e = Entry(root)
	e.pack()
	l2 = Label(root,text = "Enter second no.")
	l2.pack()
	e2 = Entry(root)
	e2.pack()

def ADD():
	global e,e2
	no1 = float(e.get())
	no2 = float(e2.get())
	result = no1 + no2
	m = messagebox.showinfo("   Addition    ",result)
	m.pack()



def SUB():
	global e,e2
	no1 = float(e.get())
	no2 = float(e2.get())
	result = no1 - no2
	m = messagebox.showinfo("Substraction ",result)
	m.pack()

def MUL():
	global e,e2
	no1 = float(e.get())
	no2 = float(e2.get())
	result = no1 * no2
	m = messagebox.showinfo("Multiplication",result)
	m.pack()

def DIV():
	global e,e2
	no1 = float(e.get())
	no2 = float(e2.get())
	result = no1 / no2
	m = messagebox.showinfo("   Division     ",result)
	m.pack()
def text():
	str = "Creator : Shekhar Patil\nVersion : 1.0.0\nThank you."
	mes = messagebox.showinfo("About",str)


def main():
	global root
	root = Tk()
	menu1 = Menu(root)
	menu2 = Menu(root)

	m = Menu(menu1)
	m.add_command(label = "Exit",command = root.destroy)
	m.add_separator()
	m.add_command(label = "About",command = text)
	menu1.add_cascade(label="File", menu=m)

	
	root.config(m=menu1)
	root.geometry("400x300")

	Input(root)

	b = Button(root,text = "   Addition    ",command = ADD)
	b.pack()
	b2 = Button(root,text = "Substraction ", command = SUB)
	b2.pack()
	b3 = Button(root,text = "Multiplication",command = MUL)
	b3.pack()
	b4 = Button(root,text = "   Division     ",command = DIV)
	b4.pack()

	root.mainloop()
main()