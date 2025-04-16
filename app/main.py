from fastapi import FastAPI
from app.routers import table_router

# from .routers import tables, reservations

app = FastAPI(version="0.0.1b", title="Restaurant booking API")

app.include_router(router=table_router, tags=["Столы"])
# app.include_router(reservations.router)


@app.get(path="/", tags=["Greetings"])
async def root():
    return {"message": "Restaurant Booking API"}
