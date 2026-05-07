import json
from pathlib import Path

# Load meals from JSON file
data_path = Path(__file__).parent / "meals.json"

with open(data_path, encoding='utf-8') as f:
    meals = json.load(f)