# DS - US04: Calcular Movimento Uniforme (MU)

**User Story:** Como estudante, eu quero calcular o movimento uniforme, para que eu possa compreender o deslocamento de um corpo.

---

## Fluxo Principal — Calcular Posição Final no MU

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuVel as menu_velocidades
    participant Dispatcher as MenuDispatcher
    participant Registro as registro_operacoes
    participant Op as OperacaoMovimentoUniforme
    participant Calc as velocidades.py (movimento_uniforme)

    MenuVel-->>Usuario: Exibe menu de velocidades
    Usuario->>MenuVel: Digita "2" (Movimento Uniforme)
    MenuVel->>Registro: criar_operacoes_velocidades()
    Registro-->>MenuVel: {operacoes com OperacaoMovimentoUniforme, ...}
    MenuVel->>Dispatcher: executar("2")
    Dispatcher->>Op: OperacaoMovimentoUniforme.calcular()
    Op->>Calc: movimento_uniforme()

    Calc-->>Usuario: "Digite a posição inicial (em metros): "
    Usuario->>Calc: Informa s0 (ex: 10)
    Calc-->>Usuario: "Digite a velocidade (em m/s): "
    Usuario->>Calc: Informa velocidade (ex: 5)
    Calc-->>Usuario: "Digite o tempo (em segundos): "
    Usuario->>Calc: Informa tempo (ex: 8)
    Calc->>Calc: calcular_posicao_movimento_uniforme(10, 5, 8) → 10 + 5*8 = 50.00
    Calc-->>Usuario: "Posição final: 50.00 m"
```

---

## Fluxo Alternativo — Corpo em repouso (velocidade = 0)

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (movimento_uniforme)

    Calc-->>Usuario: "Digite a posição inicial (em metros): "
    Usuario->>Calc: Informa s0 (ex: 20)
    Calc-->>Usuario: "Digite a velocidade (em m/s): "
    Usuario->>Calc: Informa velocidade = 0
    Calc-->>Usuario: "Digite o tempo (em segundos): "
    Usuario->>Calc: Informa tempo (ex: 10)
    Calc->>Calc: calcular_posicao_movimento_uniforme(20, 0, 10) → 20 + 0 = 20.00
    Calc-->>Usuario: "Posição final: 20.00 m"

    Note over Calc,Usuario: Corpo em repouso — posição final igual à posição inicial.
```

---

## Fluxo Alternativo — Velocidade negativa (movimento em sentido contrário)

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (movimento_uniforme)

    Calc-->>Usuario: "Digite a posição inicial (em metros): "
    Usuario->>Calc: Informa s0 (ex: 50)
    Calc-->>Usuario: "Digite a velocidade (em m/s): "
    Usuario->>Calc: Informa velocidade = -3
    Calc-->>Usuario: "Digite o tempo (em segundos): "
    Usuario->>Calc: Informa tempo (ex: 5)
    Calc->>Calc: calcular_posicao_movimento_uniforme(50, -3, 5) → 50 + (-3)*5 = 35.00
    Calc-->>Usuario: "Posição final: 35.00 m"

    Note over Calc,Usuario: Velocidade negativa indica movimento no sentido contrário ao referencial.
```

---

## Fluxo de Exceção — Entrada Inválida (dado não numérico)

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (ler_numero)

    Note over Calc,Usuario: O erro pode ocorrer em qualquer um dos 3 prompts<br/>(posição inicial, velocidade ou tempo).

    Calc-->>Usuario: "Digite a velocidade (em m/s): "
    Usuario->>Calc: Digita texto inválido (ex: "rapido")
    Calc->>Calc: float("rapido") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError: could not convert string to float

    Note over Calc,Usuario: Entradas anteriores já coletadas são descartadas.<br/>O usuário precisa reiniciar a operação do zero.
```

---

## Fluxo de Exceção — Campo em Branco

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (ler_numero)

    Calc-->>Usuario: "Digite o tempo (em segundos): "
    Usuario->>Calc: Pressiona Enter sem digitar nada ("")
    Calc->>Calc: float("") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError: could not convert string to float
```
