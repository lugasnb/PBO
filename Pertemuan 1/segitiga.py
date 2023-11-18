from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class LuasKelilingSegitiga:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Alas:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi 1:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi 2:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi 3:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=6, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling:").grid(row=7, column=0, sticky=W, padx=5, pady=5)

        self.txtAlas = Entry(mainFrame)
        self.txtAlas.grid(row=0, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame)
        self.txtTinggi.grid(row=1, column=1, padx=5, pady=5)
        self.txtSisi1 = Entry(mainFrame)
        self.txtSisi1.grid(row=2, column=1, padx=5, pady=5)
        self.txtSisi2 = Entry(mainFrame)
        self.txtSisi2.grid(row=3, column=1, padx=5, pady=5)
        self.txtSisi3 = Entry(mainFrame)
        self.txtSisi3.grid(row=4, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=6, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=7, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung Luas', command=self.onHitungLuas)
        self.btnHitung.grid(row=5, column=0, padx=5, pady=5)
        self.btnHitungKeliling = Button(mainFrame, text='Hitung Keliling', command=self.onHitungKeliling)
        self.btnHitungKeliling.grid(row=5, column=1, padx=5, pady=5)

    def onHitungLuas(self, event=None):
        alas = float(self.txtAlas.get())
        tinggi = float(self.txtTinggi.get())
        luas = 0.5 * alas * tinggi
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

    def onHitungKeliling(self, event=None):
        sisi1 = float(self.txtSisi1.get())
        sisi2 = float(self.txtSisi2.get())
        sisi3 = float(self.txtSisi3.get())
        keliling = sisi1 + sisi2 + sisi3
        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END, str(keliling))

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = LuasKelilingSegitiga(root, "Program Luas dan Keliling Segitiga")
    root.mainloop()
