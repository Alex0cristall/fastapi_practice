import uvicorn

from fastapi import FastAPI


from api.routes.api import router as api_router
from db.events import init_models





def get_application() -> FastAPI:
    application = FastAPI()

    # application.add_event_handler(
    #     'startup',
    #     init_models
    # )

    application.include_router(api_router)

    return application




if __name__ == '__main__':
    uvicorn.run('main:get_application', reload=True)
