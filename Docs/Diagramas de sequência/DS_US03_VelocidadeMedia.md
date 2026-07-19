# DS - US03: Calcular Velocidade Média

**User Story:** Como estudante de física, eu quero calcular a velocidade média, para que eu possa resolver problemas de cinemática.

---

## Fluxo Principal — Calcular Velocidade Média

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuFis as menu_fisica
    participant MenuVel as menu_velocidades
    participant Dispatcher as MenuDispatcher
    participant Registro as registro_operacoes
    participant Op as OperacaoVelocidadeMedia
    participant Calc as velocidades.py (velocidade_media)

    Usuario->>MenuFis: Digita "1" (Velocidades)
    MenuFis->>Dispatcher: executar("1")
    Dispatcher->>MenuVel: menu_velocidades()
    MenuVel->>MenuVel: Exibe menu de velocidades
    MenuVel-->>Usuario: "1-Velocidade Média / 2-MU / 3-MUV / ..."

    Usuario->>MenuVel: Digita "1" (Velocidade Média)
    MenuVel->>Registro: criar_operacoes_velocidades()
    Registro-->>MenuVel: {operacoes com OperacaoVelocidadeMedia, ...}
    MenuVel->>Dispatcher: executar("1")
    Dispatcher->>Op: OperacaoVelocidadeMedia.calcular()
    Op->>Calc: velocidade_media()
    Calc-->>Usuario: "Digite a distância percorrida (em metros): "
    Usuario->>Calc: Informa distância (ex: 150)
    Calc-->>Usuario: "Digite o tempo gasto (em segundos): "
    Usuario->>Calc: Informa tempo (ex: 30)
    Calc->>Calc: calcular_velocidade_media(150, 30) → 150/30 = 5.00
    Calc-->>Usuario: "Velocidade média: 5.00 m/s"
```

---

## Fluxo de Exceção — Tempo igual a zero

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (velocidade_media)

    Calc-->>Usuario: "Digite a distância percorrida (em metros): "
    Usuario->>Calc: Informa distância (ex: 100)
    Calc-->>Usuario: "Digite o tempo gasto (em segundos): "
    Usuario->>Calc: Informa tempo = 0
    Calc->>Calc: calcular_velocidade_media(100, 0) → ZeroDivisionError
    Calc-->>Usuario: Erro de divisão por zero (exceção não tratada)

    Note over Calc,Usuario: Comportamento atual: o Python lança ZeroDivisionError.<br/>Melhoria sugerida: validar tempo > 0 antes de calcular.
```

---

## Fluxo de Exceção — Entrada Inválida (dado não numérico)

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (ler_numero)

    Calc-->>Usuario: "Digite a distância percorrida (em metros): "
    Usuario->>Calc: Digita texto inválido (ex: "cinquenta")
    Calc->>Calc: float("cinquenta") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError: could not convert string to float

    Note over Calc,Usuario: O erro pode ocorrer em qualquer um dos prompts de entrada.<br/>O fluxo é interrompido imediatamente, sem possibilidade<br/>de correção pelo usuário na sessão atual.
```

---

## Fluxo de Exceção — Campo em Branco

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (ler_numero)

    Calc-->>Usuario: "Digite o tempo gasto (em segundos): "
    Usuario->>Calc: Pressiona Enter sem digitar nada ("")
    Calc->>Calc: float("") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError: could not convert string to float
```
