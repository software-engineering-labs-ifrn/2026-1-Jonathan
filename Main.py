"""Ponto de entrada da calculadora interativa."""

from registro_operacoes import (
    criar_operacoes_area,
    criar_operacoes_perimetro,
    criar_operacoes_velocidades,
)


class MenuDispatcher:
    """Dispara ações do menu sem depender de implementações concretas."""

    def __init__(self, operacoes):
        self.operacoes = operacoes

    def executar(self, opcao):
        """Executa a ação associada à opção escolhida."""
        acao = self.operacoes.get(opcao)
        if acao is None:
            print("Opção inválida! Tente novamente.")
            return True
        if hasattr(acao, "calcular"):
            acao.calcular()
            return True

        resultado = acao()
        return True if resultado is None else resultado


def executar_menu(opcao, operacoes):
    """Executa um menu utilizando o dispatcher de ações."""
    dispatcher = MenuDispatcher(operacoes)
    return dispatcher.executar(opcao)


def voltar_menu():
    """Retorna False para indicar que o menu deve voltar."""
    return False


def sair_programa():
    """Imprime a mensagem de saída e indica encerramento."""
    print("\nAté logo!")
    return False


def menu_principal():
    """Exibe o menu principal do projeto"""
    while True:
        print("\n" + "="*50)
        print("    CALCULADORA DE FORMAS & FÍSICA")
        print("="*50)
        print("\n1 - Matemática")
        print("2 - Física")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")
        operacoes = {
            "1": menu_matematica,
            "2": menu_fisica,
            "0": sair_programa,
        }

        dispatcher = MenuDispatcher(operacoes)
        if not dispatcher.executar(opcao):
            break


def menu_matematica():
    """Menu para cálculos matemáticos"""
    while True:
        print("\n" + "-"*50)
        print("           CÁLCULOS MATEMÁTICOS")
        print("-"*50)
        print("\n1 - Calcular Perímetro")
        print("2 - Calcular Área")
        print("0 - Voltar ao menu principal")

        opcao = input("\nEscolha uma opção: ")
        operacoes = {
            "1": menu_perimetro,
            "2": menu_area,
            "0": voltar_menu,
        }

        dispatcher = MenuDispatcher(operacoes)
        if not dispatcher.executar(opcao):
            break


def menu_fisica():
    """Menu para cálculos de física"""
    while True:
        print("\n" + "-"*50)
        print("           CÁLCULOS DE FÍSICA")
        print("-"*50)
        print("\n1 - Velocidades")
        print("0 - Voltar ao menu principal")

        opcao = input("\nEscolha uma opção: ")
        operacoes = {
            "1": menu_velocidades,
            "0": voltar_menu,
        }

        dispatcher = MenuDispatcher(operacoes)
        if not dispatcher.executar(opcao):
            break


def menu_perimetro():
    """Menu para calcular perímetros"""
    while True:
        print("\n" + "-"*50)
        print("           CALCULADORA DE PERÍMETROS")
        print("-"*50)
        print("\n1 - Quadrado")
        print("2 - Retângulo")
        print("3 - Triângulo")
        print("4 - Círculo")
        print("5 - Pentágono")
        print("6 - Hexágono")
        print("7 - Polígono de N lados")
        print("0 - Voltar ao menu principal")

        opcao = input("\nEscolha uma opção (1-7): ")
        operacoes = criar_operacoes_perimetro()
        operacoes["0"] = voltar_menu

        dispatcher = MenuDispatcher(operacoes)
        if not dispatcher.executar(opcao):
            break


def menu_area():
    """Menu para calcular áreas"""
    while True:
        print("\n" + "-"*50)
        print("             CALCULADORA DE ÁREAS")
        print("-"*50)
        print("\n1 - Quadrado")
        print("2 - Retângulo")
        print("3 - Triângulo")
        print("4 - Círculo")
        print("5 - Pentágono")
        print("6 - Hexágono")
        print("7 - Polígono de N lados")
        print("0 - Voltar ao menu anterior")

        opcao = input("\nEscolha uma opção (1-7): ")
        operacoes = criar_operacoes_area()
        operacoes["0"] = voltar_menu

        dispatcher = MenuDispatcher(operacoes)
        if not dispatcher.executar(opcao):
            break


def menu_velocidades():
    """Menu para calcular velocidades"""
    while True:
        print("\n" + "-"*50)
        print("           CALCULADORA DE VELOCIDADES")
        print("-"*50)
        print("\n1 - Velocidade Média")
        print("2 - Movimento Uniforme (MU)")
        print("3 - Movimento Uniformemente Variado (MUV)")
        print("4 - Velocidade Final no MUV")
        print("5 - Equação de Torricelli")
        print("6 - Queda Livre")
        print("7 - Lançamento Vertical")
        print("8 - Velocidade Angular")
        print("0 - Voltar ao menu anterior")

        opcao = input("\nEscolha uma opção (1-8): ")
        operacoes = criar_operacoes_velocidades()
        operacoes["0"] = voltar_menu

        dispatcher = MenuDispatcher(operacoes)
        if not dispatcher.executar(opcao):
            break


if __name__ == "__main__":
    menu_principal()
