import math


def ler_numero(mensagem):
    """Lê um valor numérico em ponto flutuante."""
    return float(input(mensagem))


def ler_inteiro(mensagem):
    """Lê um valor inteiro."""
    return int(input(mensagem))


def calcular_perimetro_quadrado(lado):
    """Calcula o perímetro de um quadrado."""
    return 4 * lado


def calcular_perimetro_retangulo(comprimento, largura):
    """Calcula o perímetro de um retângulo."""
    return 2 * (comprimento + largura)


def calcular_perimetro_triangulo(lado1, lado2, lado3):
    """Calcula o perímetro de um triângulo."""
    return lado1 + lado2 + lado3


def calcular_perimetro_circulo(raio):
    """Calcula o perímetro (circunferência) de um círculo."""
    return 2 * math.pi * raio


def calcular_perimetro_pentagono(lado):
    """Calcula o perímetro de um pentágono regular."""
    return 5 * lado


def calcular_perimetro_hexagono(lado):
    """Calcula o perímetro de um hexágono regular."""
    return 6 * lado


def calcular_perimetro_poligono_n_lados(n, lado):
    """Calcula o perímetro de um polígono com N lados."""
    return n * lado


def perimetro_quadrado():
    """Lê os dados e imprime o perímetro do quadrado."""
    lado = ler_numero("Digite o valor do lado do quadrado: ")
    perimetro = calcular_perimetro_quadrado(lado)
    print(f"Perímetro do quadrado: {perimetro}\n")


def perimetro_retangulo():
    """Lê os dados e imprime o perímetro do retângulo."""
    comprimento = ler_numero("Digite o comprimento do retângulo: ")
    largura = ler_numero("Digite a largura do retângulo: ")
    perimetro = calcular_perimetro_retangulo(comprimento, largura)
    print(f"Perímetro do retângulo: {perimetro}\n")


def perimetro_triangulo():
    """Lê os dados e imprime o perímetro do triângulo."""
    lado1 = ler_numero("Digite o primeiro lado do triângulo: ")
    lado2 = ler_numero("Digite o segundo lado do triângulo: ")
    lado3 = ler_numero("Digite o terceiro lado do triângulo: ")
    perimetro = calcular_perimetro_triangulo(lado1, lado2, lado3)
    print(f"Perímetro do triângulo: {perimetro}\n")


def perimetro_circulo():
    """Lê os dados e imprime o perímetro da circunferência."""
    raio = ler_numero("Digite o raio do círculo: ")
    perimetro = calcular_perimetro_circulo(raio)
    print(f"Perímetro (circunferência) do círculo: {perimetro:.2f}\n")


def perimetro_pentagono():
    """Lê os dados e imprime o perímetro do pentágono."""
    lado = ler_numero("Digite o valor do lado do pentágono: ")
    perimetro = calcular_perimetro_pentagono(lado)
    print(f"Perímetro do pentágono: {perimetro}\n")


def perimetro_hexagono():
    """Lê os dados e imprime o perímetro do hexágono."""
    lado = ler_numero("Digite o valor do lado do hexágono: ")
    perimetro = calcular_perimetro_hexagono(lado)
    print(f"Perímetro do hexágono: {perimetro}\n")


def perimetro_poligono_n_lados():
    """Lê os dados e imprime o perímetro do polígono."""
    n = ler_inteiro("Digite a quantidade de lados: ")
    lado = ler_numero(f"Digite o valor do lado do polígono de {n} lados: ")
    perimetro = calcular_perimetro_poligono_n_lados(n, lado)
    print(f"Perímetro do polígono de {n} lados: {perimetro}\n")
