from config import config
from ontbo import Ontbo, SceneMessage
from pathlib import Path
import json


if __name__ == "__main__":

    PROFILE_NAME = "youssef_0"

    ontbo = Ontbo(token=config["API_KEY"], base_url=config["BASE_URL"])

    profile=ontbo.profile(PROFILE_NAME)

    print(profile.query_facts("What is the user's job?"))


