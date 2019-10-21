
# TATIANA
# Flor Esthela Barbosa & Laura Santacruz

# PARSER

import sys
import ply.yacc as yacc
from lexer import tokens


# PROGRAM
def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON program1 program2 star
    '''
    p[0] = "PROGRAM COMPILED"

def p_program1(p):
    '''
    program1 : vars
            | empty
    '''

def p_program2(p):
    '''
    program2 : function program2
            | empty
    '''

# STAR
def p_star(p):
    '''
    star : MULTIPLICATION OPENBRACES star2 star1 CLOSEBRACES
    '''


def p_star1(p):
    '''
    star1 : stmt star1
        | empty
    '''

def p_star2(p):
    '''
    star2 : vars
          | empty
    '''


# LOOP
def p_loop(p):
    '''
    loop : while
        | for
    '''


# STMT
def p_stmt(p):
    '''
    stmt : assignment
        | condition
        | print
        | loop
        | read
        | graphstmt
        | graphr
        | funCall
        | return
    '''


#VARS
def p_vars(p):
    '''
    vars : VARS type ID vars1 SEMICOLON
    '''


def p_vars1(p):
    '''
    vars1 : EQUALS exp vars2
        | OPENBRACKET CTEINT CLOSEBRACKET vars3
        | empty vars2
    '''


def p_vars2(p):
    '''
    vars2 : COMMA ID vars1
          | COMMA vars4
          | empty
    '''


def p_vars3(p):
    '''
    vars3 : OPENBRACKET CTEINT CLOSEBRACKET
        | empty
    '''


def p_vars4(p):
    '''
    vars4 : type ID vars1
          | empty
    '''


# TYPE
def p_type(p):
    '''
    type : INT
         | FLOAT
         | CHAR
    '''


# PRINT
def p_print(p):
    '''
    print : PRINT OPENPAREN exp CLOSEPAREN SEMICOLON
    '''

# READ
def p_read(p):
    '''
    read : READ OPENPAREN ID read1 CLOSEPAREN SEMICOLON
    '''


def p_read1(p):
    '''
    read1 : OPENBRACKET exp CLOSEBRACKET OPENBRACKET exp CLOSEBRACKET
              | OPENBRACKET exp CLOSEBRACKET
              | empty
    '''


# ASSIGNMENT -LAURA
def p_assignment(p):
    '''
    assignment : ID assignment1 EQUALS assignment3 SEMICOLON
    '''



def p_assignment1(p):
    '''
    assignment1 : assignment2
                | assignment2 assignment1
                | empty
    '''



def p_assignment2(p):
    '''
    assignment2 : OPENBRACKET exp CLOSEBRACKET
    '''



def p_assignment3(p):
    '''
    assignment3 : exp
                | read
    '''



# VAR_CTE
def p_vcte(p):
    '''
    vcte : cte
        | ID vcte1
        | funCall
    '''
    p[0] = p[1]
    print(p[0])


def p_vcte1(p):
    '''
    vcte1 : OPENBRACKET exp CLOSEBRACKET vcte3
          | empty
    '''

def p_vcte3(p):
    '''
    vcte3 : OPENBRACKET exp CLOSEBRACKET
        | empty

    '''

# CTE
def p_cte(p):
    '''
    cte : CTEINT
        | CTEFLOAT
        | CTECHAR
    '''

# RETURN
def p_return(p):
    '''
    return : RETURN return1 SEMICOLON
    '''


def p_return1(p):
    '''
    return1 : vcte
            | exp
    '''


# expression
def p_expression(p):
    '''
    expression : exp expression1
    '''


def p_expression1(p):
    '''
    expression1 : loper exp
             | empty
    '''


# L_OP
def p_loper(p):
    '''
    loper : GREATER
          | LESS
          | NOTEQUAL
          | ISEQUAL
    '''


# LOGICAL
def p_logical(p):
    '''
    logical : expression logical1 expression
    '''


def p_logical1(p):
    '''
    logical1 : OR
             | AND
    '''


# CONDITION
def p_condition(p):
    '''
    condition : IF head body condition1
    '''


def p_condition1(p):
    '''
    condition1 : ELSEIF head body condition1
               | ELSE body
               | empty
    '''


# HEAD
def p_head(p):
    '''
    head : OPENPAREN head1 CLOSEPAREN
    '''


def p_head1(p):
    '''
    head1 : expression
          | logical
    '''

# BODY
def p_body(p):
    '''
    body : OPENBRACES body1 CLOSEBRACES
    '''

def p_body1(p):
    '''
    body1 : stmt body1
          | empty
    '''


# FOR
def p_for(p):
    '''
    for : FOR OPENPAREN ID TWODOTS exp CLOSEPAREN body
    '''


# WHILE
def p_while(p):
    '''
    while : WHILE  head body
    '''


# FUN_CALL
def p_funCall(p):
    '''
    funCall : ID OPENPAREN funCall2 CLOSEPAREN SEMICOLON
    '''


def p_funCall2(p):
    '''
    funCall2 : exp funCall3
             | empty
    '''

def p_funCall3(p):
    '''
    funCall3 : COMMA exp funCall2
             | empty
    '''

# FUNCTION
def p_function(p):
    '''
    function : FUN function1 ID function2 OPENBRACES function6 function4 CLOSEBRACES
    '''

def p_function1(p):
    '''
    function1 : type
              | VOID
    '''

# valor que regresa el llamado a una función
# a = fun1(1,3)

def p_function2(p):
    '''
    function2 : OPENPAREN function3 CLOSEPAREN
    '''

def p_function3(p):
    '''
    function3 : type ID function5
              | empty
    '''

def p_function4(p):
    '''
    function4 : stmt function4
              | empty
    '''
def p_function5(p):
    '''
    function5 : COMMA type ID function3
    '''

def p_function6(p):
    '''
    function6 : vars
              | empty
    '''


def p_laRegla(p):
    '''
    laRegla : OPENPAREN exp COMMA exp CLOSEPAREN
    '''


def p_laRegla2(p):
    '''
    laRegla2 : OPENPAREN exp CLOSEPAREN
    '''


# GRAPH_STMT
def p_graphstmt(p):
    '''
    graphstmt : graphfig
             | graphview
             | graphmove
    '''

# GRAPH_FIGURE
def p_graphfig(p):
    '''
    graphfig : graphfig1 SEMICOLON
    '''

def p_graphfig1(p):
    '''
    graphfig1 : CIRCLE laRegla2
            | SQUARE laRegla2
            | TRIANGLE laRegla
            | RECTANGLE laRegla
    '''

# GRAPH_MOVEMENT
def p_graphmove(p):
    '''
    graphmove :  graphmove1  SEMICOLON
    '''

def p_graphmove1(p):
    '''
    graphmove1 : HAND_DOWN
              | HAND_UP
              | graphmove2
    '''

def p_graphmove2(p):
    '''
    graphmove2 : GO laRegla2
              | LEFT laRegla2
              | RIGHT laRegla2
              | BACK laRegla2
              | ARC laRegla
    '''

# GRAPH_REPEAT
def p_graphr(p):
    '''
    graphr : REPEAT exp OPENBRACES graphstmt graphr1 CLOSEBRACES
    '''

def p_graphr1(p):
    '''
    graphr1 : graphstmt graphr1
           | empty
    '''

# GRAPH_VIEW
def p_graphview(p):
    '''
    graphview : graphview1 SEMICOLON
    '''

def p_graphview1(p):
    '''
    graphview1 : HIDE_STAR
              | SHOW_STAR
              | graphview2 exp
    '''

def p_graphview2(p):
    '''
    graphview2 : SETXY graphview3
              | COLOR_STAR
              | SIZE_STAR
    '''

def p_graphview3(p):
    '''
    graphview3 : exp COMMA
              | laRegla
    '''

# exp
def p_exp(p):
    '''
    exp : term exp1
    '''

def p_exp1(p):
    '''
    exp1 : ADDITION exp
               | SUBSTRACTION exp
               | empty
    '''

# FACTOR
def p_factor(p):
    '''
    factor : vcte
           | factor1
    '''

def p_factor1(p):
    '''
    factor1 : factor2 vcte
            | OPENPAREN expression CLOSEPAREN
    '''

def p_factor2(p):
    '''
    factor2 : ADDITION
            | SUBSTRACTION
    '''

# TERM
def p_term(p):
    '''
    term : factor term1
    '''


def p_term1(p):
    '''
    term1 : MULTIPLICATION term
          | DIVISION term
          | empty
    '''


def p_empty(p):
    '''empty :'''

def p_error(p):
    print("ERROR {}".format(p))

yacc.yacc()


if __name__ == '__main__':
    try:
        nombreArchivo = 'pruebas/prueba6.txt'
        arch = open(nombreArchivo, 'r')
        print("Archivo a leer: " + nombreArchivo)
        info = arch.read()
        print(info)
        arch.close()
        if(yacc.parse(info, tracking=True) == 'PROGRAM COMPILED'):
            print("SINTAXIS VALIDA :) ")
        else:
            print("ERRORES EN LA SINTAXIS :( ")

    except EOFError:
        print(EOFError)
