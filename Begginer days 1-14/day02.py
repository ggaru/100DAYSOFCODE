#O uso dos [] faz com que o print seja direcionado apenas ao caracter de numero 4 na string
#Retorna a letra "O"
print("Hello"[4])
#É possivel também contar do final para o começo, retornando a letra "H". (mesmo resultado que utilizar o [0])
#A contagem começa apartir do -1.
print("Hello"[-5])

#Tipos de dados
#Strings - Letras ou cadeia de letras reconheciveis pelo uso de ""
print("Olá")
#Integers - Números
print(123)
#Large_Integers
print(123_234)
#Float - Números quebrados, reconheciveis pelo "."
print(24.97)
#Boolean - Tipo de dado que só retorna dois possiveis valores. "0" sendo Falso e "1" sendo Verdadeiro
#retorna 1
print(True)
#retorna 0
print(False)

#A função Len() recebe uma string e retorna a quantidade total de caracteres da string. O retorno será 4
print(len("Vini"))

#A função Type() recebe qualquer tipo de váriavel e retorna o seu tipo de data.
#O retorno será "String"
print(type("Vini"))
#O retorno será "Integer"
print(type(2))
#O retorno será "Float"
print(type(2.5))
#O retorno será "Boolean"
print(type(True))

#A função Int() recebe uma váriavel e converte-a para o tipo de data Integer. Não é possivel utilizar letras.
int("2")
#O retorno será o tipo Integer 5
print(int("2") + int("3"))

#A função Str() recebe uma váriavel e transforma-a em texto, convertendo-a para o tipo String
print(str(2))

#A função Float() recebe uma variável e transforma-a em um número quebrado, convertendo-a para o tipo Float.
#Não é possivel utilizar letras.
print(float(5))

#A função Bool() recebe uma variável e converte-a para o tipo Boolean, sendo Verdadeiro ou Falso.
print(bool(0))

#O que acontece neste código é que o usuário é primeiramente recebido por um input (seu nome).
#Por se tratar de um tipo String, o programa chama a função Len() para ver o Length, que retorna um número.
#Para evitar erro de concatenação, o retorno precisa então ser convertido em String.
#Como String, o retorno é adicionado ao print e retorna o número de letras no nome do usuário.
print("Quantidade de letras no seu nome:" + str(len(input("Qual seu nome?: "))))

#Operadores
#Retorna a Soma dos valores.
print(4 + 4)
#Retorna a Subtração dos valores.
print(4 - 4)
#Retorna a Divisão dos valores, retornando o tipo Float.
print(4 / 4)
#Retorna a Divisão dos valores e então, converte-o em Int.
print(4 // 4)
#Retorna a Multiplicação dos valores.
print(4 * 4)
#Retorna a Exponênciação dos valores.
print(4 ** 4)

#Define uma variavel chamada Val com o tipo Float
val = 30.85
#Retorna a variavel Val
print(val)
#Retorna também a variavel, porém, por converte-la para int, os valores depois do "." são excluidos. O retorno será "30"
print(int(val))
#A função Round() recebe uma variavel do tipo Float e arredonda o seu valor. O retorno será "31"
print(round(val))
#É possivel também usa-la para definir o limite de caracteres depois do ".". O retorno será "30.9
print(round(val,1))

#Setando duas váriaveis
x = 11
y = 15
#O uso do "F" no começo da String acontece para fazer a inserção, utilizando as {}, de variáveis dentro da String
print(f"Eu tenho {x} anos e ele tem {y} anos")

#DESAFIO DIA 02 - TIP CALCULATOR
print("Bem vindo ao Tip Calculator!")
total = float(input("Quanto foi o total?: "))
tip = int(input("Quanto de taxa você gostaria de pagar? (10%, 12% ou 15%): "))
div = int(input("Quantas pessoas irão dividir?: "))
result = round(((total + ((tip/100)*total))/div),2)
print(round(result,2))