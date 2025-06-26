from settings.log import logger
from functions.press_any_key import press_any_key
from functions.clear import clear
from app.styles import custom_style

import questionary as qt


def calculadora_simples() -> None:
    """
    English: Starts the Simple Calculator menu loop, handles user input, performs calculations, and logs actions.
    Português: Inicia o loop do menu da Calculadora Simples, lida com a entrada do usuário, realiza cálculos e registra ações.
    """
    logger.info(
        "'Calculadora Simples' iniciada"
    )  # English: Simple Calculator started | Português: Calculadora Simples iniciada

    while True:
        clear()  # English: Clear the terminal screen | Português: Limpa a tela do terminal
        option = qt.select(
            message="Escolha uma operação",  # English: Choose an operation | Português: Escolha uma operação
            choices=[
                "Soma",  # English: Addition | Português: Soma
                "Subtração",  # English: Subtraction | Português: Subtração
                "Multiplicação",  # English: Multiplication | Português: Multiplicação
                "Divisão",  # English: Division | Português: Divisão
                "Módulo",  # English: Modulo | Português: Módulo
                "Potência",  # English: Power | Português: Potência
                "Raiz Quadrada",  # English: Square Root | Português: Raiz Quadrada
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
            logger.info("Sistema 'SigmaCalc' encerrado pelo usuário.")
            print("Saindo da Calculadora Simples...")
            break  # English: Exit if 'Sair' is selected | Português: Sai se 'Sair' for selecionado

        else:
            logger.info(
                f"Operação selecionada: {option}"
            )  # English: Log selected operation | Português: Loga a operação selecionada
            print(
                f"Você escolheu a operação: {option}"
            )  # English: Show selected operation | Português: Mostra a operação selecionada

            try:
                if option == "Soma":
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    resultado = num1 + num2
                    print(f"O resultado da soma é: {resultado}")

                elif option == "Subtração":
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    resultado = num1 - num2
                    print(f"O resultado da subtração é: {resultado}")

                elif option == "Multiplicação":
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    resultado = num1 * num2
                    print(f"O resultado da multiplicação é: {resultado}")

                elif option == "Divisão":
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    if num2 == 0:
                        print(
                            "Erro: Divisão por zero não é permitida."
                        )  # English: Division by zero error | Português: Erro de divisão por zero
                    else:
                        resultado = num1 / num2
                        print(f"O resultado da divisão é: {resultado}")

                elif option == "Módulo":
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    resultado = num1 % num2
                    print(f"O resultado do módulo é: {resultado}")

                elif option == "Potência":
                    base = float(input("Digite a base: "))
                    expoente = float(input("Digite o expoente: "))
                    resultado = base**expoente
                    print(f"O resultado da potência é: {resultado}")

                elif option == "Raiz Quadrada":
                    num = float(input("Digite o número: "))
                    if num < 0:
                        print(
                            "Erro: Raiz quadrada de número negativo não é permitida."
                        )  # English: Negative square root error | Português: Erro de raiz quadrada negativa
                    else:
                        resultado = num**0.5
                        print(f"A raiz quadrada de {num} é: {resultado}")
            except ValueError:
                print(
                    "Erro: Entrada inválida. Por favor, digite um número válido."
                )  # English: Invalid input error | Português: Erro de entrada inválida

            press_any_key()  # English: Prompt to press any key to continue | Português: Solicita ao usuário pressionar qualquer tecla para continuar
