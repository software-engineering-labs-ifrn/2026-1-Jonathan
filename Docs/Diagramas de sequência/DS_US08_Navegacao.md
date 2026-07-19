# DS - US08: Navegar entre Matemática e Física

**User Story:** Como usuário, eu quero escolher entre operações de Matemática e Física, para que eu possa acessar rapidamente a funcionalidade desejada.

---

## Fluxo Principal — Selecionar Matemática

```mermaid
sequenceDiagram
    actor Usuario
    participant Main as Main (menu_principal)
    participant Dispatcher as MenuDispatcher
    participant MenuMat as menu_matematica

    Usuario->>Main: Executa o programa
    Main->>Main: Exibe menu principal
    Main-->>Usuario: "1 - Matemática / 2 - Física / 0 - Sair"

    Usuario->>Main: Digita "1"
    Main->>Dispatcher: executar("1")
    Dispatcher->>MenuMat: menu_matematica()
    MenuMat->>MenuMat: Exibe menu de cálculos matemáticos
    MenuMat-->>Usuario: "1 - Calcular Perímetro / 2 - Calcular Área / 0 - Voltar"
```

---

## Fluxo Alternativo — Selecionar Física

```mermaid
sequenceDiagram
    actor Usuario
    participant Main as Main (menu_principal)
    participant Dispatcher as MenuDispatcher
    participant MenuFis as menu_fisica

    Usuario->>Main: Executa o programa
    Main->>Main: Exibe menu principal
    Main-->>Usuario: "1 - Matemática / 2 - Física / 0 - Sair"

    Usuario->>Main: Digita "2"
    Main->>Dispatcher: executar("2")
    Dispatcher->>MenuFis: menu_fisica()
    MenuFis->>MenuFis: Exibe menu de cálculos de física
    MenuFis-->>Usuario: "1 - Velocidades / 0 - Voltar"
```

---

## Fluxo de Exceção — Opção Inválida

```mermaid
sequenceDiagram
    actor Usuario
    participant Main as Main (menu_principal)
    participant Dispatcher as MenuDispatcher

    Usuario->>Main: Executa o programa
    Main-->>Usuario: Exibe menu principal

    Usuario->>Main: Digita "9" (opção inválida)
    Main->>Dispatcher: executar("9")
    Dispatcher->>Dispatcher: operacoes.get("9") retorna None
    Dispatcher-->>Usuario: "Opção inválida! Tente novamente."
    Main->>Main: Retorna ao loop do menu principal
```

---

## Fluxo — Sair do programa

```mermaid
sequenceDiagram
    actor Usuario
    participant Main as Main (menu_principal)
    participant Dispatcher as MenuDispatcher

    Usuario->>Main: Digita "0"
    Main->>Dispatcher: executar("0")
    Dispatcher->>Dispatcher: chama sair_programa()
    Dispatcher-->>Usuario: "Até logo!"
    Main->>Main: break — encerra o loop principal
```
