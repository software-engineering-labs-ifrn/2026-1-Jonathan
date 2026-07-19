# DS - US10: Visualizar o Resultado

**User Story:** Como usuário, eu quero visualizar o resultado do cálculo, para que eu possa utilizá-lo em meus estudos.

> Esta User Story é transversal — representa a etapa final de toda operação do sistema, onde o resultado processado é exibido ao usuário. Os fluxos abaixo mostram os padrões de exibição e os cenários de saída com erro.

---

## Fluxo Principal — Resultado Exibido com Sucesso

```mermaid
sequenceDiagram
    actor Usuario
    participant Op as Operação Concreta
    participant Calc as Módulo de Cálculo
    participant Dispatcher as MenuDispatcher

    Usuario->>Op: Fornece todos os dados de entrada
    Op->>Calc: Chama função de cálculo com os parâmetros
    Calc->>Calc: Executa fórmula e obtém resultado
    Calc-->>Usuario: Exibe resultado formatado (ex: "Área do quadrado: 25.0")
    Calc-->>Op: Retorna (None — saída via print)
    Op-->>Dispatcher: Retorna controle
    Dispatcher-->>Dispatcher: return True — mantém loop do menu ativo
```

---

## Fluxo Alternativo — Resultado com Formatação de Casas Decimais

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as Módulo de Cálculo

    Note over Calc,Usuario: Operações que usam f-string com :.2f<br/>(ex: área do círculo, velocidades, queda livre)

    Calc->>Calc: Calcula resultado (ex: π * 7² = 153.93804...)
    Calc-->>Usuario: "Área do círculo: 153.94"

    Note over Calc,Usuario: Resultado arredondado para 2 casas decimais<br/>para melhor legibilidade.
```

---

## Fluxo Alternativo — Resultado Inteiro ou Sem Arredondamento

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as Módulo de Cálculo

    Note over Calc,Usuario: Operações que usam f-string sem formatação<br/>(ex: área do quadrado, perímetro do triângulo)

    Calc->>Calc: Calcula resultado (ex: 5² = 25.0)
    Calc-->>Usuario: "Área do quadrado: 25.0"

    Note over Calc,Usuario: Resultado exibido como float sem arredondamento explícito.
```

---

## Fluxo de Exceção — Resultado Inválido (Torricelli negativo)

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as velocidades.py (equacao_torricelli)

    Calc->>Calc: Calcula v² = v0² + 2*a*Δs → valor negativo
    Calc->>Calc: calcular_velocidade_final_torricelli() → retorna None
    Calc-->>Usuario: "Erro: Velocidade ao quadrado não pode ser negativa!"

    Note over Calc,Usuario: Único caso do sistema com tratamento<br/>explícito de resultado inválido antes de exibir.
```

---

## Fluxo — Sequência Completa: Entrada → Processamento → Exibição

```mermaid
sequenceDiagram
    actor Usuario
    participant Menu as Menu Ativo
    participant Dispatcher as MenuDispatcher
    participant Op as Operação Concreta
    participant Calc as Módulo de Cálculo

    Usuario->>Menu: Seleciona operação desejada
    Menu->>Dispatcher: executar(opcao)
    Dispatcher->>Op: op.calcular()
    Op->>Calc: Chama função específica

    loop Para cada dado necessário
        Calc-->>Usuario: Solicita entrada
        Usuario->>Calc: Informa valor
    end

    Calc->>Calc: Executa cálculo com os dados fornecidos
    Calc-->>Usuario: Exibe resultado formatado
    Calc-->>Op: Retorna None
    Op-->>Dispatcher: Retorna None
    Dispatcher-->>Menu: return True
    Menu->>Menu: Aguarda próxima interação do usuário
```
