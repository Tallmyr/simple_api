from starlite import Starlite

from app.controllers.maths import MathsController

app = Starlite(route_handlers=[MathsController])
