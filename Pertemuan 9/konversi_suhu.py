import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        # Konversi suhu
        if from_unit == 'Celsius':
            if to_unit == 'Fahrenheit':
                result = (temperature * 9/5) + 32
            elif to_unit == 'Reamur':
                result = temperature * 4/5
            elif to_unit == 'Kelvin':
                result = temperature + 273.15
            else:
                result = temperature  # Same unit
        elif from_unit == 'Fahrenheit':
            if to_unit == 'Celsius':
                result = (temperature - 32) * 5/9
            elif to_unit == 'Reamur':
                result = (temperature - 32) * 4/9
            elif to_unit == 'Kelvin':
                result = (temperature - 32) * 5/9 + 273.15
            else:
                result = temperature  # Same unit
        elif from_unit == 'Reamur':
            if to_unit == 'Celsius':
                result = temperature * 5/4
            elif to_unit == 'Fahrenheit':
                result = temperature * 9/4 + 32
            elif to_unit == 'Kelvin':
                result = temperature * 5/4 + 273.15
            else:
                result = temperature  # Same unit
        elif from_unit == 'Kelvin':
            if to_unit == 'Celsius':
                result = temperature - 273.15
            elif to_unit == 'Fahrenheit':
                result = (temperature - 273.15) * 9/5 + 32
            elif to_unit == 'Reamur':
                result = (temperature - 273.15) * 4/5
            else:
                result = temperature  # Same unit
        else:
            result = temperature  # Same unit

        label_result.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter a valid number.")

# Membuat GUI
app = tk.Tk()
app.title("Temperature Converter")
app.geometry("550x250")
app.resizable(width=True, height=True)

# Label dan Entry untuk suhu
label_temperature = ttk.Label(app, text="Temperature:")
label_temperature.grid(row=0, column=1, padx=10, pady=20)

entry_temperature = ttk.Entry(app)
entry_temperature.grid(row=0, column=2, padx=10, pady=20)

# Combobox untuk unit suhu
units = ['Celsius', 'Fahrenheit', 'Reamur', 'Kelvin']

label_from = ttk.Label(app, text="From:")
label_from.grid(row=1, column=0, padx=10, pady=20)
combo_from = ttk.Combobox(app, values=units)
combo_from.grid(row=1, column=1, padx=10, pady=20)
combo_from.set('Celsius')

label_to = ttk.Label(app, text="To:")
label_to.grid(row=1, column=2, padx=10, pady=20)
combo_to = ttk.Combobox(app, values=units)
combo_to.grid(row=1, column=3, padx=10, pady=20)
combo_to.set('Celsius')

# Tombol konversi
button_convert = ttk.Button(app, text="Convert", command=convert_temperature)
button_convert.grid(row=3, column=1, columnspan=2, padx=10, pady=20)

# Hasil konversi
label_result = ttk.Label(app, text="Result:")
label_result.grid(row=3, column=2, columnspan=2, padx=10, pady=20)

# Menjalankan aplikasi
app.mainloop()

