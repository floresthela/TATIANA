'''
TATIANA
Archivo para la memoria de ejecución

Flor Esthela Barbosa y Laura Santacruz
'''


class Memoria:

    def __init__(self):
        
        # mejor usamos diccionarios, más rápido
        
        self.mem_global = {}
        self.mem_local = {}
        self.mem_constantes = {}

    
    def record_activacion(self, scope):
        print("nada")
