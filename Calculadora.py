import tkinter as tk

def sumar():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        resultado = num1 + num2
        label_result.config(text=f"La suma es: {resultado}")
    except ValueError:
        label_result.config(text="Por favor ingresa números válidos.")

root = tk.Tk()
root.title("Calculadora de Suma")

label1 = tk.Label(root, text="Ingresar el Primer Número:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Ingresar el Segundo Número:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

btn_sumar = tk.Button(root, text="Sumar", command=sumar)
btn_sumar.pack()

label_result = tk.Label(root, text="La suma es:")
label_result.pack()

root.mainloop()