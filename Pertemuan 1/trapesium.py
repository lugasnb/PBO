from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class LuasKelilingTrapesium:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Sisi Atas:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi Bawah:").grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi Kanan:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Sisi Kiri:").grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=6, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Keliling:").grid(row=7, column=0, sticky=W, padx=5, pady=5)

        self.txtSisiAtas = Entry(mainFrame)
        self.txtSisiAtas.grid(row=0, column=1, padx=5, pady=5)
        self.txtSisiBawah = Entry(mainFrame)
        self.txtSisiBawah.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame)
        self.txtTinggi.grid(row=2, column=1, padx=5, pady=5)
        self.txtSisiKanan = Entry(mainFrame)
        self.txtSisiKanan.grid(row=3, column=1, padx=5, pady=5)
        self.txtSisiKiri = Entry(mainFrame)
        self.txtSisiKiri.grid(row=4, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=6, column=1, padx=5, pady=5)
        self.txtKeliling = Entry(mainFrame)
        self.txtKeliling.grid(row=7, column=1, padx=5, pady=5)

        self.btnHitung = Button(mainFrame, text='Hitung Luas', command=self.onHitungLuas)
        self.btnHitung.grid(row=5, column=0, padx=5, pady=5)
        self.btnHitungKeliling = Button(mainFrame, text='Hitung Keliling', command=self.onHitungKeliling)
        self.btnHitungKeliling.grid(row=5, column=1, padx=5, pady=5)

    def onHitungLuas(self, event=None):
        sisi_atas = float(self.txtSisiAtas.get())
        sisi_bawah = float(self.txtSisiBawah.get())
        tinggi = float(self.txtTinggi.get())
        luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

    def onHitungKeliling(self, event=None):
        sisi_atas = float(self.txtSisiAtas.get())
        sisi_bawah = float(self.txtSisiBawah.get())
        sisi_kanan = float(self.txtSisiKanan.get())
        sisi_kiri = float(self.txtSisiKiri.get())
        keliling = sisi_atas + sisi_bawah + sisi_kanan + sisi_kiri
        self.txtKeliling.delete(0, END)
        self.txtKeliling.insert(END, str(keliling))

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = LuasKelilingTrapesium(root, "Program Luas dan Keliling Trapesium")
    root.mainloop()
