mensagens_originais = [
    "H3llo World!",
    "Temos1",
    "Pr0blema."
]

chave_substituicao = {
    'a': 'x', 'b': 'y', 'c': 'z', 'd': 'w', 'e': 'v',
    'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
    'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
    'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
    'u': 'f', 'v': 'e', 'w': 'd', 'x': 'a', 'y': 'b',
    'z': 'c'
}

chave_numerica = 5  # Chave para a codificação numérica

mensagens_codificadas = []
for mensagem in mensagens_originais:
    mensagem_criptografada = ""
    for char in mensagem:
        if 'a' <= char <= 'z':
            mensagem_criptografada += chave_substituicao.get(char, char)
        elif 'A' <= char <= 'Z':
            mensagem_criptografada += chave_substituicao.get(char.lower(), char.lower()).upper()
        elif '0' <= char <= '9':
            numero_criptografado = (int(char) + chave_numerica) % 10
            mensagem_criptografada += str(numero_criptografado)
        else:
            mensagem_criptografada += char
    mensagens_codificadas.append(mensagem_criptografada)

print("Mensagens Codificadas:")
for msg in mensagens_codificadas:
    print(msg)

print("\nDecodificando as mensagens:")

chave_de_substituicao_inversa = {v: k for k, v in chave_substituicao.items()}
chave_numerica_decifracao = -5

for mensagem_codificada in mensagens_codificadas:
    mensagem_decifrada = ""
    for char in mensagem_codificada:
        if 'a' <= char <= 'z':
            mensagem_decifrada += chave_de_substituicao_inversa.get(char, char)
        elif 'A' <= char <= 'Z':
            mensagem_decifrada += chave_de_substituicao_inversa.get(char.lower(), char.lower()).upper()
        elif '0' <= char <= '9':
            numero_decifrado = (int(char) + chave_numerica_decifracao) % 10
            mensagem_decifrada += str(numero_decifrado)
        else:
            mensagem_decifrada += char
    print(f"Mensagem Codificada: {mensagem_codificada}")
    print(f"Mensagem Decifrada: {mensagem_decifrada}")