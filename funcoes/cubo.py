def calcular_volume(raio):
    volume_esfera = (4 / 3) * 3.14159 * raio**3
    volume_cubo = raio**3
    print(f"O volume da esfera é: {volume_esfera:.2f} metro cúbico")
    print(f"O volume do cubo é: {volume_cubo:.2f} metro cúbico")

raio_informado = float(input("Insira o valor do raio: "))
calcular_volume(raio_informado)


