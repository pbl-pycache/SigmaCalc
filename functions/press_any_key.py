import questionary as qt


def press_any_key() -> None:
    """
    English: Prompts the user to press any key to continue using questionary.
    Português: Solicita ao usuário pressionar qualquer tecla para continuar usando o questionary.
    """
    qt.press_any_key_to_continue(
        message="Pressione qualquer botão para continuar ..."
    ).ask()  # English: Message to continue | Português: Mensagem para continuar
