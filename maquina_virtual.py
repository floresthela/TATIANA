'''
TATIANA
Archivo para la máquina virtual

Flor Esthela Barbosa y Laura Santacruz
'''
import sys
import json
from turtle import Turtle, Screen, Shape

from memoria import Memoria

class MaquinaVirtual:
    def __init__(self):
        self.memoria = Memoria()
        self.estrella = Turtle()
        self.screen = Screen()


    def agarra_ta(self,program):
        '''
        Recibe archivo .ta con todo { Quads:, FunDir:, tConstantes: }
        :param program: Nombre del archivo
        '''
        arch = f"pruebas/{program}.ta"
        archivo = open(arch, 'r')
        todito = json.load(archivo)

        self.estrella.screen.title(program)
        # fundir
        fun_dir = todito["FunDir"]
        # print(fun_dir)
        # creamos memoria de constantelapiz...
        self.haz_constantes(todito['tConstantes'])


        self.haz_quads(todito['Quads'],fun_dir)

    # dnb
    def haz_quads(self,quads,fun_dir,sig=0):
        '''
        Procesar cada cuadruplo de la lista de Quads recibida
        :param quads: Lista con todos los quads
        :param fun_dir: Directorio de funciones
        :param sig: Apuntador al siguiente cuádruplo
        '''
        s = Turtle()
        screen = Screen()
        self.dibuja_estrella(s)
        screen.clear()

        self.star = Turtle(shape="estrella")

        while True:
            operador = quads[sig][0]
            op_izq = quads[sig][1]
            op_der = quads[sig][2]
            res = quads[sig][3]

            if operador == '=':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                tipo_res = self.dame_tipo(res)
                mem_r[res] = tipo_res(mem1[op_izq])
                sig += 1

            elif operador == '+':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] + mem2[op_der]
                sig += 1

            elif operador == '-':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] - mem2[op_der]
                sig += 1

            elif operador == '*':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] * mem2[op_der]
                sig += 1

            elif operador == '/':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                tipo_res = self.dame_tipo(res)

                if mem2[op_der] == 0:
                    raise TypeError(f"Error: No se puede dividir entre 0")

                mem_r[res] = tipo_res(mem1[op_izq] / mem2[op_der])
                sig += 1

            elif operador == '>':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] > mem2[op_der]
                sig +=1

            elif operador == '<':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] < mem2[op_der]
                sig +=1

            elif operador == '!=':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] != mem2[op_der]

                sig +=1

            elif operador == '==':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] != mem2[op_der]

                sig +=1

            elif operador == 'print':
                mem_r = self.dame_mem(res)
                print(mem_r[res])
                sig +=1
                break

            elif operador == 'Goto_main':
                jump = res -1
                sig = jump
                # activamos memoria star

            elif operador == 'END':
                break




    def haz_constantes(self, t):
        '''
        Genera tabla de constantes
        :param t: Tabla de constantes
        '''
        for const in t:
            dir = const[0]
            val = const[1]
            self.memoria.mem_constantes[dir] = val

        '''
        GLOBAL
        i [1000  -  5999]
        f [6000  - 10999]
        s [11000 - 15999]
        b [16000 - 20999]


        LOCAL
        i [21000 - 25999]
        f [26000 - 30999]
        s [31000 - 35999]
        b [36000 - 40999]

        CONSTANTES
        c [41000 - 51999]

        '''

    def dame_memorias(self, op_i, op_d, res):
        return self.dame_mem(op_i) , self.dame_mem(op_d), self.dame_mem(res)

    def dame_mem(self, dir):
        '''
        Regresa la dirección a la que pertenece la variable global, local o de constantes
        :param dir: Dirección de variable
        '''
        if dir is None:
            return None
        elif 1000 <= dir < 21000:
            return self.memoria.mem_global
        elif 21000 <= dir < 41000:
            # hay que poner la activa
            return self.memoria.mem_local
        else:
            return self.memoria.mem_constantes

    def dame_tipo(self,dir):
        '''
        Regresa el tipo de variable
        :param dir: Dirección de variable
        '''
        if 1000 <= dir < 6000 or 21000 <= dir < 26000:
            return int
        elif 6000 <= dir < 11000 or 26000 <= dir < 31000:
            return float
        elif 11000 <= dir < 16000 or 31000 <= dir < 36000:
            return str
        else:
            return bool

    def dibuja_estrella(self,lapiz):
        '''
        Define una figura de estrella como el lapiz que dibujará
        '''
        fig = Shape("compound")
        lapiz.setx(0)
        lapiz.sety(4)

        lapiz.begin_poly()
        lapiz.goto(1,1)
        lapiz.goto(3.5,1)
        lapiz.goto(1.5,-0.5)
        lapiz.goto(2.5,-3)
        lapiz.goto(0,1.5)
        lapiz.goto(-2.5,-3)
        lapiz.goto(-1.5,-0.5)
        lapiz.goto(-3.5,1)
        lapiz.goto(-1,1)
        lapiz.end_poly()

        fig.addcomponent(lapiz.get_poly(),"purple","purple")
        self.screen.register_shape("estrella",fig)
        lapiz.reset()
