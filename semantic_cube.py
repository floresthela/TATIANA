'''
TATIANA
Archivo del cubo semántico del lenguaje con las operaciones permitadas de acuerdo a los tipos y sus operadores

Flor Esthela Barbosa y Laura Santacruz
'''

import sys
from enum import Enum


class Operators(Enum):
    ADDITION = '+'
    SUBSTRACTION = '-'
    MULTIPLICATION = '*'
    DIVISION = '/'
    GREATER = '>'
    LESS = '<'
    GREATEREQ = '>='
    LESSEQ = '<='
    NOT_EQUAL = '!='
    ISEQUAL = '=='
    EQUAL = '='
    RETURN = 'return'


class SemanticCube:
    '''
    Cubo Semántico
    '''
    def __init__(self):
        '''
        inicializa cubo semántico
        '''
        self.semantic_cube = {
            Operators.ADDITION: {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'string'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'string'
                },
                'string': {
                    'int': 'string',
                    'float': 'string',
                    'string': 'string'
                }
            },
            Operators.SUBSTRACTION: {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err'
                }
            },
            Operators.MULTIPLICATION: {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err'
                }
            },

            Operators.DIVISION: {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'string': 'err'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err'
                }
            },
            # agregamos bool como tipo entonces ???? EVIDENTEMENTE lo necesitamos...
            Operators.GREATER: {
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err'
                }
            },

            Operators.LESS: {
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err'
                }
            },
            Operators.GREATEREQ: {
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err'
                }
            },

            Operators.LESSEQ: {
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'err'
                }
            },
            Operators.ISEQUAL: {
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'string'
                }
            },
            Operators.NOT_EQUAL: {
                'int': {
                    'int': 'bool',
                    'float': 'err',
                    'string': 'err'
                },
                'float': {
                    'int': 'err',
                    'float': 'bool',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'bool'
                }
            },
            Operators.EQUAL: {
                'int': {
                    'int': 'int',
                    'float': 'int',
                    'string': 'err'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'string'
                }
            },
            Operators.RETURN: {
                'int': {
                    'int': 'int',
                    'float': 'err',
                    'string': 'err'
                },
                'float': {
                    'int': 'err',
                    'float': 'float',
                    'string': 'err'
                },
                'string': {
                    'int': 'err',
                    'float': 'err',
                    'string': 'string'
                }
            }


        }

    def semantics(self, left_type, right_type, operator):
        '''
        Will determine if given two types of variables and an operator, the operation will be valid or not
        :param left_type: type of left variable of operation
        :param right_type: type of right variable of operation
        :param operator: operator given for the operation
        '''
        if self.semantic_cube[operator][left_type][right_type] != 'err':
            return self.semantic_cube[operator][left_type][right_type]
        raise TypeError("No se puede aplicar el operador {} a los tipos {} y {}".format(
            operator.name, left_type, right_type))


# https://docs.python.org/3/library/enum.html
