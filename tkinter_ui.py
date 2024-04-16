import tkinter as tk
from tkinter import messagebox
from main import execute_parser, execute_python
import interpreter

def procesar():
    interpreter.variables = []
    interpreter.value_variable = []
    interpreter.func = []
    interpreter.for_out = []
    interpreter.out_pps = ""
    entrada = text_area_entrada.get('1.0', tk.END).strip()  # Obtener y limpiar la entrada
    if not entrada:
        messagebox.showerror("Error", "La entrada no puede estar vacía.")
        return

    # Mostrar el resultado del análisis léxico/sintáctico
    text_area_lexico.delete('1.0', tk.END)
    resultado_parser = execute_parser(entrada)
    text_area_lexico.insert(tk.END, resultado_parser)

    try:
        text_area_python.delete('1.0', tk.END)
        codigo_python = execute_python(entrada)
        text_area_python.insert(tk.END, codigo_python)

        messagebox.showinfo("Éxito", "Declaraciones analizadas y ejecutadas")
    except Exception as e:
        messagebox.showerror("Error de ejecución", str(e))

# Configuración de la GUI (esto permanece igual)
root = tk.Tk()
root.title("Nova Analyzer")

# Colores
color_fondo = "#D8BFD8"  
color_botones = "#9370DB" 
color_texto = "#FFF8DC"  

root.config(bg=color_fondo)

# Frame para el área de entrada
frame_entrada = tk.Frame(root, bg=color_fondo)
frame_entrada.pack(padx=10, pady=10, fill=tk.X)

label_entrada = tk.Label(frame_entrada, text="NOVA LENGUAJE", font=("Helvetica", 12, "bold"), bg=color_fondo, fg=color_botones)
label_entrada.pack(side=tk.LEFT, padx=10, pady=5)

text_area_entrada = tk.Text(frame_entrada, height=5, width=100)
text_area_entrada.pack(side=tk.LEFT, padx=10, pady=5)

# Botón de procesamiento
boton_procesar = tk.Button(root, text="ANALIZAR", command=procesar, bg=color_botones, fg=color_texto, font=("Helvetica", 12, "bold"))
boton_procesar.pack(padx=10, pady=5, fill=tk.X)

# Frame para los resultados
frame_resultados = tk.Frame(root, bg=color_fondo)
frame_resultados.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Resultado del análisis léxico/sintáctico
frame_salida_lexico = tk.Frame(frame_resultados, bg=color_fondo)
frame_salida_lexico.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

label_lexico = tk.Label(frame_salida_lexico, text="Analizador lexico y sintactico", font=("Helvetica", 12, "bold"), bg=color_fondo, fg=color_botones)
label_lexico.pack(side=tk.TOP, padx=10, pady=(0, 5))

text_area_lexico = tk.Text(frame_salida_lexico, height=10, width=50)
text_area_lexico.pack(side=tk.TOP, padx=10, pady=(0, 10))

# Resultado del análisis en Python
frame_salida_python = tk.Frame(frame_resultados, bg=color_fondo)
frame_salida_python.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

label_python = tk.Label(frame_salida_python, text="Salida ejecutada", font=("Helvetica", 12, "bold"), bg=color_fondo, fg=color_botones)
label_python.pack(side=tk.TOP, padx=10, pady=(0, 5))

text_area_python = tk.Text(frame_salida_python, height=10, width=50)
text_area_python.pack(side=tk.TOP, padx=10, pady=(0, 10))

root.mainloop()