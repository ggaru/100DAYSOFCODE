        #Os parametros de uma função são passados para que algo aconteça utilizando-se AQUELES parametros
def format_name(f_name, l_name):
    """Usado abaixo da função para adicionar uma descrição a ela, podendo também ser utilizado para comentários de
        múltiplas linhas"""
    if f_name or l_name == "":
        return "You did'nt provide valid input's"
    formated_fname = f_name.title()
    formated_lname = l_name.title()
        #O uso do RETURN é feito para que, ao ser chamado a função, o que quer que venha dps do return seja o dado
        #que a função irá retornar ao programa. Nesse caso, ela toma o lugar do print() retornando as variaveis.
        #Essa deve ser a última linha da função.
    return f"{formated_fname}, {formated_lname}"
        #Passando os parametros para que a função chamada realize seu código, atráves de uma input
#print(format_name(input("Qual seu primeiro nome?"), input("Qual seu segundo nome?")))

#Prática 01 - Leap Year (ano bissexto)
def is_leap_year(year):
    if (year%4) != 0 or (year%400) != 0:
        return False
    return True
#print(is_leap_year(int(input("Digite um ano:"))))

#DESAFIO DAY 10 - CALCULATOR
n = 0
x = float(input("Digite um números:"))
def add(x, y):
    x = x+y
    return x
def sub(x, y):
    x = x-y
    return x
def div(x, y):
    x = x/y
    return x
def mult(x, y):
    x = x*y
    return x

def ops(x,y):
    if op == "+":
        result = add(x,y)
        print(result)
        return result
    elif op == "-":
        result = sub(x, y)
        print(result)
        return result
    elif op == "/":
        result = div(x, y)
        print(result)
        return result
    elif op == "*":
        result = mult(x, y)
        print(result)
        return result

playing = True

while playing != False:
    op = input("Digite um operador:")
    y = float(input("Digite outro número: "))
    x = ops(x,y)
    if input("Deseja continuar? ") != "s":
        playing = False