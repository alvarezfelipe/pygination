from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#criando tabela
tv = ttk.Treeview(None, columns=('#1','#2','#3','#4','#5','#6'), show='headings')
tv.column('#1', minwidth=0, width=50)
tv.heading('#1', text='#1')
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