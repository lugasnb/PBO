import tkinter as tk 

class LuasKelilingPersegiPanjang:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = tk.Frame(self.parent, bd=10)
        mainFrame.pack(fill=tk.BOTH, expand=tk.YES)

        tk.Label(mainFrame, text='Luas dan Volume Kubus').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        tk.Label(mainFrame, text='Rusuk:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        tk.Label(mainFrame, text="Luas:").grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        tk.Label(mainFrame, text="Volume:").grid(row=6, column=0, sticky=tk.W, padx=5, pady=5)

        self.txtRusuk = tk.Entry(mainFrame)
        self.txtRusuk.grid(row=1, column=1, padx=5, pady=5)
        self.txtLuas = tk.Entry(mainFrame)
        self.txtLuas.grid(row=5, column=1, padx=5, pady=5)
        self.txtVolume = tk.Entry(mainFrame)
        self.txtVolume.grid(row=6, column=1, padx=5, pady=5)

        self.btnHitung = tk.Button(mainFrame, text='Hitung Luas', command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)
        self.btnHitungVolume = tk.Button(mainFrame, text='Hitung Volume', command=self.onHitungKeliling)
        self.btnHitungVolume.grid(row=4, column=1, padx=5, pady=5)

    def onHitung(self, event=None):
        rusuk = float(self.txtRusuk.get())
        luas = 6 * rusuk * rusuk
        self.txtLuas.delete(0, tk.END)
        self.txtLuas.insert(tk.END, str(luas))

    def onHitungKeliling(self, event=None):
        rusuk = float(self.txtRusuk.get())
        keliling = rusuk * rusuk * rusuk
        self.txtVolume.delete(0, tk.END)
        self.txtVolume.insert(tk.END, str(keliling))

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = LuasKelilingPersegiPanjang(root, "Program Luas dan Volume Kubus")
    root.mainloop()
