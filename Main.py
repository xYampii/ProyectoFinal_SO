import matplotlib.pyplot as plt
import random
from Planificador import Planificador, fifo, sjf, round_robin  # Importar la clase Planificador y los algoritmos FIFO, SJF y Round Robin
from Proceso import Proceso

# Función que crea y muestra el gráfico
def mostrar_grafico(datos_procesos):
    tiempos_llegada = [proceso.tiempo_llegada for proceso in datos_procesos]
    memorias = [proceso.memoria for proceso in datos_procesos]
    ids_procesos = [proceso.id_proceso for proceso in datos_procesos]
    
    plt.plot(ids_procesos, memorias, marker='o', color='green', label="Consumo de Memoria")
    plt.xlabel('ID del Proceso')
    plt.ylabel('Memoria Consumida (MB)')
    plt.title('Gráfico de Memoria Consumida por Procesos')
    plt.legend()
    plt.grid(True)
    
    # Muestra el gráfico sin bloquear la ejecución
    plt.show(block=False)

# Función para mostrar la cola de procesos y sus estados
def mostrar_cola_procesos(procesos):
    print("\nCola de procesos:")
    for proceso in procesos:
        estado = proceso.estado
        tiempo_completado = proceso.tiempo_completado if proceso.tiempo_completado is not None else "N/A"
        print(f"Proceso {proceso.id_proceso}: Estado = {estado}, Tiempo completado = {tiempo_completado}")

# Menú principal que se repite después de cerrar el gráfico
def menu_principal():
    while True:
        print("\n--- Menú de Algoritmos de Planificación ---")
        print("1. FIFO (First In First Out)")
        print("2. SJF (Shortest Job First)")
        print("3. Round Robin")
        print("4. Salir")
        opcion = input("Seleccione un algoritmo (1-4): ")

        if opcion == '1':
            print("\n--- Simulación FIFO ---")
            num_procesos = int(input("Ingrese el número de procesos: "))
            procesos = []
            for i in range(num_procesos):
                tiempo_llegada = int(input(f"Ingrese el tiempo de llegada del proceso {i+1}: "))
                
                # Asignar tiempo de ejecución y memoria de manera aleatoria
                rafaga_cpu = random.randint(1, 10)  # Tiempo de ejecución aleatorio entre 1 y 10 unidades de tiempo
                memoria = random.randint(100, 500)  # Memoria aleatoria entre 100 MB y 500 MB
                
                print(f"  Tiempo de ejecución (aleatorio): {rafaga_cpu}")
                print(f"  Memoria consumida (aleatorio): {memoria} MB")
                
                procesos.append(Proceso(id_proceso=i+1, tiempo_llegada=tiempo_llegada, rafaga_cpu=rafaga_cpu, memoria=memoria))

            # Llamar a la función que genera el gráfico
            mostrar_grafico(procesos)

            # Llamar a la simulación
            planificador = Planificador(fifo)
            for proceso in procesos:
                planificador.agregar_proceso(proceso)
            
            # Iniciar la simulación y mostrar el estado de la cola de procesos después de cada ejecución
            planificador.simular()

            # Mostrar la cola de procesos después de la simulación
            mostrar_cola_procesos(planificador.procesos)

            # Esperar hasta que se cierre el gráfico
            input("Presione Enter para continuar y regresar al menú...")

        elif opcion == '2':
            print("\n--- Simulación SJF ---")
            num_procesos = int(input("Ingrese el número de procesos: "))
            procesos = []
            for i in range(num_procesos):
                tiempo_llegada = int(input(f"Ingrese el tiempo de llegada del proceso {i+1}: "))
                
                # Asignar tiempo de ejecución y memoria de manera aleatoria
                rafaga_cpu = random.randint(1, 10)
                memoria = random.randint(100, 500)
                
                print(f"  Tiempo de ejecución (aleatorio): {rafaga_cpu}")
                print(f"  Memoria consumida (aleatorio): {memoria} MB")
                
                procesos.append(Proceso(id_proceso=i+1, tiempo_llegada=tiempo_llegada, rafaga_cpu=rafaga_cpu, memoria=memoria))

            # Llamar a la función que genera el gráfico
            mostrar_grafico(procesos)

            # Llamar a la simulación
            planificador = Planificador(sjf)
            for proceso in procesos:
                planificador.agregar_proceso(proceso)
            
            # Iniciar la simulación y mostrar el estado de la cola de procesos después de cada ejecución
            planificador.simular()

            # Mostrar la cola de procesos después de la simulación
            mostrar_cola_procesos(planificador.procesos)

            input("Presione Enter para continuar y regresar al menú...")

        elif opcion == '3':
            print("\n--- Simulación Round Robin ---")
            num_procesos = int(input("Ingrese el número de procesos: "))
            quantum = int(input("Ingrese el quantum para Round Robin: "))
            procesos = []
            for i in range(num_procesos):
                tiempo_llegada = int(input(f"Ingrese el tiempo de llegada del proceso {i+1}: "))
                
                # Asignar tiempo de ejecución y memoria de manera aleatoria
                rafaga_cpu = random.randint(1, 10)
                memoria = random.randint(100, 500)
                
                print(f"  Tiempo de ejecución (aleatorio): {rafaga_cpu}")
                print(f"  Memoria consumida (aleatorio): {memoria} MB")
                
                procesos.append(Proceso(id_proceso=i+1, tiempo_llegada=tiempo_llegada, rafaga_cpu=rafaga_cpu, memoria=memoria))

            # Llamar a la función que genera el gráfico
            mostrar_grafico(procesos)

            # Llamar a la simulación
            planificador = Planificador(round_robin, quantum=quantum)
            for proceso in procesos:
                planificador.agregar_proceso(proceso)
            
            # Iniciar la simulación y mostrar el estado de la cola de procesos después de cada ejecución
            planificador.simular()

            # Mostrar la cola de procesos después de la simulación
            mostrar_cola_procesos(planificador.procesos)

            input("Presione Enter para continuar y regresar al menú...")

        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Llamada al menú principal
if __name__ == "__main__":
    menu_principal()
