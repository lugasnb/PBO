from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class LuasVolumeLimasSegiempat:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Luas dan Volume Limas Segiempat').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Panjang Alas:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Lebar Alas:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi Limas:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=6, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=7, column=0, sticky=W, padx=5, pady=5)

        self.txtPanjangAlas = Entry(mainFrame)
        self.txtPanjangAlas.grid(row=1, column=1, padx=5, pady=5)
        self.txtLebarAlas = Entry(mainFrame)
        self.txtLebarAlas.grid(row=2, column=1, padx=5, pady=5)
        self.txtTinggiLimas = Entry(mainFrame)
        self.txtTinggiLimas.grid(row=3, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=6, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=7, column=1, padx=5, pady=5)

        self.btnHitungLuas = Button(mainFrame, text='Hitung Luas', command=self.onHitungLuas)
        self.btnHitungLuas.grid(row=4, column=1, padx=5, pady=5)
        self.btnHitungVolume = Button(mainFrame, text='Hitung Volume', command=self.onHitungVolume)
        self.btnHitungVolume.grid(row=5, column=1, padx=5, pady=5)

    def onHitungLuas(self, event=None):
        panjang_alas = float(self.txtPanjangAlas.get())
        lebar_alas = float(self.txtLebarAlas.get())
        tinggi_limas = float(self.txtTinggiLimas.get())
        luas = (panjang_alas * lebar_alas) + 2 * ((panjang_alas * tinggi_limas) + (lebar_alas * tinggi_limas))
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

    def onHitungVolume(self, event=None):
        panjang_alas = float(self.txtPanjangAlas.get())
        lebar_alas = float(self.txtLebarAlas.get())
        tinggi_limas = float(self.txtTinggiLimas.get())
        volume = (1/3) * (panjang_alas * lebar_alas * tinggi_limas)
        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, str(volume))

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = LuasVolumeLimasSegiempat(root, "Program Luas dan Volume Limas Segiempat")
    root.mainloop()
