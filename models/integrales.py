import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from typing import Callable
import os

# Diego Flores y Juan Pablo Mora

def f1(x: float, y: float) -> float:
    """Función z = x + y"""
    return x + y


def f2(x: float, y: float) -> float:
    """Función z = x^2 + y^2"""
    return x ** 2 + y ** 2


def f3(x: float, y: float) -> float:
    """Función z = sin(x) * cos(y)"""
    return np.sin(x) * np.cos(y)


def calcular_volumen_riemann(
        f: Callable[[float, float], float],
        x_min: float,
        x_max: float,
        y_min: float,
        y_max: float,
        nx: int,
        ny: int,
        metodo: str = 'midpoint'
) -> float:
    dx = (x_max - x_min) / nx
    dy = (y_max - y_min) / ny

    volumen = 0.0
    for i in range(nx):
        for j in range(ny):
            if metodo == 'left':
                x_i = x_min + i * dx
                y_j = y_min + j * dy
            elif metodo == 'right':
                x_i = x_min + (i + 1) * dx
                y_j = y_min + (j + 1) * dy
            else:  # midpoint
                x_i = x_min + (i + 0.5) * dx
                y_j = y_min + (j + 0.5) * dy
            volumen += f(x_i, y_j) * dx * dy

    return volumen


class IntegralesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Volumen - Sumas de Riemann")

        # Variables
        self.funcion_var = tk.StringVar(value='1')
        self.x_min_var = tk.StringVar(value='0')
        self.x_max_var = tk.StringVar(value='1')
        self.y_min_var = tk.StringVar(value='0')
        self.y_max_var = tk.StringVar(value='1')
        self.nx_var = tk.StringVar(value='10')
        self.ny_var = tk.StringVar(value='10')
        self.metodo_var = tk.StringVar(value='midpoint')

        # Marco principal
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Panel izquierdo para inputs
        left_frame = ttk.LabelFrame(main_frame, text="Parámetros", padding="5")
        left_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)

        # Función
        ttk.Label(left_frame, text="Función:").grid(row=0, column=0, sticky=tk.W)
        functions = [
            ("z = x + y", '1'),
            ("z = x² + y²", '2'),
            ("z = sin(x)cos(y)", '3')
        ]
        for i, (text, value) in enumerate(functions):
            ttk.Radiobutton(left_frame, text=text, value=value,
                            variable=self.funcion_var).grid(row=i + 1, column=0, sticky=tk.W)

        # Intervalos
        ttk.Label(left_frame, text="Intervalo x:").grid(row=4, column=0, sticky=tk.W)
        ttk.Entry(left_frame, textvariable=self.x_min_var, width=10).grid(row=4, column=1)
        ttk.Label(left_frame, text="a").grid(row=4, column=2)
        ttk.Entry(left_frame, textvariable=self.x_max_var, width=10).grid(row=4, column=3)

        ttk.Label(left_frame, text="Intervalo y:").grid(row=5, column=0, sticky=tk.W)
        ttk.Entry(left_frame, textvariable=self.y_min_var, width=10).grid(row=5, column=1)
        ttk.Label(left_frame, text="a").grid(row=5, column=2)
        ttk.Entry(left_frame, textvariable=self.y_max_var, width=10).grid(row=5, column=3)

        # Particiones
        ttk.Label(left_frame, text="Particiones:").grid(row=6, column=0, sticky=tk.W)
        ttk.Label(left_frame, text="nx:").grid(row=7, column=0, sticky=tk.W)
        ttk.Entry(left_frame, textvariable=self.nx_var, width=10).grid(row=7, column=1)
        ttk.Label(left_frame, text="ny:").grid(row=8, column=0, sticky=tk.W)
        ttk.Entry(left_frame, textvariable=self.ny_var, width=10).grid(row=8, column=1)

        # Método
        ttk.Label(left_frame, text="Método:").grid(row=9, column=0, sticky=tk.W)
        methods = [("Izquierda", "left"), ("Derecha", "right"), ("Punto medio", "midpoint")]
        for i, (text, value) in enumerate(methods):
            ttk.Radiobutton(left_frame, text=text, value=value,
                            variable=self.metodo_var).grid(row=10 + i, column=0, sticky=tk.W)

        # Botón calcular
        ttk.Button(left_frame, text="Calcular", command=self.calcular).grid(row=13, column=0,
                                                                            columnspan=4, pady=10)

        # Panel derecho para gráfica
        self.right_frame = ttk.LabelFrame(main_frame, text="Visualización", padding="5")
        self.right_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5)

        # Resultado
        self.resultado_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.resultado_var).grid(row=1, column=0,
                                                                    columnspan=2, pady=5)

    def get_funcion(self) -> Callable[[float, float], float]:
        funciones = {
            '1': lambda x, y: x + y,
            '2': lambda x, y: x ** 2 + y ** 2,
            '3': lambda x, y: np.sin(x) * np.cos(y)
        }
        return funciones[self.funcion_var.get()]

    def calcular(self):
        try:
            f = self.get_funcion()
            x_min = float(self.x_min_var.get())
            x_max = float(self.x_max_var.get())
            y_min = float(self.y_min_var.get())
            y_max = float(self.y_max_var.get())
            nx = int(self.nx_var.get())
            ny = int(self.ny_var.get())
            metodo = self.metodo_var.get()

            # Validaciones
            if x_max <= x_min or y_max <= y_min:
                raise ValueError("Los intervalos deben ser válidos (max > min)")
            if nx <= 0 or ny <= 0:
                raise ValueError("El número de particiones debe ser positivo")

            # Calcular volumen
            volumen = calcular_volumen_riemann(f, x_min, x_max, y_min, y_max, nx, ny, metodo)
            self.resultado_var.set(f"Volumen aproximado: {volumen:.6f}")

            # Actualizar gráfica
            self.actualizar_grafica(f, x_min, x_max, y_min, y_max, nx, ny, metodo)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def actualizar_grafica(self, f, x_min, x_max, y_min, y_max, nx, ny, metodo):
        # Clear right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Create new figure
        fig = plt.figure(figsize=(10, 5))

        # Surface plot
        ax1 = fig.add_subplot(121, projection='3d')
        x = np.linspace(x_min, x_max, 50)
        y = np.linspace(y_min, y_max, 50)
        X, Y = np.meshgrid(x, y)
        Z = f(X, Y)
        ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
        ax1.set_title('Superficie')

        # Partitions with volume labels
        ax2 = fig.add_subplot(122, projection='3d')
        dx = (x_max - x_min) / nx
        dy = (y_max - y_min) / ny

        for i in range(nx):
            for j in range(ny):
                if metodo == 'left':
                    x_i = x_min + i * dx
                    y_j = y_min + j * dy
                elif metodo == 'right':
                    x_i = x_min + (i + 1) * dx
                    y_j = y_min + (j + 1) * dy
                else:  # midpoint
                    x_i = x_min + (i + 0.5) * dx
                    y_j = y_min + (j + 0.5) * dy

                z = f(x_i, y_j)
                volume = z * dx * dy

                # Draw prism
                ax2.bar3d(x_i - dx / 2, y_j - dy / 2, 0, dx, dy, z, color='orange', alpha=0.5)

                # Add volume text slightly above the prism
                ax2.text(x_i, y_j, z + 0.1, f'{volume:.2f}',
                         horizontalalignment='center',
                         verticalalignment='bottom')

        ax2.set_title('Particiones con Volúmenes')

        # Show in GUI
        canvas = FigureCanvasTkAgg(fig, master=self.right_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        plt.close(fig)

    def draw_rectangles(self, fx, a, b, n, method='left'):
        # Existing setup code...
        delta_x = (b - a) / n

        for i in range(n):
            x = a + i * delta_x
            if method == 'left':
                height = fx(x)
            elif method == 'right':
                height = fx(x + delta_x)
            elif method == 'middle':
                height = fx(x + delta_x / 2)

            # Convert to canvas coordinates
            x1 = self.transform_x(x)
            y1 = self.transform_y(0)
            x2 = self.transform_x(x + delta_x)
            y2 = self.transform_y(height)

            # Draw rectangle
            self.canvas.create_rectangle(x1, y1, x2, y2, fill='lightblue')

            # Calculate and display area of this rectangle
            area = height * delta_x
            text_x = (x1 + x2) / 2  # Center of rectangle
            text_y = (y1 + y2) / 2  # Center of rectangle
            area_text = f"{area:.3f}"  # Format to 3 decimal places
            self.canvas.create_text(text_x, text_y, text=area_text, fill='black')


if __name__ == "__main__":
    root = tk.Tk()
    app = IntegralesGUI(root)
    root.mainloop()
