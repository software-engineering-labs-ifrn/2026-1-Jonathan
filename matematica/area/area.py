import math


def ler_numero(mensagem):
    """Lê um valor numérico em ponto flutuante."""
    return float(input(mensagem))


def ler_inteiro(mensagem):
    """Lê um valor inteiro."""
    return int(input(mensagem))


def calcular_area_quadrado(lado):
    """Calcula a área de um quadrado."""
    return lado ** 2


def calcular_area_retangulo(comprimento, largura):
    """Calcula a área de um retângulo."""
    return comprimento * largura


def calcular_area_triangulo(base, altura):
    """Calcula a área de um triângulo."""
    return (base * altura) / 2


def calcular_area_circulo(raio):
    """Calcula a área de um círculo."""
    return math.pi * raio ** 2


def calcular_area_pentagono(lado):
    """Calcula a área de um pentágono regular."""
    return (lado ** 2 * math.sqrt(25 + 10 * math.sqrt(5))) / 4


def calcular_area_hexagono(lado):
    """Calcula a área de um hexágono regular."""
    return (3 * math.sqrt(3) * lado ** 2) / 2


def calcular_area_poligono_n_lados(n, lado, apotema):
    """Calcula a área de um polígono regular com N lados."""
    perimetro = n * lado
    return (perimetro * apotema) / 2


def area_quadrado():
    """Lê os dados e imprime a área do quadrado."""
    lado = ler_numero("Digite o valor do lado do quadrado: ")
    area = calcular_area_quadrado(lado)
    print(f"Área do quadrado: {area}\n")


def area_retangulo():
    """Lê os dados e imprime a área do retângulo."""
    comprimento = ler_numero("Digite o comprimento do retângulo: ")
    largura = ler_numero("Digite a largura do retângulo: ")
    area = calcular_area_retangulo(comprimento, largura)
    print(f"Área do retângulo: {area}\n")


def area_triangulo():
    """Lê os dados e imprime a área do triângulo."""
    base = ler_numero("Digite a base do triângulo: ")
    altura = ler_numero("Digite a altura do triângulo: ")
    area = calcular_area_triangulo(base, altura)
    print(f"Área do triângulo: {area}\n")


def area_circulo():
    """Lê os dados e imprime a área do círculo."""
    raio = ler_numero("Digite o raio do círculo: ")
    area = calcular_area_circulo(raio)
    print(f"Área do círculo: {area:.2f}\n")


def area_pentagono():
    """Lê os dados e imprime a área do pentágono."""
    lado = ler_numero("Digite o valor do lado do pentágono: ")
    area = calcular_area_pentagono(lado)
    print(f"Área do pentágono: {area:.2f}\n")


def area_hexagono():
    """Lê os dados e imprime a área do hexágono."""
    lado = ler_numero("Digite o valor do lado do hexágono: ")
    area = calcular_area_hexagono(lado)
    print(f"Área do hexágono: {area:.2f}\n")


def area_poligono_n_lados():
    """Lê os dados e imprime a área do polígono regular."""
    n = ler_inteiro("Digite a quantidade de lados: ")
    lado = ler_numero("Digite o valor do lado do polígono: ")
    apotema = ler_numero("Digite o valor do apótema do polígono: ")
    area = calcular_area_poligono_n_lados(n, lado, apotema)
    print(f"Área do polígono de {n} lados: {area:.2f}\n")
