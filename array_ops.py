#definicion de la funcion basic ops

def basic_ops(a,b,op):
    #op es el ID de la operacion
    #a es el primer operando
    #b el segundo operando

    import math #aca se separan en dos varables la parte decimal y entera de a y b
    parte_decimal_a, parte_entera_a = math.modf(a)
    parte_decimal_b, parte_entera_b = math.modf(b)

    if parte_decimal_a or parte_decimal_b != 0: #verifica que sean numeros enteros a y b
        print("Error en alguno de los operadores")
        print("Digite únicamente números enteros")
    else:  
        if -127 << a << 127 and -127 << b << 127: #a y b solo puede estar en el rango de -127 a 127
            if op == 0: #ID = 0 corresponde a la operacion suma a+b
                suma = a+b
                return suma
            if op == 1: #ID = 1 corresponde a la operacion resta a-b
                resta = a-b
                return resta
            if op == 2: #ID = 2 corresponde a la operacion AND
                if a & b != 0:
                    return True #al ser una operacion booleana retorna falso o verdadero
                else:
                    return False
            if op == 3: #ID = 3 corresponde a la operacion OR
                if a or b != 0:
                    return True #al ser una operacion booleana retorna falso o verdadero
                else:
                    return False
            else:
                print("Error de operación")
                print("Seleccione una operación con los números 0, 1, 2 o 3")
        else:
            print("Error de magnitud en los operandos")
            print("Digite operandos mayores que -127 y menores que 127")

def array_ops():
    gr1 = [] #crea el arreglo 1
    gr2 = [] #crea el arreglo 2  
    resultado = [] #arreglo de resultado

    n = int(input("Ingrese cantidad de elementos para los arreglos: "))

    for i in range(0,n): #agrega elementos al primer arreglo
        temp = int(input("Ingrese elemento primer arreglo:"))
        gr1.append(temp)

    for j in range(0,n): #agrega elementos al segundo arreglo
        temp = int(input("Ingrese elemento segundo arreglo:"))
        gr2.append(temp)

    op = int(input("Eliga la operacion que desea realizar (0:suma,1:resta,2:and,3:or)"))

    for k in range(0,n):
        resultado.append(basic_ops (gr1[k],gr2[k],op))

    print(resultado)
