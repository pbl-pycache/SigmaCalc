import questionary as qt
from settings.log import logger
from functions.press_any_key import press_any_key
from functions.clear import clear

# English: Custom style for questionary prompts
# Português: Estilo personalizado para prompts do questionary
custom_style = qt.Style(
    [
        (
            "qmark",
            "fg:#673ab7 bold",
        ),  # English: Question mark style | Português: Estilo do ponto de interrogação
        ("question", "bold"),  # English: Question text | Português: Texto da pergunta
        (
            "answer",
            "fg:#f44336 bold",
        ),  # English: Submitted answer text | Português: Texto da resposta enviada
        (
            "pointer",
            "fg:#673ab7 bold",
        ),  # English: Pointer in select/checkbox | Português: Ponteiro em seleção/checkbox
        (
            "highlighted",
            "fg:#673ab7 bold",
        ),  # English: Highlighted choice | Português: Opção destacada
        (
            "selected",
            "fg:#cc5454",
        ),  # English: Selected item style | Português: Estilo do item selecionado
        (
            "separator",
            "fg:#cc5454",
        ),  # English: Separator in lists | Português: Separador em listas
        (
            "instruction",
            "",
        ),  # English: User instructions | Português: Instruções ao usuário
        ("text", ""),  # English: Plain text | Português: Texto simples
        (
            "disabled",
            "fg:#858585 italic",
        ),  # English: Disabled choices | Português: Opções desabilitadas
    ]
)


def main() -> None:
    """
    English: Main entry point for SigmaCalc. Displays the main menu and handles user selection.
    Português: Ponto de entrada principal do SigmaCalc. Exibe o menu principal e lida com a seleção do usuário.
    """
    logger.info(
        "'SigmaCalc' foi iniciada"
    )  # English: Log that SigmaCalc has started | Português: Loga que o SigmaCalc foi iniciado

    while True:
        clear()  # English: Clear the terminal screen | Português: Limpa a tela do terminal

        option = qt.select(
            message="Escolha uma opção",  # English: Choose an option | Português: Escolha uma opção
            choices=[
                "Calculadora Simples",  # English: Simple Calculator | Português: Calculadora Simples
                "Calculadora Avançada",  # English: Advanced Calculator | Português: Calculadora Avançada
                "Calculadora Cientifica",  # English: Scientific Calculator | Português: Calculadora Científica
                "Graficos",  # English: Graphs | Português: Gráficos
                "Sair",  # English: Exit | Português: Sair
            ],
            style=custom_style,
        ).ask()

        if option is None:
            logger.warning("O usuário encerrou o programa sem escolher uma opção.")
            logger.warning("Sistema 'SigmaCalc' encerrado pelo usuário sem seleção.")
            exit(
                1
            )  # English: Exit if no option is selected | Português: Sai se nenhuma opção for selecionada

        elif option == "Sair":
            # English: Log exit choice | Português: Loga a escolha de sair
            logger.info("Sistema 'SigmaCalc' encerrado pelo usuário.")
            print("Saindo do SigmaCalc...")

        else:
            # English: Log user choice | Português: Loga a escolha do usuário
            logger.info(
                f"Usuário escolheu: '{option}'"
            )  # English: Log user choice | Português: Loga a escolha do usuário
            print(
                f"Esta função ainda não foi implementada: {option}"
            )  # English: This function is not yet implemented | Português: Esta função ainda não foi implementada
            press_any_key()  # English: Prompt to press any key to continue | Português: Solicita ao usuário pressionar

            return  # English: Exit after one loop (for now) | Português: Sai após um loop (por enquanto)

        break  # English: Exit after one loop (for now) | Português: Sai após um loop (por enquanto)


if __name__ == "__main__":
    main()  # English: Run the main function | Português: Executa a função principal
