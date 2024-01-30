import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from obat import obat

class Formobat:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kode:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtkdobat = Entry(mainFrame) 
        self.txtkdobat.grid(row=0, column=1, padx=5, pady=5) 
        self.txtkdobat.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='Nama:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = StringVar()
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Berat:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtberat = StringVar()
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=2, column=1, padx=5, pady=5)

        Label(mainFrame, text='Bentuk:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtbentuk = StringVar()
        Cbo = ttk.Combobox(mainFrame, width = 27, textvariable = self.txtbentuk) 
        Cbo.grid(row=4, column=1, padx=5, pady=5)
        Cbo['values'] = ('Tablet','Kapsul','Pil','Serbuk','Supositoria','Ovula','Sirup',
                         'Suspensi','Emulsi','Eliksir','Larutan','Injeksi','Obat tetes','Inhalasi','Aerosol','Tubhaler')
        Cbo.current()      
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('idobt', 'kdobat', 'nama','berat','bentuk')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('idobt', text='ID')
        self.tree.column('idobt', width="30")
        self.tree.heading('kdobat', text='Kode')
        self.tree.column('kdobat', width="60")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="200")
        self.tree.heading('berat', text='Berat')
        self.tree.column('berat', width="30")
        self.tree.heading('bentuk', text='Bentuk')
        self.tree.column('bentuk', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtkdobat.delete(0,END)
        self.txtkdobat.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")       
        self.txtbentuk.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data obat
        obt = obat()
        result = obt.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        students=[]
        for row_data in result:
            students.append(row_data)

        for student in students:
            self.tree.insert('',END, values=student)
    
    def onCari(self, event=None):
        kdobat = self.txtkdobat.get()
        obt = obat()
        res = obt.getBykdobat(kdobat)
        rec = obt.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNama.focus()
        return res
        
    def TampilkanData(self, event=None):
        kdobat = self.txtkdobat.get()
        obt = obat()
        res = obt.getBykdobat(kdobat)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obt.nama)
        berat = obt.berat
        self.txtbentuk.set(obt.bentuk)   
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        kdobat = self.txtkdobat.get()
        nama = self.txtNama.get()
        berat = self.txtberat.get()
        bentuk = self.txtbentuk.get()
        
        obt = obat()
        obt.kdobat = kdobat
        obt.nama = nama
        obt.berat = berat
        obt.bentuk = bentuk
        if(self.ditemukan==True):
            res = obt.updateBykdobat(kdobat)
            ket = 'Diperbarui'
        else:
            res = obt.simpan()
            ket = 'Disimpan'
            
        rec = obt.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        kdobat = self.txtkdobat.get()
        obt = obat()
        obt.kdobat = kdobat
        if(self.ditemukan==True):
            res = obt.deleteBykdobat(kdobat)
            rec = obt.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = Formobat(root, "Aplikasi Data obat")
    root.mainloop() 