import sys
import ply.yacc as yacc
from lexer import tokens

# PROGRAM - flor
def p_program(p):
    '''
    programa: PROGRAM ID 
    '''
# STAR - flor
def p_star(p):
    '''

    '''
# LOOP - flor
def p_loop(p):
    '''
    loop: while
        | for
    '''

# STMT - flor
def p_stmt(p):
    '''
    stmt: assignment
        | condition
        | print
        | loop
        | read
        | graph_stmt
        | graph_repeat
        | fun_call
        | repeat
    '''
# VARS - flor
def p_vars(p):
    '''
    '''

# TYPE - flor
def p_type(p):
    '''
    '''
# PRINT - flor
def p_print(p):
    '''
    print: PRINT OPENPAREN expression CLOSEPAREN SEMICOLON
    '''
# READ
def p_read(p):
    '''
    '''
# ASSIGNMENT
# VAR_CTE - flor
# CTE - flor
# EXPRESSION - flor
# RETURN 
# COMPARE 
# L_OP


# LOGICAL
# CONDITION
# HEAD  
# BODY
# FOR
# WHILE
# FUN_CALL
# FUNCTION
# GRAPH_FIGURE - flor
# GRAPH_MOVEMENT - flor
# GRAPH_REPEAT - flor
# GRAPH_VIEW - flor
# OPERATION
# FACTOR
# TERM