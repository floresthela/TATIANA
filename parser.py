'''
TATIANA
Archivo parser del lenguaje que contiene las reglas gramaticales

Flor Esthela Barbosa y Laura Santacruz
'''
# PARSER
import sys
from ply import yacc
import json
import genera_comp

from functools import reduce
from lexer import tokens
from vars_table import VarsTable
from intermediate_code_generation import Intermediate_CodeGeneration

vars_t = VarsTable()
cg = Intermediate_CodeGeneration()
#contador para la llamada de funcion
# k = 0

# IMPORTANTE: descomentar el vars_t de remove a las funciones para eliminarlas

# PROGRAM
def p_program(p):
    '''
    program : programp ID SEMICOLON declara_vars program_modules
    '''

    p[0] = "PROGRAM COMPILED"
    vars_t.delete_vars('global')

    print(vars_t.table)
    print(cg.Quads)
    print(cg.constantes)
    f_quads = cg.format_quads()
    f_constantes = cg.format_constantes()
    genera_comp.genera_arch(p[2],vars_t.table, f_quads, f_constantes)


def p_program_modules(p):
    '''
    program_modules : program_fun star
    '''
    cg.generate_GOTO_star()

def p_programp(p):
    '''
    programp : PROGRAM
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

    vars_t.delete_vars('star')
    cg.generate_END()


def p_starI(p):
    '''
    starI : star_sign OPENBRACES
    '''
    cg.reset_locales()
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
    vars : type ID dimensionada equals exp SEMICOLON
         | type ID dimensionada SEMICOLON
    '''
    p[0] = (p[1], p[2])

    print(p[3])
    # variables dimensionadas
    if isinstance(p[3], tuple):
        dimensionada = True
        var_dim = p[3]
        tam = var_dim[0] * var_dim[1]

    else:
        dimensionada = False
        var_dim = None
        tam = 1
    print(tam)

    if not vars_t.initialized:
        vars_t.FunDirectory('global', 'np',None)
    
    if vars_t.current_scope == 'global':
        dir = cg.direccion_mem('global',p[1],tam)
    
    else:
        dir = cg.direccion_mem('local',p[1],tam)
    # def insert_var(var_id, var_type, dir, b_dim, dim):
    
    vars_t.insert_var(p[2],p[1],dir,dimensionada,var_dim)

    if dimensionada:
        if cg.POper and cg.POper[-1] in ['=']:
            
            # checar que las tuplas con tamaños sean iguales
            if var_dim == p[5]:
                cg.POper.pop()
                # asignamos direcciones
                for i in range(tam-1,-1,-1):
                    cg.POper.append('=')
                    cg.PilaO.append(dir + i)
                    cg.PTypes.append(p[1])

                    cg.generate_quad(vars_t.current_scope)
            else:
                raise TypeError(f"Variable dimensionada {p[2]} debe ser de tamaño {var_dim}")
        
        
        else:
            # arreglo en blanco
            if p[1] == 'int':
                blanco = 0
            elif p[1] == 'float':
                blanco = 0.0
            elif p[1] == 'string':
                blanco = ""
            
            blanco = cg.direccion_mem('constantes',p[1],val=blanco)

            for i in range(tam -1,-1,-1):
                cg.PilaO.append(blanco)
                cg.POper.append('=')
                cg.PilaO.append(dir + i)
                
                cg.PTypes.append(p[1])
                cg.PTypes.append(p[1])

                cg.generate_quad(vars_t.current_scope)
 
    else:
        # print('ok')
        if cg.POper and cg.POper[-1] in ['=']:
            cg.PilaO.append(dir)
            cg.PTypes.append(p[1])
            result = cg.generate_quad(vars_t.current_scope)



        

# variable dimensionada o no..
def p_dimensionada(p):
    '''
    dimensionada : OPENBRACKET CTEINT CLOSEBRACKET
           | OPENBRACKET CTEINT CLOSEBRACKET OPENBRACKET CTEINT CLOSEBRACKET
           | empty
    '''
    if len(p) == 2:
        p[0] = None
    
    # si es variable dimensionada mandamos parriba las dimensiones [0...CTEINT]
    # (renglones,columnas)
    elif len(p) == 4:
        p[0] = (1, int(p[2]))
    else:
        p[0] = (int(p[2]),int(p[5]))

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
        | funCall SEMICOLON
        | return
    '''

def p_assignment(p):
    '''
    assignment : id equals assignment3 SEMICOLON
    '''
    # c = a + b; -> mete c a pilao

def p_assignment3(p):
    '''
    assignment3 : exp
                | read
    '''
    p[0] = p[1]
    if cg.POper[-1] == '=':
        cg.generate_quad(vars_t.current_scope);


# VAR_CTE
def p_vcte(p):
    '''
    vcte : cte_int
         | cte_float
         | cte_string
         | id
         | funCall
         | vectormatriz
    '''
    p[0] = p[1]
    # 1. PilaO.Push(id.name)
    # if len(p) == 2:
    #     cg.PilaO.append(p[1])
    


# asignar valores a variable dimensionada
# [1,2,3,4]
# [[3,4,5],[5,6,7]]

def p_vectormatriz(p):
    '''
    vectormatriz : OPENBRACKET vm1 CLOSEBRACKET
                 | vm1
    '''
    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_vm1(p):
    '''
    vm1 : OPENBRACKET vm2 CLOSEBRACKET COMMA vm1
        | OPENBRACKET vm2 CLOSEBRACKET 
    '''
    if len(p) > 4:
        if p[5][1] == p[2]:
            p[0] = (p[5][0] + 1, p[2])
        else:
            raise TypeError(f"Las matrices deben tener arreglos del mismo tamaño")
    else:
        p[0] = (1,p[2])

def p_vm2(p):
    '''
    vm2 : exp COMMA vm2
        | exp
        | empty
    '''
    if len(p) > 2:
        p[0] = 1 + p[3]
    else:
        p[0] = 1


# FUNCTION
def p_functionI(p):
    '''
    functionI : type ID
              | VOID ID
        '''
    #vars_t.FunDirectory(p[2], p[1])
    #cg.generate_ERA(p[2])
    p[0] = p[2]

    cg.reset_locales()
    beginFun = len(cg.Quads) + 1
    vars_t.FunDirectory(p[2],p[1],beginFun)
    # mete las funciones como variables globales...
    vars_t.table['global']['vars'][p[0]] = { 'id': p[0], 'type':p[1]}




def p_function(p):
    '''
    function : FUN functionI function2 inicia_fun declara_vars function4 termina_fun
    '''
    if p[7] is not None:
        vars = p[7]
        vars = vars[:-1]
        p[0] = vars


    # vars_t.delete_vars(p[2])

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

    dir = cg.direccion_mem('local', p[1])
    print('fun',vars_t.current_scope)
    vars_t.insert_var(p[2], p[1], dir)


# VARS


# TYPE
def p_type(p):
    '''
    type : INT
         | FLOAT
         | STRING
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
    id : ID vectormatriz
    '''
    p[0] = p[1]
    cg.PilaO.append(p[1])
    t = vars_t.search_var(p[1])
    if t:
        cg.PilaO.append(t['dir'])
        cg.PTypes.append(t['type'])

# FUN_CALL
def p_funCall(p):
    '''
    funCall : ID iniciaFunCall funCall2 terminaFunCall
    '''
    cg.PilaO.append(p[1])
    if p[1] in vars_t.table:
        p[0] = p[1]
        # print("HOLAA")
        # print(p[0])

        init = vars_t.table[p[0]]['begin']
        #print("Direccion", vars_t.table[p[3]]['dir'])
        # busca = vars_t.search_var(p[1])
        # print("ABER", busca)
        # parametros = vars_t.table[p[1]]['params']
        # print("PARAMETROSS DE LA vars table")
        # print(parametros)
        # # print("INIT")
        # print(init)
        cg.fill_ERA(init)
        # print("PRUEBAAA")
        # print(p[3])

        cg.generate_goSub(p[1])
    else:
        raise TypeError(f"Function '{p[1]}' not declared")

# def p_funID(p):
#     '''
#     funID : ID
#     '''
#     cg.generate_ERA()


def p_iniciaFunCall(p):
    '''
    iniciaFunCall : OPENPAREN
    '''
    cg.generate_ERA()


def p_terminaFunCall(p):
    '''
    terminaFunCall : CLOSEPAREN
    '''


def p_funCall2(p):
    '''
    funCall2 : funCallParam funCall3
             | empty
    '''
    # if len(p) == 3:
    #     print("AQUI ESTAA??",p[1])


def p_funCall3(p):
    '''
    funCall3 : COMMA funCallParam funCall3
             | empty
    '''


def p_funCallParam(p):
    '''
    funCallParam : exp
    '''
    print('FUNCALLPARAMS', p[1])
    vt = vars_t.search_var(p[1])
    dir = vt['dir']
    print("Direcccion",dir)
    cg.generate_paramQuad(dir)


# CTE
def p_cte_int(p):
    '''
    cte_int : CTEINT
    '''

    dir = cg.direccion_mem('constantes','int',1, p[1])
    p[0] = dir
    cg.PTypes.append('int')
    cg.PilaO.append(dir)


def p_cte_float(p):
    '''
    cte_float : CTEFLOAT
    '''
    dir = cg.direccion_mem('constantes','float',1, p[1])
    p[0] = dir
    cg.PTypes.append('float')
    cg.PilaO.append(dir)

def p_cte_string(p):
    '''
    cte_string : CTESTRING
    '''
    dir = cg.direccion_mem('constantes','string', 1, p[1])
    p[0] = dir
    cg.PilaO.append(dir)
    cg.PTypes.append('string')


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
# def p_for(p):
#     '''
#     for : FOR OPENPAREN ID TWODOTS exp CLOSEPAREN body
#     '''


# FOR
# TODO: cuádruplos para for
def p_for(p):
    '''
    for : for1 body
    '''
    end = cg.PJumps.pop()
    return_for = cg.PJumps.pop()
    id = cg.PilaO.pop()
    id += 1
    cg.generate_GOTO()
    cg.fill_goto(return_for)
    cg.fill_quad(end)


def p_for1(p):
    '''
    for1 : forInit OPENPAREN ID for2
    '''
    p[0] = p[3]
    # 2
    #cg.PilaO.push()
    cg.check_type(p[3])


def p_for2(p):
    '''
    for2 : TWODOTS exp for3
    '''
    # 3
    cg.PilaO.append(p[2])
    # tmp1 = cg.PilaO.pop()
    # tmp2 = cg.PilaO.pop()
    # cg.PilaO.append(tmp2)


def p_for3(p):
    '''
    for3 : CLOSEPAREN
    '''
    # 4
    cg.generate_GOTOV()


def p_forInit(p):
    '''
    forInit : FOR
    '''
    # 1
    cg.PJumps.append(len(cg.Quads)+1)


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


def p_while_w(p):
    '''
    while_w : WHILE
    '''
    # 1.-
    cg.PJumps.append(len(cg.Quads) + 1)


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

# expression
def p_expression(p):
    '''
    expression : exp loper exp
               | exp
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1:]

# exp
def p_exp(p):
    '''
    exp : term
        | term exp_o exp
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1:]

    if cg.POper and cg.POper[-1] in ['>','<','==','!=']:
        cg.generate_quad(vars_t.current_scope)

def p_exp_o(p):
    '''
    exp_o : ADDITION
          | SUBSTRACTION
    '''
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

# TERM
def p_term(p):
    '''
    term : factor term_o term
         | factor
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1:]

    if cg.POper and cg.POper[-1] in ['+', '-']:
        t = cg.generate_quad(vars_t.current_scope)

        vars_t.insert_temp(t,vars_t.current_scope)


def p_term_o(p):
    '''
    term_o : MULTIPLICATION
           | DIVISION
    '''
    cg.POper.append(p[1])


# FACTOR
def p_factor(p):
    '''
    factor : vcte
           | openP expression closeP
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1:]

    if cg.POper and cg.POper[-1] in ['*', '/']:
        t = cg.generate_quad(vars_t.current_scope)
        vars_t.insert_temp(t,vars_t.current_scope)

# def p_factor1(p):
#     '''
#     factor1 : factor2 vcte
#             | openP expression closeP
#     '''

# def p_factor2(p):
#     '''
#     factor2 : ADDITION
#             | SUBSTRACTION
#     '''
#     # 2.POper.push(+ or -)
#     p[0] = p[1]
#     cg.POper.append(p[0])

def p_empty(p):
    '''empty :'''
    p[0] = None
    pass


def p_error(p):

    if p is not None:
        err = f"{p.value} en la linea {p.lineno}"

    raise TypeError(f"Error de sintaxis: {err}")

def flatten(li):
    return sum(([x] if not isinstance(x, list) else flatten(x) for x in li), [])

parser = yacc.yacc(start='program')
