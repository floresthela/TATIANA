# TATIANA
# Flor Esthela Barbosa & Laura Santacruz

# INTERMEDIATE-CODE GENERATION
# CUÁDRUPLOS

from semantic_cube import Operators, SemanticCube

# TODO: hay que hacer cuadruplos especiales para nuestros statements de graficar

# DUDA cuándo checamos si las variables ya fueron declaradas cuando las estamos usando en algo ??¿?¿?¿?¿?¿??¿


class Quadruple:
    def __init__(self, left_op, right_op, operator, result):
        '''
        Inicializa cuádruplo
        '''
        self.left_op = left_op
        self.right_op = right_op
        self.operator = operator
        self.result = result

class Intermediate_CodeGeneration:
    def __init__(self):
        # pending operators
        self.POper = []
        # types
        self.PTypes = []
        # pending operands
        self.PilaO = []

        self.temps = 0
        self. PJumps = []
        self.Quads = []
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
                temp_actual = "t" + str(self.temps)
                self.temps += 1
                result = temp_actual
                quadruple = Quadruple(left_op,right_op, operator, result)
                self.muestramelo(quadruple)
            else:
                result = left_op
                quadruple = Quadruple(right_op, None, operator, result)
                self.muestramelo(quadruple)

        self.Quads.append(quadruple)
        self.PilaO.append(result)
        self.PTypes.append(result_type)

    def generate_quad_print(self):
        '''
        Genera cuádruplo para print
        '''
        result = self.PilaO.pop()
        # no nos importa el tipo xq no lo usaremos después ni nunca
        self.PTypes.pop()
        operator = self.POper.pop()
        quadruple = Quadruple(None,None,operator,result)
        self.muestramelo(quadruple)



    def generate_quad_read(self):
        '''
        Generar cuádruplo para stmt read
        '''
        result = self.PilaO.pop()
        self.PTypes.pop()
        operator = self.POper.pop()
        quadruple = Quadruple(None,None,operator,result)
        self.muestramelo(quadruple)

    # def generate_quad_graph(self):

    def muestramelo(self, quad):
        print('quad',f'[{quad.operator},{quad.left_op},{quad.right_op},{quad.result}]')

        #     print(result)
        #     self.POper.append(result)
        #     self.PTypes.append(result_type)
