from starlite import Starlite

from app.controllers.maths import MathsController
from app.controllers.logic import LogicController

app = Starlite(route_handlers=[MathsController, LogicController])
