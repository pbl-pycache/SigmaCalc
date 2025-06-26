import os


def clear() -> None:
    """
    English: Clears the terminal screen for Windows or Unix systems.
    Português: Limpa a tela do terminal para sistemas Windows ou Unix.
    """
    if os.name == "nt":
        os.system("cls")  # English: Clear for Windows | Português: Limpa no Windows
    else:
        os.system(
            "clear"
        )  # English: Clear for Unix/Linux | Português: Limpa no Unix/Linux
