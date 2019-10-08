import sys
import ply.yacc as yacc
from lexer import tokens


# PROGRAM - flor
def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON program1 program2 star
    '''
    p[0] = "PROGRAM COMPILED"


def p_program1(p):
    '''
    program1 : VAR
            | empty
    '''


def p_program2(p):
    '''
    program2 : function program2
            | empty
    '''


# STAR - flor
def p_star(p):
    '''
    star : MULTIPLICATION OPENBRACES vars star1 CLOSEBRACES
    '''


def p_star1(p):
    '''
    star1 : stmt star1
        | empty
    '''


# LOOP - flor
def p_loop(p):
    '''
    loop : while
        | for
    '''


# STMT - flor
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


# VARS - flor
def p_vars(p):
    '''
    vars : VAR type ID vars1 SEMICOLON
    '''


def p_vars1(p):
    '''
    vars1 : EQUALS expression vars2
        | OPENBRACKET CTEINT CLOSEBRACKET vars3
    '''


def p_vars2(p):
    '''
    vars2 : COMMA ID vars1 vars2
        | empty
    '''


def p_vars3(p):
    '''
    vars3 : OPENBRACKET CTEINT CLOSEBRACKET
        | empty
    '''


# TYPE - flor
def p_type(p):
    '''
    type : INT
        | FLOAT
        | CHAR
    '''


# PRINT - flor
def p_print(p):
    '''
    print : PRINT OPENPAREN expression CLOSEPAREN SEMICOLON
    '''


# READ - LAURA
def p_read(p):
    '''
    read : READ OPENPAREN ID read1 CLOSEPAREN SEMICOLON
    '''


def p_read1(p):
    '''
    read1 : OPENBRACKET expression CLOSEBRACKET OPENBRACKET expression CLOSEBRACKET
              | OPENBRACKET expression CLOSEBRACKET
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
    assignment2 : OPENBRACKET expression CLOSEBRACKET
    '''


def p_assignment3(p):
    '''
    assignment3 : expression
                | read
    '''


# VAR_CTE - flor
def p_vcte(p):
    '''
    vcte : cte
        | ID vcte1 vcte2
    '''


def p_vcte1(p):
    '''
    vcte1 : OPENBRACKET expression CLOSEBRACKET vcte3
    '''


def p_vcte2(p):
    '''
    vcte2 : OPENPAREN expression vcte4
        | empty
    '''


def p_vcte3(p):
    '''
    vcte3 : OPENBRACKET expression CLOSEBRACKET
        | empty

    '''


def p_vcte4(p):
    '''
    vcte4 : COMMA expression vcte4
        | empty
    '''


# CTE - flor
def p_cte(p):
    '''
    cte : CTEINT
        | CTEFLOAT
        | CTECHAR
    '''


# EXPRESSION - flor
def p_expression(p):
    '''
    expression : vcte
              | operation
              | empty
    '''


# RETURN - LAURA
def p_return(p):
    '''
    return : RETURN return1 SEMICOLON
    '''


def p_return1(p):
    '''
    return1 : vcte
            | operation
    '''


# COMPARE - LAURA
def p_compare(p):
    '''
    compare : expression loper expression
    '''


# L_OP - LAURA
def p_loper(p):
    '''
    loper : GREATER
          | LESS
          | NOTEQUAL
          | ISEQUAL
    '''


# LOGICAL - LAURA
def p_logical(p):
    '''
    logical : compare logical1 compare
    '''


def p_logical1(p):
    '''
    logical1 : OR
                 | AND
    '''


# CONDITION --LAURA
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


# HEAD --laura
def p_head(p):
    '''
    head : OPENPAREN head1 CLOSEPAREN
    '''


def p_head1(p):
    '''
    head1 : compare
              | logical
    '''


# BODY --LAURA
def p_body(p):
    '''
    body : OPENBRACES body1 CLOSEBRACES
    '''

def p_body1(p):
    '''
    body1 : stmt body1
          | empty
    '''


# FOR -LAURA
def p_for(p):
    '''
    for : FOR OPENPAREN ID TWODOTS expression CLOSEPAREN body
    '''


# WHILE
def p_while(p):
    '''
    while : WHILE  head body
    '''


# FUN_CALL - LAURA
def p_funCall(p):
    '''
    funCall : ID OPENPAREN expression CLOSEPAREN SEMICOLON
    '''


# FUNCTION - laura
def p_function(p):
    '''
    function : FUN function1 ID function2 OPENBRACES vars function4 CLOSEBRACES
    '''


def p_function1(p):
    '''
    function1 : type
              | VOID
    '''


def p_function2(p):
    '''
    function2 : OPENPAREN function3 CLOSEPAREN
    '''


def p_function3(p):
    '''
    function3 : type ID
              | function3 COMMA
              | empty
    '''


def p_function4(p):
    '''
    function4 : stmt function4
              | empty
    '''


# GRAPH_STMT - flor
def p_graphstmt(p):
    '''
    graphstmt : graphfig
             | graphview
             | graphmove
    '''


# GRAPH_FIGURE - flor
def p_graphfig(p):
    '''
    graphfig : graphfig1 expression SEMICOLON
    '''


def p_graphfig1(p):
    '''
    graphfig1 : CIRCLE
            | SQUARE
            | TRIANGLE expression
            | RECTANGLE expression
    '''

# GRAPH_MOVEMENT - flor


def p_graphmove(p):
    '''
    graphmove : graphmove1 SEMICOLON
    '''


def p_graphmove1(p):
    '''
    graphmove1 : HAND_DOWN
              | HAND_UP
              | graphmove2 expression
    '''


def p_graphmove2(p):
    '''
    graphmove2 : GO
              | LEFT
              | RIGHT
              | BACK
              | ARC expression
    '''



# GRAPH_REPEAT - flor
def p_graphr(p):
    '''
    graphr : REPEAT expression OPENBRACES graphstmt graphr1 CLOSEBRACES
    '''


def p_graphr1(p):
    '''
    graphr1 : graphstmt graphr1
           | empty
    '''


# GRAPH_VIEW - flor
def p_graphview(p):
    '''
    graphview : graphview1 SEMICOLON
    '''


def p_graphview1(p):
    '''
    graphview1 : HIDE_STAR
              | SHOW_STAR
              | graphview2 expression
    '''
def p_graphview2(p):
    '''
    graphview2 : SETXY expression
              | COLOR_STAR
              | SIZE_STAR
    '''


# OPERATION
def p_operation(p):
    '''
    operation : term operation1
    '''


def p_operation1(p):
    '''
    operation1 : ADDITION
               | SUBSTRACTION
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
            | OPENPAREN compare CLOSEPAREN
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
    term1 : MULTIPLICATION
          | DIVISION
          | empty
    '''


def p_empty(p):
    '''empty :'''


def p_error(p):
    print("ERROR {}".format(p))


yacc.yacc()


if __name__ == '__main__':
    try:
        nombreArchivo = 'prueba1.txt'
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
