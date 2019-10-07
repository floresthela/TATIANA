import sys
import ply.yacc as yacc
from lexer import tokens

# PROGRAM - flor
def p_program(p):
    '''
    programa: PROGRAM ID SEMICOLON program1 program2 star
    '''

def p_program1(p):
    '''
    program1: VAR 
            | empty
    '''

def p_program2(p):
    '''
    program2: function program2 
            | empty
    '''
# STAR - flor
def p_star(p):
    '''
    star: MULTIPLICATION OPENBRACES vars star1 CLOSEBRACES
    '''

def p_star1(p):
    '''
    star1: stmt star1 
        | empty
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
    vars: VARS type ID vars1 SEMICOLON
    '''

def p_vars1(p):
    '''
    vars1: EQUALS expression vars2
        | OPENBRACKET CTEINT CLOSEBRACKET vars3  
    '''

def p_vars2(p):
    '''
    vars2: COMMA ID vars1 vars2
        | empty
    '''

def p_vars3(p):
    '''
    vars3: OPENBRACKET CTEINT CLOSEBRACKET
        | empty
    '''

# TYPE - flor
def p_type(p):
    '''
    type: INT 
        | FLOAT
        | CHAR
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
def p_vcte(p):
    '''
    vcte: cte
        | ID vcte1 vcte2
    '''

def p_vcte1(p):
    '''
    vcte1: OPENBRACKET expression CLOSEBRACKET vcte3
    '''

def p_vcte2(p):
    '''
    vcte2: OPENPAREN expression vcte4
        | empty
    '''

def p_vcte3(p):
    '''
    vcte3: OPENBRACKET expression CLOSEBRACKET
        | empty
    
    '''

def p_vcte4(p):
    '''
    vcte4: COMMA expression vcte4
        | empty
    '''
# CTE - flor
def p_cte(p):
    '''
    cte: CTEINT
        | CTEFLOAT
        | CTECHAR
    '''
# EXPRESSION - flor
def p_expression(p):
    '''
    expression: vcte
              | operation
    '''
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
# GRAPH_STMT - flor
def graphstmt(p):
    '''
    graphstmt: graphfig
             | graphview
             | graphmove
    '''
# GRAPH_FIGURE - flor
def p_graphfig(p):
    '''
    graphfig: graphfig1 expression SEMICOLON
    '''

def p_graphfig1(p):
    '''
    graphfig1: CIRCLE
            | SQUARE
            | TRIANGLE expression
            | RECTANGLE expression
    '''

# GRAPH_MOVEMENT - flor

def p_graphmove(p):
    '''
    graphmove: graphmove1 SEMICOLON
    '''
def p_graphmove1(p):
    '''
    graphmove1: HAND_DOWN
              | HAND_UP 
              | graphmove2 expression 
    '''
def p_graphmove2(p):
    '''
    graphmove2: GO
              | LEFT
              | RIGHT
              | BACK
              | ARC expression
    '''

# GRAPH_REPEAT - flor
def p_graphr(p):
    '''
    graphr: REPEAT expression OPENBRACES graphstmt graphr1 CLOSEBRACES
    '''
def p_graphr1(p):
    '''
    graphr1: graphstmt graphr1 
           | empty
    '''
# GRAPH_VIEW - flor
def p_graphview(p):
    '''
    graphview: graphview1 SEMICOLON
    '''
def p_graphview1(p):
    '''
    graphview1: HIDE_STAR
              | SHOW_STAR
              | graphview2 expression
    '''
def p_graphview2(p):
    '''
    graphview2: SETXY expression
              | COLOR_STAR
              | SIZE_STAR
    '''
# OPERATION
# FACTOR
# TERM