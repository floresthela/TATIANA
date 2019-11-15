'''
TATIANA
Archivo para la memoria

Flor Esthela Barbosa y Laura Santacruz
'''

class Memoria:
    '''
    Clase para el manejo de las memorias global y locales
    '''

    self.mem_global = {}
    self.mem_local = {}
    self.mem_constantes = {}

    self.contador = 0
    self.record_acti = None

    def activa_funcion(self, fun, size):
        '''
        Agrega un módulo a la memoria de ejecución. 
        :param fun: Función en la que se hace el llamado a la función
        :param size: Tamaño de la función
        '''

        