import math

def perimetro_quadrado():
    """Calcula o perímetro de um quadrado"""
    lado = float(input("Digite o valor do lado do quadrado: "))
    perimetro = 4 * lado
    print(f"Perímetro do quadrado: {perimetro}\n")


def perimetro_retangulo():
    """Calcula o perímetro de um retângulo"""
    comprimento = float(input("Digite o comprimento do retângulo: "))
    largura = float(input("Digite a largura do retângulo: "))
    perimetro = 2 * (comprimento + largura)
    print(f"Perímetro do retângulo: {perimetro}\n")


def perimetro_triangulo():
    """Calcula o perímetro de um triângulo"""
    lado1 = float(input("Digite o primeiro lado do triângulo: "))
    lado2 = float(input("Digite o segundo lado do triângulo: "))
    lado3 = float(input("Digite o terceiro lado do triângulo: "))
    perimetro = lado1 + lado2 + lado3
    print(f"Perímetro do triângulo: {perimetro}\n")


def perimetro_circulo():
    """Calcula o perímetro (circunferência) de um círculo"""
    raio = float(input("Digite o raio do círculo: "))
    perimetro = 2 * math.pi * raio
    print(f"Perímetro (circunferência) do círculo: {perimetro:.2f}\n")


def perimetro_pentagono():
    """Calcula o perímetro de um pentágono regular"""
    lado = float(input("Digite o valor do lado do pentágono: "))
    perimetro = 5 * lado
    print(f"Perímetro do pentágono: {perimetro}\n")


def perimetro_hexagono():
    """Calcula o perímetro de um hexágono regular"""
    lado = float(input("Digite o valor do lado do hexágono: "))
    perimetro = 6 * lado
    print(f"Perímetro do hexágono: {perimetro}\n")


def perimetro_poligono_n_lados():
    """Calcula o perímetro de um polígono com N lados"""
    n = int(input("Digite a quantidade de lados: "))
    lado = float(input(f"Digite o valor do lado do polígono de {n} lados: "))
    perimetro = n * lado
    print(f"Perímetro do polígono de {n} lados: {perimetro}\n")
