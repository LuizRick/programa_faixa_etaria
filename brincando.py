import random

numero_secreto = random.randint(1,10)
#print(numero_secreto)
tentativa = 1
tentativas = 5
while tentativa <= tentativas:
    chute = int(input ('Informe um número de 1 a 10: '))
    print(f'O número escolhido foi {chute}!')

    if tentativa == 4:
        print(f'Fim das tentativas! O número secreto era {numero_secreto}!')
    
    elif chute == numero_secreto:
        print(f'Parabéns você acertou na tentativa {tentativa}. O número secreto: {chute}!')
        break
    elif chute > numero_secreto:
        print(f'Que pena, você errou! O numero secreto é menor que {chute}  Tentativa: {tentativa}')
    elif chute < numero_secreto:
        print(f'Que pena, você errou! O numero secreto é maior que {chute} Tentativa: {tentativa} :(')
    tentativa += 1
    

'''if tentativa == tentativas:
    print(f'Fim das tentativas! O número secreto era {numero_secreto}!')
     '''

