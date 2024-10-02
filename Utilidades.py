import matplotlib.pyplot as plt
from Proceso import Proceso
import random

# Función para ingresar manualmente los procesos
def ingresar_procesos():
    num_procesos = int(input("Ingrese el número de procesos: "))
    procesos = []
    
    for i in range(num_procesos):
        print(f"\nProceso {i+1}:")
        tiempo_llegada = int(input(f"  Ingrese el tiempo de llegada del proceso {i+1}: "))
        
        # Asignar tiempo de ejecución aleatorio entre 1 y 10
        rafaga_cpu = random.randint(1, 10)
        memoria = random.randint(100, 500)
        
        print(f"  Tiempo de ejecución (aleatorio): {rafaga_cpu}")
        print(f"  Memoria consumida (aleatorio): {memoria} MB")
        
        procesos.append(Proceso(id_proceso=i+1, tiempo_llegada=tiempo_llegada, rafaga_cpu=rafaga_cpu, memoria=memoria))
    
    return procesos

# Función para mostrar el gráfico
def mostrar_grafico(procesos):
    ids_procesos = [p.id_proceso for p in procesos]
    memorias = [p.memoria for p in procesos]
    
    plt.plot(ids_procesos, memorias, marker='o', color='green', label="Consumo de Memoria")
    plt.xlabel('ID del Proceso')
    plt.ylabel('Memoria Consumida (MB)')
    plt.title('Gráfico de Memoria Consumida por Procesos')
    plt.legend()
    plt.grid(True)
    plt.show(block=False)
