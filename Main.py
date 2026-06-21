from matematica.perimetro.perimetro import *
from matematica.area.area import *


def menu_principal():
    """Exibe o menu principal do projeto"""
    while True:
        print("\n" + "="*50)
        print("       CALCULADORA DE FORMAS GEOMÉTRICAS")
        print("="*50)
        print("\n1 - Calcular Perímetro")
        print("2 - Calcular Área")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            menu_perimetro()
        elif opcao == "2":
            menu_area()
        elif opcao == "0":
            print("\nAté logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


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
        
        if opcao == "1":
            perimetro_quadrado()
        elif opcao == "2":
            perimetro_retangulo()
        elif opcao == "3":
            perimetro_triangulo()
        elif opcao == "4":
            perimetro_circulo()
        elif opcao == "5":
            perimetro_pentagono()
        elif opcao == "6":
            perimetro_hexagono()
        elif opcao == "7":
            perimetro_poligono_n_lados()
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")


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
        print("0 - Voltar ao menu principal")
        
        opcao = input("\nEscolha uma opção (1-7): ")
        
        if opcao == "1":
            area_quadrado()
        elif opcao == "2":
            area_retangulo()
        elif opcao == "3":
            area_triangulo()
        elif opcao == "4":
            area_circulo()
        elif opcao == "5":
            area_pentagono()
        elif opcao == "6":
            area_hexagono()
        elif opcao == "7":
            area_poligono_n_lados()
        elif opcao == "0":
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu_principal()
