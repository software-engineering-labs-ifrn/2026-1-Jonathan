# DS - US01: Calcular Área de Figuras Geométricas

**User Story:** Como estudante, eu quero calcular a área de diferentes figuras geométricas, para que eu possa resolver exercícios de matemática com rapidez.

---

## Fluxo Principal — Calcular Área do Quadrado

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuMat as menu_matematica
    participant MenuArea as menu_area
    participant Dispatcher as MenuDispatcher
    participant Registro as registro_operacoes
    participant Op as OperacaoAreaQuadrado
    participant Calc as area.py (area_quadrado)

    Usuario->>MenuMat: Digita "2" (Calcular Área)
    MenuMat->>Dispatcher: executar("2")
    Dispatcher->>MenuArea: menu_area()
    MenuArea->>MenuArea: Exibe opções de figuras
    MenuArea-->>Usuario: "1-Quadrado / 2-Retângulo / 3-Triângulo / ..."

    Usuario->>MenuArea: Digita "1" (Quadrado)
    MenuArea->>Registro: criar_operacoes_area()
    Registro-->>MenuArea: {operacoes com OperacaoAreaQuadrado, ...}
    MenuArea->>Dispatcher: executar("1")
    Dispatcher->>Op: OperacaoAreaQuadrado.calcular()
    Op->>Calc: area_quadrado()
    Calc-->>Usuario: "Digite o valor do lado do quadrado: "
    Usuario->>Calc: Informa o lado (ex: 5)
    Calc->>Calc: calcular_area_quadrado(5) → 25.0
    Calc-->>Usuario: "Área do quadrado: 25.0"
```

---

## Fluxo Alternativo — Calcular Área do Retângulo

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuArea as menu_area
    participant Dispatcher as MenuDispatcher
    participant Op as OperacaoAreaRetangulo
    participant Calc as area.py (area_retangulo)

    MenuArea-->>Usuario: Exibe menu de áreas
    Usuario->>MenuArea: Digita "2" (Retângulo)
    MenuArea->>Dispatcher: executar("2")
    Dispatcher->>Op: OperacaoAreaRetangulo.calcular()
    Op->>Calc: area_retangulo()
    Calc-->>Usuario: "Digite o comprimento do retângulo: "
    Usuario->>Calc: Informa comprimento (ex: 4)
    Calc-->>Usuario: "Digite a largura do retângulo: "
    Usuario->>Calc: Informa largura (ex: 3)
    Calc->>Calc: calcular_area_retangulo(4, 3) → 12.0
    Calc-->>Usuario: "Área do retângulo: 12.0"
```

---

## Fluxo Alternativo — Calcular Área do Triângulo

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuArea as menu_area
    participant Dispatcher as MenuDispatcher
    participant Op as OperacaoAreaTriangulo
    participant Calc as area.py (area_triangulo)

    MenuArea-->>Usuario: Exibe menu de áreas
    Usuario->>MenuArea: Digita "3" (Triângulo)
    MenuArea->>Dispatcher: executar("3")
    Dispatcher->>Op: OperacaoAreaTriangulo.calcular()
    Op->>Calc: area_triangulo()
    Calc-->>Usuario: "Digite a base do triângulo: "
    Usuario->>Calc: Informa base (ex: 6)
    Calc-->>Usuario: "Digite a altura do triângulo: "
    Usuario->>Calc: Informa altura (ex: 4)
    Calc->>Calc: calcular_area_triangulo(6, 4) → 12.0
    Calc-->>Usuario: "Área do triângulo: 12.0"
```

---

## Fluxo Alternativo — Calcular Área do Círculo

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuArea as menu_area
    participant Dispatcher as MenuDispatcher
    participant Op as OperacaoAreaCirculo
    participant Calc as area.py (area_circulo)

    MenuArea-->>Usuario: Exibe menu de áreas
    Usuario->>MenuArea: Digita "4" (Círculo)
    MenuArea->>Dispatcher: executar("4")
    Dispatcher->>Op: OperacaoAreaCirculo.calcular()
    Op->>Calc: area_circulo()
    Calc-->>Usuario: "Digite o raio do círculo: "
    Usuario->>Calc: Informa raio (ex: 7)
    Calc->>Calc: calcular_area_circulo(7) → π * 7² ≈ 153.94
    Calc-->>Usuario: "Área do círculo: 153.94"
```

---

## Fluxo Alternativo — Calcular Área do Polígono de N Lados

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuArea as menu_area
    participant Dispatcher as MenuDispatcher
    participant Op as OperacaoAreaPoligonoNLados
    participant Calc as area.py (area_poligono_n_lados)

    MenuArea-->>Usuario: Exibe menu de áreas
    Usuario->>MenuArea: Digita "7" (Polígono N lados)
    MenuArea->>Dispatcher: executar("7")
    Dispatcher->>Op: OperacaoAreaPoligonoNLados.calcular()
    Op->>Calc: area_poligono_n_lados()
    Calc-->>Usuario: "Digite a quantidade de lados: "
    Usuario->>Calc: Informa N (ex: 8)
    Calc-->>Usuario: "Digite o valor do lado do polígono: "
    Usuario->>Calc: Informa lado (ex: 5)
    Calc-->>Usuario: "Digite o valor do apótema do polígono: "
    Usuario->>Calc: Informa apótema (ex: 6.04)
    Calc->>Calc: calcular_area_poligono_n_lados(8, 5, 6.04) → (8*5*6.04)/2 ≈ 120.8
    Calc-->>Usuario: "Área do polígono de 8 lados: 120.80"
```

---

## Fluxo — Voltar ao Menu Anterior

```mermaid
sequenceDiagram
    actor Usuario
    participant MenuArea as menu_area
    participant Dispatcher as MenuDispatcher

    MenuArea-->>Usuario: Exibe menu de áreas
    Usuario->>MenuArea: Digita "0" (Voltar)
    MenuArea->>Dispatcher: executar("0")
    Dispatcher->>Dispatcher: chama voltar_menu() → retorna False
    MenuArea->>MenuArea: break — retorna ao menu_matematica
```

---

## Fluxo de Exceção — Entrada Inválida (dado não numérico)

```mermaid
sequenceDiagram
    actor Usuario
    participant Op as OperacaoAreaXxx
    participant Calc as area.py (ler_numero)

    Op->>Calc: Chama função de área (ex: area_quadrado)
    Calc-->>Usuario: "Digite o valor do lado do quadrado: "
    Usuario->>Calc: Digita texto inválido (ex: "abc")
    Calc->>Calc: float("abc") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError: could not convert string to float

    Note over Calc,Usuario: O programa encerra o fluxo com erro.<br/>Não há solicitação de nova entrada.<br/>Melhoria sugerida: envolver ler_numero() em try/except<br/>e repetir o prompt até receber valor válido.
```

---

## Fluxo de Exceção — Campo em Branco

```mermaid
sequenceDiagram
    actor Usuario
    participant Calc as area.py (ler_numero)

    Calc-->>Usuario: "Digite o valor do lado do quadrado: "
    Usuario->>Calc: Pressiona Enter sem digitar nada ("")
    Calc->>Calc: float("") → ValueError (não tratado)
    Calc-->>Usuario: Traceback — ValueError: could not convert string to float

    Note over Calc,Usuario: Mesmo comportamento do caso anterior.
```
