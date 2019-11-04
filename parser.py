# TATIANA
# Flor Esthela Barbosa & Laura Santacruz

# PARSER
import sys
import ply.yacc as yacc
from lexer import tokens
from functools import reduce
from vars_table import VarsTable
from intermediate_code_generation import Intermediate_CodeGeneration

vars_t = VarsTable()
cg = Intermediate_CodeGeneration()

# PROGRAM
def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON declara_vars program2 star
    '''
    conta = 1
    # print(cg.Quads)
    for q in cg.Quads:
        print(conta,q)
        conta += 1

    p[0] = "PROGRAM COMPILED"

    vars_t.remove_table('global')

# def p_program_vars(p):
#     '''
#     program_vars : vars program_vars
#             | empty
#     '''
#     if len(p) == 3:
#         p[0] = p[1:]
#         p[0] = flatten(p[0])


def p_program2(p):
    '''
    program2 : function program2
            | empty
    '''
    if len(p) == 3:
        p[0] = p[1]
        # if p[2] != None:


# STAR
def p_star(p):
    '''
    star : starI declara_vars star1 CLOSEBRACES
    '''
    vars_t.remove_table('star')


def p_starI(p):
    '''
    starI : MULTIPLICATION OPENBRACES
    '''
    vars_t.FunDirectory('star', 'star')

def p_star1(p):
    '''
    star1 : stmt star1
        | empty
    '''


def p_declara_vars(p):
    '''
    declara_vars : vars declara_vars
          | empty
    '''
    if len(p) == 3:
        p[0] = p[1:]
        p[0] = flatten(p[0])


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
        | funCall SEMICOLON
        | return
    '''

    p[0] = p[1]


# FUNCTION

def p_functionI(p):
    '''
    functionI : type ID
              | VOID ID
    '''
    vars_t.FunDirectory(p[2],p[1])

def p_function(p):
    '''
    function : FUN functionI function2 inicia_fun declara_vars function4 termina_fun
    '''

    if p[7] != None:
        vars = p[7]
        vars = vars[:-1]
        p[0] = vars

    vars_t.remove_table(p[3])

# def p_function1(p):
#     '''
#     function1 : type
#               | VOID
#     '''
#     p[0] = p[1]


def p_inicia_fun(p):
    '''
    inicia_fun : OPENBRACES
    '''


def p_termina_fun(p):
    '''
    termina_fun : CLOSEBRACES
    '''

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
    if p[1] is not None:
        p[0] = p[1:]
        p[0] = flatten(p[0])


def p_function5(p):
    '''
    function5 : COMMA type ID function3
    '''


# def p_fun_vars(p):
#     '''
#     fun_vars : vars fun_vars
#               | empty
#     '''
#     if len(p) == 3:
#         p[0] = p[1:]
#         p[0] = flatten(p[0])
#
#         #list.pop(obj = list[-1])

# VARS
# al final hay que actualizar diagramas

def flatten(li):
    return sum(([x] if not isinstance(x, list) else flatten(x) for x in li), [])

def p_vars(p):
    '''
    vars : type ID vars1 equals exp SEMICOLON
         | type ID vars1 SEMICOLON
    '''
    p[0] = (p[1], p[2])

    if len(p) == 7:
        cg.PilaO.append(p[2])
        cg.PTypes.append(p[1])
        if cg.POper and cg.POper[-1] in '=':
            cg.generate_quad()
    if not vars_t.initialized:
        vars_t.FunDirectory('global', 'np')
        vars_t.insert_var(p[2],p[1])
    else:
        vars_t.insert_var(p[2],p[1])

# TODO: una regla para arreglos y usarla siempre que necesitemos [] , [][]
def p_vars1(p):
    '''
    vars1 : OPENBRACKET CTEINT CLOSEBRACKET vars3
        | empty
    '''

# matrix
def p_vars3(p):
    '''
    vars3 : OPENBRACKET CTEINT CLOSEBRACKET
        | empty
    '''


# TYPE
def p_type(p):
    '''
    type : INT
         | FLOAT
         | CHAR
    '''
    p[0] = p[1]


# PRINT
def p_print(p):
    '''
    print : PRINT OPENPAREN expression CLOSEPAREN SEMICOLON
    '''
    cg.POper.append('print')
    cg.generate_quad_print()

# READ
# qué pedo con el read?
def p_read(p):
    '''
    read : READ OPENPAREN id read1 CLOSEPAREN SEMICOLON
    '''
    cg.POper.append('read')
    cg.generate_quad_read()

# arreglo
def p_read1(p):
    '''
    read1 : OPENBRACKET exp CLOSEBRACKET OPENBRACKET exp CLOSEBRACKET
              | OPENBRACKET exp CLOSEBRACKET
              | empty
    '''

def p_equals(p):
    '''
    equals : EQUALS
    '''
    cg.POper.append(p[1])


# ASSIGNMENT

def p_id(p):
    '''
    id : ID
    '''
    p[0] = p[1]
    t = vars_t.search_var(p[1])
    if t:
        cg.PilaO.append(p[1])
        cg.PTypes.append(t['type'])

def p_assignment(p):
    '''
    assignment : id assignment1 equals assignment3 SEMICOLON
    '''
    # c = a + b; -> mete c a pilao



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
    p[0] = p[1]
    if cg.POper[-1] == '=':
        cg.generate_quad();

# VAR_CTE
def p_vcte(p):
    '''
    vcte : cte_int
         | cte_float
         | cte_char
         | id vcte1
         | funCall
    '''
    # 1. PilaO.Push(id.name)
    if len(p) == 2:
        cg.PilaO.append(p[1])


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
def p_cte_int(p):
    '''
    cte_int : CTEINT
    '''
    p[0] = p[1]
    cg.PTypes.append('int')

def p_cte_float(p):
    '''
    cte_float : CTEFLOAT
    '''
    p[0] = p[1]
    cg.PTypes.append('float')

def p_cte_char(p):
    '''
    cte_char : CTECHAR
    '''
    p[0] = p[1]
    cg.PTypes.append('char')

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
    p[0] = p[1]


# expression
def p_expression(p):
    '''
    expression : exp expression1
    '''

# POR QUÉ TENEMOS QUE PUEDE SER EMPTY ?? JAJA VERGA
def p_expression1(p):
    '''
    expression1 : loper exp
             | empty
    '''
    if cg.POper and cg.POper[-1] in ['>','<','==','!=']:
        cg.generate_quad()



# L_OP - LOGICAL OPERATOR
def p_loper(p):
    '''
    loper : GREATER
          | LESS
          | NOTEQUAL
          | ISEQUAL
    '''
    # 8. POper.Push(rel.op)
    cg.POper.append(p[1])

# LOGICAL
# CREO QUE DEBERÍAMOS QUITAR ESTO... NO?
def p_logical(p):
    '''
    logical : expression logical1 expression
    '''

# ??
def p_logical1(p):
    '''
    logical1 : OR
             | AND
    '''


# CONDITION
def p_condition(p):
    '''
    condition : IF head_cond body condition1
    '''
    # 2.-
    end = cg.PJumps.pop()
    cg.fill_quad(end)

def p_condition1(p):
    '''
    condition1 : elseif head_cond body condition1
               | else body
               | empty
    '''
    if len(p) == 5:
        end = cg.PJumps.pop()
        cg.fill_quad(end)
def p_elseif(p):
    '''
    elseif : ELSEIF
    '''
    cg.generate_else()
    # cg.generate_elseif()

def p_else(p):
    '''
    else : ELSE
    '''
    cg.generate_else()

# HEAD
# def p_head(p):
#     '''
#     head : OPENPAREN head1 CLOSEPAREN
#     '''

def p_head_cond(p):
    '''
    head_cond : OPENPAREN head1 close_condition
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

# termina la condición
def p_close_condition(p):
    '''
    close_condition : CLOSEPAREN
    '''
    # genera GOTOF...
    cg.generate_GOTOF()

def p_body1(p):
    '''
    body1 : stmt body1
          | empty
    '''


# FOR
# TODO: cuádruplos para for
def p_for(p):
    '''
    for : FOR OPENPAREN ID TWODOTS exp CLOSEPAREN body
    '''


# WHILE
def p_while(p):
    '''
    while : while1 body
    '''
    end = cg.PJumps.pop()
    w_return = cg.PJumps.pop()

    cg.generate_GOTO()
    cg.fill_goto(w_return)

    cg.fill_quad(end)

def p_while1(p):
    '''
    while1 : while_w OPENPAREN expression CLOSEPAREN
    '''
    cg.generate_GOTOF()
# de tanto ver y escribir la palabra while siento que esta bien rara y la estoy escribiendo mal
def p_while_w(p):
    '''
    while_w : WHILE
    '''
    # 1.-
    cg.PJumps.append(len(cg.Quads) + 1)

# FUN_CALL
def p_funCall(p):
    '''
    funCall : ID OPENPAREN funCall2 CLOSEPAREN
    '''
    if p[1] in vars_t.table:
        p[0] = p[1]

    else:
         raise TypeError(f"Function '{p[1]}' not declared")


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


# (exp,exp)
def p_laRegla(p):
    '''
    laRegla : OPENPAREN exp COMMA exp CLOSEPAREN
    '''


# (exp)
def p_laRegla2(p):
    '''
    laRegla2 : OPENPAREN exp CLOSEPAREN
    '''

# TODAS LAS EXP DE GRAPH STMTS DEBERÁN SER INTS ALV
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
    graphr : REPEAT laRegla2 OPENBRACES graphr1 CLOSEBRACES
    '''

def p_graphr1(p):
    '''
    graphr1 : graphstmt COMMA graphr1
            | graphstmt
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

# NOTA: Hay que arreglar este pedo, creo que no están bien declaradas... btw... y si borramos el graph repeat??
def p_graphview2(p):
    '''
    graphview2 : SETXY laRegla
              | COLOR_STAR laRegla2
              | SIZE_STAR laRegla2
    '''

# Esto está malisimo
# def p_graphview3(p):
#     '''
#     graphview3 : exp COMMA
#               | laRegla
#     '''

# exp


def p_exp(p):
    '''
    exp : term exp1
    '''
    p[0] = p[1]
    if cg.POper and cg.POper[-1] in ['+','-']:
        cg.generate_quad()

def p_exp1(p):
    '''
    exp1 : ADDITION exp
         | SUBSTRACTION exp
         | empty
    '''
    # 2. POper.push(+ or -)
    if len(p) == 3:
        cg.POper.append(p[1])



def p_openP(p):
    '''
    openP : OPENPAREN
    '''
    # 6. crea fondo falso
    cg.POper.append(p[1])


def p_closeP(p):
    '''
    closeP : CLOSEPAREN
    '''
    # 7. quita fondo falso
    cg.POper.pop()

# FACTOR


def p_factor(p):
    '''
    factor : vcte
           | factor1
    '''
    p[0] = p[1]

def p_factor1(p):
    '''
    factor1 : factor2 vcte
            | openP expression closeP
    '''


def p_factor2(p):
    '''
    factor2 : ADDITION
            | SUBSTRACTION
    '''
    # 2.POper.push(+ or -)
    p[0] = p[1]
    cg.POper.append(p[0])

# al chile no se que estoy haciendo
# TODO: checar bien los quads en expresiones
# por ejemplo, c = 4 + glob1 * glob2 / b + c;
# hace primero la division y luego la multiplicación...
# TERM
def p_term(p):
    '''
    term : factor term1
    '''
    p[0] = p[1]
    if cg.POper and cg.POper[-1] in ['*','/']:
        cg.generate_quad()


def p_term1(p):
    '''
    term1 : MULTIPLICATION term
          | DIVISION term
          | empty
    '''
    # 3. POper.push(* or /)
    p[0] = p[1]
    if len(p) == 3:
        cg.POper.append(p[1])



def p_empty(p):
    '''empty :'''
    p[0] = None
    pass


def p_error(p):
    print("ERROR {}".format(p))


yacc.yacc()

# hay que ver CÓMO ponemos que hay errores en la sintaxis pero más específicos o algo asi
if __name__ == '__main__':
    try:
        nombreArchivo = 'pruebas/tati.tati'

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
