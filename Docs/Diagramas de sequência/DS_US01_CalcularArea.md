# DS - US01: Calcular Área de Figuras Geométricas

**User Story:** Como estudante, eu quero calcular a área de diferentes figuras geométricas, para que eu possa resolver exercícios de matemática com rapidez.

---

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuMat as menu_matematica
    participant MenuArea as menu_area
    participant Dispatcher as MenuDispatcher
    participant Registro as registro_operacoes
    participant Op as OperacaoAreaXxx
    participant Calc as area.py

    Usuario->>MenuMat: Digita "2" (Calcular Área)
    MenuMat->>Dispatcher: executar("2")
    Dispatcher->>MenuArea: menu_area()
    MenuArea-->>Usuario: Exibe opções de figuras (1-Quadrado, 2-Retângulo, 3-Triângulo, 4-Círculo ... 0-Voltar)

    alt Opção válida de figura
        Usuario->>MenuArea: Digita opção (ex: "1" Quadrado)
        MenuArea->>Registro: criar_operacoes_area()
        Registro-->>MenuArea: mapa de operações instanciadas
        MenuArea->>Dispatcher: executar(opcao)
        Dispatcher->>Op: op.calcular()
        Op->>Calc: chama função específica (ex: area_quadrado())

        loop Para cada dado necessário
            Calc-->>Usuario: Solicita entrada (ex: "Digite o valor do lado: ")
            alt Entrada válida
                Usuario->>Calc: Informa valor numérico (ex: 5)
            else Entrada inválida (texto ou campo vazio)
                Usuario->>Calc: Digita valor inválido (ex: "abc" ou "")
                Calc->>Calc: float("abc") → ValueError não tratado
                Calc-->>Usuario: Traceback — programa encerra o fluxo com erro
            end
        end

        Calc->>Calc: Executa cálculo com os valores informados
        Calc-->>Usuario: Exibe resultado (ex: "Área do quadrado: 25.0")

    else Opção "0" — Voltar
        Usuario->>MenuArea: Digita "0"
        MenuArea->>Dispatcher: executar("0")
        Dispatcher->>Dispatcher: voltar_menu() → retorna False
        MenuArea->>MenuArea: break — retorna ao menu_matematica

    else Opção inválida
        Usuario->>MenuArea: Digita opção inexistente (ex: "9")
        MenuArea->>Dispatcher: executar("9")
        Dispatcher->>Dispatcher: operacoes.get("9") → None
        Dispatcher-->>Usuario: "Opção inválida! Tente novamente."
    end
```
