import random

print("Seja bem vindo ao Adivinhando!")
choice_number = input("Digite o número teto do desavio: ")

if choice_number.isdigit():
    choice_number = int(choice_number) 
else:
    print("ERROR: valor informado não é númerico. Favor executar o desafio novamnete e informe um numero!")
    quit()
    

random_number = random.randint(0, choice_number)

n_choices = 0 

while True:
    answer_user = input("Adivinhe o numero: ")
            
    if answer_user.isdigit():
        answer_user = int(answer_user)    
    else:    
        print("ERROR: valor informado não é númerico. Favor informe um numero!")
        continue

        n_choices = n_choices + 1

    if answer_user == random_number:
        print("Parabêns, você acertou!")
        break     
        
    elif answer_user > random_number:
        print("Chutou alto, o numero random é menor que isso...")
    else:
        print("Chutou baixo, o numero random é maior que isso...") 
        
print("Numero de tentativas: " + str(n_choices))        
