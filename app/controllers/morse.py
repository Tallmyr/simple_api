from starlite import Controller, post

from app.functions.morse import text_to_morse, morse_to_text
from app.models.morse import Morse, Text


class MorseController(Controller):
    path = "/morse"
    tags = ["morse"]

    @post(["/text_to_morse"])
    def text_to_morse(self, data: Text) -> Morse:
        return Morse(morse_code=text_to_morse(data.text))

    @post(["/morse_to_text"])
    def morse_to_text(self, data: Morse) -> Text:
        return Text(text=morse_to_text(data.morse_code))
