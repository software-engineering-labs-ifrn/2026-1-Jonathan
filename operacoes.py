"""Abstrações e implementações concretas das operações da calculadora."""

from abc import ABC, abstractmethod

from matematica.area.area import (
    area_circulo,
    area_hexagono,
    area_pentagono,
    area_poligono_n_lados,
    area_quadrado,
    area_retangulo,
    area_triangulo,
)
from matematica.perimetro.perimetro import (
    perimetro_circulo,
    perimetro_hexagono,
    perimetro_pentagono,
    perimetro_poligono_n_lados,
    perimetro_quadrado,
    perimetro_retangulo,
    perimetro_triangulo,
)
from fisica.velocidades import (
    equacao_torricelli,
    lancamento_vertical,
    movimento_uniforme,
    movimento_uniformemente_variado,
    queda_livre,
    velocidade_angular,
    velocidade_final_muv,
    velocidade_media,
)


class OperacaoMatematica(ABC):
    """Interface para operações matemáticas."""

    @abstractmethod
    def calcular(self):
        """Executa a operação."""
        pass


class OperacaoFisica(ABC):
    """Interface para operações de física."""

    @abstractmethod
    def calcular(self):
        """Executa a operação."""
        pass


class OperacaoPerimetroQuadrado(OperacaoMatematica):
    def calcular(self):
        return perimetro_quadrado()


class OperacaoPerimetroRetangulo(OperacaoMatematica):
    def calcular(self):
        return perimetro_retangulo()


class OperacaoPerimetroTriangulo(OperacaoMatematica):
    def calcular(self):
        return perimetro_triangulo()


class OperacaoPerimetroCirculo(OperacaoMatematica):
    def calcular(self):
        return perimetro_circulo()


class OperacaoPerimetroPentagono(OperacaoMatematica):
    def calcular(self):
        return perimetro_pentagono()


class OperacaoPerimetroHexagono(OperacaoMatematica):
    def calcular(self):
        return perimetro_hexagono()


class OperacaoPerimetroPoligonoNLados(OperacaoMatematica):
    def calcular(self):
        return perimetro_poligono_n_lados()


class OperacaoAreaQuadrado(OperacaoMatematica):
    def calcular(self):
        return area_quadrado()


class OperacaoAreaRetangulo(OperacaoMatematica):
    def calcular(self):
        return area_retangulo()


class OperacaoAreaTriangulo(OperacaoMatematica):
    def calcular(self):
        return area_triangulo()


class OperacaoAreaCirculo(OperacaoMatematica):
    def calcular(self):
        return area_circulo()


class OperacaoAreaPentagono(OperacaoMatematica):
    def calcular(self):
        return area_pentagono()


class OperacaoAreaHexagono(OperacaoMatematica):
    def calcular(self):
        return area_hexagono()


class OperacaoAreaPoligonoNLados(OperacaoMatematica):
    def calcular(self):
        return area_poligono_n_lados()


class OperacaoVelocidadeMedia(OperacaoFisica):
    def calcular(self):
        return velocidade_media()


class OperacaoMovimentoUniforme(OperacaoFisica):
    def calcular(self):
        return movimento_uniforme()


class OperacaoMovimentoUniformementeVariado(OperacaoFisica):
    def calcular(self):
        return movimento_uniformemente_variado()


class OperacaoVelocidadeFinalMuv(OperacaoFisica):
    def calcular(self):
        return velocidade_final_muv()


class OperacaoEquacaoTorricelli(OperacaoFisica):
    def calcular(self):
        return equacao_torricelli()


class OperacaoQuedaLivre(OperacaoFisica):
    def calcular(self):
        return queda_livre()


class OperacaoLancamentoVertical(OperacaoFisica):
    def calcular(self):
        return lancamento_vertical()


class OperacaoVelocidadeAngular(OperacaoFisica):
    def calcular(self):
        return velocidade_angular()
