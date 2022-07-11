from starlite import OpenAPIConfig, Starlite

from app.controllers.maths import MathsController
from app.controllers.logic import LogicController
from app.controllers.morse import MorseController

app = Starlite(
    route_handlers=[MathsController, LogicController, MorseController],
    openapi_config=OpenAPIConfig(
        create_examples=True, title="Boomi Sample API's", version="1.0.0"
    ),
)
