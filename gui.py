#tKINTER gUI Design project

# from tkinter import *

# root_neuron = Tk()

# root_neuron.geometry('900*600+150+120')

# root_neuron.maxsize(900,600)
# root_neuron.minimize(900,600)
# root_neuron.title("Welcome to the Dashboard")

# root_neuron.mainloop()



# import tkinter as tk
# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()


# using canvs ton to draw poicftures and complex graphics layout 


# from tkinter import *
# master = Tk()
# w = Canvas(master, width=40, height=60)
# w.pack()
# canvas_height=1000
# canvas_width=2000
# y = int(canvas_height / 2)
# w.create_line(0, y, canvas_width, y )
# mainloop()


# from tkinter import *
# master = Tk()
# var1 = IntVar()
# Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
# var2 = IntVar()
# Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)
# mainloop()

# from tkinter import *
# master = Tk()
# Label(master, text='First Name').grid(row=0)
# Label(master, text='Last Name').grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# mainloop()


#Frame : It acts like a container for holding widgets 

# from tkinter import *
  
# root = Tk()
# frame = Frame(root)
# frame.pack()
# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )
# redbutton = Button(frame, text = 'Red', fg ='red')
# redbutton.pack( side = LEFT)
# greenbutton = Button(frame, text = 'Brown', fg='brown')
# greenbutton.pack( side = LEFT )
# bluebutton = Button(frame, text ='Blue', fg ='blue')
# bluebutton.pack( side = LEFT )
# blackbutton = Button(bottomframe, text ='Black', fg ='black')
# blackbutton.pack( side = BOTTOM)
# root.mainloop()

# LIST BOX 

# from tkinter import *
  
# top = Tk()
# Lb = Listbox(top)
# Lb.insert(1, 'Menu')
# Lb.insert(2, 'Update')
# Lb.insert(3, 'Subscribe')
# Lb.insert(4, 'Any other')
# Lb.pack()
# top.mainloop()

#Radio button 
# from tkinter import *
# root = Tk()
# v = IntVar()
# Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)
# Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)
# mainloop()



#Adding Menu 

# from tkinter import *
  
# top = Tk()
# mb =  Menubutton ( top, text = "Click")
# mb.grid()
# mb.menu  =  Menu ( mb, tearoff = 0 )
# mb["menu"]  =  mb.menu
# cVar  = IntVar()
# aVar = IntVar()
# mb.menu.add_checkbutton ( label ='Contact', variable = cVar )
# mb.menu.add_checkbutton ( label = 'About', variable = aVar )
# mb.pack()
# top.mainloop()

# from tkinter import *
      
# root = Tk()
# menu = Menu(root)
# root.config(menu=menu)
# filemenu = Menu(menu)
# menu.add_cascade(label='File' , menu=filemenu)
# # menu.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New')
# filemenu.add_command(label='Open...')
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=root.quit)
# helpmenu = Menu(menu)
# menu.add_cascade(label='Help', menu=helpmenu)
# helpmenu.add_command(label='About')
# mainloop()

#Message box

# from tkinter import *
# main = Tk()
# ourMessage ='Welcome to the Dashboard'
# messageVar = Message(main, text = ourMessage)
# messageVar.config(bg='lightgreen')
# messageVar.pack( )
# main.mainloop( )

# # Import Module
# from tkinter import *
 
# # create root window
# root = Tk()
 
# # root window title and dimension
# root.title("Welcome to Dashboard")
# # Set geometry(widthxheight)
# root.geometry('650x400')
 
# # adding menu bar in root window
# # new item in menu bar labelled as 'New'
# # adding more items in the menu bar
# menu = Menu(root)
# item = Menu(menu)
# item.add_command(label='New')
# menu.add_cascade(label='File', menu=item)
# root.config(menu=menu)
 
# # adding a label to the root window
# lbl = Label(root, text = "Are you a Geek?")
# lbl.grid()
 
# # adding Entry Field
# txt = Entry(root, width=10)
# txt.grid(column =1, row =0)
 
 
# # function to display user text when
# # button is clicked
# def clicked():
 
#     res = " You wrote " + " " +  txt.get()
#     lbl.configure(text = res)
#     # lbl.configure(text = "I just got clicked")  #sec pr
# # button widget with red color text inside
# btn = Button(root, text = "Click me" ,
#              fg = "red", command=clicked)
# # Set Button Grid
# btn.grid(column=2, row=0)
 
# # Execute Tkinter
# root.mainloop()





import tkinter as tk


window = tk.Tk()
window.title("Eat-Up")

window.rowconfigure(0, minsize=800, weight=1)   #The first argument is 0, which sets the height of the first row to 800 pixels and makes sure that the height of the row grows proportionally to the height of the window. There’s only one row in the application layout, so these settings apply to the entire window.
window.columnconfigure(1, minsize=800, weight=1)
txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Welcome")
btn_save = tk.Button(frm_buttons, text="Upgrade")
#

# ...

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)


frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# ...

window.mainloop()



