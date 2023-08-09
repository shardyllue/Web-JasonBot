from fastapi import FastAPI

import endpoint


app = FastAPI(
    title="API for Jason's Project",
    version="0.0.3",
    description="API for Jason's Project",
    openapi_url="/jasonapi.json"
)

app.include_router(endpoint.routers)


