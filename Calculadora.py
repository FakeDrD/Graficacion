import tkinter as tk

def calcular(operacion):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '/':
            resultado = num1 / num2 if num2 != 0 else 'Error: División por cero'
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        label_resultado.config(text="Error: Ingresa números válidos")

root = tk.Tk()
root.title("Calculadora Simple")

tk.Label(root, text="Número 1:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Número 2:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="+", width=5, command=lambda: calcular('+')).grid(row=2, column=0)
tk.Button(root, text="-", width=5, command=lambda: calcular('-')).grid(row=2, column=1)
tk.Button(root, text="*", width=5, command=lambda: calcular('*')).grid(row=3, column=0)
tk.Button(root, text="/", width=5, command=lambda: calcular('/')).grid(row=3, column=1)

label_resultado = tk.Label(root, text="Resultado: ")
label_resultado.grid(row=4, column=0, columnspan=2)

root.mainloop()