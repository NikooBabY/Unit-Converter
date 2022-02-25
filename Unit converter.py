from tkinter import *
import tkinter.font as font
from functools import partial
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


def answer(n1):
    num1=n1.get()
    try:
        number1 = int(num1)
    except:
        messagebox.showerror('Error',"Use valid terms.")

    if result_from == 'Dhur' and result_to == 'Dhur':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Dhur' and result_to == 'Kattha':
        calculate = number1*0.05
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Dhur' and result_to == 'Bigha':
        calculate = number1*0.0025
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Dhur' and result_to == 'Ropani':
        calculate = number1*0.033275
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Dhur' and result_to == 'Aana':
        calculate = number1*0.5324
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Dhur' and result_to == 'Paisa':
        calculate = number1*2.1296
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kattha' and result_to == 'Kattha':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kattha' and result_to == 'Dhur':
        calculate = number1*20
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kattha' and result_to == 'Bigha':
        calculate = number1*0.05
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kattha' and result_to == 'Ropani':
        calculate = number1*0.6655
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kattha' and result_to == 'Aana':
        calculate = number1*10.648
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Kattha' and result_to == 'Paisa':
        calculate = number1*42.592
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Bigha' and result_to == 'Bigha':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Bigha' and result_to == 'Dhur':
        calculate = number1*400
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Bigha' and result_to == 'Kattha':
        calculate = number1*20
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Bigha' and result_to == 'Ropani':
        calculate = number1*13.31
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Bigha' and result_to == 'Aana':
        calculate = number1*212.96
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Bigha' and result_to == 'Paisa':
        calculate = number1*851.84
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Ropani' and result_to == 'Ropani':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Ropani' and result_to == 'Dhur':
        calculate = number1*30.05259
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Ropani' and result_to == 'Kattha':
        calculate = number1*1.50262
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Ropani' and result_to == 'Bigha':
        calculate = number1*0.07513
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Ropani' and result_to == 'Aana':
        calculate = number1*16
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Ropani' and result_to == 'Paisa':
        calculate = number1*64
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Aana' and result_to == 'Aana':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Aana' and result_to == 'Dhur':
        calculate = number1*1.87828
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Aana' and result_to == 'Bigha':
        calculate = number1*0.00469
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Aana' and result_to == 'Ropani':
        calculate = number1*0.0625
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Aana' and result_to == 'Paisa':
        calculate = number1*4
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Paisa' and result_to == 'Paisa':
        calculate = number1
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Paisa' and result_to == 'Dhur':
        calculate = number1*0.46957
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Paisa' and result_to == 'Kattha':
        calculate = number1*0.02347
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Paisa' and result_to == 'Bigha':
        calculate = number1*0.001173
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Paisa' and result_to == 'Ropani':
        calculate = number1*0.015625
        result.cget('text')
        result.configure(text=(calculate,result_to))

    elif result_from == 'Paisa' and result_to == 'Aana':
        calculate = number1*0.25
        result.cget('text')
        result.configure(text=(calculate,result_to))

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
#unitdd.current()
unitdd.bind('<<ComboboxSelected>>' ,selected)


f=StringVar()
fromdd= ttk.Combobox(root,width='35',textvariable=f)
fromdd.place(relx='0.57',rely='0.37',anchor='center')
#fromdd.current()
fromdd.bind('<<ComboboxSelected>>',fromfunc)

num=StringVar()
num_from=Entry(root,width=10,textvariable= num)
num_from.place(relx='0.9',rely='0.37',anchor='center')

answer=partial(answer,num_from)



t=StringVar()
todd=ttk.Combobox(root,width='35',textvariable=t)
todd.place(relx='0.57', rely='0.47', anchor='center')
#todd.current()
todd.bind('<<ComboboxSelected>>',tofunc)

result=Label(root,text='',bg='white',width=20)
result['font']=f3
result.place(relx='0.21',rely='0.6')

convert=Button(root,text='Convert',bg='#c8cfde',command=answer)
convert['font']=f2
convert.place(relx='0.46',rely='0.7')


root.mainloop()