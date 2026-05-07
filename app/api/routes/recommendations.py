from fastapi import APIRouter
from app.schemas.recommendations import RecommendationsResponse, RecommendationRequest
from app.services.recommendation_service import get_recommendations

router = APIRouter()

@router.post("/recommendations", response_model=RecommendationsResponse)
def recommendations(request: RecommendationRequest):
    return get_recommendations(request.mood, request.dietary_tags, request.effort, request.preparation_time_mins)

