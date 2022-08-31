from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def aplicar():    
    tv.insert("","end", values=(
        entry_um.get(),
        entry_dois.get(),
        entry_tres.get(),
        entry_quatro.get(),
        entry_cinco.get(),
        entry_seis.get()
    ))

    entry_um.delete(0, END)
    entry_dois.delete(0, END)
    entry_tres.delete(0, END)
    entry_quatro.delete(0, END)
    entry_cinco.delete(0, END)
    entry_seis.delete(0, END)

def fifo():
    pass

def otimo():
    pass

def lru():
    pass

def lifo():
    pass

app = Tk()
app.title('Ordenação')
app.geometry('600x300')

#Criando Labels e Entrys
lb_numeros = Label(app, text='Informe os dados ')
lb_numeros.grid(row=0, column=0, columnspan=3)
entry_um = Entry(app)
entry_dois = Entry(app)
entry_tres = Entry(app)
entry_quatro = Entry(app)
entry_cinco = Entry(app)
entry_seis = Entry(app)

entry_um.grid(row=1, column=0)
entry_dois.grid(row=1, column=1)
entry_tres.grid(row=1, column=2)
entry_quatro.grid(row=1, column=3)
entry_cinco.grid(row=1, column=4)
entry_seis.grid(row=1, column=5)

#criando botões
bt_aplicar = Button(app, text='Aplicar', command=aplicar)
bt_fifo = Button(app, text='fifo', command=fifo)
bt_lru = Button(app, text='lru', command=lru)
bt_otimo = Button(app, text='otimo', command=otimo)
bt_lifo = Button(app, text='lifo', command=lifo)

bt_aplicar.grid(row=2, column=2)
bt_fifo.grid(row=3, column=3)
bt_lru.grid(row=3, column=4)
bt_otimo.grid(row=4, column=3)
bt_lifo.grid(row=4, column=4)

#criando tabela
tv = ttk.Treeview(app, columns=('#1','#2','#3','#4','#5','#6'), show='headings')
tv.column('#1', minwidth=0, width=50)
tv.heading('#1', text=entry_um.get())
tv.column('#2', minwidth=0, width=50)
tv.heading('#2', text='#2')
tv.column('#3', minwidth=0, width=50)
tv.heading('#3', text='#3')
tv.column('#4', minwidth=0, width=50)
tv.heading('#4', text='#4')
tv.column('#5', minwidth=0, width=50)
tv.heading('#5', text='#5')
tv.column('#6', minwidth=0, width=50)
tv.heading('#6', text='#6')


tv.grid(column=0,row=3,columnspan=3, pady=5)

app.mainloop()