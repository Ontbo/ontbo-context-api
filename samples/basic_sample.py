# Sample application for the Ontbo API Python client.
# (c) 2025 Ontbo / Aphelior S.A.S.

from ontbo import Ontbo, SceneMessage

import time
import json
import requests


# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------

# Replace with your real API token 
# (Create your Ontbo account, then get one at https://api.ontbo.com/tokens)
TOKEN = "<YOU_API_TOKEN>"  

# -----------------------------------------------------------------------------
# Utilitary function for error handling
# -----------------------------------------------------------------------------

def handle_http_error(e: requests.exceptions.HTTPError, context: str = ""):
    """Centralized HTTP error handler."""
    response = e.response
    print(f"\n❌ HTTP error during {context}: {e}")
    if response is not None:
        print("Status code:", response.status_code)
        try:
            print(
                "Server response (JSON):", 
                json.dumps(response.json(), indent=2))
            
        except ValueError:
            print("Server response (text):", response.text)
    exit()

if __name__ == "__main__":

    # -------------------------------------------------------------------------
    # Step 1: client intialization.
    # We create an instance of the Ontbo class. This class is used to aceess
    # all the functions of the Ontbo API.
    #
    # To use this class you must have an Ontbo account, and a valid API key.
    # Create your Ontbo account (for free) here: https://api.ontbo.com/
    # -------------------------------------------------------------------------

    ontbo = Ontbo(token=TOKEN)
    print("Ontbo client initialized.\n")

    # -------------------------------------------------------------------------
    # (optional) Listing existing profiles. 
    # -------------------------------------------------------------------------

    try:
        profiles = ontbo.profile_ids
        print("Existing profiles:", profiles)
        
    except requests.exceptions.HTTPError as e:
        handle_http_error(e, "fetching profiles")

    # -------------------------------------------------------------------------
    # Step 2: create a new profile.
    # A profile stores all data regarding a specific person.
    # -------------------------------------------------------------------------

    profile_name = f"alice_test_{int(time.time())}"
    try:
        new_profile = ontbo.create_profile(profile_name)
        if not new_profile:
            raise Exception("Error: profile not created.")        
        
        print(f"\nProfile created: {new_profile.id}")

    except requests.exceptions.HTTPError as e:
        handle_http_error(e, "creating profile")

    # -------------------------------------------------------------------------
    # Step 3: create a scene.
    # 
    # A scene is one interaction between you user and the system. As of this
    # version of the API, it is user to represent a chat between the user and
    # an AI.
    # -------------------------------------------------------------------------
    
    SCENE_NAME = "scene_test"

    try:
        scene = new_profile.create_scene(SCENE_NAME)

        if not scene:
            raise Exception("Error: scene not created.")         

        print(f"Scene created: {scene.id}")

    except requests.exceptions.HTTPError as e:
        handle_http_error(e, "creating scene")


    # -------------------------------------------------------------------------
    # Step 4: Add messages to the scene.
    # 
    # Basically a scene is a list of exchanges of text messages. We use a
    # representation close to what we found with mainstream LLMs:
    # [
    #   {
    #       "role": "user", <- either "user" or "assistant"
    #       "content": "content", <- the message itself
    #       "timestamp": "timestamp" <- the Unix timestamp of the message.
    #   },
    #   ...
    # ]    
    # -------------------------------------------------------------------------

    MESSAGES = [
        SceneMessage(
            content="Hello, my name is Alice!", 
            role="user", 
            timestamp=time.time()),

        SceneMessage(
            content="Hi Alice! I am your assistant.", 
            role="assistant", 
            timestamp=time.time())
    ]

    try:
        scene.add_messages(
            MESSAGES, 
            update_now=True, 
            wait_for_result=True)
        
        print(f"Messages added")

    except requests.exceptions.HTTPError as e:
        handle_http_error(e, "adding messages")

    # -------------------------------------------------------------------------
    # Step 5: query facts.
    # 
    # You can ask a question about the profile.
    # In real-world application, the profile quering will be done in a 
    # different part of your application, when you want to retrieve information
    # about the user.
    # -------------------------------------------------------------------------

    try:
        QUERY = "What is the user's name?"
        answer = new_profile.query_facts(QUERY)
        print(f"Answer for query \"{QUERY}\": {answer}")

    except requests.exceptions.HTTPError as e:
        handle_http_error(e, "querying facts")

    # -------------------------------------------------------------------------
    # (optional) cleanup: delete the profile.
    # -------------------------------------------------------------------------
    
    try:
        deleted_profile = ontbo.delete_profile(new_profile.id)
        print(f"Profile deleted: {deleted_profile}")

    except requests.exceptions.HTTPError as e:
        handle_http_error(e, "deleting profile")
