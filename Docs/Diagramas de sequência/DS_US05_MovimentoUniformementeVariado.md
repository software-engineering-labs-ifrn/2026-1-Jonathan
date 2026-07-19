# DS - US05: Calcular Movimento Uniformemente Variado (MUV)

**User Story:** Como estudante, eu quero calcular problemas de MUV, para que eu possa resolver exercícios de física.

---

## Fluxo Principal — Calcular Posição Final no MUV

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuVel as menu_velocidades
    participant Dispatcher as MenuDispatcher
    participant Registro as registro_operacoes
    participant Op as OperacaoMovimentoUniformementeVariado
    participant Calc as velocidades.py (movimento_uniformemente_variado)

    MenuVel-->>Usuario: Exibe menu de velocidades
    Usuario->>MenuVel: Digita "3" (MUV)
    MenuVel->>Registro: criar_operacoes_velocidades()
    Registro-->>MenuVel: {operacoes com OperacaoMovimentoUniformementeVariado, ...}
    MenuVel->>Dispatcher: executar("3")
    Dispatcher->>Op: OperacaoMovimentoUniformementeVariado.calcular()
    Op->>Calc: movimento_uniformemente_variado()

    Calc-->>Usuario: "Digite a posição inicial (em metros): "
    Usuario->>Calc: Informa s0 (ex: 0)
    Calc-->>Usuario: "Digite a velocidade inicial (em m/s): "
    Usuario->>Calc: Informa v0 (ex: 10)
    Calc-->>Usuario: "Digite a aceleração (em m/s²): "
    Usuario->>Calc: Informa aceleração (ex: 2)
    Calc-->>Usuario: "Digite o tempo (em segundos): "
    Usuario->>Calc: Informa tempo (ex: 5)
    Calc->>Calc: calcular_posicao_muv(0, 10, 2, 5) → 0 + 10*5 + (2*25)/2 = 75.00
    Calc-->>Usuario: "Posição final: 75.00 m"
```

---

## Fluxo Alternativo — Calcular Velocidade Final no MUV

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuVel as menu_velocidades
    participant Dispatcher as MenuDispatcher
    participant Op as OperacaoVelocidadeFinalMuv
    participant Calc as velocidades.py (velocidade_final_muv)

    MenuVel-->>Usuario: Exibe menu de velocidades
    Usuario->>MenuVel: Digita "4" (Velocidade Final no MUV)
    MenuVel->>Dispatcher: executar("4")
    Dispatcher->>Op: OperacaoVelocidadeFinalMuv.calcular()
    Op->>Calc: velocidade_final_muv()

    Calc-->>Usuario: "Digite a velocidade inicial (em m/s): "
    Usuario->>Calc: Informa v0 (ex: 10)
    Calc-->>Usuario: "Digite a aceleração (em m/s²): "
    Usuario->>Calc: Informa aceleração (ex: 2)
    Calc-->>Usuario: "Digite o tempo (em segundos): "
    Usuario->>Calc: Informa tempo (ex: 5)
    Calc->>Calc: calcular_velocidade_final_muv(10, 2, 5) → 10 + 2*5 = 20.00
    Calc-->>Usuario: "Velocidade final: 20.00 m/s"
```

---

## Fluxo Alternativo — Calcular via Equação de Torricelli

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuVel as menu_velocidades
    participant Dispatcher as MenuDispatcher
    participant Op as OperacaoEquacaoTorricelli
    participant Calc as velocidades.py (equacao_torricelli)

    MenuVel-->>Usuario: Exibe menu de velocidades
    Usuario->>MenuVel: Digita "5" (Equação de Torricelli)
    MenuVel->>Dispatcher: executar("5")
    Dispatcher->>Op: OperacaoEquacaoTorricelli.calcular()
    Op->>Calc: equacao_torricelli()

    Calc-->>Usuario: "Digite a velocidade inicial (em m/s): "
    Usuario->>Calc: Informa v0 (ex: 5)
    Calc-->>Usuario: "Digite a aceleração (em m/s²): "
    Usuario->>Calc: Informa aceleração (ex: 3)
    Calc-->>Usuario: "Digite o deslocamento (em metros): "
    Usuario->>Calc: Informa deslocamento (ex: 10)
    Calc->>Calc: v² = 5² + 2*3*10 = 25 + 60 = 85 → √85 ≈ 9.22
    Calc-->>Usuario: "Velocidade final: 9.22 m/s"
```

---

## Fluxo de Exceção — Torricelli com resultado negativo sob raiz

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (equacao_torricelli)

    Calc-->>Usuario: "Digite a velocidade inicial (em m/s): "
    Usuario->>Calc: Informa v0 (ex: 2)
    Calc-->>Usuario: "Digite a aceleração (em m/s²): "
    Usuario->>Calc: Informa aceleração (ex: -10)
    Calc-->>Usuario: "Digite o deslocamento (em metros): "
    Usuario->>Calc: Informa deslocamento (ex: 5)
    Calc->>Calc: v² = 4 + 2*(-10)*5 = 4 - 100 = -96 < 0
    Calc->>Calc: calcular_velocidade_final_torricelli() → retorna None
    Calc-->>Usuario: "Erro: Velocidade ao quadrado não pode ser negativa!"
```

---

## Fluxo de Exceção — Entrada Inválida (dado não numérico)

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (ler_numero)

    Note over Calc,Usuario: MUV e Torricelli exigem 3 ou 4 entradas em sequência.<br/>O erro pode ocorrer em qualquer uma delas.

    Calc-->>Usuario: "Digite a aceleração (em m/s²): "
    Usuario->>Calc: Digita texto inválido (ex: "dois")
    Calc->>Calc: float("dois") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError: could not convert string to float

    Note over Calc,Usuario: Todas as entradas anteriores são perdidas.<br/>O usuário precisa reiniciar a operação.
```

---

## Fluxo de Exceção — Campo em Branco

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (ler_numero)

    Calc-->>Usuario: "Digite o deslocamento (em metros): "
    Usuario->>Calc: Pressiona Enter sem digitar nada ("")
    Calc->>Calc: float("") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError: could not convert string to float
```
