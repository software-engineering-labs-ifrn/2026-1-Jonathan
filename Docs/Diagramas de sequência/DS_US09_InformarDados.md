# DS - US09: Informar Dados para os Cálculos

**User Story:** Como usuário, eu quero inserir os valores necessários para cada operação, para que eu possa obter resultados corretos.

> Esta User Story é transversal — ela representa o comportamento de entrada de dados que ocorre em todas as operações do sistema. Os fluxos abaixo mostram o padrão de coleta de dados e os cenários de entrada inválida.

---

## Fluxo Principal — Entrada de Dado Numérico Válido

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as Módulo de Cálculo (ler_numero)

    Calc-->>Usuario: Exibe prompt de entrada (ex: "Digite o valor do lado: ")
    Usuario->>Calc: Digita um valor numérico válido (ex: "7.5")
    Calc->>Calc: float("7.5") → 7.5
    Calc-->>Calc: Retorna 7.5 para a função de cálculo
    Note over Calc,Usuario: Valor aceito — fluxo de cálculo prossegue normalmente.
```

---

## Fluxo Alternativo — Entrada de Número Inteiro Válido

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as Módulo de Cálculo (ler_inteiro)

    Calc-->>Usuario: Exibe prompt de entrada (ex: "Digite a quantidade de lados: ")
    Usuario->>Calc: Digita um valor inteiro (ex: "8")
    Calc->>Calc: int("8") → 8
    Calc-->>Calc: Retorna 8 para a função de cálculo
    Note over Calc,Usuario: Usado em operações com polígonos de N lados.
```

---

## Fluxo — Múltiplas Entradas em Sequência

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as Módulo de Cálculo

    Note over Calc,Usuario: Exemplo: MUV exige 4 entradas em sequência.

    Calc-->>Usuario: "Digite a posição inicial (em metros): "
    Usuario->>Calc: "0"
    Calc-->>Usuario: "Digite a velocidade inicial (em m/s): "
    Usuario->>Calc: "10"
    Calc-->>Usuario: "Digite a aceleração (em m/s²): "
    Usuario->>Calc: "2"
    Calc-->>Usuario: "Digite o tempo (em segundos): "
    Usuario->>Calc: "5"
    Calc->>Calc: Todos os dados coletados — executa o cálculo
    Calc-->>Usuario: Exibe resultado
```

---

## Fluxo de Exceção — Dado Não Numérico Informado

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as Módulo de Cálculo (ler_numero)

    Calc-->>Usuario: Exibe prompt de entrada (ex: "Digite o valor do lado: ")
    Usuario->>Calc: Digita texto não numérico (ex: "abc")
    Calc->>Calc: float("abc") → ValueError
    Calc-->>Usuario: Erro não tratado — programa exibe traceback

    Note over Calc,Usuario: Comportamento atual: ValueError não capturado.<br/>Melhoria sugerida: envolver ler_numero() em try/except<br/>e solicitar nova entrada ao usuário.
```

---

## Fluxo de Exceção — Campo Deixado em Branco

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as Módulo de Cálculo (ler_numero)

    Calc-->>Usuario: Exibe prompt de entrada
    Usuario->>Calc: Pressiona Enter sem digitar nada ("")
    Calc->>Calc: float("") → ValueError
    Calc-->>Usuario: Erro não tratado — programa exibe traceback

    Note over Calc,Usuario: Mesmo comportamento do caso anterior.<br/>Ambos os casos evidenciam ausência de validação de entrada.
```
