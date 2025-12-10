import os
from ontbo import Ontbo, SceneMessage, ProfileNotFoundError, SceneNotFoundError, UpdateStatus

API_KEY=os.getenv("API_KEY")
ONTBO_SERVER_ROOT=os.getenv("ONTBO_SERVER_ROOT")

ontbo = Ontbo(API_KEY, base_url=ONTBO_SERVER_ROOT)


# Scene.id

# Scene.exists

def test_scene_exists():
    ontbo = Ontbo(API_KEY, ONTBO_SERVER_ROOT)

    profile = ontbo.create_profile()

    scene = profile.scene("this_scene_does_not_exists")

    assert not scene.exists

    scene = profile.create_scene()

    assert scene.exists

    ontbo.delete_profile(profile.id)

# Scene.title

# Scene.source_type

# Scene.source_url

# Scene.set_properties

# Scene.add_messages

# Scene.clear_messages

# Scene.messages