import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        content = file.read()
        entry.delete("1.0", tk.END)
        entry.insert("1.0", content)
        result_label.config(text="File telah dibuka!", foreground='white')

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    with open(file_path, 'w') as file:
        content = entry.get("1.0", tk.END)
        file.write(content)
        result_label.config(text="File telah disimpan!", foreground='white')

window = tk.Tk()
window.title("Aplikasi Jadwal Pelajaran")
window['bg'] = 'gray'

entry = tk.Text(window, width=40, height=15)
entry.grid(row=0, column=0, padx=20, pady=20)

frame = tk.Frame(window)
frame.grid(row=0, column=1, padx=10, pady=10)
frame['bg'] = 'gray'

browse_button = tk.Button(frame, text="Buka File", command=browse_file)
browse_button.grid(row=1, column=0, padx=10, pady=10)

save_button = tk.Button(frame, text="Simpan File", command=save_file)
save_button.grid(row=2, column=0, padx=10, pady=10)

result_label = tk.Label(frame, text="")
result_label.grid(row=3, column=0, pady=10)
result_label['bg'] = 'gray'

window.mainloop()
