'''
TATIANA
Archivo main para utilizar el parser y semántica dado un archivo del lenguaje

Flor Esthela Barbosa y Laura Santacruz
'''
import sys
import parser
import genera_comp
import json
from vars_table import VarsTable
from intermediate_code_generation import Intermediate_CodeGeneration


vars_t = VarsTable()
cg = Intermediate_CodeGeneration()

if __name__ == '__main__':
    try:
        path = 'pruebas/'
        nombreArchivo = 'prueba7.tati'
        path += nombreArchivo
        arch = open(path, 'r')
        print(f"Leyendo archivo {nombreArchivo}...")
        info = arch.read()
        arch.close()
        
        if(parser.yacc.parse(info, tracking=True) == 'PROGRAM COMPILED'):
            print("SINTAXIS VALIDA :) ")
        else:
            print("ERRORES EN LA SINTAXIS :( ")

        
        

    except EOFError:
        print(EOFError)