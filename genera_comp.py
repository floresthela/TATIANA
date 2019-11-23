'''
TATIANA
Archivo para la generación de un archivo json de la información de la compilación

Flor Esthela Barbosa y Laura Santacruz
'''
import sys
import json
from maquina_virtual import MaquinaVirtual

def genera_arch(program,varst,quads,consts):
    '''
    Genera el archivo con los cuádruplos, tablas de funciones y constantes del programa
    '''
    archivo_comp = {
        "Quads" : quads,
        "FunDir" : varst,
        "tConstantes": consts
    }

    with open(f'pruebas/{program}_comp.ta', 'w') as nuevo_arch:
        json.dump(archivo_comp,nuevo_arch, separators = (',',':'))


    # manda datos a máquina virtual
    MaquinaVirtual().agarra_datos(program)

