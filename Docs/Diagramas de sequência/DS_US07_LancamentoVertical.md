# DS - US07: Calcular Lançamento Vertical

**User Story:** Como estudante, eu quero calcular lançamentos verticais, para que eu possa resolver exercícios de física.

---

## Fluxo Principal — Calcular Altura Máxima

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuVel as menu_velocidades
    participant Dispatcher as MenuDispatcher
    participant Registro as registro_operacoes
    participant Op as OperacaoLancamentoVertical
    participant Calc as velocidades.py (lancamento_vertical)

    MenuVel-->>Usuario: Exibe menu de velocidades
    Usuario->>MenuVel: Digita "7" (Lançamento Vertical)
    MenuVel->>Registro: criar_operacoes_velocidades()
    Registro-->>MenuVel: {operacoes com OperacaoLancamentoVertical, ...}
    MenuVel->>Dispatcher: executar("7")
    Dispatcher->>Op: OperacaoLancamentoVertical.calcular()
    Op->>Calc: lancamento_vertical()
    Calc-->>Usuario: "1-Altura máxima / 2-Tempo total / 3-Altura em tempo específico"

    Usuario->>Calc: Digita "1" (Altura máxima)
    Calc-->>Usuario: "Digite a velocidade inicial (em m/s): "
    Usuario->>Calc: Informa v0 (ex: 20)
    Calc->>Calc: calcular_altura_maxima_lancamento(20, g=10) → (20²)/(2*10) = 20.00
    Calc-->>Usuario: "Altura máxima: 20.00 m"
```

---

## Fluxo Alternativo — Calcular Tempo Total do Lançamento

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (lancamento_vertical)

    Calc-->>Usuario: "1-Altura máxima / 2-Tempo total / 3-Altura em tempo específico"
    Usuario->>Calc: Digita "2" (Tempo total)
    Calc-->>Usuario: "Digite a velocidade inicial (em m/s): "
    Usuario->>Calc: Informa v0 (ex: 30)
    Calc->>Calc: calcular_tempo_total_lancamento(30, g=10) → (2*30)/10 = 6.00
    Calc-->>Usuario: "Tempo total: 6.00 s"
```

---

## Fluxo Alternativo — Calcular Altura em Instante Específico

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (lancamento_vertical)

    Calc-->>Usuario: "1-Altura máxima / 2-Tempo total / 3-Altura em tempo específico"
    Usuario->>Calc: Digita "3" (Altura em tempo específico)
    Calc-->>Usuario: "Digite a velocidade inicial (em m/s): "
    Usuario->>Calc: Informa v0 (ex: 20)
    Calc-->>Usuario: "Digite o tempo (em segundos): "
    Usuario->>Calc: Informa tempo (ex: 2)
    Calc->>Calc: calcular_altura_lancamento(20, 2, g=10) → 20*2 - (10*4)/2 = 40 - 20 = 20.00
    Calc-->>Usuario: "Altura: 20.00 m"
```

---

## Fluxo de Exceção — Opção Inválida no Sub-menu

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (lancamento_vertical)

    Calc-->>Usuario: "1-Altura máxima / 2-Tempo total / 3-Altura em tempo específico"
    Usuario->>Calc: Digita "5" (opção inválida)
    Calc->>Calc: opcao não é "1", "2" ou "3"
    Calc-->>Usuario: "Opção inválida!"
    Note over Calc,Usuario: O fluxo retorna ao menu de velocidades.
```

---

## Fluxo de Exceção — Entrada Inválida (dado não numérico)

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (ler_numero)

    Note over Calc,Usuario: Após escolher a sub-opção (1, 2 ou 3),<br/>o usuário é solicitado a informar a velocidade inicial<br/>e, na opção 3, também o tempo.

    Calc-->>Usuario: "Digite a velocidade inicial (em m/s): "
    Usuario->>Calc: Digita texto inválido (ex: "vinte")
    Calc->>Calc: float("vinte") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError: could not convert string to float

    Note over Calc,Usuario: O fluxo é interrompido com erro.<br/>O usuário precisa reiniciar a operação.
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
