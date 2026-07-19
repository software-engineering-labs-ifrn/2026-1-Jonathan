# Índice — Diagramas de Sequência

Diagramas de sequência do projeto **Calculadora de Formas & Física**. Cada arquivo contém um único diagrama por User Story, cobrindo o fluxo principal (caminho feliz) e os fluxos alternativos/de exceção (falhas) dentro do mesmo diagrama usando `alt` e `opt`.

---

## Diagramas

| ID    | User Story                                     | Arquivo                                                                                                    |
|-------|------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| US01  | Calcular área de figuras geométricas           | [DS_US01_CalcularArea.md](DS_US01_CalcularArea.md)                                                         |
| US02  | Calcular perímetro de figuras geométricas      | [DS_US02_CalcularPerimetro.md](DS_US02_CalcularPerimetro.md)                                               |
| US03  | Calcular velocidade média                      | [DS_US03_VelocidadeMedia.md](DS_US03_VelocidadeMedia.md)                                                   |
| US04  | Calcular Movimento Uniforme (MU)               | [DS_US04_MovimentoUniforme.md](DS_US04_MovimentoUniforme.md)                                               |
| US05  | Calcular Movimento Uniformemente Variado (MUV) | [DS_US05_MovimentoUniformementeVariado.md](DS_US05_MovimentoUniformementeVariado.md)                       |
| US06  | Calcular queda livre                           | [DS_US06_QuedaLivre.md](DS_US06_QuedaLivre.md)                                                             |
| US07  | Calcular lançamento vertical                   | [DS_US07_LancamentoVertical.md](DS_US07_LancamentoVertical.md)                                             |
| US08  | Navegar entre Matemática e Física              | [DS_US08_Navegacao.md](DS_US08_Navegacao.md)                                                               |
| US09  | Informar dados para os cálculos                | [DS_US09_InformarDados.md](DS_US09_InformarDados.md)                                                       |
| US10  | Visualizar o resultado                         | [DS_US10_VisualizarResultado.md](DS_US10_VisualizarResultado.md)                                           |

---

## Estrutura de cada diagrama

Todos os diagramas seguem o mesmo padrão:

- **Fluxo principal** — sequência completa com entradas válidas e resultado exibido com sucesso.
- **`alt` para entradas** — dentro de cada `loop` de coleta de dados, mostra o que acontece com entrada inválida (texto, campo vazio, tipo errado).
- **`alt` para resultados** — quando o cálculo pode produzir um resultado inválido (ex: Torricelli com v² < 0 ou divisão por zero na velocidade média).
- **`alt` para navegação** — opção voltar e opção inválida de menu onde aplicável.

---

## Exceções documentadas por US

| Exceção                                      | US afetadas  | Comportamento atual                     |
|----------------------------------------------|--------------|-----------------------------------------|
| Entrada não numérica (`float("abc")`)        | US01–US07,09 | `ValueError` não tratado — traceback    |
| Campo vazio (`float("")`)                    | US01–US07,09 | `ValueError` não tratado — traceback    |
| Float onde int é esperado (`int("3.5")`)     | US02, US09   | `ValueError` não tratado — traceback    |
| Tempo = 0 na velocidade média                | US03         | `ZeroDivisionError` não tratado         |
| Torricelli com v² < 0                        | US05         | Retorna `None` + exibe mensagem de erro |
| Sub-opção inválida (queda livre / lanç. vert.)| US06, US07  | Exibe "Opção inválida!" e retorna       |
| Opção inválida no menu principal             | US08         | Exibe "Opção inválida!" e retorna       |
