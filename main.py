'''
TATIANA

Archivo main para utilizar el parser y semántica dado un archivo del lenguaje TATIANA

Flor Esthela Barbosa y Laura Santacruz
'''
import sys
import parser
import json
from vars_table import VarsTable
from intermediate_code_generation import Intermediate_CodeGeneration

vars_t = VarsTable()
cg = Intermediate_CodeGeneration()

if __name__ == '__main__':
    
    args = sys.argv[1:]
    nombreArchivo = args[0] 
    
    try:
        path = 'pruebas/'

        path += nombreArchivo
        arch = open(path, 'r')
        info = arch.read()
        arch.close()

        if(parser.yacc.parse(info, tracking=True) == 'PROGRAM COMPILED'):
            print(f"Archivo {nombreArchivo} fue compilado")
        else:
            print("Errores en compilación")
    
    except FileNotFoundError:
        print(f"No se encontró el archivo {nombreArchivo}.")

    except EOFError:
        print(EOFError)
