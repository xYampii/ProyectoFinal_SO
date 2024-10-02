class Proceso:
    def __init__(self, id_proceso, tiempo_llegada, rafaga_cpu, memoria, prioridad=None):
        """
        Clase que representa un proceso en el sistema de planificación.
        
        :param id_proceso: Identificador único del proceso.
        :param tiempo_llegada: Tiempo en el que el proceso llega al sistema.
        :param rafaga_cpu: Tiempo de CPU que el proceso necesita.
        :param memoria: Cantidad de memoria consumida por el proceso.
        :param prioridad: Prioridad del proceso (opcional).
        """
        self.id_proceso = id_proceso
        self.tiempo_llegada = tiempo_llegada
        self.rafaga_cpu = rafaga_cpu
        self.memoria = memoria
        self.prioridad = prioridad
        self.estado = 'listo'
        self.tiempo_ejecucion = 0
        self.tiempo_restante = rafaga_cpu
        self.tiempo_completado = None

    def __str__(self):
        """
        Método para imprimir la información del proceso de manera legible.
        """
        return (f"Proceso {self.id_proceso}: "
                f"Tiempo de llegada = {self.tiempo_llegada}, "
                f"Ráfaga de CPU = {self.rafaga_cpu}, "
                f"Memoria consumida = {self.memoria} MB"
                + (f", Prioridad = {self.prioridad}" if self.prioridad is not None else ""))

    def ejecutar(self):
        """
        Simula la ejecución del proceso, imprimiendo su información.
        """
        print(f"Ejecutando {self}")

    def obtener_info(self):
        """
        Devuelve un diccionario con la información del proceso para análisis o visualización.
        """
        return {
            'id_proceso': self.id_proceso,
            'tiempo_llegada': self.tiempo_llegada,
            'rafaga_cpu': self.rafaga_cpu,
            'memoria': self.memoria,
            'prioridad': self.prioridad
        }
