'''
TATIANA
Archivo para la generación de un archivo json de la información de la compilación

Flor Esthela Barbosa y Laura Santacruz
'''
import sys
import json

def genera_arch(program,varst,quads,consts):
    '''
    Genera el archivo con los cuádruplos, tablas de funciones y constantes del programa
    '''
    archivo = {
        "Quads" : quads,
        "FunDir" : varst,
        "tConstantes": consts
    }
    with open(f'pruebas/{program}.ta*', 'w') as nuevo_arch:
        json.dump(archivo,nuevo_arch, separators = (',',':'))

