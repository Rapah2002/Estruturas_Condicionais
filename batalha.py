num_misseis = 5

naves_inimigas = ["Destruidor", "Aniquilador", "Predador", "Barba_Negra"]

print("Iniciando batalha intergaláctica!")
print(f"Mísseis disponíveis: {num_misseis}")
print(f"Naves inimigas detectadas: {naves_inimigas}\n")


while num_misseis > 0 and naves_inimigas:
    print(f"Mísseis restantes: {num_misseis}")
    print("Naves inimigas:")
    for i, nave in enumerate(naves_inimigas):
        print(f"{i} - {nave}")

    try:
        alvo_indice = int(input("Digite o índice da nave inimiga para atacar: "))

        if 0 <= alvo_indice < len(naves_inimigas):
            nave_destruida = naves_inimigas.pop(alvo_indice)
            num_misseis -= 1
            print(f"Nave inimiga '{nave_destruida}' destruída!\n")
        else:
            print("Índice inválido. Por favor, digite um índice da lista de naves.\n")
            continue
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.\n")
        continue

if num_misseis == 0:
    print("Sem mísseis! Retirada estratégica!")
elif not naves_inimigas:
    print("Vitória! Todas as naves inimigas foram destruídas!")