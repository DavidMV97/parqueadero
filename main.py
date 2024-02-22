
import tkinter as tk
from tkinter import messagebox
from collections import namedtuple

Puesto = namedtuple('Puesto', 'nivel numero')
Placa = namedtuple('Placa', 'nivel numero placa')

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



# def crear_parqueadero(numero_niveles, cantidad_puestos):
#     parqueadero = Stack()
#     cont_niveles = 1
#     while cont_niveles <= numero_niveles:
#         cont_vehiculos = cantidad_puestos
#         while cont_vehiculos >= 1:
#             parqueadero.push(Puesto(cont_niveles, cont_vehiculos))
#             cont_vehiculos -= 1
#         cont_niveles += 1
#     return parqueadero

def crear_parqueadero(numero_niveles, cantidad_puestos):
    parqueadero = Stack()
    for nivel in range(1, numero_niveles + 1):
        for numero in range(1, cantidad_puestos + 1):
            parqueadero.push(Puesto(nivel, numero))
    return parqueadero


def obtener_puesto_libre(parqueadero):
    if parqueadero.isEmpty():
        return None
    
    for i in range(len(parqueadero.stack) - 1, -1, -1):
        if not isinstance(parqueadero.stack[i], Placa):
            elemento_eliminado = parqueadero.stack.pop(i)
            return elemento_eliminado
            
   

    

def ingresar_puesto_libre(parqueadero, puesto, libre):
    parqueadero.stack.insert(libre, puesto)



def mostrar_parqueadero(parqueadero, puestos_ocupados):
    # window = tk.Tk()
    # window.title("Parqueadero")

    # text_widget = tk.Text(window, height=10, width=70)
    # text_widget.pack()

    current_nivel = None
    for item in parqueadero.stack:
        print(item)
        # if isinstance(item, Puesto):
        #     if item.nivel != current_nivel:
        #         text_widget.insert(tk.END, "\n")
        #         current_nivel = item.nivel
        #     text_widget.insert(tk.END, f"Nivel {item.nivel} Puesto {item.numero} ", "puesto")
        # elif isinstance(item, Placa):
        #     text_widget.insert(tk.END, f"Placa {item.placa} en Nivel {item.nivel} Puesto {item.numero}\n", "placa")

    # Configuración de colores
    # text_widget.tag_config("puesto", foreground="black")  # Color para los puestos
    # text_widget.tag_config("placa", foreground="green")  # Color para las placas
    # window.mainloop()



def menu():
    print("\nSeleccione una opción:")
    print("1. Ingresar vehículo al parqueadero")
    print("2. Mostrar parqueadero")
    print("3. Eliminar vehículo del parqueadero")
    print("4. Salir")



parqueadero = crear_parqueadero(2, 4)
puestos_ocupados = []
current_index = 0 


while True:
    menu()
    opcion = input("Opción: ")

    if opcion == "1":
        puesto_libre = obtener_puesto_libre(parqueadero)
        
        if puesto_libre:
            my_placa = input('Ingrese la placa del vehiculo: ')
            placa_ya_ingresada = False
            for puestos in parqueadero.stack:
                if my_placa in puestos:
                    placa_ya_ingresada = True
                    break
                
                
            if placa_ya_ingresada:
                messagebox.showwarning("Placa ya ingresada", f"La placa {my_placa} ya ha sido ingresada anteriormente.")
            else:
                messagebox.showinfo("Asignación de Puesto", f"Se ha asignado el puesto {puesto_libre} al vehículo.")
                puestos_ocupados.insert(0,{puesto_libre: my_placa})
                placa= Placa(puesto_libre.nivel, puesto_libre.numero, my_placa)
                print(f'Longitud => {len(parqueadero.stack)}')
                for puesto in reversed(parqueadero.stack):
                    
                    current_index-= 1
                    #print(f'index => {current_index}')
                    print(f'Puesto => {puesto} Index => {current_index}')
                    if isinstance(puesto, Puesto):
                        parqueadero.push(placa)
                        current_index = 0
                        print('ENTRA EN IF ****')
                        break
                    else:
                        parqueadero.stack.insert(current_index, placa)
                        print('ENTRA EN ELSE ******')
                        break
                
                
        else:
            messagebox.showwarning("Parqueadero lleno", "El parqueadero está lleno, no hay puestos disponibles.")

    elif opcion == "2":
        mostrar_parqueadero(parqueadero, puestos_ocupados)
    elif opcion == "3":
        placa_eliminar = input("Ingrese la placa del vehículo a eliminar: ")
        index = 0
        for puesto in parqueadero.stack:
            index+=1
            if placa_eliminar in puesto:
                puesto_libre = Puesto(puesto.nivel, puesto.numero)
                current_index= - (len(parqueadero.stack) - (index + 1))
                ingresar_puesto_libre(parqueadero, puesto_libre, index)
                parqueadero.stack.remove(puesto)
                
                messagebox.showinfo("Eliminación placa vehiculo", f"Vehículo con placa {placa_eliminar} eliminado del parqueadero")
                break
        else:
            messagebox.showwarning("Placa no encontrada", f"No se encontró ningún vehículo con placa {placa_eliminar} en el parqueadero.")

    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        messagebox.showerror("Opción  inválida", "Opción  inválida. Por favor seleccione una opción válida.")

