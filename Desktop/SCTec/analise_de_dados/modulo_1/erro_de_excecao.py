def dividir(a,b):
    r = 0
    try:
        r = a / b
        return print(r)
    except ZeroDivisionError:
        print('Erro inesperado. Desculpe')
    finally:
        print('Função executada')    

dividir(4,0)       