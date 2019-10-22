# TATIANA
# Flor Esthela Barbosa & Laura Santacruz

# INTERMEDIATE-CODE GENERATION


from semantic_cube import Operators, SemanticCube


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
        self.POper = []
        self.PTypes = []
        self.Quads = []
        self.PilaO = []
        self. PJumps = []
        self.temps = 0

# 1. = 10 a
# 2. = 2 b
# 3. + a b t1
# 4. = t1 c

    def generate_quad(self):
        for x in self.PilaO:
            print(x)

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
