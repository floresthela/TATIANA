
# TATIANA
# Flor Esthela Barbosa & Laura Santacruz

# SEMANTIC CUBE

import sys
from enum import Enum


class Operators(Enum):
    ADDITION = '+'
    SUBSTRACTION = '-'
    MULTIPLICATION = '*'
    DIVISION = '/'
    GREATER = '>'
    LESS = '<'
    ISEQUAL = '=='
    AND = 'and'
    OR = 'or'


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

        }



# https://docs.python.org/3/library/enum.html
