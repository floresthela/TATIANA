# TATIANA
# Flor Esthela Barbosa & Laura Santacruz

# INTERMEDIATE-CODE GENERATION
# CUÁDRUPLOS

from semantic_cube import Operators, SemanticCube


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
        return f"{self.operator},{self.left_op},{self.right_op},{self.result}\n"

    def cambia_res(self,res):
        '''
        Cambia el resultado del cuádruplo (posición 4)
        :param result: el resultado nuevo
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
        # self.c_temps = [0,0,0]
        self.c_params = 0
        self.c_global = [0,0,0]
        self.c_local = [0,0,0]
        self.c_constantes = [0,0,0]

        self.Quads = [] # lista de cuádruplos que llevamos
        self.contador = 1 # creo que este no lo necesitamos
        self.cubo = SemanticCube()

        # Tabla de constantes [valor,dir]
        self.constantes = {}

        # bases para memoria
        self.base_global = 1000

        # temporales locales a los módulos
        self.base_local = 16000
        self.base_constantes = 31000

        self.b_int = 0
        self.b_float = 5000
        self.b_char = 10000

    def reset_locales(self):
        '''
        Resetea el contador de las variables locales
        '''
        self.c_local = [0,0,0]

    def direccion_mem(self, mem, type, val = None):
        '''
        Ingresa variable en memoria y regresa la dirección
        :param mem: tipo de memoria en la que se encuentra
        :param type: tipo de variable
        '''

        if type == 'int':
            # para checar al rato que no nos pasemos
            t_inicia = self.b_int
            t_fin = self.b_float - 1
            indice = 0
        elif type == 'float':
            t_inicia = self.b_float
            t_fin = self.b_char - 1
            indice = 1
        elif type == 'char':
            t_inicia = self.b_char
            t_fin = 14999
            indice = 2
        else:
            raise TypeError(f"Tipo '{type}' desconocido")

        if mem == 'global':
            dir = self.base_global + t_inicia + self.c_global[indice]
            self.c_global[indice] += 1

            # falta checar que no nos pasemos de los rangos vvv
        elif mem == 'local':
            dir = self.base_local + t_inicia + self.c_local[indice]
            self.c_local[indice] += 1
        elif mem == 'constantes':
            if val != None:
                for v in self.constantes:
                    if val == v[0]:
                        return v[1]


                dir = self.base_constantes + t_inicia + self.c_constantes[indice]
                self.c_constantes[indice] += 1
                self.constantes[type[0]] = [val, dir]
            else:
                raise TypeError(f"Valor de constante no especificado")
        else:
            raise TypeError(f"Tipo de memoria '{mem}' desconocida")

        print(dir)
        return dir

    def generate_quad(self):
        # print(self.PilaO)
        # print(self.POper)
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
                result = self.direccion_mem('local',result_type)
                quadruple = Quadruple(operator, left_op, right_op, result)
                self.PilaO.append(result)
                self.PTypes.append(result_type)

            else:
                result = left_op
                quadruple = Quadruple(operator, right_op, None, result)
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

    def check_type(self, var):
        '''
        Checks if the id is an int or a float, used in 'for'
        param: the variable (id) to append to the stack of operands
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

    def generate_quad_repeat(self):
        '''
        Cuádruplo para graph stmt REPEAT
        '''
        exp_type = self.PTypes.pop()
        if exp_type != 'int':
            raise TypeError("ERROR: Type-mismatch")
        else:
            # supongo que esto terminará siendo parecido a un FOR
            result = self.PilaO.pop()
            quadruple = Quadruple('Repeat', None, None, None)
            self.Quads.append(quadruple)
            self.PJumps.append(len(self.Quads)-1)

    def generate_ERA(self):
        '''
        Genera cuadruplo de ERA (llamada a funcion)
        :param fun_id: el nombre de la funcion
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

    # def generate_paramQuad(self, arg1, arg2):
    #     '''
    #     Generate params quad
    #     '''
    #     resp = self.PilaO.pop()
    #     tipo = self.PTypes.pop()
    #     quadruple = ('param', resp, None,  )

    def generate_goSub(self, funcName):
        '''
        Generate goSub quadruple
        Param: the function name
        '''
        quadruple = Quadruple('gosub', None, None, funcName)
        self.Quads.append(quadruple)
