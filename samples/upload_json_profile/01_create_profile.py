from config import config
from ontbo import Ontbo, SceneMessage
from pathlib import Path
import json


if __name__ == "__main__":

    PROFILE_NAME = "youssef"
    DATA_PATH = "datasets/youssef_50_sessions"

    ontbo = Ontbo(token=config["API_KEY"], base_url=config["BASE_URL"])

    profile=ontbo.create_profile(PROFILE_NAME)

    print(f"Profile created profile ID is {profile.id}")
    print(f"Use this ID to query the profile in the query script")


    data_dir = Path(__file__).resolve().parent / DATA_PATH

    json_files = list(data_dir.glob("*.json"))

    chat_count = len(json_files)
    current_chat=0

    for file in json_files:
        current_chat += 1
        print(f"Uploading chat {current_chat}/{chat_count}")

        with open(file) as f:
            conversation_data = json.loads(f.read())

        mesages = [SceneMessage(
                content=message["content"],
                role=message["role"],
                timestamp=message["timestamp"]
            ) for message in conversation_data]
        
        scene=profile.create_scene("scene")
        scene.add_messages(mesages, update_now=True, wait_for_result=False)

    print(f"Scene upload complete, whait for a few minutes so the server"\
          "processes all scenes.")
    


