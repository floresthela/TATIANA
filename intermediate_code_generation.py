# TATIANA
# Flor Esthela Barbosa & Laura Santacruz

# INTERMEDIATE-CODE GENERATION
# CUÁDRUPLOS

from semantic_cube import Operators, SemanticCube

# TODO: hay que hacer cuadruplos especiales para nuestros statements de graficar

class Quadruple:
    def __init__(self, operator,left_op, right_op, result):
        '''
        Inicializa cuádruplo
        '''
        self.left_op = left_op
        self.right_op = right_op
        self.operator = operator
        self.result = result #DUDA: Podemos tener una tupla como resultado (para stmts de graph que llevan varios valores)???? por qué tengo una obsesión con las tuplas ??

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
        self. PJumps = []

        self.temps = 0
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
                temp_actual = "t" + str(self.temps)
                self.temps += 1
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

    def generate_quad_graph(self):
        '''
        Generar cuádruplos con expresiones para graficar...
        '''
        # hay que ver... unos no llevan nada, otros llevan uno o dos números
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

    def generate_else_GOTO(self):
        '''
        Genera GOTO para else
        '''
        # 3.-
        quadruple = Quadruple('GOTO',None,None,None)
        self.Quads.append(quadruple)
        position = self.PJumps.pop()
        self.PJumps.append(len(self.Quads) - 1)
        self.fill_quad(position)

    def generate_elseif(self):
        '''
        Genera cuádruplo para elseif statement
        '''
        position = self.PJumps.pop()
        self.PJumps.append(len(self.Quads) - 1)
        self.fill_quad(position)


    def fill_quad(self,p):
        '''
        Rellena (FILL) al cuádruplo
        :param p: La posición del cuádruplo a completar
        '''
        self.Quads[p].cambia_res(len(self.Quads)+1)
