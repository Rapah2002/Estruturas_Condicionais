import random

distancia_segura = 15

print(f"Distância segura inicial: {distancia_segura}")

while True:
    distancia_asteroide = random.randint(1, 10)
    print(f"Distância do asteroide mais próximo: {distancia_asteroide}")

    if distancia_asteroide < 3:
        print("PERIGO! Rota de colisão iminente!")
        break

    if distancia_asteroide < distancia_segura / 2:
        print("Aproximando-se de asteroide! Manobrando para manter distância...")

    distancia_segura += 2
    print(f"Nova distância segura: {distancia_segura}\n")

else:
    print("Navegação concluída com segurança! Todos os asteroides foram evitados.")