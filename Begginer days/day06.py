#Funções
#As funções tem um papel importantissimo durante um código. As funções são nada mais nada menos que
#um conjunto de códigos que tem um objetivo especifico, e pode ser utilizada pelo programa inteiro, sem a
#necessidade de recriar todo o mesmo código sempre que for necessário.

#Uma função é definida com a palavra chave Def, seguida do nome da função e após isso os ()
def func():
    print("Olá!")

#Uma função por si só não é capaz de fazer nada, a menos que ela seja chamada pelo programa.
#O Call da funão acontece quando se escreve apenas o nome da função, em qualquer parte do código, juntamente
#dos parenteses e, se necessário, os atributos da função
func()

#A função While(), como o for() é um operador de repetição no qual, diferente do for(), usa-se quando não se
#sabe ao certo quantas vezes a ação será repetida.
#Seu set é Enquanto (algo for verdadeiro) todo o código abaixo acontecerá.

#Setando a variavel de comando do while.
bool = True
#Setando uma var de controle de quantidade.
cont = 0
#Enquanto a variavel Bool for verdadeira
while(bool):
    #A função func() será chamada e a var cont será aumentada em 1
    func()
    cont += 1
    #Quando a var cont for 5 ou maior, a variavel de comando bool ira se tornar falsa, e o loop irá parar.
    if cont >=5:
        bool = False
