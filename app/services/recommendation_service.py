# One function
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
        score = 0
        reason_parts = []
        if mood in meal["mood_tags"]:
            reason_parts.append(f"It matches your current mood ({mood}).")
            score += 2.5
        if effort == meal["effort"]:
            reason_parts.append(f"It requires ({effort}) effort.")
            score += 2.5
        if preparation_time_mins >= meal["preparation_time_mins"]:
            reason_parts.append(f"It can be prepared within your requested time limit ({preparation_time_mins} mins).")
            score += 2.5
        if any(tag in meal["dietary_tags"] for tag in dietary_tags):
            reason_parts.append(f"It matches your dietary preferences ({', '.join(dietary_tags)}).")
            score += 2.5

        reason = " ".join(reason_parts)

        if score == 0:
            reason = "No strong matches, but this meal could still be a good choice!"

        # 4 Return top recommendations
        recommendations.append({
            "meal_name": meal["name"],
            "score": score,
            "reason": reason
        })
    
    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return {"recommendations": recommendations[:3]}