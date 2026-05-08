import random

alfabeto = ["A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S","T", "U", "V", "W", "X", "Y", "Z"]

random.shuffle(alfabeto)

letra = input("Digite uma letra do alfabeto: ").upper()

while not letra.isalpha() or len(letra) != 1:
    letra = input("Letra inválida. Digite apenas UMA letra: ").upper()

posicao = input("Em que posição você acha que ela está? (0 a 25): ")

while not posicao.isdigit() or int(posicao) >= len(alfabeto):
    posicao = input("Digite apenas números (0 a 25): ")

posicao = int(posicao)

if alfabeto[posicao] == letra:
    print("Você ACERTOU!")
else:
    print(f"Você errou!\nA letra {letra} estava na posição {alfabeto.index(letra)}")
print(alfabeto)