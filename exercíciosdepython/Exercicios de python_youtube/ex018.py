from math import radians,sin, cos, tan
angulo = float(input("Digite o ângulo: "))
seno = round(sin(radians(angulo)), 4)
cosseno = round(cos(radians(angulo)), 4)
tangente = round(tan(radians(angulo)), 4)

print(f"O ângulo de: {angulo} graus tem:\n"
        f"seno de: {seno}"
        f"\ncosseno de: {cosseno}"
        f"\ntangente de: {tangente}")