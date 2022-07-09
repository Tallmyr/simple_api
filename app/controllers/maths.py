from starlite import Controller, ValidationException, get


class MathsController(Controller):
    path = "/maths"
    tags = ["Maths"]

    @get(["/add"])
    def add_numbers(self, first: int, second: int) -> int:
        return first + second

    @get(["/subtract"])
    def subtract_numbers(self, first: int, second: int) -> int:
        return first - second

    @get(["/multiply"])
    def multiply_numbers(self, first: int, second: int) -> int:
        return first * second

    @get(["/divide"])
    def divide_numbers(self, first: int, second: int) -> int:
        try:
            assert second != 0
        except AssertionError as e:
            raise ValidationException(detail="Do not divide by zero") from e

        return first / second
