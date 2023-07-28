from fastapi import FastAPI

from routers import ROUTERS



app = FastAPI()

for router in ROUTERS:

    app.include_router(router)


