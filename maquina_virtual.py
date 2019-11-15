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
        Recibe archivo .ta* con todo (Quads, FunDir, tConstantes)
        :param program: Nombre del archivo
        '''
        arch = program + '.ta*'
        archivo = open(program, 'r')
        todito = json.load(archivo)

        for const in todito['tConstantes']:
            dir = const[0]
            valor = const[1]
            self.memoria.mem_constantes[dir] = self.convert_to_type(valor)
            