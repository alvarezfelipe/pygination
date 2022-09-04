from tkinter import *

import subst

class APP:
    global lista
    lista = list()

    def __init__(self, master=None):
        self.titleFont = ("MS Sans Serif", "16", "bold")
        self.subtitleFont = ("MS Sans Serif", "14", "bold")
        self.basicFont = {
            "family": "Arial",
            "size": "10",
            "weight": "normal",
            "slant": "roman",
            "underline": "0",
            "overstrike": "0"
        }

        self.widget1 = Frame(
            master,
            pady=10,
            padx=20
            )
        self.widget1.pack()

        self.widget2 = Frame(
            master,
            pady=10
            )
        self.widget2.pack()

        self.widget3 = Frame(
            master,
            pady=10
            )
        self.widget3.pack()

        self.widget4 = Frame(master)
        self.widget4.pack()

        self.widget5 = Frame(
            master,
            pady=10
            )
        self.widget5.pack()

        self.widget6 = Frame(
            master,
            pady=10
            )
        self.widget6.pack()

        self.widget6 = Frame(
            master,
            pady=10
            )
        self.widget6.pack()

        self.widget7 = Frame(
            master,
            pady=10
            )
        self.widget7.pack()

        self.widget8 = Frame(
            master,
            pady=10
            )
        self.widget8.pack()

        self.title = Label(
            self.widget1,
            text='ALGORITMOS DE PAGINAÇÃO',
            font = self.titleFont
            ).pack()

        self.labelPhrase = Label(
            self.widget3,
            text='*** Entre com os dados (separe-os por vírgulas) ***',
            font=(
                self.basicFont['family'],
                self.basicFont['size'],
                "bold"
                )
            ).pack()
        self.phrase = Entry(self.widget3)
        self.phrase.pack()        

        self.radioChoice = {
            'FIFO': '1',
            'ÓTIMO': '2',
            'LRU': '3',
            'LIFO': '4'
        }

        self.v1 = IntVar()
        self.v2 = IntVar()

        for (text, value) in self.radioChoice.items():
            Radiobutton(
                self.widget4,
                text=text,
                variable = self.v1,
                value=value, 
            ).pack(side=LEFT)

        self.submit = Button(
            self.widget6,
            text='Enviar',
            command=self.submit
        ).pack()        

    def submit(self):
        global lista        
        lista = list(self.phrase.get().split(','))

        if self.v1.get() == 1:
            referencias = lista
            quadros = int(lista[0])
            fifo = subst.FIFO(referencias,quadros)
        elif self.v1.get() == 2:
            referencias = lista
            quadros = int(lista[0])
            fifo = subst.OTIMO(referencias,quadros)
        elif self.v1.get() == 3:
            referencias = lista
            quadros = int(lista[0])
            fifo = subst.LRU(referencias,quadros)

        self.labelFalta = Label(
            self.widget8,
            font=(
            self.basicFont['family'],
            self.basicFont['size']
            ),
            text= f'Falhas = {fifo}'
        ).pack()

        #montando a tabela
        total_linhas = len(lista)
        total_colunas = len(lista[0])

        for i in range(total_linhas):
            for j in range(total_colunas):
                self.e = Entry(
                    self.widget7,
                    width=20,
                    font=(
                        self.basicFont['family'],
                        self.basicFont['size'],
                        "bold"
                    )
                )                
                self.e.grid(row=j, column=i)
                self.e.insert(END, lista[i][j])


root = Tk()
APP(root)
root.mainloop()