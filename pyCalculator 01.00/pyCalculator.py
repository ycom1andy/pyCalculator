from tkinter import *
from array import *

root = Tk()

root.title="andys calculator"
root.font='Sans Serif, 10, bold'
# inputField = if#
iF = Entry(root, relief = SUNKEN, borderwidth = 0, width=40,  fg='darkred', bg='#ffffff', justify=RIGHT, font=('Sans Serif', 11, 'bold') )
iF.grid(row=0, column=0, columnspan=4)
tF = Entry(root, relief = SUNKEN, borderwidth = 0, width=40, fg='darkred', bg='#ffffff', justify=RIGHT, font=('Sans Serif', 11, 'bold'))

 

def button_click(number):
    
    current = iF.get()
    iF.delete(0,END)
    iF.insert(0, str(current) + str(number))
    

    
def button_clear():
    iF.delete(0, END)
    tF.delete(0, END)

    

def clear_last():
    current = iF.get()
    z = len(current)
    y = (z-1)
    iF.delete(y,z)


     
def button_equal():
    # operation chain 
    tF.delete(0, END)
    opc = iF.get()
   
    res = eval(opc)

    tF.insert(0,' = '+str(res))



# create Buttons#
 
button_1 = Button(root, text="1", width=8, height=4, bg="#3b4358", fg="white", command=lambda: button_click(1))
button_2 = Button(root, text="2", width=8, height=4, bg="#3b4358", fg="white", command=lambda: button_click(2))
button_3 = Button(root, text="3", width=8, height=4, bg="#3b4358", fg="white", command=lambda: button_click(3))
button_4 = Button(root, text="4", width=8, height=4, bg="#3b4358", fg="white", command=lambda: button_click(4))
button_5 = Button(root, text="5", width=8, height=4, bg="#3b4358", fg="white", command=lambda: button_click(5))
button_6 = Button(root, text="6", width=8, height=4, bg="#3b4358", fg="white", command=lambda: button_click(6))
button_7 = Button(root, text="7", width=8, height=4, bg="#3b4358", fg="white", command=lambda: button_click(7))
button_8 = Button(root, text="8", width=8, height=4, bg="#3b4358", fg="white", command=lambda: button_click(8))
button_9 = Button(root, text="9", width=8, height=4, bg="#3b4358", fg="white", command=lambda: button_click(9))
button_0 = Button(root, text="0", width=8, height=4, bg="#3b4358", fg="white", command=lambda: button_click(0))

timesBtn = Button(root, text="x", width=8, height=4, bg="#526599", fg="white", command=lambda: button_click('*'))
over_Btn = Button(root, text="/", width=8, height=4, bg="#526599", fg="white", command=lambda: button_click('/'))

brck_lft = Button(root, text="(", width=8, height=4, bg="#526599", fg="white", command=lambda: button_click('('))
brck_rgt = Button(root, text=")", width=8, height=4, bg="#526599", fg="white", command=lambda: button_click(')'))
setpoint = Button(root, text=".", width=8, height=4, bg="#526599", fg="white", command=lambda: button_click('.'))                                    

 
clearOneBtn = Button(root, text="CE", width=8, height=4, bg="#d03709", fg="white", command=clear_last)
                  
                  
clearBtn    = Button(root, text="c", width=8, bg="darkred", fg="white", height=4, command=button_clear)


add_Btn  = Button(root, text="+", width=8, height=4, bg="#526599", fg="white", command=lambda: button_click('+'))
sub_Btn  = Button(root, text="-", width=8, height=4, bg="#526599", fg="white", command=lambda: button_click('-'))
equalBtn = Button(root, text="=", width=8, bg="#2a3f5d", fg="orange", height=4, command=button_equal)
                  



# configure root
root.configure(bg="white")

# put the Buttons on screen #
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

clearBtn.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

add_Btn.grid(row=4, column=3)


button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

sub_Btn.grid(row=5, column=3)


button_0.grid(row=5, column=0)
timesBtn.grid(row=5, column=1)
over_Btn.grid(row=5, column=2)

clearOneBtn.grid(row=3, column=3)



setpoint.grid(row=6, column=0)
brck_lft.grid(row=6, column=1)
brck_rgt.grid(row=6, column=2)
equalBtn.grid(row=6, column=3)



tF.grid(row=1, column=0, columnspan=4)


root.mainloop()

