from enum import Enum
from pydantic import BaseModel, Field


class Space_separator(str, Enum):
    slash = "/"
    dots = "....."
    dash = "-----"


class Morse(BaseModel):
    morse_code: str = Field(
        title="Morse Code",
        description="Morse Code with Dots and Dashes. Spaces for letter separation.",
    )


class MorseInput(Morse):
    space_separator: Space_separator = Field(
        "/", title="Space Separator", description="Choose how to separate words."
    )


class Text(BaseModel):
    text: str = Field(
        title="Text", description="Alphanumeric Text (A-Z, 0-9 and Space only)"
    )


class TextInput(Text):
    space_separator: Space_separator = Field(
        "/", title="Space Separator", description="Choose how to separate words."
    )
