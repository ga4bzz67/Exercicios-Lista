tabuleiro = [" "] * 9
jogador = "X"

print("Posições: \n 0 | 1 | 2\n---+---+---\n 3 | 4 | 5\n---+---+---\n 6 | 7 | 8")

while True:
    print()
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}\n---+---+---\n {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}\n---+---+---\n {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
    print()

    posicao = input(f"Jogador {jogador}, digite uma posição: ")
    while not posicao.isdigit() or int(posicao) < 0 or int(posicao) > 8 or tabuleiro[int(posicao)] != " ":
        posicao = input("Posição inválida, digite novamente: ")
    posicao = int(posicao)
    
    tabuleiro[posicao] = jogador

    venceu = False

    combinacoes = [[0,1,2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for combinacao in combinacoes:
        a = combinacao[0]
        b = combinacao[1]
        c = combinacao[2]

        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] != " ":
            venceu = True
    
    if venceu:
        print()
        print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}\n---+---+---\n {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}\n---+---+---\n {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
        print()

        print(f"O Jogador {jogador} venceu!")
        break
    
    if " " not in tabuleiro:
        print()
        print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}\n---+---+---\n {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}\n---+---+---\n {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")
        print()
        print("Empate!")
        break

    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"