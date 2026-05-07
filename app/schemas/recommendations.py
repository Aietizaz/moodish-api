from pydantic import BaseModel

class MealRecommendation(BaseModel):
    meal_name: str
    score: float
    reason: str

# so essentiallly meal recommendation is a meal name, a score and a reason for the recommendation. The meals are then listed in the recommendations request which is a list of meal recommendations. This is what the API will return when the user requests meal recommendations based on their mood and dietary preferences. The score can be used to rank the recommendations and the reason can provide some insight into why the meal was recommended.

class RecommendationRequest(BaseModel):
    mood: str
    dietary_tags: list[str]
    effort: str
    preparation_time_mins: int

class RecommendationsResponse(BaseModel):
    recommendations: list[MealRecommendation]