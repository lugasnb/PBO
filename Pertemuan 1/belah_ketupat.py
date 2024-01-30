from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class LuasKelilingBelahKetupat:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Diagonal 1:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Diagonal 2:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling:").grid(row=5, column=0, sticky=W, padx=5, pady=5)

        self.txtDiagonal1 = Entry(mainFrame)
        self.txtDiagonal1.grid(row=0, column=1, padx=5, pady=5)
        self.txtDiagonal2 = Entry(mainFrame)
        self.txtDiagonal2.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=5, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung Luas', command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        self.btnHitungKeliling = Button(mainFrame, text='Hitung Keliling', command=self.onHitungKeliling)
        self.btnHitungKeliling.grid(row=3, column=1, padx=5, pady=5)

    def onHitung(self, event=None):
        diagonal1 = float(self.txtDiagonal1.get())
        diagonal2 = float(self.txtDiagonal2.get())
        luas = 0.5 * diagonal1 * diagonal2
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

    def onHitungKeliling(self, event=None):
        diagonal1 = float(self.txtDiagonal1.get())
        keliling = 4 * diagonal1
        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END, str(keliling))

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = LuasKelilingBelahKetupat(root, "Program Luas dan Keliling Belah Ketupat")
    root.mainloop()
