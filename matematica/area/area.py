import math

def area_quadrado():
    """Calcula a área de um quadrado"""
    lado = float(input("Digite o valor do lado do quadrado: "))
    area = lado ** 2
    print(f"Área do quadrado: {area}\n")


def area_retangulo():
    """Calcula a área de um retângulo"""
    comprimento = float(input("Digite o comprimento do retângulo: "))
    largura = float(input("Digite a largura do retângulo: "))
    area = comprimento * largura
    print(f"Área do retângulo: {area}\n")


def area_triangulo():
    """Calcula a área de um triângulo"""
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area = (base * altura) / 2
    print(f"Área do triângulo: {area}\n")


def area_circulo():
    """Calcula a área de um círculo"""
    raio = float(input("Digite o raio do círculo: "))
    area = math.pi * raio ** 2
    print(f"Área do círculo: {area:.2f}\n")


def area_pentagono():
    """Calcula a área de um pentágono regular"""
    lado = float(input("Digite o valor do lado do pentágono: "))
    area = (lado ** 2 * math.sqrt(25 + 10 * math.sqrt(5))) / 4
    print(f"Área do pentágono: {area:.2f}\n")


def area_hexagono():
    """Calcula a área de um hexágono regular"""
    lado = float(input("Digite o valor do lado do hexágono: "))
    area = (3 * math.sqrt(3) * lado ** 2) / 2
    print(f"Área do hexágono: {area:.2f}\n")


def area_poligono_n_lados():
    """Calcula a área de um polígono regular com N lados"""
    n = int(input("Digite a quantidade de lados: "))
    lado = float(input(f"Digite o valor do lado do polígono: "))
    apotema = float(input("Digite o valor do apótema do polígono: "))
    perimetro = n * lado
    area = (perimetro * apotema) / 2
    print(f"Área do polígono de {n} lados: {area:.2f}\n")
