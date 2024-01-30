from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class LuasKelilingPersegiPanjang:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Panjang:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Lebar:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling:").grid(row=5, column=0, sticky=W, padx=5, pady=5)

        self.txtPanjang = Entry(mainFrame)
        self.txtPanjang.grid(row=0, column=1, padx=5, pady=5)
        self.txtLebar = Entry(mainFrame)
        self.txtLebar.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=4, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=5, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung Luas', command=self.onHitung)
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        self.btnHitungKeliling = Button(mainFrame, text='Hitung Keliling', command=self.onHitungKeliling)
        self.btnHitungKeliling.grid(row=3, column=1, padx=5, pady=5)

    def onHitung(self, event=None):
        panjang = float(self.txtPanjang.get())
        lebar = float(self.txtLebar.get())
        luas = panjang * lebar
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

    def onHitungKeliling(self, event=None):
        panjang = float(self.txtPanjang.get())
        lebar = float(self.txtLebar.get())
        keliling = 2 * (panjang + lebar)
        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END, str(keliling))

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = LuasKelilingPersegiPanjang(root, "Program Luas dan Keliling Persegi Panjang")
    root.mainloop()
