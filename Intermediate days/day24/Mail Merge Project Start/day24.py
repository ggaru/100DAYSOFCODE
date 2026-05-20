
def montaNomes():
    list_names = []
    nome = ""
    for i in invited_names:
        if i == "\n":
            list_names.append(nome)
            nome = ""
        else:
            nome += i
    return list_names    
        
def montaCartas(names):
    for i in names:
        changed_letter = letter.replace('[name]',i)
        new_letter = open(f"Intermediate days\\day24\\Mail Merge Project Start\\Input\\Letters\\{i}.txt", "w")
        new_letter.write(changed_letter)


with open("Intermediate days\\day24\\Mail Merge Project Start\\Input\\Names\\invited_names.txt", "r") as names:
    invited_names = names.read()
       
with open("Intermediate days\\day24\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt") as letter:
    letter = letter.read()
   
list_names = montaNomes()
montaCartas(list_names)
#print(list_names)



