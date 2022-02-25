from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from tkinter import ttk

root=Tk()
root.geometry('500x600+500+100')
root.minsize(500,600)
root.maxsize(500,600)
root.title('Unit Converter')
root.configure(bg='Sky blue')

f1=font.Font(family='Serif',size='30')
f2=font.Font(family='Serif',size='10')
f3=font.Font(family='Serif',size='20')

values_dict = {
        "Dhur" : {"Dhur" : 1, "Kattha" : 0.05, "Bigha" : 0.0025, "Ropani" : 0.033275, "Aana" : 0.5324, "Paisa" : 2.1296},
        "Kattha" : {"Dhur" : 20, "Kattha" : 1, "Bigha" : 0.05, "Ropani" : 0.6655, "Aana" : 10.648, "Paisa" : 42.592},
        "Bigha" : {"Dhur" : 400, "Kattha" : 20, "Bigha" : 1, "Ropani" : 13.31, "Aana" : 212.96, "Paisa" : 851.84},
        "Ropani" : {"Dhur" : 30.05259, "Kattha" : 1.50262, "Bigha" : 0.07513, "Ropani" : 1, "Aana" : 16, "Paisa" : 64},
        "Aana" : {"Dhur" : 1087828, "Kattha" : 0.09391, "Bigha" : 0.00469, "Ropani" : 0.0625, "Aana" : 1, "Paisa" : 4},
        "Paisa" : { "Dhur" : 0.46957, "Kattha" : 0.02347, "Bigha" : 0.001173, "Ropani" : 0.015625, "Aana" : 0.25, "Paisa" : 1},
                    }

def cver_value(var1, var2, values_dict=values_dict):
    return values_dict[var1].get(var2)

def answer(var1, var2, num):
    try:
        num = int(num)
        if cver_value(var1, var2) == None:
            messagebox.showerror('Error',"Use valid terms.")
        else:
            result.cget("text")
            result.configure(text=((num * cver_value(var1, var2), var2)))
    except:
        messagebox.showerror()

def selected(event):
    global unit
    unit=event.widget.get()
    if unit == 'LandAreaMeasurement':
        fromdd['values']=('Dhur', 'Kattha', 'Bigha', 'Ropani', 'Aana', 'Paisa')
        todd['values']=('Dhur', 'Kattha', 'Bigha', 'Ropani', 'Aana', 'Paisa')


def fromfunc(event):
    global result_from
    result_from=event.widget.get()


def tofunc(event):
    global result_to
    result_to=event.widget.get()



main =Label(root,text='Unit Converter', bg='Sky blue',fg='Red')
main['font']=f1
main.place(relx='0.48',rely='0.1', anchor='center')

unit = Label(root, text='Unit:', bg='Sky blue')
unit['font']=f2
unit.place(relx='0.25', rely='0.28')

label_from = Label(root, text='From:',bg='Sky blue')
label_from['font']=f2
label_from.place(relx='0.238', rely='0.35')

to = Label(root, text='To:', bg='Sky blue')
to['font'] = f2
to.place(relx='0.268', rely='0.45')

unitdd=ttk.Combobox(root,width='35',)
unitdd['values']=('LandAreaMeasurement')
unitdd.place(relx='0.57',rely=0.3,anchor='center')
unitdd.bind('<<ComboboxSelected>>' ,selected)


f=StringVar()
fromdd= ttk.Combobox(root,width='35',textvariable=f)
fromdd.place(relx='0.57',rely='0.37',anchor='center')
fromdd.bind('<<ComboboxSelected>>',fromfunc)

num=StringVar()
num_from=Entry(root,width=10,textvariable= num)
num_from.place(relx='0.9',rely='0.37',anchor='center')


t=StringVar()
todd=ttk.Combobox(root,width='35',textvariable=t)
todd.place(relx='0.57', rely='0.47', anchor='center')
todd.bind('<<ComboboxSelected>>',tofunc)

result=Label(root,text='',bg='white',width=20)
result['font']=f3
result.place(relx='0.21',rely='0.6')

convert=Button(root,text='Convert',bg='#c8cfde',command=lambda: answer(f.get(), t.get(), num.get()))
convert['font']=f2
convert.place(relx='0.46',rely='0.7')

root.mainloop()