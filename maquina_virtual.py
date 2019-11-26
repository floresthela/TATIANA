'''
TATIANA
Archivo para la máquina virtual

Flor Esthela Barbosa y Laura Santacruz
'''
import sys
import json
from turtle import Turtle, Screen, Shape
from memoria import Memoria

class MaquinaVirtual:
    def __init__(self):

        self.programa = None
        self.memoria = Memoria()
        # self.mem_local = MemLocal()
        
        self.estrella = None
        self.screen = None
        self.turtle_activa = False

        self.pila_contextos = []


    def agarra_datos(self,program):
        '''
        Recibe archivos con cuádruplos y el directorio de funciones y constantes
        :param program: Nombre del programa compilado
        '''

        compilado = f"pruebas/{program}_comp.ta"


        arch_compilado = open(compilado, 'r')
        
        todito = json.load(arch_compilado)
        
        self.pila_contextos.append('star')
        self.programa = program

        self.haz_constantes(todito['tConstantes'])
        self.haz_quads(todito['Quads'],todito['FunDir'])



    # dnb
    def haz_quads(self,quads,fun_dir,sig=0):
        '''
        Procesar cada cuadruplo de la lista de Quads recibida hasta que encuentre END
        :param quads: Lista con todos los quads
        :param fun_dir: Directorio de funciones
        :param sig: Apuntador al siguiente cuádruplo
        '''
        
        # parametros que estamos mandando
        parametros = []
        retornado = None

        while True:            
            operador = quads[sig][0]
            op_izq = quads[sig][1]
            op_der = quads[sig][2]
            res = quads[sig][3]

            # checamos que si traen ( ) y vamos por su valor
            if isinstance(op_izq,str) and op_izq[0] == '(':
                op_izq = self.dame_contenido(op_izq)
            if isinstance(op_der,str) and op_der[0] == '(': 
                op_der = self.dame_contenido(op_der)
            if isinstance(res,str) and res[0] == '(':
                res = self.dame_contenido(res)

            if operador == '=':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                tipo_res = self.dame_tipo(res)
                
                mem_r[res] = tipo_res(mem1[op_izq])
                sig += 1

            elif operador == '+':

                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                
                # suma de un string con algo más
                if(isinstance(mem1[op_izq], str) and not isinstance(mem2[op_der], str)) or (isinstance(mem2[op_der],str) and not isinstance(mem1[op_izq],str)):
                    mem_r[res] = str(mem1[op_izq]) + str(mem2[op_der])
                else:
                    
                    mem_r[res] = mem1[op_izq] + mem2[op_der]
                sig += 1

            elif operador == '-':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] - mem2[op_der]
                sig += 1

            elif operador == '*':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] * mem2[op_der]
                sig += 1

            elif operador == '/':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                tipo_res = self.dame_tipo(res)

                if mem2[op_der] == 0:
                    raise TypeError(f"Error: No se puede dividir entre 0")

                mem_r[res] = tipo_res(mem1[op_izq] / mem2[op_der])
                sig += 1

            elif operador == '>':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] > mem2[op_der]
                sig +=1

            elif operador == '<':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                
                mem_r[res] = mem1[op_izq] < mem2[op_der]
                sig +=1
            
            elif operador == '>=':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] >= mem2[op_der]
                sig +=1

            elif operador == '<=':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] <= mem2[op_der]
                sig +=1


            elif operador == '!=':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] != mem2[op_der]

                sig +=1

            elif operador == '==':
                mem1, mem2, mem_r = self.dame_memorias(op_izq, op_der, res)
                mem_r[res] = mem1[op_izq] == mem2[op_der]
                
                sig +=1

            elif operador == 'print':
                mem = self.dame_mem(res)
                # no borrar este print
                print(mem[res])
                sig +=1

            elif operador == 'read':
                mem = self.dame_mem(res)
                mem[res] = input()
                sig += 1

            elif operador == 'GotoF':
                # memoria de valor booleano
                mem_b = self.dame_mem(op_izq)
                if not mem_b[op_izq]:
                    sig = int(res) - 1
                else:
                    sig += 1
                    
            elif operador == 'GotoV':
                mem_b = self.dame_mem(op_izq)
                if mem_b[op_izq]:
                    sig = int(res) - 1
                else:
                    sig += 1

            elif operador == 'Goto_main' or operador == 'Goto':
                sig = int(res) - 1
                # activamos memoria star

            elif operador == 'END':
                
                self.memoria.cuello()
                self.pila_contextos.pop()
                # tenemos que borrar algo más ?
                break

            #################################### GRAPH STATEMENTS ####################################
            # 0 exp
            elif operador == 'hand_down':
                if not self.turtle_activa:
                    self.activa_tortuga()
                    
                self.estrella.pd()
                sig += 1

            elif operador == 'hand_up':
                if not self.turtle_activa:
                    self.activa_tortuga()
                    
                self.estrella.pu()
                sig += 1

            elif operador == 'hide_star':
                if not self.turtle_activa:
                    self.activa_tortuga()
                    
                self.estrella.hideturtle()
                sig += 1
            
            elif operador == 'show_star':
                if not self.turtle_activa:
                    self.activa_tortuga()
                    
                self.estrella.showturtle()
                sig += 1
            
            elif operador == 'exitonclick':
                if not self.turtle_activa:
                    self.activa_tortuga()
                    
                self.screen.exitonclick()
                sig += 1

            elif operador == 'clear':
                if not self.turtle_activa:
                    self.activa_tortuga()

                self.screen.clear()
                sig += 1
            
            elif operador == 'begin_fill':
                if not self.turtle_activa:
                    self.activa_tortuga()
                
                self.estrella.begin_fill()
                sig += 1

            elif operador == 'end_fill':
                if not self.turtle_activa:
                    self.activa_tortuga()

                self.estrella.end_fill()
                sig += 1


            # 1 exp
            elif operador == 'circle':
                mem = self.dame_mem(op_izq)
                if not self.turtle_activa:
                    self.activa_tortuga()
                    
                self.estrella.circle(mem[op_izq])
                sig += 1
            
            elif operador == 'left':
                mem = self.dame_mem(op_izq)
                angle = float(mem[op_izq])
                if not self.turtle_activa:
                    self.activa_tortuga()
                    
                if angle > 360:
                    raise TypeError(f"Valor no debe exceder 360 grados")
                self.estrella.lt(angle)
                sig += 1

            elif operador == 'right':
                mem = self.dame_mem(op_izq)
                angle = float(mem[op_izq])
                if not self.turtle_activa:
                    self.activa_tortuga()
                    
                if angle > 360:
                    raise TypeError(f"Valor no debe exceder 360 grados")
                self.estrella.rt(angle)
                sig += 1
            
            elif operador == 'back':
                mem = self.dame_mem(op_izq)
                if not self.turtle_activa:
                    self.activa_tortuga()
                    
                self.estrella.bk(mem[op_izq])
                sig += 1

            elif operador == 'go':
                mem = self.dame_mem(op_izq)
                if not self.turtle_activa:
                    self.activa_tortuga()
                    
                self.estrella.fd(mem[op_izq])
                sig += 1
            
            elif operador == 'square':
                mem = self.dame_mem(op_izq)

                if not self.turtle_activa:
                    self.activa_tortuga()

                # grafica cuadrado
                self.estrella.forward(mem[op_izq])
                self.estrella.left(90) 
                self.estrella.forward(mem[op_izq])
                self.estrella.left(90)
                self.estrella.forward(mem[op_izq])
                self.estrella.left(90)
                self.estrella.forward(mem[op_izq])
                self.estrella.left(90)
                sig += 1
            
            elif operador == 'rectangle':
                mem1 = self.dame_mem(op_izq) # base
                mem2 = self.dame_mem(op_der) # altura
                
                base = mem1[op_izq]
                altura = mem2[op_der]

                if not self.turtle_activa:
                    self.activa_tortuga()

                # grafica rectangulo
                self.estrella.fd(base)
                self.estrella.lt(90) 
                self.estrella.fd(altura)
                self.estrella.lt(90)
                self.estrella.fd(base)
                self.estrella.lt(90)
                self.estrella.fd(altura)
                self.estrella.lt(90)
                sig += 1

            elif operador == 'triangle':
                mem = self.dame_mem(op_izq)

                if not self.turtle_activa:
                    self.activa_tortuga()

                # dibuja triangulo equilatero de base ingresada
                self.estrella.fd(mem[op_izq])
                
                self.estrella.lt(120)
                self.estrella.fd(mem[op_izq])

                self.estrella.lt(120)
                self.estrella.fd(mem[op_izq])

                sig += 1
            
            elif operador == 'speed':
                mem = self.dame_mem(op_izq)

                if not self.turtle_activa:
                    self.activa_tortuga()

                speed = mem[op_izq]
                print(type(speed))
                if self.dame_tipo(op_izq) is not str:
                    if not 1 <= speed <= 10:
                        raise TypeError(f"Valor de la velocidad debe estar entre 0 y 10.")
                elif speed not in ['fastest','fast','normal','slow','slowest']:
                    raise TypeError(f"Velocidad {speed} no válida.")
                self.estrella.speed(mem[op_izq])
                sig += 1
            
            elif operador == 'color_star':
                mem = self.dame_mem(op_izq)

                if not self.turtle_activa:
                    self.activa_tortuga()
                color = mem[op_izq]
                self.estrella.color(color)
                sig += 1
            
            elif operador == 'size_star':
                mem = self.dame_mem(op_izq)

                if not self.turtle_activa:
                    self.activa_tortuga()
                
                size = mem[op_izq]
                self.estrella.pensize(size)
                sig += 1

            # 2 exp
            elif operador == 'position':
                mem1 = self.dame_mem(op_izq)
                mem2 = self.dame_mem(op_der)

                if not self.turtle_activa:
                    self.activa_tortuga()
                    

                self.estrella.setpos(mem1[op_izq],mem2[op_der])
                sig += 1


            elif operador == 'arc':
                # arc(angulo,radio)
                mem1 = self.dame_mem(op_izq)
                mem2 = self.dame_mem(op_der)
            
                if not self.turtle_activa:
                    self.activa_tortuga()
                    
                
                self.estrella.circle(mem2[op_der],mem1[op_izq])
                sig += 1
            
            ##########################################################################################

            elif operador == 'VER':
                
                mem1 = self.dame_mem(op_izq)
                mem2 = self.dame_mem(op_der)
                if not(0 <= mem1[op_izq] < mem2[op_der]):
                    raise TypeError(f"Out of bouuunddsss")
                
                sig += 1
            
            
            ############ FUNCIONES ############

            elif operador == 'ERA':
                fun = fun_dir[res]
                
                if self.memoria.activa is not None:
                    superior = self.memoria.activa
                else:
                    superior = self.memoria
                self.memoria.record_activacion(superior, fun['vars'])
                sig += 1

            elif operador == 'GOSUB':
                self.memoria.activa = self.memoria.mem_ejec[list(self.memoria.mem_ejec.keys())[-1]]
                
                self.pila_contextos.append(res)

                # mem = self.dame_mem(res)
                self.memoria.activa.matcheo(parametros)
                parametros.clear()
                val = self.haz_quads(quads, fun_dir, int(res)-1)

                # return
                if val is not None:
                    mem = self.dame_mem(op_izq)
                    mem[op_izq] = val
                
                sig += 1
                

            elif operador == 'RETURN':
                mem = self.dame_mem(res)
                
                # jaja que pedo con el nombre k le puse ?¿
                retornado = mem[res]

                sig += 1
            
            elif operador == 'param':
                mem = self.dame_mem(res)
                parametros.append(mem[res])

                sig += 1
            
            elif operador == 'ENDPROC':
                
                self.memoria.cuello()
                self.pila_contextos.pop()

                if retornado is not None:
                    return retornado
                else:
                    break

            # TODO: 
            # agregar clear
            # agregar fill
            
    


    def haz_constantes(self, t):
        '''
        Genera tabla de constantes y las carga a memoria
        :param t: Tabla de constantes
        '''
        for const in t:
            dir = const[0]
            val = const[1]
            self.memoria.mem_constantes[dir] = val

        '''
        GLOBAL
        i [1000  -  5999]
        f [6000  - 10999]
        s [11000 - 15999]
        b [16000 - 20999]


        LOCAL
        i [21000 - 25999]
        f [26000 - 30999]
        s [31000 - 35999]
        b [36000 - 40999]

        CONSTANTES
        c [41000 - 51999]

        '''


    def dame_memorias(self, op_i, op_d, res):
        '''
        Regresa las direcciones de memoria a las que pertenecen los elementos de un cuádruplo a excepción del operador
        :param op_i: Operador izquierdo del quad
        :param op_d: Operador derecho del quad
        :param res: Resultado del quad
        :return: Memoria correspondiente
        '''
        return self.dame_mem(op_i) , self.dame_mem(op_d), self.dame_mem(res)

    def dame_mem(self, dir):
        '''
        Regresa la dirección a la que pertenece la variable global, local o de constantes
        :param dir: Dirección de variable
        '''
        
        if dir is None:
            return None
        elif 1000 <= dir < 21000:
            return self.memoria.mem_global
        elif 21000 <= dir < 41000:
            return self.memoria.activa.mem_local if self.memoria.activa is not None else self.memoria.mem_local
        else:
            return self.memoria.mem_constantes

    def dame_tipo(self,dir):
        '''
        Regresa el tipo de variable
        :param dir: Dirección de variable
        '''
        if 1000 <= dir < 6000 or 21000 <= dir < 26000:
            return int
        elif 6000 <= dir < 11000 or 26000 <= dir < 31000:
            return float
        elif 11000 <= dir < 16000 or 31000 <= dir < 36000:
            return str
        elif dir >= 41000:
            return type(self.memoria.mem_constantes[dir])
        else:
            return bool

    def activa_tortuga(self):
        self.turtle_activa = True
        
        s = Turtle()
        self.screen = Screen()
        self.dibuja_estrella(s)
        
        # self.star = Turtle(shape="estrella")

        self.screen.title(self.programa)
        self.screen.clear()
        self.estrella = Turtle(shape="estrella")
        # self.screen.clear()
        # self.screen.exitonclick()
        

    def dibuja_estrella(self,lapiz):
        '''
        Define una figura de estrella como el lapiz que dibujará
        '''

        fig = Shape("compound")
        lapiz.setx(0)
        lapiz.sety(4)

        lapiz.begin_poly()
        lapiz.goto(1,1)
        lapiz.goto(3.5,1)
        lapiz.goto(1.5,-0.5)
        lapiz.goto(2.5,-3)
        lapiz.goto(0,1.5)
        lapiz.goto(-2.5,-3)
        lapiz.goto(-1.5,-0.5)
        lapiz.goto(-3.5,1)
        lapiz.goto(-1,1)
        lapiz.end_poly()

        fig.addcomponent(lapiz.get_poly(),"purple","purple")
        self.screen.register_shape("estrella",fig)
        lapiz.reset()

    def dame_contenido(self, dir):
        # my_list = my_list[1:-1]
        dir_aux = int(dir[1:-1])
        dir_mem = self.dame_mem(dir_aux)
        return dir_mem[dir_aux]
 
