from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.meals import router as meals_router
from app.api.routes.recommendations import router as recommendations_router

app = FastAPI()
app.include_router(health_router)
app.include_router(meals_router)
app.include_router(recommendations_router)

@app.get("/")
def root():
    return {"message": "Moodish"}