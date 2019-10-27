
# TATIANA
# Flor Esthela Barbosa & Laura Santacruz

# SEMANTIC CUBE of operations

import sys
from enum import Enum


class Operators(Enum):
    ADDITION = '+'
    SUBSTRACTION = '-'
    MULTIPLICATION = '*'
    DIVISION = '/'
    GREATER = '>'
    LESS = '<'
    NOT_EQUAL = '!='
    ISEQUAL = '=='
    AND = 'and'
    OR = 'or'
    EQUAL = '='


class SemanticCube:
    '''
    Cubo Semántico
    '''

    def __init__(self):
        self.semantic_cube: {
            Operators.ADDITION: {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'char': 'err'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'char': 'err'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'err'
                }
            },
            Operators.SUBSTRACTION: {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'char': 'err'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'char': 'err'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'err'
                }
            },
            Operators.MULTIPLICATION: {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'char': 'err'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'char': 'err'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'err'
                }
            },

            Operators.DIVISION: {
                'int': {
                    'int': 'int',
                    'float': 'float',
                    'char': 'err'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'char': 'err'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'err'
                }
            },
            # agregamos bool como tipo entonces ???? EVIDENTEMENTE lo necesitamos...
            Operators.GREATER: {
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'char': 'err'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'char': 'err'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'err'
                }
            },

            Operators.LESS: {
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'char': 'err'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'char': 'err'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'err'
                }
            },

            Operators.ISEQUAL: {
                'int': {
                    'int': 'bool',
                    'float': 'bool',
                    'char': 'err'
                },
                'float': {
                    'int': 'bool',
                    'float': 'bool',
                    'char': 'err'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'err'
                }
            },

            Operators.AND: {
                'int': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'err'
                },
                'float': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'err'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'err'
                }
            },

            Operators.OR: {
                'int': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'err'
                },
                'float': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'err'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'err'
                }
            },
            Operators.NOT_EQUAL: {
                'int': {
                    'int': 'bool',
                    'float': 'err',
                    'char': 'err'
                },
                'float': {
                    'int': 'err',
                    'float': 'bool',
                    'char': 'err'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'bool'
                }
            },
            Operators.EQUAL: {
                'int': {
                    'int': 'int',
                    'float': 'int',
                    'char': 'err'
                },
                'float': {
                    'int': 'float',
                    'float': 'float',
                    'char': 'err'
                },
                'char': {
                    'int': 'err',
                    'float': 'err',
                    'char': 'char'
                }
            },

        }

    def semantics(self, left_type, right_type, operator):
        '''
        Will determine if given two types of variables and an operator, the operation will be valid or not
        :param left_type: type of left variable of operation
        :param right_type: type of right variable of operation
        :param operator: operator given for the operation
        '''
        if 'err' not in self.semantic_cube[left_type][right_type][operator]:
            return self.semantic_cube[left_type][right_type][operator]
        raise TypeError("Unable to apply operator {} to types {} and {}".format(
            operator, left_type, right_type))


# https://docs.python.org/3/library/enum.html
