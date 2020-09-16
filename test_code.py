# definicion de la funcion basic ops
def basic_ops(a, b, op):
    # op es el ID de la operacion
    # a es el primer operando
    # b el segundo operando
    try:
        # intenta obtener parte entera de a y b
        int(a)
        int(b)
        import math
        # se separan en dos variables la parte decimal y entera de a y b
        parte_decimal_a, parte_entera_a = math.modf(a)
        parte_decimal_b, parte_entera_b = math.modf(b)
        if parte_decimal_a or parte_decimal_b != 0:
            # verifica si a o b tienen decimales
            print("Math argument out of domain of func")
            return 33
        else:
            if -127 < a < 127 and -127 < b < 127:
                # a y b solo puede estar en el rango de -127 a 127
                if op == 0:
                    # ID = 0 corresponde a la operacion suma a+b
                    suma = a+b
                    return suma
                if op == 1:
                    # ID = 1 corresponde a la operacion resta a-b
                    resta = a-b
                    return resta
                if op == 2:
                    # ID = 2 corresponde a la operacion AND
                    x = a & b
                    return x
                if op == 3:
                    # ID = 3 corresponde a la operacion OR
                    y = a | b
                    return y
                else:
                    print("No such process")
                    # si el parametro de entrada op es diferente de 0, 1, 2 o 3
                    return 3
            else:
                print("Value too large for defined data type")
                # cuando a o b no esta dentro del rango aceptado
                return 75
    except Exception:
        print("Math argument out of domain of func")
        # cuando a o b son strings
        return 33


def test_basicops0():
    assert basic_ops(1, 2, 0) == 3


def test_basicops1():
    assert basic_ops(1, 2, 1) == -1


def test_basicops2():
    assert basic_ops(4, 3, 2) == 0


def test_basicops3():
    assert basic_ops(4, 3, 3) == 7


def test_basicopserror3():
    assert basic_ops(2, 3, 4) == 3


def test_basicopserror33():
    assert basic_ops(4.5, 3, 0) == 33


def test_basicopserror75():
    assert basic_ops(130, 3, 0) == 75
