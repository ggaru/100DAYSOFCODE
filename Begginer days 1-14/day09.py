
#Dicionários, em python, são identificáveis pelo uso de {} na sua definição.
#Os dicionários recebem dois tipos de dados, as Keys e os Values.
first_dict = {
     "Teste" : "Testando o dicionário",
     "Teste2": "Teste de segunda entrada de dicionário",
     "Teste3": "dicionários são incriveis!"
 }

#printando todo o dicionário
print(first_dict)
#pritando o Value da Key "Teste"
print(first_dict["Teste"])

#Manipulação de dicionários
for i in first_dict:
    #printando cada Key no dicionário
    print(i)
    #usando as Keys para printar todos os valores
    print(first_dict[i])


#excluindo todo o dicionário
first_dict = {}
print(first_dict)

#Adicionando um novo Key e Value no Dicionário
first_dict["Novo"] = "Adicionando um novo item"
print(first_dict)

#Mudando o valor do Key no dicionário
first_dict["Novo"] = "Mudando o valor do dicionário"

#Prática 01 - Grading Program
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for i in student_scores:
    if student_scores[i] >= 91:
        student_grades[i] = "Outstanding"
    elif student_scores[i] >= 81 and student_scores[i] <= 90:
        student_grades[i] = "Exceeds Expectations"
    elif student_scores[i] >= 71 and student_scores[i] <= 80:
        student_grades[i] = "Acceptable"
    elif student_scores[i] <= 70:
        student_grades[i] = "Fail"
print(student_grades)

#Aninhando listas dentro do dicionário
travel_log = {
    "Brasil": ["Fortaleza", "Pernambuco", "São Paulo"],
    "Japão": ["Hiroshima", "Tóquio", "Osaka"]
}

#Printando uma posição especifica dentro da lista
print(travel_log["Brasil"][1])

#Lendo cada key e printando cada valor
for key in travel_log:
    for value in travel_log[key]:
        print(value)

#Aninhando dicionários e listas dentro de um mesmo dicionário.
#Note que a lista Cidades visitadas está dentro do dicionário Brasil, dentro do dicionário Travel_log2
travel_log2 = {
    "Brasil": {
        "Cidades visitadas": ["Fortaleza", "Bahia"],
        "Total de visitas": 12
    },
    "Japão": {
        "Cidades visitadas": ["Osaka", "Nagasaki"],
        "Total de visitas": 3
    }
}

#Acesse a cidade "Osaka"
print(travel_log2["Japão"]["Cidades visitadas"][0])

###DESAFIO DAY 09 - BLIND BID
bid_log = {}
playing = True
while playing:
    max_bid = {
        "buyer": 0
    }
    buyer = input("Qual seu nome?")
    bid = int(input("Qual sua aposta?"))
    bid_log[buyer] = bid

    for key in bid_log:
        for i in max_bid:
            if bid_log[key] > max_bid[i]:
                max_bid = {}
                max_bid[key] = bid_log[key]

    choose = input("Tem algum outro comprador?")
    if choose == "nao":
        for key in max_bid:
            print(f"E o vencedor foi '{key}' com a aposta no total de: {max_bid[key]}")
        playing = False
