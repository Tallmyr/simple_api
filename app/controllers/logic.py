from starlite import Controller, get


class LogicController(Controller):
    path = "/logic"
    tags = ["Logic"]

    @get(["/isodd/{number:int}"])
    def is_odd(self, number: int) -> bool:
        return number % 2 != 0

    @get(["/iseven/{number:int}"])
    def is_even(self, number: int) -> bool:
        return number % 2 == 0
