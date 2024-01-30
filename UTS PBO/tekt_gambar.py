import tkinter as tk
from tkinter import filedialog
from PIL import Image

class ImageToTextConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Image to Text Converter")

        self.create_widgets()

    def create_widgets(self):
        self.btn_select_image = tk.Button(self.master, text="Pilih Gambar", command=self.load_image)
        self.btn_select_image.pack(pady=10)

        self.btn_convert = tk.Button(self.master, text="Konversi", command=self.convert_image)
        self.btn_convert.pack(pady=10)

        self.txt_output = tk.Text(self.master, wrap=tk.WORD, width=50, height=20)
        self.txt_output.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image_path = file_path

    def convert_image(self):
        try:
            img = Image.open(self.image_path)
            img = img.convert('L')  # Konversi ke mode greyscale

            width, height = img.size
            aspect_ratio = height / width

            # Ubah ukuran gambar agar sesuai dengan lebar yang diinginkan
            new_width = 100
            new_height = int(new_width * aspect_ratio)
            img = img.resize((new_width, new_height))

            pixels = img.getdata()

            # Daftar karakter ASCII untuk penggantian nilai piksel
            ascii_characters = "@%#*+=-:. "

            # Hitung nilai keabuan normalisasi
            ascii_text = ''.join([ascii_characters[pixel // (256 // len(ascii_characters))] for pixel in pixels])

            # Reshape karakter ke dalam baris
            ascii_text = '\n'.join([ascii_text[i:i+new_width] for i in range(0, len(ascii_text), new_width)])

            self.txt_output.delete(1.0, tk.END)
            self.txt_output.insert(tk.END, ascii_text)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextConverter(root)
    root.mainloop()
