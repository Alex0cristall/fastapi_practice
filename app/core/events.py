from fastapi import FastAPI



def create_start_app_handler(app: FastAPI):
    async def start_app() -> None:
        ...

    return start_app()
