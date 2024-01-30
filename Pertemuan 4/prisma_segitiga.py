from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class LuasVolumePrismaSegitiga:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Luas dan Volume Prisma Segitiga').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Alas Segitiga:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi Segitiga:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi Prisma:").grid(row=3, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=6, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=7, column=0, sticky=W, padx=5, pady=5)

        self.txtAlasSegitiga = Entry(mainFrame)
        self.txtAlasSegitiga.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggiSegitiga = Entry(mainFrame)
        self.txtTinggiSegitiga.grid(row=2, column=1, padx=5, pady=5)
        self.txtTinggiPrisma = Entry(mainFrame)
        self.txtTinggiPrisma.grid(row=3, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=6, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=7, column=1, padx=5, pady=5)

        self.btnHitungLuas = Button(mainFrame, text='Hitung Luas', command=self.onHitungLuas)
        self.btnHitungLuas.grid(row=4, column=1, padx=5, pady=5)
        self.btnHitungVolume = Button(mainFrame, text='Hitung Volume', command=self.onHitungVolume)
        self.btnHitungVolume.grid(row=5, column=1, padx=5, pady=5)

    def onHitungLuas(self, event=None):
        alas_segitiga = float(self.txtAlasSegitiga.get())
        tinggi_segitiga = float(self.txtTinggiSegitiga.get())
        luas = (1/2) * alas_segitiga * tinggi_segitiga
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

    def onHitungVolume(self, event=None):
        alas_segitiga = float(self.txtAlasSegitiga.get())
        tinggi_segitiga = float(self.txtTinggiSegitiga.get())
        tinggi_prisma = float(self.txtTinggiPrisma.get())
        volume = alas_segitiga * tinggi_segitiga * tinggi_prisma
        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, str(volume))

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = LuasVolumePrismaSegitiga(root, "Program Luas dan Volume Prisma Segitiga")
    root.mainloop()
