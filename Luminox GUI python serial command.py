import serial
import time
import tkinter as tk
from tkinter import ttk
#Diego Rojas de Ita 2024
# Configura el puerto serie y la velocidad de baudios
ser = serial.Serial('COM4', 9600, timeout=1)  # Reemplaza 'COM4' con el puerto que uses

def send_command(command):
    # Añadir terminador '\r\n' al comando
    #command += '\r\n'
    ser.write(command.encode())  # Enviar el comando
    print(f"Comando py: {command.strip()}")

    # Leer la respuesta del sensor
    response = ""
    while not response:
        if ser.in_waiting > 0:
            response = ser.read_all().decode().strip()
    print(f"Respuesta: {response}")
    display_response(response)  # Actualizar el cuadro de texto de respuestas

def display_response(response):
    response_text.config(state='normal')
    response_text.insert(tk.END, response + '\n')
    response_text.config(state='disabled')

def send_command_from_gui():
    command = command_text.get()
    command_text.delete(0, tk.END)  # Borrar el campo de texto después de enviar
    send_command(command)

def close_serial():
    ser.close()
    print("Serial port closed")
    window.destroy()  # Cerrar la ventana principal

# Crear la ventana principal
window = tk.Tk()
window.title("Serial Communication Tool")

# Crear el campo de texto para comandos
command_text = tk.Entry(window, width=30)
command_text.pack(pady=10)

# Crear el botón "Enviar"
send_button = tk.Button(window, text="Enviar", command=send_command_from_gui)
send_button.pack(pady=5)

# Crear el cuadro de texto para respuestas
response_text = tk.Text(window, height=10, width=30)
response_text.config(state='disabled')
response_text.pack(pady=10)

# Crear el botón "Terminar"
close_button = tk.Button(window, text="Terminar", command=close_serial)
close_button.pack(pady=5)

# Abrir el puerto serie y mostrar la ventana principal
try:
    if ser.isOpen():
        print(f"Conectado con {ser.port}")
        window.mainloop()
finally:
    ser.close()
    print("Serial port closed")
