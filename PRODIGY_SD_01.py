import tkinter as tk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    original_unit = original_unit_var.get().lower()
    temperature = float(temperature_entry.get())
    
    if original_unit == "celsius":
        fahrenheit = celsius_to_fahrenheit(temperature)
        kelvin = celsius_to_kelvin(temperature)
        result_label.config(text=f"{temperature} {original_unit} is equivalent to:\n"
                             f"{fahrenheit:.2f} Fahrenheit\n"
                             f"{temperature:.2f} Celsius\n"  # Use the same temperature value here
                             f"{kelvin:.2f} Kelvin")
    elif original_unit == "fahrenheit":
        celsius = fahrenheit_to_celsius(temperature)
        kelvin = fahrenheit_to_kelvin(temperature)
        result_label.config(text=f"{temperature} {original_unit} is equivalent to:\n"
                             f"{temperature:.2f} Fahrenheit\n"  # Use the same temperature value here
                             f"{celsius:.2f} Celsius\n"
                             f"{kelvin:.2f} Kelvin")
    elif original_unit == "kelvin":
        celsius = kelvin_to_celsius(temperature)
        fahrenheit = kelvin_to_fahrenheit(temperature)
        result_label.config(text=f"{temperature} {original_unit} is equivalent to:\n"
                             f"{fahrenheit:.2f} Fahrenheit\n"
                             f"{celsius:.2f} Celsius\n"
                             f"{temperature:.2f} Kelvin")  # Use the same temperature value here

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create and pack labels and entry widgets
original_unit_label = tk.Label(root, text="Enter the original temperature unit:")
original_unit_label.pack()

original_unit_var = tk.StringVar()
original_unit_entry = tk.Entry(root, textvariable=original_unit_var)
original_unit_entry.pack()

temperature_label = tk.Label(root, text="Enter the temperature value:")
temperature_label.pack()

temperature_entry = tk.Entry(root)
temperature_entry.pack()

# Create and pack the conversion button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

# Create and pack the result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter main loop
root.mainloop()
