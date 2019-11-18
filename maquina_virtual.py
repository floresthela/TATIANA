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

        # fundir
        fun_dir = todito["FunDir"]
        # print(fun_dir)
        # creamos memoria de constantes...
        self.haz_constantes(todito['tConstantes'])


        self.haz_quads(todito['Quads'],fun_dir)
        print(todito['Quads'])
    # dnb
    def haz_quads(self,quads,fun_dir,i=0):
        '''
        Procesar cada cuadruplo de la lista de Quads recibida
        :param quads: Lista con todos los quads
        :param fun_dir: Directorio de funciones
        :param i: Apuntador al siguiente cuádruplo
        '''
        while True:
            operador = quads[i][0]
            op_izq = quads[i][1]
            op_der = quads[i][2]
            res = quads[i][3]
            
            if operador == '=':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                tipo_res = self.dame_tipo(res)
                mem_r[res] = tipo_res(mem1[op_izq])
                i += 1
        
            elif operador == '+':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] + mem2[op_der]
                i += 1
          
            elif operador == '-':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] - mem2[op_der]
                i += 1
            
            elif operador == '*':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] * mem2[op_der]
                i += 1
            
            elif operador == '/':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                if mem2[op_der] == 0:
                    raise TypeError(f"Error: No se puede dividir entre 0")
                mem_r[res] = mem1[op_izq] / mem2[op_der]
                i += 1
            
            elif operador == '>': 
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] > mem2[op_der]
                i+=1
            
            elif operador == '<':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] < mem2[op_der]
                i+=1
            
            elif operador == '!=':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] != mem2[op_der]
                print('hola',mem_r[res])
                i+=1
            
            
            # elif operador == 'OPERADOR':
            #     i+=1

            elif operador == 'END':
                break

            self.haz_quads(quads,fun_dir,i)
            print(self.memoria.mem_global)
        
        '''
        GLOBAL
        i [1000  -  5999]
        f [6000  -  9999]
        s [11000 - 15999]
        

        LOCAL
        i [16000 - 20999]
        f [21000 - 25999]
        s [26000 - 30999]
        
        CONSTANTES
        c [31000 - 40999]

        '''
    def haz_constantes(self, t):
        '''
        Genera tabla de constantes
        :param t: Tabla de constantes
        '''
        for const in t:
            dir = const[0]
            val = const[1]
            self.memoria.mem_constantes[dir] = val

    def dame_memorias(self, op_i, op_d, res):
        return self.dame_mem(op_i) , self.dame_mem(op_d), self.dame_mem(res)

    def dame_mem(self, dir):
        
        if dir is None:
            return None
        elif 1000 <= dir < 16000:
            return self.memoria.mem_global
        elif 16000 <= dir < 31000:
            # hay que poner la activa
            return self.memoria.mem_local
        else:
            return self.memoria.mem_constantes
    
    def dame_tipo(self,dir):
        if 1000 <= dir < 6000 or 16000 <= dir < 21000:
            return int
        elif 6000 <= dir < 11000 or 21000 <= dir < 26000:
            return float
        elif 11000 <= dir < 16000 or 26000 <= dir < 31000:
            return str
        else:
            return bool
