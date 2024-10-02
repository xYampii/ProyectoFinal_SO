from Proceso import Proceso

# FIFO
def fifo(planificador):
    planificador.procesos.sort(key=lambda p: p.tiempo_llegada)
    return planificador.procesos.pop(0)

# SJF
def sjf(planificador):
    listos = [p for p in planificador.procesos if p.estado == 'listo']
    if listos:
        # Elige el proceso con la ráfaga más corta
        return min(listos, key=lambda p: p.rafaga_cpu)
    return None

# Round Robin
def round_robin(planificador):
    proceso_actual = planificador.procesos.pop(0)
    if proceso_actual.tiempo_restante > planificador.quantum:
        proceso_actual.tiempo_restante -= planificador.quantum
        planificador.procesos.append(proceso_actual)
    else:
        proceso_actual.tiempo_restante = 0
        proceso_actual.estado = 'terminado'
    return proceso_actual

# Clase Planificador
class Planificador:
    def __init__(self, algoritmo, quantum=None):
        self.procesos = []
        self.reloj = 0
        self.algoritmo = algoritmo
        self.quantum = quantum
        self.resultados = []

    def agregar_proceso(self, proceso):
        self.procesos.append(proceso)

    def simular(self):
        while any(p.estado != 'terminado' for p in self.procesos):
            # Mostrar la cola de procesos pendientes
            print(f"\nTiempo actual: {self.reloj}")
            print("Cola de procesos:")
            for p in self.procesos:
                estado = 'Pendiente' if p.estado != 'terminado' else 'Terminado'
                print(f"  Proceso {p.id_proceso} - Estado: {estado} - Ráfaga CPU restante: {p.rafaga_cpu}")

            # Ejecutar el proceso según el algoritmo
            proceso_actual = self.algoritmo(self)
            
            if proceso_actual:
                print(f"\nEjecutando proceso {proceso_actual.id_proceso} en el tiempo {self.reloj}")
                
                # Incrementa el reloj de la simulación
                self.reloj += 1
                
                # Ejecutar el proceso
                proceso_actual.tiempo_ejecucion += 1
                proceso_actual.tiempo_restante -= 1
                
                # Si el proceso ha terminado
                if proceso_actual.tiempo_restante == 0:
                    proceso_actual.estado = 'terminado'
                    proceso_actual.tiempo_completado = self.reloj
                    self.resultados.append((proceso_actual.id_proceso, proceso_actual.tiempo_completado))
                    print(f"Proceso {proceso_actual.id_proceso} ha terminado en el tiempo {self.reloj}.")
            else:
                print(f"No hay procesos listos para ejecutar en el tiempo {self.reloj}.")
                self.reloj += 1

    def evaluar(self):
        tiempos_respuesta = [p.tiempo_completado - p.tiempo_llegada for p in self.procesos if p.tiempo_completado is not None]
        if tiempos_respuesta:
            promedio_respuesta = sum(tiempos_respuesta) / len(tiempos_respuesta)
            print(f"Tiempo de respuesta promedio: {promedio_respuesta}")
        else:
            print("No hay procesos completados.")
            promedio_respuesta = 0
        return tiempos_respuesta
