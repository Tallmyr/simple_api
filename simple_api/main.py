from starlite import Starlite

from simple_api.controllers.maths import MathsController

app = Starlite(route_handlers=[MathsController])
