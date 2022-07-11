morse_table = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--. ",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/",
}


def text_to_morse(text: str) -> str:
    return "".join(f"{morse_table[letter]} " for letter in text.upper())


def morse_to_text(morse: str) -> str:
    letter_table = {v: k for k, v in morse_table.items()}
    return "".join(f"{letter_table[code]}" for code in morse.split())
