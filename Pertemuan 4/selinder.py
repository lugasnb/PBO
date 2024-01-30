from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W
import math

class LuasVolumeSilinder:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        Label(mainFrame, text='Luas dan Volume Selinder (Tabung)').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Jari-jari:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=2, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=5, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=6, column=0, sticky=W, padx=5, pady=5)

        self.txtJariJari = Entry(mainFrame)
        self.txtJariJari.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggi = Entry(mainFrame)
        self.txtTinggi.grid(row=2, column=1, padx=5, pady=5)
        self.txtLuas = Entry(mainFrame)
        self.txtLuas.grid(row=5, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame)
        self.txtVolume.grid(row=6, column=1, padx=5, pady=5)

        self.btnHitungLuas = Button(mainFrame, text='Hitung Luas', command=self.onHitungLuas)
        self.btnHitungLuas.grid(row=3, column=1, padx=5, pady=5)
        self.btnHitungVolume = Button(mainFrame, text='Hitung Volume', command=self.onHitungVolume)
        self.btnHitungVolume.grid(row=4, column=1, padx=5, pady=5)

    def onHitungLuas(self, event=None):
        jari_jari = float(self.txtJariJari.get())
        tinggi = float(self.txtTinggi.get())
        luas = 2 * math.pi * jari_jari * (jari_jari + tinggi)
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, str(luas))

    def onHitungVolume(self, event=None):
        jari_jari = float(self.txtJariJari.get())
        tinggi = float(self.txtTinggi.get())
        volume = math.pi * jari_jari**2 * tinggi
        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, str(volume))

    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    aplikasi = LuasVolumeSilinder(root, "Program Luas dan Volume Silinder (Tabung)")
    root.mainloop()
