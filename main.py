from lib.ontbo import Ontbo
from lib.scene_message import SceneMessage
from lib.query_type import QueryType

import time
import json
import requests


# ------------------------------
# CONFIGURATION
# ------------------------------
TOKEN = "..."  # Replace with your real API key (https://api.ontbo.com/tokens)
BASE_URL = "https://api.ontbo.com/api/tests/"  # Optional (default: https://api.ontbo.com/api/)

# ------------------------------
# ERROR HANDLER
# ------------------------------
def handle_http_error(e: requests.exceptions.HTTPError, context: str = ""):
    """Centralized HTTP error handler."""
    response = e.response
    print(f"\n❌ HTTP error during {context}: {e}")
    if response is not None:
        print("Status code:", response.status_code)
        try:
            print("Server response (JSON):", json.dumps(response.json(), indent=2))
        except ValueError:
            print("Server response (text):", response.text)
    exit()


# ------------------------------
# CLIENT INITIALIZATION
# ------------------------------
ontbo = Ontbo(token=TOKEN, base_url=BASE_URL)
print("Ontbo client initialized.\n")

# ------------------------------
# LIST EXISTING PROFILES
# ------------------------------
try:
    profiles = ontbo.profile_ids
    print("Existing profiles:", profiles)
except requests.exceptions.HTTPError as e:
    handle_http_error(e, "fetching profiles")

# ------------------------------
# CREATE A NEW PROFILE
# ------------------------------
profile_name = f"alice_test_{int(time.time())}"
new_profile = None
try:
    new_profile = ontbo.create_profile(profile_name)
    print(f"\nProfile created: {new_profile.id}")
except requests.exceptions.HTTPError as e:
    handle_http_error(e, "creating profile")

# ------------------------------
# CREATE A SCENE
# ------------------------------
scene = None
if new_profile:
    scene_name = "scene_test"
    try:
        scene = new_profile.create_scene(scene_name)
        print(f"Scene created: {scene.id}")
    except requests.exceptions.HTTPError as e:
        handle_http_error(e, "creating scene")

# ------------------------------
# ADD MESSAGES TO THE SCENE
# ------------------------------
if new_profile and scene:
    messages = [
        SceneMessage(content="Hello, my name is Alice!", role="user", timestamp=time.time()),
        SceneMessage(content="Hi Alice! I am your assistant.", role="assistant", timestamp=time.time())
    ]

    try:
        msg_batch_id = scene.add_messages(messages, update_now=True, wait_for_result=True)
        print("Messages added, batch ID:", msg_batch_id)
    except requests.exceptions.HTTPError as e:
        handle_http_error(e, "adding messages")

# ------------------------------
# TEST QUERY FACTS (optional)
# ------------------------------
if new_profile:
    try:
        answer = new_profile.query_facts("What is my name?", query_type=QueryType.FULL_DATA)
        print("\nAnswer to the question on facts:", answer)
    except requests.exceptions.HTTPError as e:
        handle_http_error(e, "querying facts")

# ------------------------------
# CLEANUP: delete scene and profile
# ------------------------------
if new_profile and scene:
    try:
        scene.clear_messages()
        deleted_scene = new_profile.delete_scene(scene.id)
        print(f"\nScene deleted: {deleted_scene}")
    except requests.exceptions.HTTPError as e:
        handle_http_error(e, "deleting scene")

if new_profile:
    try:
        deleted_profile = ontbo.delete_profile(new_profile.id)
        print(f"Profile deleted: {deleted_profile}")
    except requests.exceptions.HTTPError as e:
        handle_http_error(e, "deleting profile")
