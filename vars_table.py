'''
TATIANA
Archivo para el diseño del directorio de funciones y sus tablas de variables

Flor Esthela Barbosa y Laura Santacruz
'''


class VarsTable:
    '''
    Clase para la generación del directorio de funciones con la tabla de variables de cada una así como las funciones asociadas para la manipulación del directorio correspondiente
    '''

    def __init__(self):
        self.table = {
            'global': {
                'program': '',
                'vars': {},
                # [vars,temps]
                # 'size': {'i':[0,0],'f':[0,0],'s':[0,0],'b':[0,0]},
            },
            'star': {
                'type': 'void',
                'vars': {},
                'begin': None,
                # [vars,temps]
                # 'size': {'i':[0,0],'f':[0,0],'s':[0,0],'b':[0,0]},
            }
        }
        self.current_type = ''
        self.current_scope = 'global'
        self.initialized = False

    def FunDirectory(self, fun_id, type, start):
        # print(self.table)
        '''
        Create main directory to store all functions created on a program, current scope is global
        : param fun_id: Nombre del programa, función creada por usuario o star (main)
        : param type: Tipo de la función (programa = np, star = void)
        '''

        if type == 'np':
            self.current_scope = 'global'
            self.current_type = type
            self.table['global']['program'] = fun_id

        elif type == 'star':
            self.current_scope = 'star'
            self.current_type = type
            self.table['star']['begin'] = start

        elif fun_id not in self.table:
            vt_name = 'vars-' + fun_id
            self.table[fun_id] = {
                'type': type,
                'vars': {},
                'params': [],
                'begin': start,
            }
            self.current_scope = fun_id
            self.current_type = type
        else:
            raise TypeError(f'Función {fun_id} ya fue declarada')
        self.initialized = True


    def insert_var(self, var_id, var_type, dir, b_dim, dim):
        '''
        Agrega nueva variable a la tabla de variables del scope actual.
        :param var_id: Nombre de variable
        :param var_type: Tipo de la variable
        :param dir: Dirección asignada a la variable
        :param b_dim: Booleano si es dimensionada
        :param dim: Tamaño de la variable dimensionada
        '''
        scope = self.current_scope

        # Función declarada por el usuario
        if var_id not in self.table[scope]['vars'] and var_id not in self.table['global']['vars'] and scope != 'global' and scope != 'star' and var_id not in self.table[scope]['params']:
            new_var = {
                'id': var_id,
                'type': var_type,
                'dir': dir,
                'esdimensionada': b_dim,
                'var_dim':dim
            }
            self.table[scope]['vars'][var_id] = new_var

        # Global o main
        elif var_id not in self.table[scope]['vars'] and var_id not in self.table['global']['vars'] and (scope == 'global' or scope == 'star'):
            new_var = {
                'id': var_id,
                'type': var_type,
                'dir': dir,
                'esdimensionada':b_dim,
                'var_dim':dim
            }
            self.table[scope]['vars'][var_id] = new_var

        else:
            raise TypeError(f'Variable {var_id} ya fue declarada')


    def insert_param(self,param_id,param_type):
        scope = self.current_scope
        if param_id not in self.table[scope]['params'] and param_id not in self.table['global']['vars']:
            self.table[scope]['params'].append(param_type)
        else:
            raise TypeError(f'Parametro {param_id} ya fue declarado')

    def search_var(self, var_id):
        '''
        Search of variables function to detect multiple declaration of same id on a specific scope
        :param var_id: Name of the variable to be searched
        '''
        scope = self.current_scope
        if var_id in self.table[scope]['vars']:
            return self.table[scope]['vars'][var_id]
        elif var_id in self.table['global']['vars']:
            return self.table['global']['vars'][var_id]
        else:
            raise TypeError(f"Variable {var_id} no ha sido declarada")

    def delete_vars(self, table_id):
        '''
        Remove a vars table after function is no longer needed
        : param table_id: Name assigned to the function
        '''
        if table_id in self.table:
            del self.table[table_id]['vars']
        else:
            raise TypeError(f"Tabla de variables para {table_id} no se encontró")

