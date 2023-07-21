from fastapi.routing import APIRoute
from typing import Callable
from fastapi import Request, Response

class LogRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            """
            Do Something
            """
            response: Response = await original_route_handler(request)
            return response