# DS - US02: Calcular Perímetro de Figuras Geométricas

**User Story:** Como estudante, eu quero calcular o perímetro de figuras geométricas, para que eu possa conferir os resultados dos meus exercícios.

---

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuMat as menu_matematica
    participant MenuPer as menu_perimetro
    participant Dispatcher as MenuDispatcher
    participant Registro as registro_operacoes
    participant Op as OperacaoPerimetroXxx
    participant Calc as perimetro.py

    Usuario->>MenuMat: Digita "1" (Calcular Perímetro)
    MenuMat->>Dispatcher: executar("1")
    Dispatcher->>MenuPer: menu_perimetro()
    MenuPer-->>Usuario: Exibe opções de figuras (1-Quadrado, 2-Retângulo, 3-Triângulo, 4-Círculo ... 0-Voltar)

    alt Opção válida de figura
        Usuario->>MenuPer: Digita opção (ex: "1" Quadrado)
        MenuPer->>Registro: criar_operacoes_perimetro()
        Registro-->>MenuPer: mapa de operações instanciadas
        MenuPer->>Dispatcher: executar(opcao)
        Dispatcher->>Op: op.calcular()
        Op->>Calc: chama função específica (ex: perimetro_quadrado())

        loop Para cada dado necessário
            Calc-->>Usuario: Solicita entrada (ex: "Digite o valor do lado: ")
            alt Entrada válida (número)
                Usuario->>Calc: Informa valor numérico (ex: 5)
            else Entrada inválida — texto ou campo vazio
                Usuario->>Calc: Digita valor inválido (ex: "abc" ou "")
                Calc->>Calc: float("abc") → ValueError não tratado
                Calc-->>Usuario: Traceback — programa encerra o fluxo com erro
            else Entrada inválida — float onde int é esperado (polígono N lados)
                Usuario->>Calc: Digita "3.5" no campo de quantidade de lados
                Calc->>Calc: int("3.5") → ValueError não tratado
                Calc-->>Usuario: Traceback — programa encerra o fluxo com erro
            end
        end

        Calc->>Calc: Executa cálculo com os valores informados
        Calc-->>Usuario: Exibe resultado (ex: "Perímetro do quadrado: 20.0")

    else Opção "0" — Voltar
        Usuario->>MenuPer: Digita "0"
        MenuPer->>Dispatcher: executar("0")
        Dispatcher->>Dispatcher: voltar_menu() → retorna False
        MenuPer->>MenuPer: break — retorna ao menu_matematica

    else Opção inválida
        Usuario->>MenuPer: Digita opção inexistente (ex: "9")
        MenuPer->>Dispatcher: executar("9")
        Dispatcher->>Dispatcher: operacoes.get("9") → None
        Dispatcher-->>Usuario: "Opção inválida! Tente novamente."
    end
```
