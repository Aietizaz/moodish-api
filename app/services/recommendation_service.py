# One functtion
# 1. gets all meals
# 2. scores them
# 3. returns top recommendations
from app.services.meal_service import get_all_meals

def get_recommendations(mood: str, dietary_tags: list[str], effort: str, preparation_time_mins: int):
    # 1. Get all meals
    meals = get_all_meals()

    # 2. Score meals based on mood and dietary tags
    recommendations = []
    for meal in meals:
        reason = ""
        score = 0;
        if mood in meal["mood_tags"]:
            score += 5
        for tag in dietary_tags:
            if tag in meal["dietary_tags"]:
                score += 5
        if effort == meal["effort"]:
            score += 5
        if preparation_time_mins >= meal["preparation_time_mins"]:
            score += 5
        # 3. Add reason for recommendation
        if mood in meal["mood_tags"]:
            reason += f"Matches your mood ({mood}). "

        # 4 Return top recommendations
        recommendations.append({
            "meal_name": meal["name"],
            "score": score,
            "reason": reason
        })
    
    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return {"recommendations": recommendations}

# user request



