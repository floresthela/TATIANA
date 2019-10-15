
# TATIANA
# Flor Esthela Barbosa & Laura Santacruz

# VARS AND PROCEDURES TABLES

import pandas as pd


class VarsTable:
    '''
    VarsTable contains all functions for creating and manipulating functions
    and its variables inside the corresponding table
    and main directory (FunDirectory)
    '''

    def __init__(self):
        self.table = ''
        self.current_type = ''
        self.current_scope = ''
        self.initialized = False

    def initialize(self):
        self.table = {
            'global': {
                'type': 'void',
                'vars': {}
            }
        }

        # hacemos otra tabla tambien para funcion star ?

        self.current_type = ''
        self.current_type = self.table['global']['type']
        self.initialized = True

# agregar var - insert
    def insertVar(self, variable):
        if variable not in self.data:
            self.data = variable

# crear tabla
    def createFunDir(self, type, scope):
        self.columns = type
# search
