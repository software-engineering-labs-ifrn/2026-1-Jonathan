import math


def ler_numero(mensagem):
    """Lê um valor numérico em ponto flutuante."""
    return float(input(mensagem))


def calcular_velocidade_media(distancia, tempo):
    """Calcula a velocidade média."""
    return distancia / tempo


def calcular_posicao_movimento_uniforme(s0, velocidade, tempo):
    """Calcula a posição final no movimento uniforme."""
    return s0 + velocidade * tempo


def calcular_posicao_muv(s0, v0, aceleracao, tempo):
    """Calcula a posição final no movimento uniformemente variado."""
    return s0 + v0 * tempo + (aceleracao * tempo ** 2) / 2


def calcular_velocidade_final_muv(v0, aceleracao, tempo):
    """Calcula a velocidade final no MUV."""
    return v0 + aceleracao * tempo


def calcular_velocidade_final_torricelli(v0, aceleracao, deslocamento):
    """Calcula a velocidade final pela equação de Torricelli."""
    v_quadrado = v0 ** 2 + 2 * aceleracao * deslocamento
    if v_quadrado < 0:
        return None
    return math.sqrt(v_quadrado)


def calcular_altura_queda_livre(tempo, g=10):
    """Calcula a altura em queda livre."""
    return (g * tempo ** 2) / 2


def calcular_velocidade_queda_livre(tempo, g=10):
    """Calcula a velocidade em queda livre."""
    return g * tempo


def calcular_tempo_queda_livre(altura, g=10):
    """Calcula o tempo de queda livre."""
    return math.sqrt(2 * altura / g)


def calcular_altura_maxima_lancamento(v0, g=10):
    """Calcula a altura máxima no lançamento vertical."""
    return (v0 ** 2) / (2 * g)


def calcular_tempo_total_lancamento(v0, g=10):
    """Calcula o tempo total no lançamento vertical."""
    return (2 * v0) / g


def calcular_altura_lancamento(v0, tempo, g=10):
    """Calcula a altura em um instante do lançamento vertical."""
    return v0 * tempo - (g * tempo ** 2) / 2


def calcular_velocidade_angular_frequencia(frequencia):
    """Calcula a velocidade angular a partir da frequência."""
    return 2 * math.pi * frequencia


def calcular_velocidade_angular_periodo(periodo):
    """Calcula a velocidade angular a partir do período."""
    return (2 * math.pi) / periodo


def velocidade_media():
    """Lê os dados e imprime a velocidade média."""
    distancia = ler_numero("Digite a distância percorrida (em metros): ")
    tempo = ler_numero("Digite o tempo gasto (em segundos): ")
    velocidade = calcular_velocidade_media(distancia, tempo)
    print(f"Velocidade média: {velocidade:.2f} m/s\n")


def movimento_uniforme():
    """Lê os dados e imprime a posição final no movimento uniforme."""
    s0 = ler_numero("Digite a posição inicial (em metros): ")
    velocidade = ler_numero("Digite a velocidade (em m/s): ")
    tempo = ler_numero("Digite o tempo (em segundos): ")
    s = calcular_posicao_movimento_uniforme(s0, velocidade, tempo)
    print(f"Posição final: {s:.2f} m\n")


def movimento_uniformemente_variado():
    """Lê os dados e imprime a posição final no MUV."""
    s0 = ler_numero("Digite a posição inicial (em metros): ")
    v0 = ler_numero("Digite a velocidade inicial (em m/s): ")
    aceleracao = ler_numero("Digite a aceleração (em m/s²): ")
    tempo = ler_numero("Digite o tempo (em segundos): ")
    s = calcular_posicao_muv(s0, v0, aceleracao, tempo)
    print(f"Posição final: {s:.2f} m\n")


def velocidade_final_muv():
    """Lê os dados e imprime a velocidade final no MUV."""
    v0 = ler_numero("Digite a velocidade inicial (em m/s): ")
    aceleracao = ler_numero("Digite a aceleração (em m/s²): ")
    tempo = ler_numero("Digite o tempo (em segundos): ")
    v = calcular_velocidade_final_muv(v0, aceleracao, tempo)
    print(f"Velocidade final: {v:.2f} m/s\n")


def equacao_torricelli():
    """Lê os dados e imprime a velocidade final pela equação de Torricelli."""
    v0 = ler_numero("Digite a velocidade inicial (em m/s): ")
    aceleracao = ler_numero("Digite a aceleração (em m/s²): ")
    deslocamento = ler_numero("Digite o deslocamento (em metros): ")
    v = calcular_velocidade_final_torricelli(v0, aceleracao, deslocamento)

    if v is None:
        print("Erro: Velocidade ao quadrado não pode ser negativa!\n")
    else:
        print(f"Velocidade final: {v:.2f} m/s\n")


def queda_livre():
    """Lê os dados e imprime o resultado da queda livre."""
    print("\n1 - Calcular altura (H = g*t²/2)")
    print("2 - Calcular velocidade (V = g*t)")
    print("3 - Calcular tempo (t = √(2*H/g))")

    opcao = input("Escolha uma opção (1-3): ")

    g = 10

    if opcao == "1":
        tempo = ler_numero("Digite o tempo de queda (em segundos): ")
        altura = calcular_altura_queda_livre(tempo, g)
        print(f"Altura: {altura:.2f} m\n")
    elif opcao == "2":
        tempo = ler_numero("Digite o tempo de queda (em segundos): ")
        velocidade = calcular_velocidade_queda_livre(tempo, g)
        print(f"Velocidade: {velocidade:.2f} m/s\n")
    elif opcao == "3":
        altura = ler_numero("Digite a altura (em metros): ")
        tempo = calcular_tempo_queda_livre(altura, g)
        print(f"Tempo de queda: {tempo:.2f} s\n")
    else:
        print("Opção inválida!\n")


def lancamento_vertical():
    """Lê os dados e imprime o resultado do lançamento vertical."""
    print("\n1 - Altura máxima (H = V0²/2*g)")
    print("2 - Tempo total (t = 2*V0/g)")
    print("3 - Altura em um tempo específico (H = V0*t - g*t²/2)")

    opcao = input("Escolha uma opção (1-3): ")

    g = 10

    if opcao == "1":
        v0 = ler_numero("Digite a velocidade inicial (em m/s): ")
        altura_max = calcular_altura_maxima_lancamento(v0, g)
        print(f"Altura máxima: {altura_max:.2f} m\n")
    elif opcao == "2":
        v0 = ler_numero("Digite a velocidade inicial (em m/s): ")
        tempo_total = calcular_tempo_total_lancamento(v0, g)
        print(f"Tempo total: {tempo_total:.2f} s\n")
    elif opcao == "3":
        v0 = ler_numero("Digite a velocidade inicial (em m/s): ")
        tempo = ler_numero("Digite o tempo (em segundos): ")
        altura = calcular_altura_lancamento(v0, tempo, g)
        print(f"Altura: {altura:.2f} m\n")
    else:
        print("Opção inválida!\n")


def velocidade_angular():
    """Lê os dados e imprime a velocidade angular."""
    print("\n1 - Pela frequência (ω = 2π*f)")
    print("2 - Pelo período (ω = 2π/T)")

    opcao = input("Escolha uma opção (1-2): ")

    if opcao == "1":
        frequencia = ler_numero("Digite a frequência (em Hz): ")
        velocidade_angular = calcular_velocidade_angular_frequencia(frequencia)
        print(f"Velocidade angular: {velocidade_angular:.2f} rad/s\n")
    elif opcao == "2":
        periodo = ler_numero("Digite o período (em segundos): ")
        velocidade_angular = calcular_velocidade_angular_periodo(periodo)
        print(f"Velocidade angular: {velocidade_angular:.2f} rad/s\n")
    else:
        print("Opção inválida!\n")
