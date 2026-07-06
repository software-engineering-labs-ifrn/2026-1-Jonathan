```mermaid
classDiagram

classDiagram
direction LR
    class MenuDispatcher {
	    -operacoes: dict
	    +executar(opcao)
    }

    class OperacaoMatematica {
	    +calcular()
    }

    class OperacaoFisica {
	    +calcular()
    }

    class OperacaoPerimetroQuadrado {
	    +calcular()
    }

    class OperacaoPerimetroRetangulo {
	    +calcular()
    }

    class OperacaoPerimetroTriangulo {
	    +calcular()
    }

    class OperacaoPerimetroCirculo {
	    +calcular()
    }

    class OperacaoPerimetroPentagono {
	    +calcular()
    }

    class OperacaoPerimetroHexagono {
	    +calcular()
    }

    class OperacaoPerimetroPoligonoNLados {
	    +calcular()
    }

    class OperacaoAreaQuadrado {
	    +calcular()
    }

    class OperacaoAreaRetangulo {
	    +calcular()
    }

    class OperacaoAreaTriangulo {
	    +calcular()
    }

    class OperacaoAreaCirculo {
	    +calcular()
    }

    class OperacaoAreaPentagono {
	    +calcular()
    }

    class OperacaoAreaHexagono {
	    +calcular()
    }

    class OperacaoAreaPoligonoNLados {
	    +calcular()
    }

    class OperacaoVelocidadeMedia {
	    +calcular()
    }

    class OperacaoMovimentoUniforme {
	    +calcular()
    }

    class OperacaoMovimentoUniformementeVariado {
	    +calcular()
    }

    class OperacaoVelocidadeFinalMuv {
	    +calcular()
    }

    class OperacaoEquacaoTorricelli {
	    +calcular()
    }

    class OperacaoQuedaLivre {
	    +calcular()
    }

    class OperacaoLancamentoVertical {
	    +calcular()
    }

    class OperacaoVelocidadeAngular {
	    +calcular()
    }

	<<abstract>> OperacaoMatematica
	<<abstract>> OperacaoFisica

    OperacaoMatematica <|-- OperacaoPerimetroQuadrado
    OperacaoMatematica <|-- OperacaoPerimetroRetangulo
    OperacaoMatematica <|-- OperacaoPerimetroTriangulo
    OperacaoMatematica <|-- OperacaoPerimetroCirculo
    OperacaoMatematica <|-- OperacaoPerimetroPentagono
    OperacaoMatematica <|-- OperacaoPerimetroHexagono
    OperacaoMatematica <|-- OperacaoPerimetroPoligonoNLados
    OperacaoMatematica <|-- OperacaoAreaQuadrado
    OperacaoMatematica <|-- OperacaoAreaRetangulo
    OperacaoMatematica <|-- OperacaoAreaTriangulo
    OperacaoMatematica <|-- OperacaoAreaCirculo
    OperacaoMatematica <|-- OperacaoAreaPentagono
    OperacaoMatematica <|-- OperacaoAreaHexagono
    OperacaoMatematica <|-- OperacaoAreaPoligonoNLados
    OperacaoFisica <|-- OperacaoVelocidadeMedia
    OperacaoFisica <|-- OperacaoMovimentoUniforme
    OperacaoFisica <|-- OperacaoMovimentoUniformementeVariado
    OperacaoFisica <|-- OperacaoVelocidadeFinalMuv
    OperacaoFisica <|-- OperacaoEquacaoTorricelli
    OperacaoFisica <|-- OperacaoQuedaLivre
    OperacaoFisica <|-- OperacaoLancamentoVertical
    OperacaoFisica <|-- OperacaoVelocidadeAngular
    MenuDispatcher --> OperacaoMatematica : executa
    MenuDispatcher --> OperacaoFisica : executa

```