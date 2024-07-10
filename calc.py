#import
from Tkinter import*
 
#root
root = Tk()
root.title("Calculator") #this gives the app title at the top
root['bg'] = '#5DADE2'
 
 
#function
def button_click(number):
    current = inp.get()
    inp.delete(0, END)
    inp.insert(0, str(current) + str(number))
 
def button_clear():
    inp.delete(0, END)
 
def button_add():
    first_number = inp.get()
    global f_num
    global math
    math='addition'
    f_num = float(first_number)
    inp.delete(0, END)
 
def button_equal():
    second_number= inp.get()
    inp.delete(0,END)
    if math=='addition':
        inp.insert(0, f_num + float(second_number))
    elif math=='substraction':
        inp.insert(0, f_num - float(second_number))
    elif math=='multiplication':
        inp.insert(0, f_num * float(second_number))
    else:
        inp.insert(0, f_num / float(second_number))
 
def button_subtract():
    first_number = inp.get()
    global f_num
    global math
    math = 'substraction'
    f_num = float(first_number)
    inp.delete(0, END)
 
def button_divide():
    first_number = inp.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first_number)
    inp.delete(0, END)
 
def button_multiply():
    first_number = inp.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = float(first_number)
    inp.delete(0, END)
 
#entry
inp = Entry(root, width=45, fg="#2E6AD2", borderwidth=2)  #color in hexcode
inp.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
 
#button
button_1= Button(root, text="1", padx=40, pady=20,  command=lambda:button_click(1))
button_2= Button(root, text="2", padx=40, pady=20,  command=lambda:button_click(2))
button_3= Button(root, text="3", padx=40, pady=20,  command=lambda:button_click(3))
button_4= Button(root, text="4", padx=40, pady=20,  command=lambda:button_click(4))
button_5= Button(root, text="5", padx=40, pady=20,  command=lambda:button_click(5))
button_6= Button(root, text="6", padx=40, pady=20,  command=lambda:button_click(6))
button_7= Button(root, text="7", padx=40, pady=20,  command=lambda:button_click(7))
button_8= Button(root, text="8", padx=40, pady=20,  command=lambda:button_click(8))
button_9= Button(root, text="9", padx=40, pady=20,  command=lambda:button_click(9))
button_0= Button(root, text="0", padx=92, pady=20,  command=lambda:button_click(0))
 
button_add= Button(root, text="+", padx=39, pady=55.25,  command=button_add)
button_subtract= Button(root, text="-", padx=41, pady=20,  command=button_subtract)
button_multiply= Button(root, text="x", padx=41, pady=20,  command=button_multiply)
button_divide= Button(root, text="/", padx=41, pady=20,  command=button_divide)
 
button_equal= Button(root, text="=", padx=39, pady=55.25,  command=button_equal)
button_dot= Button(root, text=".", padx=43, pady=20,  command=lambda:button_click("."))
button_clear= Button(root, text="Clear", padx=29, pady=20,  command=button_clear)
 
'''When you have to use a function with parenthesis in the command you will have to use lambda: (as shown above)
   in case of a normal fucntion DO NOT USE LAMBDA as this will result in an error'''
 
#BUTTONS NUMPAD
#last row
button_1.grid(row=4,column=0,)
button_2.grid(row=4,column=1,)
button_3.grid(row=4,column=2,)
#2nd row
button_4.grid(row=3,column=0,)
button_5.grid(row=3,column=1,)
button_6.grid(row=3,column=2,)
#first number row
button_7.grid(row=2 ,column=0 ,)
button_8.grid(row=2 ,column=1 ,)
button_9.grid(row=2,column=2 ,)
button_0.grid(row=5,column=0 ,columnspan=2, )
 
#specials gird
button_equal.grid(row=4 ,column=3 ,rowspan=2)
button_clear.grid(row=1 ,column=0 ,)
button_dot.grid(row=5,column=2,)
 
button_add.grid(row=2 ,column=3 ,rowspan=2)
button_subtract.grid(row=1, column=3)
button_multiply.grid(row=1, column=2)
button_divide.grid(row=1, column=1)
#closing 
root.mainloop()