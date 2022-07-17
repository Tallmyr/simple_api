from starlite import Controller, post

from app.functions.morse import text_to_morse, morse_to_text
from app.models import morse


class MorseController(Controller):
    path = "/morse"
    tags = ["morse"]

    @post(["/text_to_morse"])
    def text_to_morse(self, data: morse.TextInput) -> morse.Morse:
        return morse.Morse(morse_code=text_to_morse(data.text, data.space_separator))

    @post(["/morse_to_text"])
    def morse_to_text(self, data: morse.MorseInput) -> morse.Text:
        return morse.Text(text=morse_to_text(data.morse_code, data.space_separator))
