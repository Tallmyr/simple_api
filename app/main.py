from starlite import OpenAPIConfig, Starlite

from app.controllers.maths import MathsController

app = Starlite(
    route_handlers=[MathsController],
    openapi_config=OpenAPIConfig(
        create_examples=True, title="Boomi Sample API's", version="1.0.0"
    ),
)
