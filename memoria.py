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

        self.mem_ejec = OrderedDict()
        self.activa = None
        self.base_fun = 40000
        self.contador = 0

    def record_activacion(self, superior, tamaño):
        '''
        Función para activar nueva memoria local de una función en su llamado y se agrega a la memoria de ejecución
        :param superior: Función en la que se manda llamar
        :param tamaño: Cantidad de variables de la función llamada
        '''
        actual = MemLocal(superior, tamaño)

        if self.contador + tamaño > 40000:
            raise TypeError(f'Stack Overflow: Pila de ejecución llena')

        dir = self.base_fun + self.contador
        self.contador = self.contador + tamaño
        self.mem_ejec[dir] = actual
    
    def cuello(self):
        '''
        Elimina scope de memoria (local) actual 
        '''
        if self.activa is not None:
            if self.activa.superior is not self:
                self.activa = self.activa.superior
            else:
                self.activa = None
            fun = list(self.mem_ejec.keys())[-1]
            self.contador -= self.mem_ejec[fun].tam
            del self.mem_ejec[fun]



class MemLocal:
    def __init__(self, superior, tam):
        self.mem_local = {}
        self.contador = 21000 # base local

        self.c_int = 0
        self.c_str = 10000
        self.c_float = 5000
        
        self.superior = superior
        self.tam = tam

    def matcheo(self,params):
        '''
        Asigna valores de parametros enviados a variables de esa función
        :param params: Lista de parametros
        '''
        
        for p in params:
            if type(p) is int:
                self.mem_local[self.contador + self.c_int] = p
                self.c_int += 1

            elif type(p) is float:
                self.mem_local[self.contador + self.c_float] = p
                self.c_float += 1
            
            elif type(p) is str:
                self.mem_local[self.contador + self.c_str] = p
                self.c_str += 1

