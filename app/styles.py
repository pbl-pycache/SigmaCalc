import questionary as qt

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
