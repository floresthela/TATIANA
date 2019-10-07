import sys
import ply.lex as lex

# list of reserved words
reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'print' : 'PRINT',
    'program' : 'PROGRAM',
    'var' : 'VAR',
    'int': 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'fun' : 'FUN',
    'or' : 'OR',
    'and' : 'AND',
    'read' : 'READ',
    'while' : 'WHILE'
}

# tokens list
tokens = [
    'id', 'dot', 'comma', 'equals',
    'openParen', 'closedParen', 'twoDots',
    'multiply', 'openBraces', 'closedBraces',
    'plus', 'minus', 'division', 'cteint', 'ctefloat',
    'ctechar', 'greater', 'less', 'notEqual'
] + list(reserved.values())


# tokens definition
t_plus = r'\+'
t_dot = r'\.'
t_comma = r'\,'
t_equals = r'\,'
t_openParen = r'\('
t_closedParen = r'\)'
t_twoDots = r'\:'
t_multiply = r'\*'
t_openBraces = r'\{'
t_closedBraces = r'\}'
t_minus = r'\-'
t_division = r'\/'
t_greater = r'/>'
t_less = r'/<'
t_notEqual = r'/!='

t_ignore = r' '

def t_cteint(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ctefloat(t):
     r'\d+\.\d+'
     t.value = float(t.value)
     return t


def t_ctechar(t):
    r'[a-zA-Z][a-zA-Z_0-9]'
    t.value = str(t.value)
    return t

def t_id(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'id')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

    lexer = lex.lex()