from tkinter import *
from googletrans import Translator

class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title('Translator')
        Label(self, text="Pilih target bahasa").grid(row=0, column=0, padx=50, pady=20)
        self.options = ['Inggris', 'Korea', 'Jepang']
        self.variable = StringVar(self)
        self.variable.set(self.options[0]) 
        self.combobox =  OptionMenu(self, self.variable, *self.options, command=lambda value: self.on_selected(value))
        self.combobox.grid(row=0, column=1, padx=50, pady=20)
        Label(self, text="Masukan kata/kalimat").grid(row=1, column=0, padx=50, pady=20)
        self.txtSrc = Entry(self)
        self.txtSrc.grid(row=1, column=1)

        self.language = ''

        self.btn = Button(self, text='Terjemahkan', command=self.btn_clicked)
        self.btn.grid(row=2, column=0,padx=50, pady=20)
        
        self.result = Entry(self)
        self.result.grid(row=2, column=1,padx=50, pady=20)

    def on_selected(self, value):
        self.language = value
        

    def btn_clicked(self):
        penerjemah = Translator()
        if self.language == 'Jepang':
            hasil = penerjemah.translate(self.txtSrc.get(), src='id', dest='ja') 
            self.result.delete(0, END)
            self.result.insert(0, hasil.text)
        elif self.language == 'Korea':
            hasil = penerjemah.translate(self.txtSrc.get(), src='id', dest='ko') 
            self.result.delete(0, END)
            self.result.insert(0, hasil.text)
        else: 
            hasil = penerjemah.translate(self.txtSrc.get(), src='id', dest='en') 
            self.result.delete(0, END)
            self.result.insert(0, hasil.text)
        
class MainFrame(Frame):
    def __init__(self,master):
        super().__init__(master)
        
app = Root()
app.geometry("500x250")
app.config(pady=10)
app.mainloop()