from fastapi import APIRouter
from app.services.meal_service import get_all_meals
from app.schemas.meals import Meal

router = APIRouter()

@router.get("/meals", response_model=list[Meal])
def get_meals():
    return get_all_meals()

