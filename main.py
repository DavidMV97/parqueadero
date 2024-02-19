import tkinter as tk
from tkinter import messagebox
from collections import namedtuple

Puesto = namedtuple('Puesto', 'nivel numero')

class Stack:
    def __init__(self):
        """
        Initializing Stack.
        """
        self.stack = []

    def isEmpty(self):
        return True if len(self.stack) == 0 else False

    def length(self):
        return len(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()


def crear_parqueadero(numero_niveles, cantidad_puestos):
    parqueadero = Stack()
    cont_niveles = 1
    while cont_niveles <= numero_niveles:
        cont_vehiculos = 1
        while cont_vehiculos <= cantidad_puestos:
            parqueadero.push(Puesto(cont_niveles, cont_vehiculos))
            cont_vehiculos += 1
        cont_niveles += 1
    return parqueadero


def obtener_puesto_libre(parqueadero):
    if parqueadero.isEmpty():
        return None
    return parqueadero.pop()


def ingresar_puesto_libre(parqueadero, puesto):
    parqueadero.push(puesto)



def mostrar_parqueadero(parqueadero, puestos_ocupados):
    window = tk.Tk()
    window.title("Parqueadero")

    text_widget = tk.Text(window, height=10, width=70)
    text_widget.pack()

    total = []
    total.append(parqueadero.stack)
    total.append(puestos_ocupados)

    current_nivel = None
    for row in total:
        for item in row:
            if isinstance(item, dict):
                key, value = list(item.items())[0]
                if key.nivel != current_nivel:
                    text_widget.insert(tk.END, "\n")  # Salto de línea si el nivel ha cambiado
                    current_nivel = key.nivel
                text_widget.insert(tk.END, f"Nivel {key.nivel} {value} ", "nivel")
            elif isinstance(item, Puesto):
                if item.nivel != current_nivel:
                    text_widget.insert(tk.END, "\n")  # Salto de línea si el nivel ha cambiado
                    current_nivel = item.nivel
                text_widget.insert(tk.END, f"Nivel {item.nivel} Puesto {item.numero} ", "puesto")

    # Configuración de colores
    text_widget.tag_config("nivel", foreground="blue")  # Color para los niveles
    text_widget.tag_config("puesto", foreground="black")  # Color para los puestos
    window.mainloop()


def menu():
    print("\nSeleccione una opción:")
    print("1. Ingresar vehículo al parqueadero")
    print("2. Mostrar parqueadero")
    print("3. Eliminar vehículo del parqueadero")
    print("4. Salir")



parqueadero = crear_parqueadero(2, 4)
puestos_ocupados = []

while True:
    menu()
    opcion = input("Opción: ")

    if opcion == "1":
        puesto_libre = obtener_puesto_libre(parqueadero)
        if puesto_libre:
            my_placa = input('Ingrese la placa del vehiculo: ')
            placa_ya_ingresada = False
            for puestos in puestos_ocupados:
                if my_placa in puestos.values():
                    placa_ya_ingresada = True
                    break
        
            if placa_ya_ingresada:
                messagebox.showwarning("Placa ya ingresada", f"La placa {my_placa} ya ha sido ingresada anteriormente.")
            else:
                messagebox.showinfo("Asignación de Puesto", f"Se ha asignado el puesto {puesto_libre} al vehículo.")
                puestos_ocupados.insert(0,{puesto_libre: my_placa})
            
        else:
            messagebox.showwarning("Parqueadero lleno", "El parqueadero está lleno, no hay puestos disponibles.")

    elif opcion == "2":
        mostrar_parqueadero(parqueadero, puestos_ocupados)
    elif opcion == "3":
        placa_eliminar = input("Ingrese la placa del vehículo a eliminar: ")
        for puesto in puestos_ocupados:
            if placa_eliminar in puesto.values():
                nivel, numero = list(puesto.keys())[0]
                puestos_ocupados.remove(puesto)
                puesto_libre = Puesto(nivel, numero)
                ingresar_puesto_libre(parqueadero, puesto_libre)
                messagebox.showinfo("Eliminación placa vehiculo", f"Vehículo con placa {placa_eliminar} eliminado del parqueadero")
                break
        else:
            messagebox.showwarning("Placa no encontrada", f"No se encontró ningún vehículo con placa {placa_eliminar} en el parqueadero.")

    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        messagebox.showerror("Opción  inválida", "Opción  inválida. Por favor seleccione una opción válida.")

