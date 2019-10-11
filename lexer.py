
# TATIANA
# Flor Esthela Barbosa & Laura Santacruz

# LEXER

import sys
import ply.lex as lex

# list of reserved words
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'print' : 'PRINT',
    'program' : 'PROGRAM',
    'vars' : 'VARS',
    'int': 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'fun' : 'FUN',
    'or' : 'OR',
    'and' : 'AND',
    'read' : 'READ',
    'while' : 'WHILE',
    'circle': 'CIRCLE',
    'square': 'SQUARE',
    'triangle': 'TRIANGLE',
    'rectangle': 'RECTANGLE',
    'hand_down': 'HAND_DOWN',
    'hand_up': 'HAND_UP',
    'go': 'GO',
    'left': 'LEFT',
    'right': 'RIGHT',
    'back': 'BACK',
    'arc': 'ARC',
    'repeat': 'REPEAT',
    'hide_star': 'HIDE_STAR',
    'show_star':'SHOW_STAR',
    'setXY': 'SETXY',
    'color_star': 'COLOR_STAR',
    'size_star': 'SIZE_STAR',
    'return': 'RETURN',
    'void': 'VOID',
    'for': 'FOR'
}

# tokens list
tokens = [
    'ID', 'COMMA', 'EQUALS',
    'OPENPAREN', 'CLOSEPAREN', 'TWODOTS',
    'MULTIPLICATION', 'OPENBRACES', 'CLOSEBRACES',
    'ADDITION', 'SUBSTRACTION', 'DIVISION', 'CTEINT', 'CTEFLOAT',
    'CTECHAR', 'GREATER', 'LESS', 'NOTEQUAL', 'SEMICOLON',
    'OPENBRACKET', 'CLOSEBRACKET', 'ISEQUAL'
] + list(reserved.values())


# tokens definition
t_ADDITION = r'\+'
t_COMMA = r'\,'
t_EQUALS = r'\='
t_OPENPAREN = r'\('
t_CLOSEPAREN = r'\)'
t_TWODOTS = r'\:'
t_MULTIPLICATION = r'\*'
t_OPENBRACES = r'\{'
t_CLOSEBRACES = r'\}'
t_SUBSTRACTION = r'\-'
t_DIVISION = r'\/'
t_GREATER = r'\>'
t_LESS = r'\<'
t_NOTEQUAL = r'\!='
t_SEMICOLON = r'\;'
t_OPENBRACKET = r'\['
t_CLOSEBRACKET = r'\]'
t_ISEQUAL = r'\=='

t_ignore = r' '

def t_CTEINT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_CTEFLOAT(t):
     r'\d+\.\d+'
     t.value = float(t.value)
     return t

def t_CTECHAR(t):
    r'^\w{1}$'
    t.value = str(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex()
