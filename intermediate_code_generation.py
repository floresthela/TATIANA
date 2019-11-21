'''
TATIANA
Archivo para la generación de código intermedio, los cuádruplos

Flor Esthela Barbosa y Laura Santacruz
'''

from semantic_cube import Operators, SemanticCube
import json
from vars_table import VarsTable

class Quadruple:
    def __init__(self, operator,left_op, right_op, result):
        '''
        Inicializa cuádruplo
        '''
        self.left_op = left_op
        self.right_op = right_op
        self.operator = operator
        self.result = result

    def __repr__(self):
        return f"\t{self.operator}\t{self.left_op}\t{self.right_op}\t{self.result}\n"

    def __str__(self):
        return f"\t{self.operator},{self.left_op},{self.right_op},{self.result}\n"

    def cambia_res(self,res):
        '''
        Cambia el resultado del cuádruplo (posición 4)
        :param result: Nuevo resultado
        '''
        self.result = res


class Intermediate_CodeGeneration:
    def __init__(self):
        # pending operators
        self.POper = []
        # types
        self.PTypes = []
        # pending operands
        self.PilaO = []
        # pending jumps
        self.PJumps = []

        self.inicia_star = None
        self.era = None

        # contadores
        # self.c_temps = [0,0,0] = [int,float,string]

        self.temps = 0

        # son 4 pero es solo para guardar booleanos, nunca los usamos
        self.c_params = 0
        self.c_global = [0,0,0,0]
        self.c_local = [0,0,0,0]
        self.c_constantes = [0,0,0,0]

        self.Quads = [] # lista de cuádruplos que llevamos
        self.contador = 1 # creo que este no lo necesitamos
        self.cubo = SemanticCube()
        self.PTemp = []  # solo la use para los params para meter el tipo de dato de cuando defines una funcion

        # Tabla de constantes [valor,dir]
        # un diccionario para buscar, si hacemos un arreglo creo que sería más tardado (for loop)
        self.constantes = {}

        # bases para memoria
        self.base_global = 1000

        # temporales locales a los módulos
        self.base_local = 21000
        self.base_constantes = 41000

        '''
        GLOBAL
        i [1000  -  5999]
        f [6000  -  9999]
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

        self.b_int = 0
        self.b_float = 5000
        self.b_string = 10000
        self.b_bool = 15000

    def reset_locales(self):
        '''
        Resetea el contador de las variables locales, temps
        '''
        self.c_local = [0,0,0,0]

    def direccion_mem(self, mem, type, size = 1, val = None):
        '''
        Ingresa variable en memoria y regresa la dirección
        :param mem: tipo de memoria en la que se encuentra
        :param type: tipo de variable
        '''

        # size es para arreglos

        if type == 'int':
            # para checar al rato que no nos pasemos
            t_inicia = self.b_int
            t_fin = self.b_float - 1
            indice = 0
        elif type == 'float':
            t_inicia = self.b_float
            t_fin = self.b_string - 1
            indice = 1
        elif type == 'string':
            t_inicia = self.b_string
            t_fin = self.b_bool
            indice = 2
        elif type == 'bool':
            t_inicia = self.b_bool
            t_fin = self.base_constantes
            indice = 3
        else:
            raise TypeError(f"Tipo '{type}' desconocido")

        if mem == 'global':
            dir = self.base_global + t_inicia + self.c_global[indice]
            self.c_global[indice] += size

            if dir + size > self.base_global + t_fin:
                raise TypeError(f"Stack Overflow: {mem} no tiene espacio para {type}")


        elif mem == 'local':
            dir = self.base_local + t_inicia + self.c_local[indice]
            self.c_local[indice] += size
            if dir + size > self.base_local + t_fin:
                raise TypeError(f"Stack Overflow: {mem} no tiene espacio para {type}")

        elif mem == 'constantes':
            if val is None:
                raise TypeError(f"Valor de constante no especificado")

            elif val in self.constantes.values():
               return [x for x, y in self.constantes.items() if y == val].pop()
            dir = self.base_constantes + t_inicia + self.c_constantes[indice]

            if dir + size > self.base_constantes + t_fin:
                raise TypeError(f"Stack Overflow: {mem} no tiene espacio para {type}")

            if indice == 2:
                val = val.strip('"')

            self.constantes[dir] = val
            self.c_constantes[indice] += size

        else:
            raise TypeError(f"Tipo de memoria '{mem}' desconocida")

        return dir

    def generate_quad(self,scope):
        right_op = self.PilaO.pop()
        right_type = self.PTypes.pop()

        left_op = self.PilaO.pop()
        left_type = self.PTypes.pop()

        operator = self.POper.pop()
        operator_s = Operators(operator)

        result_type = self.cubo.semantics(left_type, right_type, operator_s)

        if result_type:
            if operator != '=':

                # se genera temporal
                if scope == 'global':
                    result = self.direccion_mem('global',result_type)
                else :
                    result = self.direccion_mem('local',result_type)

                quadruple = Quadruple(operator, left_op, right_op, result)
                self.PilaO.append(result)
                self.PTypes.append(result_type)

            else:
                result = left_op
                quadruple = Quadruple(operator, result, None, right_op)
        self.Quads.append(quadruple)
        return result_type

    def generate_quad_print(self):
        '''
        Genera cuádruplo para print
        '''
        result = self.PilaO.pop()
        # no nos importa el tipo xq no lo usaremos después ni nunca
        self.PTypes.pop()
        operator = self.POper.pop()
        quadruple = Quadruple(operator, None, None, result)
        self.Quads.append(quadruple)

    def generate_quad_read(self):
        '''
        Generar cuádruplo para stmt read
        '''
        result = self.direccion_mem('local','string')

        operator = self.POper.pop()
        quadruple = Quadruple(operator, None, None, result)

        self.Quads.append(quadruple)
        self.POper.append(result)
        self.PTypes.append('string')

    def generate_GOTOF(self):
        '''
        Genera GOTOF para condicion y while
        '''
        # Hay que checar si sí jala un elseif igual... aunque si deberia no?? lo checamos.
        exp_type = self.PTypes.pop()
        if exp_type != 'bool':
            raise TypeError("ERROR: Type-mismatch")
        else:
            result = self.PilaO.pop()
            quadruple = Quadruple('GotoF', result, None, None)
            self.Quads.append(quadruple)
            self.PJumps.append(len(self.Quads)-1)

    def generate_GOTOV(self):
        '''
        Genera GOTOV para for
        '''
        for_type = self.PTypes.pop()
        if for_type != 'bool':
            raise TypeError("ERROR: Type-mismatch")
        else:
            cond = self.PilaO.pop()
            quadruple = Quadruple('GotoV', cond, None, None)
            self.Quads.append(quadruple)
            self.PJumps.append(len(self.Quads)-1)


    def generate_END(self):
        '''
        Genera cuádruplo de END para determinar el fin del archivo
        '''
        quadruple = Quadruple('END',None,None,None)
        self.Quads.append(quadruple)

    def check_type(self, var):
        '''
        Checa que el tipo de la variable (id)
        param: Variable (id) que se agrega a PilaO
        '''
        tipo = self.PTypes.pop()
        if tipo != 'int' or tipo != 'float':
            raise TypeError("ERROR: Type mismatch")
        else:
            self.PilaO.append(var)

    def generate_compare_quad(self):
        '''
        Generate comparisson quad used in for loop
        '''
        tmp1 = self.PilaO.pop()
        tmp2 = self.PilaO.pop()


    def generate_else(self):
        '''
        Genera GOTO para ELSE
        '''
        # 3.-
        quadruple = Quadruple('Goto', None, None, None)
        self.Quads.append(quadruple)
        position = self.PJumps.pop()
        self.PJumps.append(len(self.Quads) - 1)
        self.fill_quad(position)

    def generate_GOTO(self):
        '''
        Genera GOTO vacío que se rellenará después (while, for)
        '''
        quadruple = Quadruple('Goto', None, None, None)
        self.Quads.append(quadruple)

    def generate_GOTO_star(self):
        '''
        Genera goto para ir al main (función estrella)
        '''
        quadruple = Quadruple("Goto_main",None,None,None)
        self.Quads.append(quadruple)
        self.inicia_star = len(self.Quads) - 1

    def fill_goto_star(self,result):
        '''
        Rellen el GOTO para ir a función star
        :param result: Posición a llenar, donde comienza el main
        '''
        if self.inicia_star is not None:
            self.Quads[self.inicia_star].cambia_res(result)

    def fill_quad(self,p):
        '''
        Rellena (FILL) al cuádruplo
        :param p: La posición del cuádruplo a completar
        '''
        self.Quads[p].cambia_res(len(self.Quads)+1)

    def fill_goto(self, result):
        '''
        Rellena el goto con el resultado
        :param result: Valor a rellenar para el goto
        '''
        position = len(self.Quads) - 1
        self.Quads[position].cambia_res(result)

    def generate_quad_graph0(self, type):
        '''
        Genera cuádruplo de gráfica que no lleva ningún parámetro
        :param type: tipo de acción para graficar (hand_down o hand_up)
        '''
        quadruple = Quadruple(type, None, None, None)
        self.Quads.append(quadruple)

    def generate_quad_graph1(self,type):
        '''
        Genera cuádruplo de gráfica que lleva solo un parámetro
        :param type: tipo de acción para graficar
        '''
        exp_type = self.PTypes.pop()
        if exp_type != 'int':
            raise TypeError("ERROR: Type-mismatch")
        else:
            result = self.PilaO.pop()
            quadruple = Quadruple(type, result, None, None)
            self.Quads.append(quadruple)

    def generate_quad_graph2(self,type):
        '''
        Genera cuádruplo de gráfica que lleva un parámetro (dos expresiones)
        :param type: tipo de acción para graficar
        '''
        # igual que un quad normal creo
        expT_1 = self.PTypes.pop()
        expT_2 = self.PTypes.pop()

        if expT_1 != 'int' or expT_2 != 'int':
            raise TypeError("ERROR: Type-mismatch")
        else:
            exp_1 = self.PilaO.pop()
            exp_2 = self.PilaO.pop()
            quadruple = Quadruple(type, exp_2, exp_1, None)
            self.Quads.append(quadruple)

    def generate_ERA(self):
        '''
        Genera cuadruplo de ERA (llamada a funcion)
        :param fun: el nombre de la funcion
        '''
        quadruple = Quadruple('ERA', None, None, None)
        self.Quads.append(quadruple)
        self.era = len(self.Quads)-1


    def fill_ERA(self, funcName):
        '''
        Rellena el era con el num
        '''
        if self.era is not None:
            self.Quads[self.era].cambia_res(funcName)

    def generate_paramQuad(self, direccion):
        '''
        Generate params quad
        '''
        quadruple = Quadruple('param', None, None, direccion)
        self.Quads.append(quadruple)

    def generate_GOSUB(self, begin):
        '''
        Generate goSub quadruple
        '''
        quadruple = Quadruple('GOSUB', None, None, begin)
        self.Quads.append(quadruple)


    def checa_Tipo_Params(self, params_dec, params_fun):
        '''
        para checar si los parametros de la llamada a la funcion
        son del mismo tipo que cuando se declara
        '''
        len1 = len(params_dec)
        len2 = len(params_fun)

        if len(params_fun) != len(params_dec):
            raise TypeError("ERROR: Expected "+str(len1)+" params, got "+str(len2)+" instead")
        elif params_dec != params_fun:
            raise TypeError("ERROR: Type mismatch in parameters")

    def genera_matrices(self, base, r, c, var_dim):
        '''
        Generación de cuádruplos correspondientes para el acceso a una matriz
        :param base: Dirección base
        :param var_dim: Variable dimensionada
        '''

        base = self.direccion_mem('constantes','int',val= base)
        ren = self.direccion_mem('constantes','int',val=var_dim[0])
        col = self.direccion_mem('constantes','int',val= var_dim[1])

        # Cuádruplos para verificar rangos
        ver1 = Quadruple('VER', c, ren, None)
        ver2 = Quadruple('VER', r, col, None)

        self.Quads.append(ver1)
        self.Quads.append(ver2)

        # Genera cuádruplos para función s1 * m1 + s2 + base
        # Cuádruplos para * aux mdim T
        auxmdim = self.direccion_mem('local','int')

        q_auxmdim = Quadruple('*',c,ren,auxmdim)
        self.Quads.append(q_auxmdim)

        # Cuádruplos para + aux1 aux2 T
        sumaux = self.direccion_mem('local','int')
        temp = Quadruple('+',auxmdim,r,sumaux)
        self.Quads.append(temp)

        # Cuádruplos para + T BASE T
        sumabase = self.direccion_mem('local','int')
        q_sumabase = Quadruple('+',sumaux, base, sumabase)
        self.Quads.append(q_sumabase)
        print('mat',sumabase)
        return sumabase

    def genera_arreglos(self,base,tam, var_dim):
        '''
        Generación de cuádruplos correspondientes para el acceso a un vetor
        :param base: Dirección base
        :param tam: Tamaño del arreglo
        :param var_dim: Variable dimensionada
        '''

        base = self.direccion_mem('constantes','int',val=base)
        tamano = self.direccion_mem('constantes','int',val= var_dim[1])

        # Cuádruplo para verificar
        ver = Quadruple('VER', tam, tamano, None)
        self.Quads.append(ver)

        # Sumar base

        sumabase = self.direccion_mem('local','int')
        q_sumabase = Quadruple('+',tam, base, sumabase)
        self.Quads.append(q_sumabase)
        print('arr',sumabase)
        return sumabase


    def format_quads(self):
        # print(self.Quads)
        return [(quad.operator, quad.left_op, quad.right_op, quad.result) for quad in self.Quads]

    def format_constantes(self):
        return [(k, v) for k, v in self.constantes.items()]
