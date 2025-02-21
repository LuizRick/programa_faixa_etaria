import random

numero_secreto = random.randint(1,10)
#print(numero_secreto)
tentativa = 0
tentativas = 4
while tentativa <= tentativas:
    chute = int(input ('Informe um número de 1 a 10: '))
    print(f'O número escolhido foi {chute}!')

    if tentativa == 4:
        print(f'Fim das tentativas! O número secreto era {numero_secreto}!')
    
    elif chute == numero_secreto:
        print(f'Parabéns você acertou o número secreto: {chute}!')
        break
    elif chute != numero_secreto:
        print('Que pena, você errou! :(')
    tentativa += 1
    

'''if tentativa == tentativas:
    print(f'Fim das tentativas! O número secreto era {numero_secreto}!')
     '''

