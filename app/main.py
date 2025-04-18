from fastapi import FastAPI
from app.routers import table_router, reservation_router

# from .routers import tables, reservations

app = FastAPI(version="0.0.1b", title="Restaurant booking API", debug=True)


app.include_router(router=table_router, tags=["Столы"])
app.include_router(router=reservation_router, tags=["Бронирование"])


@app.get(path="/", tags=["Greetings"])
async def root():
    return {"message": "Restaurant Booking API"}
