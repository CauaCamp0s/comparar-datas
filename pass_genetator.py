import random
import string

def pass_generator(len_pass = 8):
    ascii_options = string_ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    opitions  = ascii_options + number_options + punt_options
    
    password_user = ""
    
    for i in range(0, len_pass):
        digit = random.choice(opitions)
        password_user = password_user + digit  
        
    return password_user

choice_user = input("Quantos digitos na senha? ")

if choice_user.isdigit():
    choice_user = int(choice_user)
    
else: 
    print("Entrada invalida! ")
    quit()

response = password_generator(len_pass = choice_user)
print(f"Senha gerada:\n{response}")

