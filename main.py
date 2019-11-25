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
        print(f"Leyendo archivo {nombreArchivo}...\n")
        info = arch.read()
        arch.close()

        if(parser.yacc.parse(info, tracking=True) == 'PROGRAM COMPILED'):
            print("SINTAXIS VALIDA :) ")
        else:
            print("ERRORES EN LA SINTAXIS :( ")
    
    except FileNotFoundError:
        print(f"No se encontró el archivo {nombreArchivo}.")

    except EOFError:
        print(EOFError)
