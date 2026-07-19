# DS - US08: Navegar entre Matemática e Física

**User Story:** Como usuário, eu quero escolher entre operações de Matemática e Física, para que eu possa acessar rapidamente a funcionalidade desejada.

---

```mermaid
sequenceDiagram
    actor Usuario
    participant Main as Main (menu_principal)
    participant Dispatcher as MenuDispatcher
    participant SubMenu as menu_matematica / menu_fisica

    Usuario->>Main: Executa o programa
    Main-->>Usuario: "1 - Matemática / 2 - Física / 0 - Sair"

    loop Enquanto usuário não sair
        Usuario->>Main: Digita opção

        alt Opção "1" — Matemática
            Main->>Dispatcher: executar("1")
            Dispatcher->>SubMenu: menu_matematica()
            SubMenu-->>Usuario: Exibe sub-menu de matemática
            Note over SubMenu,Usuario: Usuário interage com o sub-menu<br/>e eventualmente volta para cá.

        else Opção "2" — Física
            Main->>Dispatcher: executar("2")
            Dispatcher->>SubMenu: menu_fisica()
            SubMenu-->>Usuario: Exibe sub-menu de física
            Note over SubMenu,Usuario: Usuário interage com o sub-menu<br/>e eventualmente volta para cá.

        else Opção "0" — Sair
            Main->>Dispatcher: executar("0")
            Dispatcher->>Dispatcher: sair_programa()
            Dispatcher-->>Usuario: "Até logo!"
            Main->>Main: break — encerra o programa

        else Opção inválida
            Main->>Dispatcher: executar(opcao)
            Dispatcher->>Dispatcher: operacoes.get(opcao) → None
            Dispatcher-->>Usuario: "Opção inválida! Tente novamente."
        end
    end
```
