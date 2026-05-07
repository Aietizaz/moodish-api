from pydantic import BaseModel

class Meal(BaseModel):
    id: int
    name: str
    preparation_time_mins: int
    effort: str
    dietary_tags: list[str]
    mood_tags: list[str]
    protein_rating: int
    comfort_rating: int
    ingredients: list[str]