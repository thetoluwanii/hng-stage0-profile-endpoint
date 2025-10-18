from django.http import JsonResponse
import requests
from datetime import datetime, timezone

def get_profile(request):
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=10)
        response.raise_for_status()
        data = response.json()
        cat_fact = data.get("fact", "Cats are awesome!")
    except Exception as e:
        print("Error fetching cat fact:", e)
        cat_fact = "Unable to fetch cat fact at the moment."

    current_time = datetime.now(timezone.utc).isoformat()

    profile_data = {
        "status": "success",
        "user": {
            "email": "gracetoluwanii@gmail.com",
            "name": "Omojunikanbi Toluwanimi Grace",
            "stack": "Python/Django"
        },
        "timestamp": current_time,
        "fact": cat_fact
    }

    return JsonResponse(profile_data)
