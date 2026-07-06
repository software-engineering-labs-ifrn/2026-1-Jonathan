```mermaid
classdiagram

flowchart LR

    Usuario[👤 Usuário]

    subgraph Sistema["Sistema Calculadora"]
        UC1((Iniciar sistema))
        UC2((Selecionar Matemática))
        UC3(("Selecionar Física"))

        UC4((Calcular Área))
        UC5((Calcular Perímetro))

        UC6((Calcular Velocidade Média))
        UC7((Calcular Movimento Uniforme))
        UC8((Calcular Movimento Uniformemente Variado))
        UC9((Calcular Velocidade Final))
        UC10((Calcular Equação de Torricelli))
        UC11((Calcular Queda Livre))
        UC12((Calcular Lançamento Vertical))
        UC13((Calcular Velocidade Angular))

        UC14((Informar Dados))
        UC15((Visualizar Resultado))
    end

    Usuario --> UC1

    UC1 --> UC2
    UC1 --> UC3

    UC2 --> UC4
    UC2 --> UC5

    UC3 --> UC6
    UC3 --> UC7
    UC3 --> UC8
    UC3 --> UC9
    UC3 --> UC10
    UC3 --> UC11
    UC3 --> UC12
    UC3 --> UC13

    UC4 -.<<include>>.-> UC14
    UC5 -.<<include>>.-> UC14
    UC6 -.<<include>>.-> UC14
    UC7 -.<<include>>.-> UC14
    UC8 -.<<include>>.-> UC14
    UC9 -.<<include>>.-> UC14
    UC10 -.<<include>>.-> UC14
    UC11 -.<<include>>.-> UC14
    UC12 -.<<include>>.-> UC14
    UC13 -.<<include>>.-> UC14

    UC14 --> UC15