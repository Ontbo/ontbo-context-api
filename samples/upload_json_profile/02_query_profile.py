from ontbo import Ontbo, SceneMessage
from pathlib import Path
import json


if __name__ == "__main__":
    # The ID of your newly created profile. 
    API_KEY="<YOUR_API_KEY>"
    PROFILE_ID = "youssef"

    ontbo = Ontbo(API_KEY)
    profile=ontbo.profile(PROFILE_ID)
    print(profile.query_facts("What is the user's job?"))


