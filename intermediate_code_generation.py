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
    def generate_quad(self):
        list = []
        # left_op = self.PilaO.pop()
        # left_type = self.PTypes.pop()

        # right_op = self.PilaO.pop()object
        # right_type = self.PTypes.pop()

        # operator = self.POper.pop()
        # operator_s = Operators(operator)

        # result_type = self.semantic_cube.semantics(left_type, right_type, operator_s)

        # if result_type:
        #     temp_actual = "t" + self.temps
        #     self.temps += 1
        #     result = temp_actual
        #     quadruple = Quadruple(left_type,right_type, operator_s, result)
        #     print(result)
        #     self.POper.append(result)
        #     self.PTypes.append(result_type)
    #def graph_quad(self):

        # para prints o así ?
    #def other_quad(self):
