# ✭ TATIANA ✭

## Propósito y Alcance

El lenguaje Tatiana pretende brindar una manera divertida de aprender a programar a través de su lenguaje para niñas y niños. Enfocado en aprender los principales aspectos de la programación, también permite graficar elementos que el usuario puede programar para crear todo tipo de dibujos y figuras creativas.

## Objetivo

Tatiana tiene como principal objetivo enseñar a las niñas y niños que no tengan ningún tipo de conocimiento de la programación y/o deseen aprender más sobre la programación a través de una programación sencilla que además les permitirá explorar las funcionalidades gráficas con las que cuenta el lenguaje para fortalecer sus conocimientos en matemáticas y geometría.

---

## Manual de rápida referencia

### **Requerimientos**

Es necesario tener instalado [Python](https://www.python.org/downloads/) (versión 3 en adelante) en la computadora donde quieras correr el achivo puesto que el lenguaje se desarrollo en este lenguaje.

Para poder utilizar las funciones de graficar del lenguaje, es necesario instalar el paquete tkinter utilizando el siguiente comando:

```
$ sudo apt-get install python3-tk 
```

### **Compilación y Ejecución**

Por ser un lenguaje orientado a niñas y niños, Tatiana realiza la compilación y ejecución en un solo comando. Para esto, necesitas tener tu archivo .tati en la carpeta de pruebas

Al estar en la terminal, con el directorio apuntando a la carpeta TATIANA, simplemente debes ingresar el siguiente comando para correr tu programa en lenguaje Tatiana:

```
$ python3 main.py <archivo.tati>
```

Esto compilará tu archivo generando uno nuevo *archivo_comp.tati* el cual será ejecutado.
### **Comenzando**

En Tatiana puedes utilizar tres (3) tipos de variables **ints**, **floats** y **strings** los cuales debes declarar al inicio de cada función o al inicio del programa.

Para declara una función es necesario que utilices la siguiente sintaxis
```
fun <void/tipo> nombre(params,...) { }
```
donde los parametros deberán llevar su tipo de variable. No olvides poner el return en caso de que la función **no** sea tipo void.

No olvides que, en cada programa debes tener **siempre** tu función *estrella* siendo esta la principal.

```
program hola;

* {
    <aquí escribes tu código>
}
```

Puedes hacer uso de condiciones
```
program condiciones;

* {
    int a = 666;
    int b = 9000;
    int c = 4 + a / 9 + (b - 1);

    if(a > b){
        print("a es mayor que b");
    }
    elseif(a == b){
        print("a y b son iguales");
    }
    else{
        print("pues entonces b es mayor que a");
    }
}
```
Además de ciclos como el while y el for
```
program ciclos;

* {
    int i = 0;
    int a = 10;

    while(a > 0){
        print(a);
        a = a - 1;
    }

    for(i:10){
        print("hola");
    }
}
```
### **Funciones**

Las funciones para graficar que el lenguaje provee son las siguientes:

| *Función (parametros,...)* |  |
| --- | ---|
| circle (**x**) | Dibuja un círculo con radio **x** |
| square (**x**) | Dibuja un cuadrado dimensionado en **x** |
| triangle (**x**) | Dibuja un triangulo equilatero dimensionado en **x** |
| rectangle (**x,y**) | Dibuja un rectangulo con base **x** y altura **y** |
| hand_up | Sube el lápiz de la estrella |
| hand_down | Baja el lápiz de la estrella |
| go (**x**) | Avanza hacia adelante **x** unidades|
| left(**x**) | Avanza hacia la izquierda **x** unidades |
| right(**x**) | Avanza hacia la derecha **x** unidades |
| back (**x**) | Retrocede **x** unidades  |
| arc (**x,y**) | Genera un arco con ángulo **x** y radio **y** |
| hide_star| Esconde la estrella que dibuja |
| show_star | Muestra la estrella que dibuja |
| exitonclick | Cierra la ventana con lo dibujado hasta que se haga click en ella |
| clear | Limpia la ventana para graficar |
| beginfill | Comienza relleno de figuras |
| endfill | Termina relleno de figuras programadas |
| color_star(**x**) | Color del lápiz, puedes ver todos los colores disponibles [aquí](https://ecsdtech.com/8-pages/121-python-turtle-colors) |
| size_star(**x**) | Tamaño **x** del grosor de la línea que dibuja |
| speed(**x**) | Velocidad **x** que lleva la estrella que dibuja, puede ser número (0-10) o ["slowest","slow","normal","fast","fastest"] |
| position(**x,y**) | Cambia la posición de la estrella que dibuja a una nueva coordenada en **x** y en **y** | 


### **Ejemplos**

Programar en Tatiana te permite realizar operaciones, manejo de condiciones, manejo de arreglos y matrices, así como recursividad en funciones. 
Aquí te mostramos algunos ejemplos del uso que le puedes dar a este lenguaje.

```
program fibo;

fun int fibonacci(int x){

    int f;
    
    if(x == 0){
        f = 0;
    }
    elseif(x == 1){
        f = 1;
    }
    else{
        f = fibonacci(x-1) + fibonacci(x-2);
    }
    return f;
}

* {
    print(fibonacci(10));
}
```

## **Variables dimensionadas**

Tatiana permite el manejo de arreglos y matrices en sus tipos de variables de enteros (ints), flotantes (floats) y strings.

Enseguida te mostramos un uso que le puedes dar para ordenar una lista, encontrar el elemento en una lista, o generar una multiplicación de matrices.

```
program bubble_sort;

int vector[10] = [5,9,3,1,10,4,8,23,7,2];

fun void burbuja(int t){
    
    int i = 0;
    int j;
    int t1;
    int t2;
    while(i < t){
        j = 0;
        while(j < t - 1){
            if(vector[j+1] < vector[j]){
                
                t1 = vector[j];
                t2 = vector[j+1];

                vector[j] = t2;
                vector[j+1] = t1;
            }

            j = j + 1;
        }

        i = i + 1;
    }
}

* {
    int tam = 10;
    burbuja(tam);
}
```

```
program busqueda_binaria;

int vector[10] = [2,3,4,1,3,87,34,234,12,-3];

fun int bu_bi(int l, int r, int x){
    
    int mitad;
    int retorno = -1;
    
    if(r >= l){

        mitad = l + (r - l) / 2;

        if(vector[mitad] == x){
            
            retorno = mitad;

        } 
        elseif(vector[mitad] > x) {

            retorno = bu_bi(l, mitad - 1, x);

        } 
        elseif(vector[mitad] < x) {
            retorno = bu_bi(mitad + 1, r, x);
        }
    }

    return retorno;
}

* {
    int x = 234;
    int len = 10;
    int resultado = bu_bi(0, len - 1, x);

    if(resultado != -1){
        print("Se encontró!");
    } else {
        print("Elemento no encontrado en la lista");
    }
}
```

```
program matrices;

int arreglo_1[5] = [1,2,3,4,5];
int arreglo_2[5] = [5,4,3,2,1];

int x[3][3] = [[1,2,3],[4,5,6],[7,8,9]];
int y[3][3] = [[1,2,3],[4,5,6],[7,8,9]];

int mul[3][3];
int trans[3][3];

fun void imprime_matriz() {
    string ren = "";
    int i = 0;
    int j;

    while(i < 3) {
        j = 0;
        while(j < 3) {
            ren = ren + trans[i][j] + " ";
            j = j + 1;
        }
        print(ren);
        i = i + 1;
        ren = "";
    }
}

fun void multiplica() {
    int i = 0;
    int j;
    int k;

    while(i < 3){
        j = 0;
        while(j < 3){
            k = 0;
            while(k < 3){
                mul[i][j] = mul[i][j] + x[i][k] * y[k][j];
                k = k + 1;
            }
            j = j + 1;
        }
        i = i + 1;
    }
}

fun void transpuesta(){
    int i = 0;
    int j;

    while(i < 3){
        j = 0;
        while(j < 3){
            trans[j][i] = x[i][j];
            j = j + 1;
        }
        i = i + 1;
    }
}

* {
    multiplica();
    transpuesta();
    imprime_matriz();
}
```

## **Graficar**

Este lenguaje te permite graficar muchas figuras y te permite sacar tu lado creativo para generar cualquier cosa.

```
program spiral;

* {
    int x = 1;
    speed("fastest");
    while(x < 400){
        go(50 + x);
        right(90.911);
        x = x + 1;
    }
    exitonclick;
}
```

