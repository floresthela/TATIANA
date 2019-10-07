import sys
import ply.lex as lex

reserved = {
    'if' : 'IF',
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'print' : 'PRINT',
    'program' : 'PROGRAM',
    'var' : 'VAR',
    'int': 'INT',
    'float' : 'FLOAT'
    'char' : 'CHAR',
    'fun' : 'FUN',
    'or' : 'OR',
    'and' : 'AND',
    'read' : 'READ',
    'while' : 'WHILE'
}

#lista de tokens
tokens = [
    'id', 'dot', 'comma', 'equals',
    'openParen', 'closedParen', 'twoDots',
    'multiply', 'openBraces', 'closedBraces',
    'plus', 'minus', 'division', 'cte_int', 'cte_float',
    'cte_char', 'greater_than', 'less_than', 'not_equal'
]
