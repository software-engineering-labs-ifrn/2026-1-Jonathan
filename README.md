# Calculadora de Formas Geométricas e Física

Aplicação em Python para calcular perímetros, áreas e alguns conceitos básicos de física por meio de um menu interativo.

## 📋 Descrição

Este projeto implementa uma calculadora que permite:

- Calcular perímetros de figuras geométricas comuns
- Calcular áreas de figuras geométricas comuns
- Resolver operações básicas de física, como velocidade média, movimento uniforme, MUV, queda livre e lançamento vertical

As figuras contempladas incluem:

- Quadrado
- Retângulo
- Triângulo
- Círculo
- Pentágono
- Hexágono
- Polígono de N lados

## 🚀 Como Executar

```bash
python Main.py
```

O programa exibe um menu interativo em que o usuário pode:
1. Escolher entre Matemática e Física
2. Selecionar o tipo de cálculo desejado
3. Informar os dados necessários
4. Visualizar o resultado calculado

## 📁 Estrutura do Projeto

```text
.
├── Main.py                  # Ponto de entrada da aplicação
├── operacoes.py             # Abstrações e implementações das operações
├── registro_operacoes.py    # Registro das operações concretas usadas pelos menus
├── README.md                # Documentação do projeto
├── Docs/
│   └── relatorio_revisao.md
├── fisica/
│   ├── __init__.py
│   └── velocidades.py
└── matematica/
    ├── __init__.py
    ├── area/
    │   ├── __init__.py
    │   └── area.py
    └── perimetro/
        ├── __init__.py
        └── perimetro.py
```

## 🧩 Arquitetura

O projeto foi organizado com foco em boas práticas de design, incluindo:

- Separação entre cálculo e interação com o usuário
- Uso de abstrações para operações
- Registro de operações para desacoplar o menu das implementações concretas
- Estrutura modular para facilitar manutenção e extensão

## 🛠️ Requisitos

- Python 3.x

## 📝 Autor

Jonathan - 2026-1