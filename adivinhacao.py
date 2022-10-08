# Jogo da Adivinhação
print('Bem Vindo!')
resposta = input('Gostaria de Jogar? (S/N): ')
dificuldade = int(input('Escolha um nível: [1,2,3]: '))
if dificuldade == 1:
    vidas = 20
elif dificuldade == 2:
    vidas = 10
elif dificuldade == 3:
    vidas = 5
valor_secreto = 42
print(f'Começando com {vidas} vidas!')
while resposta == 'S':
    chute = int(input('Chute um número: '))
    acima = chute > valor_secreto
    acerto = chute == valor_secreto
    abaixo = chute < valor_secreto
    if (acerto):
        print('Você acertou!')
        print(f'Você ganhou com {vidas} vidas!')
        break
    elif (acima):
        print('Valor acima do esperado, tente novamente!')
        vidas -= 1

    elif (abaixo):
        print('Valor abaixo do esperado, tente novamente!')
        vidas -= 1
    resposta = input(f'Gostaria de Continuar? (S/N) \nVocê tem mais {vidas} vidas!\n')
if vidas == 0 or resposta == 'N':
    print('Você perdeu :(')


