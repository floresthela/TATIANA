'''
TATIANA
Archivo para la memoria de ejecución

Flor Esthela Barbosa y Laura Santacruz
'''

from collections import OrderedDict

class Memoria:

    def __init__(self):
        
        # mejor usamos diccionarios, más rápido
        
        self.mem_global = {}
        self.mem_local = {}
        self.mem_constantes = {}

        self.mem = OrderedDict()
        self.activa = None
        self.base_fun = 40000
        self.contador = 0

    def record_activacion(self, superior, tamaño):
        actual = MemLocal(superior, tamaño)

        if self.contador + tamaño > 40000:
            raise TypeError(f'Stack Overflow: Pila de ejecución llena')

        dir = self.base_fun + self.contador
        self.contador = self.contador + tamaño
        self.mem[dir] = actual
    
    def cuello(self):
        '''
        Elimina scope de memoria (local) actual 
        '''
        if self.activa is not None:
            if self.activa.superior is not self:
                self.activa = self.activa.superior
            else:
                self.activa = None
            fun = list(self.mem.keys())[-1]
            self.contador -= self.mem[fun].size
            del self.mem[fun]



class MemLocal:
    def __init__(self, superior, tamaño):
        self.mem_local = {}
        self.contador = 21000 # base local
        
        self.superior = superior
        self. tam = tamaño

    def haz_params(self,params):
        for p in params[::-1]:
            self.mem_local[self.contador] = p
            self.contador += 1