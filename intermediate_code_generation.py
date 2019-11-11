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
        # contadores
        self.c_temps = 0
        self.c_params = 0

        self.Quads = [] # lista de cuádruplos que llevamos
        self.contador = 1 # creo que este no lo necesitamos
        self.cubo = SemanticCube()

    def generate_quad(self):
        right_op = self.PilaO.pop()
        right_type = self.PTypes.pop()

        left_op = self.PilaO.pop()
        left_type = self.PTypes.pop()

        operator = self.POper.pop()
        operator_s = Operators(operator)

        result_type = self.cubo.semantics(left_type, right_type, operator_s)

        if result_type:
            if operator != '=':
                temp_actual = "t" + str(self.c_temps)
                self.c_temps += 1
                result = temp_actual
                quadruple = Quadruple(operator, left_op,right_op, result)
                self.PilaO.append(result)
                self.PTypes.append(result_type)
            else:
                result = left_op
                quadruple = Quadruple(operator, right_op, None, result)
        self.Quads.append(quadruple)


    def generate_quad_print(self):
        '''
        Genera cuádruplo para print
        '''
        result = self.PilaO.pop()
        # no nos importa el tipo xq no lo usaremos después ni nunca
        self.PTypes.pop()
        operator = self.POper.pop()
        quadruple = Quadruple(operator, None,None,result)
        self.Quads.append(quadruple)

    def generate_quad_read(self):
        '''
        Generar cuádruplo para stmt read
        '''
        result = self.PilaO.pop()
        self.PTypes.pop()
        operator = self.POper.pop()
        quadruple = Quadruple(operator, None,None,result)
        self.Quads.append(quadruple)

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
            quadruple = Quadruple('GotoF',result,None,None)
            self.Quads.append(quadruple)
            self.PJumps.append(len(self.Quads)-1)

    def generate_else(self):
        '''
        Genera GOTO para ELSE
        '''
        # 3.-
        quadruple = Quadruple('Goto',None,None,None)
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

    def fill_goto(self,result):
        '''
        Rellena el goto con el resultado
        :param result: Valor a rellenar para el goto
        '''
        position = len(self.Quads) - 1
        self.Quads[position].cambia_res(result)

    def generate_quad_graph0(self,type):
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
