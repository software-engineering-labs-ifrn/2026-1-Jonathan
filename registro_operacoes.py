"""Registro central das operações concretas usadas pelos menus."""

from operacoes import (
    OperacaoAreaCirculo,
    OperacaoAreaHexagono,
    OperacaoAreaPentagono,
    OperacaoAreaPoligonoNLados,
    OperacaoAreaQuadrado,
    OperacaoAreaRetangulo,
    OperacaoAreaTriangulo,
    OperacaoEquacaoTorricelli,
    OperacaoLancamentoVertical,
    OperacaoMovimentoUniforme,
    OperacaoMovimentoUniformementeVariado,
    OperacaoPerimetroCirculo,
    OperacaoPerimetroHexagono,
    OperacaoPerimetroPentagono,
    OperacaoPerimetroPoligonoNLados,
    OperacaoPerimetroQuadrado,
    OperacaoPerimetroRetangulo,
    OperacaoPerimetroTriangulo,
    OperacaoQuedaLivre,
    OperacaoVelocidadeAngular,
    OperacaoVelocidadeFinalMuv,
    OperacaoVelocidadeMedia,
)


def _criar_operacoes(mapeamento):
    """Cria um mapa de opções para execução de operações."""
    return {opcao: construtor() if construtor is not None else None for opcao, construtor in mapeamento.items()}


def criar_operacoes_perimetro():
    """Registra as operações disponíveis no menu de perímetros."""
    return _criar_operacoes(
        {
            "1": OperacaoPerimetroQuadrado,
            "2": OperacaoPerimetroRetangulo,
            "3": OperacaoPerimetroTriangulo,
            "4": OperacaoPerimetroCirculo,
            "5": OperacaoPerimetroPentagono,
            "6": OperacaoPerimetroHexagono,
            "7": OperacaoPerimetroPoligonoNLados,
            "0": None,
        }
    )


def criar_operacoes_area():
    """Registra as operações disponíveis no menu de áreas."""
    return _criar_operacoes(
        {
            "1": OperacaoAreaQuadrado,
            "2": OperacaoAreaRetangulo,
            "3": OperacaoAreaTriangulo,
            "4": OperacaoAreaCirculo,
            "5": OperacaoAreaPentagono,
            "6": OperacaoAreaHexagono,
            "7": OperacaoAreaPoligonoNLados,
            "0": None,
        }
    )


def criar_operacoes_velocidades():
    """Registra as operações disponíveis no menu de velocidades."""
    return _criar_operacoes(
        {
            "1": OperacaoVelocidadeMedia,
            "2": OperacaoMovimentoUniforme,
            "3": OperacaoMovimentoUniformementeVariado,
            "4": OperacaoVelocidadeFinalMuv,
            "5": OperacaoEquacaoTorricelli,
            "6": OperacaoQuedaLivre,
            "7": OperacaoLancamentoVertical,
            "8": OperacaoVelocidadeAngular,
            "0": None,
        }
    )
