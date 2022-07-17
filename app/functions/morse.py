from starlite import ValidationException

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
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def text_to_morse(text: str, space_seperator: str) -> str:
    morse_table[" "] = space_seperator
    try:
        assert all(c in morse_table.keys() for c in text.upper())
    except AssertionError as e:
        raise ValidationException(
            detail="Unsupported characters. This function only supports A-Z, 0-9 and Space."
        ) from e
    return "".join(f"{morse_table[letter]} " for letter in text.upper())


def morse_to_text(morse: str, space_seperator: str) -> str:
    morse_table[" "] = space_seperator
    try:
        assert all(c in set(f".- {space_seperator}") for c in morse)
    except AssertionError as e:
        raise ValidationException(
            detail="Unsupported characters. This function only supports '.', '-', 'Space' and the chosen Space Seperator",
            extra=f"space_seperator = '{space_seperator}'",
        ) from e
    letter_table = {v: k for k, v in morse_table.items()}
    return "".join(f"{letter_table[code]}" for code in morse.split())
