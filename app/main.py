import questionary as qt
from settings.log import logger
from functions.press_any_key import press_any_key
from functions.clear import clear
from app.styles import custom_style
from app.calculadora.calculadora_simples import calculadora_simples


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

        elif option == "Calculadora Simples":
            # English: Start Simple Calculator | Português: Inicia a Calculadora Simples
            calculadora_simples()

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
