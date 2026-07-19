# DS - US02: Calcular Perímetro de Figuras Geométricas

**User Story:** Como estudante, eu quero calcular o perímetro de figuras geométricas, para que eu possa conferir os resultados dos meus exercícios.

---

## Fluxo Principal — Calcular Perímetro do Quadrado

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuMat as menu_matematica
    participant MenuPer as menu_perimetro
    participant Dispatcher as MenuDispatcher
    participant Registro as registro_operacoes
    participant Op as OperacaoPerimetroQuadrado
    participant Calc as perimetro.py (perimetro_quadrado)

    Usuario->>MenuMat: Digita "1" (Calcular Perímetro)
    MenuMat->>Dispatcher: executar("1")
    Dispatcher->>MenuPer: menu_perimetro()
    MenuPer->>MenuPer: Exibe opções de figuras
    MenuPer-->>Usuario: "1-Quadrado / 2-Retângulo / 3-Triângulo / ..."

    Usuario->>MenuPer: Digita "1" (Quadrado)
    MenuPer->>Registro: criar_operacoes_perimetro()
    Registro-->>MenuPer: {operacoes com OperacaoPerimetroQuadrado, ...}
    MenuPer->>Dispatcher: executar("1")
    Dispatcher->>Op: OperacaoPerimetroQuadrado.calcular()
    Op->>Calc: perimetro_quadrado()
    Calc-->>Usuario: "Digite o valor do lado do quadrado: "
    Usuario->>Calc: Informa o lado (ex: 5)
    Calc->>Calc: calcular_perimetro_quadrado(5) → 4 * 5 = 20.0
    Calc-->>Usuario: "Perímetro do quadrado: 20.0"
```

---

## Fluxo Alternativo — Calcular Perímetro do Retângulo

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuPer as menu_perimetro
    participant Dispatcher as MenuDispatcher
    participant Op as OperacaoPerimetroRetangulo
    participant Calc as perimetro.py (perimetro_retangulo)

    MenuPer-->>Usuario: Exibe menu de perímetros
    Usuario->>MenuPer: Digita "2" (Retângulo)
    MenuPer->>Dispatcher: executar("2")
    Dispatcher->>Op: OperacaoPerimetroRetangulo.calcular()
    Op->>Calc: perimetro_retangulo()
    Calc-->>Usuario: "Digite o comprimento do retângulo: "
    Usuario->>Calc: Informa comprimento (ex: 8)
    Calc-->>Usuario: "Digite a largura do retângulo: "
    Usuario->>Calc: Informa largura (ex: 3)
    Calc->>Calc: calcular_perimetro_retangulo(8, 3) → 2*(8+3) = 22.0
    Calc-->>Usuario: "Perímetro do retângulo: 22.0"
```

---

## Fluxo Alternativo — Calcular Perímetro do Triângulo

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuPer as menu_perimetro
    participant Dispatcher as MenuDispatcher
    participant Op as OperacaoPerimetroTriangulo
    participant Calc as perimetro.py (perimetro_triangulo)

    MenuPer-->>Usuario: Exibe menu de perímetros
    Usuario->>MenuPer: Digita "3" (Triângulo)
    MenuPer->>Dispatcher: executar("3")
    Dispatcher->>Op: OperacaoPerimetroTriangulo.calcular()
    Op->>Calc: perimetro_triangulo()
    Calc-->>Usuario: "Digite o primeiro lado do triângulo: "
    Usuario->>Calc: Informa lado1 (ex: 3)
    Calc-->>Usuario: "Digite o segundo lado do triângulo: "
    Usuario->>Calc: Informa lado2 (ex: 4)
    Calc-->>Usuario: "Digite o terceiro lado do triângulo: "
    Usuario->>Calc: Informa lado3 (ex: 5)
    Calc->>Calc: calcular_perimetro_triangulo(3, 4, 5) → 12.0
    Calc-->>Usuario: "Perímetro do triângulo: 12.0"
```

---

## Fluxo Alternativo — Calcular Perímetro do Círculo

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuPer as menu_perimetro
    participant Dispatcher as MenuDispatcher
    participant Op as OperacaoPerimetroCirculo
    participant Calc as perimetro.py (perimetro_circulo)

    MenuPer-->>Usuario: Exibe menu de perímetros
    Usuario->>MenuPer: Digita "4" (Círculo)
    MenuPer->>Dispatcher: executar("4")
    Dispatcher->>Op: OperacaoPerimetroCirculo.calcular()
    Op->>Calc: perimetro_circulo()
    Calc-->>Usuario: "Digite o raio do círculo: "
    Usuario->>Calc: Informa raio (ex: 7)
    Calc->>Calc: calcular_perimetro_circulo(7) → 2 * π * 7 ≈ 43.98
    Calc-->>Usuario: "Perímetro (circunferência) do círculo: 43.98"
```

---

## Fluxo Alternativo — Calcular Perímetro do Polígono de N Lados

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuPer as menu_perimetro
    participant Dispatcher as MenuDispatcher
    participant Op as OperacaoPerimetroPoligonoNLados
    participant Calc as perimetro.py (perimetro_poligono_n_lados)

    MenuPer-->>Usuario: Exibe menu de perímetros
    Usuario->>MenuPer: Digita "7" (Polígono N lados)
    MenuPer->>Dispatcher: executar("7")
    Dispatcher->>Op: OperacaoPerimetroPoligonoNLados.calcular()
    Op->>Calc: perimetro_poligono_n_lados()
    Calc-->>Usuario: "Digite a quantidade de lados: "
    Usuario->>Calc: Informa N (ex: 6)
    Calc-->>Usuario: "Digite o valor do lado do polígono de 6 lados: "
    Usuario->>Calc: Informa lado (ex: 4)
    Calc->>Calc: calcular_perimetro_poligono_n_lados(6, 4) → 6 * 4 = 24.0
    Calc-->>Usuario: "Perímetro do polígono de 6 lados: 24.0"
```

---

## Fluxo — Voltar ao Menu Anterior

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuPer as menu_perimetro
    participant Dispatcher as MenuDispatcher

    MenuPer-->>Usuario: Exibe menu de perímetros
    Usuario->>MenuPer: Digita "0" (Voltar)
    MenuPer->>Dispatcher: executar("0")
    Dispatcher->>Dispatcher: chama voltar_menu() → retorna False
    MenuPer->>MenuPer: break — retorna ao menu_matematica
```

---

## Fluxo de Exceção — Entrada Inválida (dado não numérico)

```mermaid
sequenceDiagram
    actor Usuario
    participant Op as OperacaoPerimetroXxx
    participant Calc as perimetro.py (ler_numero)

    Op->>Calc: Chama função de perímetro (ex: perimetro_quadrado)
    Calc-->>Usuario: "Digite o valor do lado do quadrado: "
    Usuario->>Calc: Digita texto inválido (ex: "abc")
    Calc->>Calc: float("abc") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError: could not convert string to float

    Note over Calc,Usuario: O programa encerra o fluxo com erro.<br/>Não há solicitação de nova entrada.<br/>Melhoria sugerida: envolver ler_numero() em try/except<br/>e repetir o prompt até receber valor válido.
```

---

## Fluxo de Exceção — Quantidade de Lados Inválida (polígono N lados)

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as perimetro.py (ler_inteiro)

    Calc-->>Usuario: "Digite a quantidade de lados: "
    Usuario->>Calc: Digita valor não inteiro (ex: "3.5" ou "abc")
    Calc->>Calc: int("3.5") ou int("abc") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError

    Note over Calc,Usuario: ler_inteiro() usa int(), que não aceita floats nem texto.
```

---

## Fluxo de Exceção — Campo em Branco

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as perimetro.py (ler_numero)

    Calc-->>Usuario: Exibe prompt de entrada
    Usuario->>Calc: Pressiona Enter sem digitar nada ("")
    Calc->>Calc: float("") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError: could not convert string to float
```
