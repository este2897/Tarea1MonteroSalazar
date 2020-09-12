#definicion de la funcion basic ops

def basic_ops(a,b,op):
    #op es el ID de la operacion
    #a es el primer operando
    #b el segundo operando

    import math #aca se separan en dos varables la parte decimal y entera de a y b
    parte_decimal_a, parte_entera_a = math.modf(a)
    parte_decimal_b, parte_entera_b = math.modf(b)

    if parte_decimal_a or parte_decimal_b != 0: #verifica que sean numeros enteros a y b
        print("Math argument out of domain of func")
        return 33
    else:  
        if -127 < a < 127 and -127 < b < 127: #a y b solo puede estar en el rango de -127 a 127
            if op == 0: #ID = 0 corresponde a la operacion suma a+b
                suma = a+b
                return suma
            if op == 1: #ID = 1 corresponde a la operacion resta a-b
                resta = a-b
                return resta
            if op == 2: #ID = 2 corresponde a la operacion AND
                x = a & b
                return x
            if op == 3: #ID = 3 corresponde a la operacion OR
                y = a | b
                return b
            else:
                print("No such process")
                return 3
        else:
            print("Value too large for defined data type")
            return 75
            

                
            
    
