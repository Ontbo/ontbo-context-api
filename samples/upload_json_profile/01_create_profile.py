from ontbo import Ontbo, SceneMessage
from pathlib import Path
import json


if __name__ == "__main__":

    # Script params.
    API_KEY="<YOUR_API_KEY>"
    PROFILE_NAME = "youssef"
    DATA_PATH = "datasets/youssef_50_sessions"
    
    ontbo = Ontbo(API_KEY)

    # (optional) If a profile with the same ID already exists, we delete it.
    if PROFILE_NAME in ontbo.profile_ids:
        ontbo.delete_profile(PROFILE_NAME)

    # Create the new profile.
    profile=ontbo.create_profile(PROFILE_NAME)

    # Check the ID of the created profile.
    print(f"Profile created profile ID is {profile.id}.")
    print(f"Use this ID to query the profile in the query script")

    # Get the list of JSON files to upload.
    data_dir = Path(__file__).resolve().parent / DATA_PATH
    json_files = list(data_dir.glob("*.json"))

    chat_count = len(json_files)
    current_chat=0

    for file in json_files:
        current_chat += 1
        print(f"Uploading chat {current_chat}/{chat_count}")

        # Load JSON data, each message is a dict, with the following structure:
        # {
        #   "content":content,
        #   "role":role,
        #   "timestamp":timestamp,
        # }
        with open(file) as f:
            conversation_data = json.loads(f.read())

        # Each dict in the conversation is conerted in a SceneMessage.
        mesages = [SceneMessage(
                content=message["content"],
                role=message["role"],
                timestamp=message["timestamp"]
            ) for message in conversation_data]
        
        # Create the scene and upload the messages.
        # If you want to be sure that the profile computation is done when the 
        # script ends, set wait_for_result to true.
        scene=profile.create_scene("scene")
        scene.add_messages(mesages, update_now=True, wait_for_result=False)

    print(f"Scene upload complete, whait for a few minutes so the server"\
          "processes all scenes.")
    


