palavras = ["Somos", "Como", "Pablo", "Escobar", "Murivaldo", "Pato"] # Palavras escolhidas pelo meu amigo Mauricio

maiores = [palavras[0]]
menores = [palavras[0]]

for palavra in palavras[1:]:

    if len(palavra) > len(maiores[0]):
        maiores = [palavra]

    elif len(palavra) == len(maiores[0]):
        maiores.append(palavra)

    if len(palavra) < len(menores[0]):
        menores = [palavra]

    elif len(palavra) == len(menores[0]):
        menores.append(palavra)

print(f"Maiores palavras: {maiores}\nMenores palavras: {menores}")