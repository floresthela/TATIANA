
# TATIANA
# Flor Esthela Barbosa & Laura Santacruz

# VARS AND PROCEDURES TABLES


class VarsTable:
    '''
    Class for the variables table which contains all functions for creating and manipulating functions
    and its variables inside the corresponding table
    and main directory (FunDirectory)
    '''

    def __init__(self):
        self.table = None
        self.current_type = None
        self.current_scope = None
        self.initialized = False

    def FunDirectory(self):
        '''
        Create main directory to store all functions created on a program, current scope is global
        '''
        self.table = {
            'global': {
                'type': 'void',
                'vars': {}
            }
        }
        self.current_type = ''
        self.current_scope = self.table['global']
        self.initialized = True


    def insert_var(self, var_id, var_type):
        # podríamos agregar un id único como los ejemplos, a través de un contador dependiendo del tipo de var

        if var_id not in self.current_scope['vars'] and var_id not in self.table['global']['vars']:
            new_var = {
                'id' : var_id,
                'type' : var_type,

            }
            self.current_scope['vars'][var_id] = new_var
        else:
            raise TypeError('Variable already declared', var_id)


    def create_table(self, table_id, fun_type, params):
        '''
        Create a vars table for declared functions on program
        : param table_id: Name assigned to the function
        : param fun_type: Return value of the function
        '''

        if table_id not in self.table:
            new_table = {
                    'type' : fun_type,
                    'vars' : {},
                    'params' : {}
            }

            self.table[table_id] = new_table
            self.current_scope = self.table[table_id]
        else:
            raise TypeError('Function has already been declared ', table_id)


    def search_var(self, var_id):
        '''
        Search of variables function to detect multiple declaration of same id on a specific scope
        :param var_id: Name of the variable to be searched
        '''
        scope = self.current_scope

        if scope is None:
            return 0
        if var_id in scope['vars']:
            return scope['vars'][var_id]
        elif var_id in self.table['global']['vars']:
            return self.table['global']['vars'][var_id]
        else:
            raise TypeError(f"Variable' {var_id} has not been declared")

    def remove_table(self, table_id):
        '''
        Remove a vars table after function is no longer needed
        : param table_id: Name assigned to the function
        '''
        if table_id in self.table:
            del self.table[table_id]
        else:
            raise TypeError(f"Table of variables for {table_id} wasn't found")
