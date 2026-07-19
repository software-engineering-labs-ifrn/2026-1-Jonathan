# DS - US06: Calcular Queda Livre

**User Story:** Como estudante, eu quero calcular situações de queda livre, para que eu possa analisar movimentos sob ação da gravidade.

---

## Fluxo Principal — Calcular Altura na Queda Livre

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuVel as menu_velocidades
    participant Dispatcher as MenuDispatcher
    participant Registro as registro_operacoes
    participant Op as OperacaoQuedaLivre
    participant Calc as velocidades.py (queda_livre)

    MenuVel-->>Usuario: Exibe menu de velocidades
    Usuario->>MenuVel: Digita "6" (Queda Livre)
    MenuVel->>Registro: criar_operacoes_velocidades()
    Registro-->>MenuVel: {operacoes com OperacaoQuedaLivre, ...}
    MenuVel->>Dispatcher: executar("6")
    Dispatcher->>Op: OperacaoQuedaLivre.calcular()
    Op->>Calc: queda_livre()
    Calc-->>Usuario: "1-Calcular altura / 2-Calcular velocidade / 3-Calcular tempo"

    Usuario->>Calc: Digita "1" (Calcular altura)
    Calc-->>Usuario: "Digite o tempo de queda (em segundos): "
    Usuario->>Calc: Informa tempo (ex: 3)
    Calc->>Calc: calcular_altura_queda_livre(3, g=10) → (10 * 9) / 2 = 45.00
    Calc-->>Usuario: "Altura: 45.00 m"
```

---

## Fluxo Alternativo — Calcular Velocidade na Queda Livre

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (queda_livre)

    Calc-->>Usuario: "1-Calcular altura / 2-Calcular velocidade / 3-Calcular tempo"
    Usuario->>Calc: Digita "2" (Calcular velocidade)
    Calc-->>Usuario: "Digite o tempo de queda (em segundos): "
    Usuario->>Calc: Informa tempo (ex: 4)
    Calc->>Calc: calcular_velocidade_queda_livre(4, g=10) → 10 * 4 = 40.00
    Calc-->>Usuario: "Velocidade: 40.00 m/s"
```

---

## Fluxo Alternativo — Calcular Tempo de Queda Livre

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (queda_livre)

    Calc-->>Usuario: "1-Calcular altura / 2-Calcular velocidade / 3-Calcular tempo"
    Usuario->>Calc: Digita "3" (Calcular tempo)
    Calc-->>Usuario: "Digite a altura (em metros): "
    Usuario->>Calc: Informa altura (ex: 80)
    Calc->>Calc: calcular_tempo_queda_livre(80, g=10) → √(2*80/10) = √16 = 4.00
    Calc-->>Usuario: "Tempo de queda: 4.00 s"
```

---

## Fluxo de Exceção — Opção Inválida no Sub-menu

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (queda_livre)

    Calc-->>Usuario: "1-Calcular altura / 2-Calcular velocidade / 3-Calcular tempo"
    Usuario->>Calc: Digita "9" (opção inválida)
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

    Note over Calc,Usuario: Após escolher a sub-opção (1, 2 ou 3),<br/>o usuário é solicitado a informar um valor numérico.

    Calc-->>Usuario: "Digite o tempo de queda (em segundos): "
    Usuario->>Calc: Digita texto inválido (ex: "tres")
    Calc->>Calc: float("tres") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError: could not convert string to float

    Note over Calc,Usuario: O fluxo é interrompido com erro.<br/>O usuário precisa reiniciar a operação.
```

---

## Fluxo de Exceção — Campo em Branco

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (ler_numero)

    Calc-->>Usuario: "Digite a altura (em metros): "
    Usuario->>Calc: Pressiona Enter sem digitar nada ("")
    Calc->>Calc: float("") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError: could not convert string to float
```
