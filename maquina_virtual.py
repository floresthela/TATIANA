'''
TATIANA
Archivo para la máquina virtual

Flor Esthela Barbosa y Laura Santacruz
'''
import sys
import json
from memoria import Memoria

class MaquinaVirtual:
    def __init__(self):
        self.memoria = Memoria()

    def agarra_ta(self,program):
        '''
        Recibe archivo .ta* con todo { Quads:, FunDir:, tConstantes: }
        :param program: Nombre del archivo
        '''
        arch = f"pruebas/{program}.ta*"
        archivo = open(arch, 'r')
        todito = json.load(archivo)

        # creamos memoria de constantes...
        Memoria.mem_constantes = todito['tConstantes']

        