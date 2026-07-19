# Índice — Diagramas de Sequência

Este documento centraliza todos os diagramas de sequência produzidos para o projeto **Calculadora de Formas & Física**, mapeando cada User Story ao seu respectivo arquivo.

---

## Visão Geral

| ID    | User Story                                      | Arquivo                                                   | Cenários |
|-------|-------------------------------------------------|-----------------------------------------------------------|----------|
| US01  | Calcular área de figuras geométricas            | [DS_US01_CalcularArea.md](DS_US01_CalcularArea.md)         | 8        |
| US02  | Calcular perímetro de figuras geométricas       | [DS_US02_CalcularPerimetro.md](DS_US02_CalcularPerimetro.md) | 9      |
| US03  | Calcular velocidade média                       | [DS_US03_VelocidadeMedia.md](DS_US03_VelocidadeMedia.md)   | 4        |
| US04  | Calcular Movimento Uniforme (MU)                | [DS_US04_MovimentoUniforme.md](DS_US04_MovimentoUniforme.md) | 5      |
| US05  | Calcular Movimento Uniformemente Variado (MUV)  | [DS_US05_MovimentoUniformementeVariado.md](DS_US05_MovimentoUniformementeVariado.md) | 6 |
| US06  | Calcular queda livre                            | [DS_US06_QuedaLivre.md](DS_US06_QuedaLivre.md)             | 6        |
| US07  | Calcular lançamento vertical                    | [DS_US07_LancamentoVertical.md](DS_US07_LancamentoVertical.md) | 6     |
| US08  | Navegar entre Matemática e Física               | [DS_US08_Navegacao.md](DS_US08_Navegacao.md)               | 4        |
| US09  | Informar dados para os cálculos                 | [DS_US09_InformarDados.md](DS_US09_InformarDados.md)       | 5        |
| US10  | Visualizar o resultado                          | [DS_US10_VisualizarResultado.md](DS_US10_VisualizarResultado.md) | 5   |

**Total: 10 User Stories · 58 cenários documentados**

---

## Participantes Recorrentes nos Diagramas

| Participante              | Papel                                                                 |
|---------------------------|-----------------------------------------------------------------------|
| `Usuario`                 | Ator externo — interage via terminal (input/output)                   |
| `menu_principal`          | Ponto de entrada; exibe menu raiz e despacha para Matemática/Física   |
| `menu_matematica`         | Sub-menu de operações matemáticas (área e perímetro)                  |
| `menu_fisica`             | Sub-menu de operações de física (velocidades)                         |
| `menu_area`               | Sub-menu de figuras para cálculo de área                              |
| `menu_perimetro`          | Sub-menu de figuras para cálculo de perímetro                         |
| `menu_velocidades`        | Sub-menu com todas as operações de velocidade e cinemática            |
| `MenuDispatcher`          | Resolve a opção digitada e chama a operação correspondente            |
| `registro_operacoes`      | Fábrica que instancia as classes concretas de operação                |
| `OperacaoXxx`             | Classe concreta (herda `OperacaoMatematica` ou `OperacaoFisica`)      |
| `area.py / perimetro.py`  | Módulos com funções puras de cálculo matemático                       |
| `velocidades.py`          | Módulo com funções puras de cálculo de física                         |

---

## Padrão de Fluxo Geral

Todos os diagramas seguem o mesmo padrão de execução do sistema:

```
Usuario → Menu → MenuDispatcher → RegistroOperacoes
       → OperacaoXxx.calcular() → função do módulo
       → solicita entradas ao Usuario
       → executa cálculo
       → exibe resultado ao Usuario
       → retorna ao loop do menu
```

---

## Observações sobre Exceções Documentadas

| Exceção                                | US       | Comportamento atual              |
|----------------------------------------|----------|----------------------------------|
| Opção de menu inválida                 | US08     | Mensagem + retorna ao loop       |
| Tempo = 0 na velocidade média          | US03     | `ZeroDivisionError` não tratado  |
| Entrada não numérica (`ler_numero`)    | US09     | `ValueError` não tratado         |
| Campo em branco (`ler_numero`)         | US09     | `ValueError` não tratado         |
| Torricelli com v² < 0                  | US05     | Retorna `None` + mensagem        |
| Sub-menu inválido (queda livre / LV)   | US06/07  | Mensagem + retorna ao menu       |
