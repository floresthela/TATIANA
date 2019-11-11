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

# IMPORTANTE: descomentar el vars_t de remove a las funciones para eliminarlas
# PROGRAM
def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON declara_vars program_modules
    '''
    conta = 1
    # print(cg.Quads)
    for q in cg.Quads:
        print(conta,q)
        conta += 1

    p[0] = "PROGRAM COMPILED"
    vars_t.delete_vars('global')
    print(vars_t.table)


def p_program_modules(p):
    '''
    program_modules : program_fun star
    '''


def p_program_fun(p):
    '''
    program_fun : function program_fun
                | empty
    '''


# STAR
def p_star(p):
    '''
    star : starI declara_vars star1 CLOSEBRACES
    '''
    s_table = vars_t.table['star']

    star = cg.PJumps.pop()
    cg.fill_goto_star(star)

    for v in s_table['vars']:
        type = s_table['vars'][v]['type']
        if type == 'int':
            s_table['size']['i'][0] += 1
        elif type == 'float':
            s_table['size']['f'][0] += 1
        elif type == 'char':
            s_table['size']['c'][0] += 1

    vars_t.delete_vars('star')


def p_starI(p):
    '''
    starI : star_sign OPENBRACES
    '''
    vars_t.FunDirectory('star', 'star',p[1])

def p_star_sign(p):
    '''
    star_sign : MULTIPLICATION
    '''
    beginStar = len(cg.Quads) + 1
    cg.PJumps.append(beginStar)
    p[0] = beginStar


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
        vars_t.FunDirectory('global', 'np',None)
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
    p[0] = p[2]

    beginFun = len(cg.Quads) + 1
    vars_t.FunDirectory(p[2],p[1],beginFun)
    # mete las funciones como variables globales...
    vars_t.table['global']['vars'][p[0]] = { 'id': p[0], 'type':p[1]}

    if len(vars_t.table) == 3:
        cg.generate_GOTO_star()



def p_function(p):
    '''
    function : FUN functionI function2 inicia_fun declara_vars function4 termina_fun
    '''

    f_table = vars_t.table[p[2]]

    if p[7] != None:
        vars = p[7]
        vars = vars[:-1]
        p[0] = vars

    for v in f_table['vars']:
        type = f_table['vars'][v]['type']
        if type == 'int':
            f_table['size']['i'][0] += 1
        elif type == 'float':
            f_table['size']['f'][0] += 1
        elif type == 'char':
            f_table['size']['c'][0] += 1


    vars_t.delete_vars(p[2])

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
    function3 : funParam function5
              | empty
    '''
    if p[1] is not None:
        p[0] = [p[1]]
        p[0].append(p[2])
        print('hey',p[0])



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
    function5 : COMMA funParam function5
              | empty
    '''
    if p[1] is not None:
        p[0] = p[2:]
        p[0] = flatten(p[0])

def p_funParam(p):
    '''
    funParam : type ID
    '''
    p[0] = (p[1],p[2])
    vars_t.insert_param(p[2],p[1])

# VARS
# al final hay que actualizar diagramas

def flatten(li):
    return sum(([x] if not isinstance(x, list) else flatten(x) for x in li), [])

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
    head_cond : OPENPAREN expression close_condition
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
def p_dosExp(p):
    '''
    dosExp : OPENPAREN exp COMMA exp CLOSEPAREN
    '''



# (exp)
def p_unaExp(p):
    '''
    unaExp : OPENPAREN exp CLOSEPAREN
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
             | graphfig2 SEMICOLON
    '''
# Figures que llevan solo una exp
def p_graphfig1(p):
    '''
    graphfig1 : CIRCLE unaExp
            | SQUARE unaExp
    '''
    p[0] = p[1]
    cg.generate_quad_graph1(p[0])

# Figures que llevan dos exp
def p_graphfig2(p):
    '''
    graphfig2 : TRIANGLE dosExp
            | RECTANGLE dosExp
    '''
    p[0] = p[1]
    cg.generate_quad_graph2(p[0])

# GRAPH_MOVEMENT
def p_graphmove(p):
    '''
    graphmove : graphmove0  SEMICOLON
              | graphmove1 SEMICOLON
              | graphmove2 SEMICOLON
    '''


def p_graphmove0(p):
    '''
    graphmove0 : HAND_DOWN
              | HAND_UP
    '''
    p[0] = p[1]
    cg.generate_quad_graph0(p[0])


def p_graphmove1(p):
    '''
    graphmove1 : GO unaExp
              | LEFT unaExp
              | RIGHT unaExp
              | BACK unaExp
    '''
    p[0] = p[1]
    cg.generate_quad_graph1(p[0])

def p_graphmove2(p):
    '''
    graphmove2 : ARC dosExp
    '''
    p[0] = p[1]
    cg.generate_quad_graph2(p[0])

# SUPER DUDA: QUADS CON VARIOS PARAMETROS ?¿?¿ CÓMO HACEMOS EL REPEAT
# pensaba hacer un tipo while pero en lugar de gotof, ir restando al número asignado de veces que se repetirá... idk

# GRAPH_REPEAT
def p_graphr(p):
    '''
    graphr : repeat rep OPENBRACES graphstmt graphr1 CLOSEBRACES
    '''
    end = cg.PJumps.pop()
    r_return = cg.PJumps.pop()
    # esto no lo sé
    cg.generate_GOTO()
    cg.fill_goto(r_return)
    cg.fill_quad(end)

def p_graphr1(p):
    '''
    graphr1 : graphstmt graphr1
            | empty
    '''

def p_rep(p):
    '''
    rep : OPENPAREN exp CLOSEPAREN
    '''
    cg.generate_quad_repeat()

def p_repeat(p):
    '''
    repeat : REPEAT
    '''
    cg.PJumps.append(len(cg.Quads) + 1)

# GRAPH_VIEW
def p_graphview(p):
    '''
    graphview : graphview0 SEMICOLON
              | graphview1 SEMICOLON
              | graphview2 SEMICOLON
    '''

def p_graphview0(p):
    '''
    graphview0 : HIDE_STAR
              | SHOW_STAR
    '''
    p[0] = p[1]
    cg.generate_quad_graph0(p[0])

def p_graphview1(p):
    '''
    graphview1 : COLOR_STAR unaExp
              | SIZE_STAR unaExp
    '''
    p[0] = p[1]
    cg.generate_quad_graph1(p[0])

def p_graphview2(p):
    '''
    graphview2 : SETXY dosExp
    '''
    p[0] = p[1]
    cg.generate_quad_graph2(p[0])

# exp
def p_exp(p):
    '''
    exp : term exp1
    '''
    p[0] = p[1]
    if cg.POper and cg.POper[-1] in ['+', '-']:
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
    if cg.POper and cg.POper[-1] in ['*', '/']:
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
        nombreArchivo = 'pruebas/prueba7.tati'

        arch = open(nombreArchivo, 'r')
        print("Archivo a leer: " + nombreArchivo)
        info = arch.read()
        # print(info)
        arch.close()
        if(yacc.parse(info, tracking=True) == 'PROGRAM COMPILED'):
            print("SINTAXIS VALIDA :) ")
        else:
            print("ERRORES EN LA SINTAXIS :( ")

    except EOFError:
        print(EOFError)
