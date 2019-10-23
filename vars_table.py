
# TATIANA
# Flor Esthela Barbosa & Laura Santacruz

# VARS AND PROCEDURES TABLES


class VarsTable:
    '''
    Class for the variables table which contains all functions for creating and manipulating functions and its variables inside the corresponding table and main directory (FunDirectory)
    '''

    def __init__(self):
        self.table = {
            'global': {
                'program': '',
                'vars': {}
            },
            'star': {
                'type':'void',
                'vars' : {}
            }
        }
        self.current_type = ''
        self.current_scope = 'global'
        self.initialized = False

    def FunDirectory(self, fun_id, type):
        '''
        Create main directory to store all functions created on a program, current scope is global
        : param fun_id: Nombre del programa, función creada por usuario o star (main)
        : param type: Tipo de la función (programa = np, star = void)
        '''


        if type == 'np':
            self.current_scope = 'global'
            self.current_type = ''
            self.table['global']['program'] = fun_id

        elif type == 'star':
            self.current_scope = 'star'
            self.current_type = type


        elif fun_id not in self.table:
            vt_name = 'vars-' + fun_id
            #print(vt_name)
            self.table[fun_id] = {
                'type': type,
                'vars': {},
                'params': {}
            }
            self.current_scope = fun_id
            self.current_type = type
        else:
            raise TypeError(f'Function {fun_id} already declared')

        self.initialized = True
        print(self.table)


    def insert_var(self, var_id, var_type):
        scope = self.current_scope
        if var_id not in self.table[scope]['vars'] and var_id not in self.table['global']['vars']:
            new_var = {
                'id' : var_id,
                'type' : var_type,
            }
            # podríamos cambiar en lugar de var_id ponerle un id como fun1-vf1, fun1-vf2, fun2-vi1, etc idk
            self.table[scope]['vars'][var_id] = new_var

        else:
            raise TypeError(f'Variable {var_id} already declared')

        # print(self.table)

    # def create_table(self, table_id, fun_type):
    #     '''
    #     Create a vars table for declared functions on program
    #     : param table_id: Name assigned to the function
    #     : param fun_type: Return value of the function
    #     '''

    #     if table_id not in self.table:
    #         new_table = {
    #                 'type' : fun_type,
    #                 'vars' : {},
    #                 'params' : {}
    #         }

    #         self.table[table_id] = new_table
    #         self.current_scope = self.table[table_id]
    #     else:
    #         raise TypeError('Function has already been declared ', table_id)


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