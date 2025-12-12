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

def test_scene_title():
    ontbo = Ontbo(API_KEY, ONTBO_SERVER_ROOT)

    profile = ontbo.create_profile()

    scene = profile.create_scene(title="Initial Title")

    assert scene.title == "Initial Title"

    scene.set_properties(title="Updated Title")

    updated_scene = profile.scene(scene.id)

    assert updated_scene.title == "Updated Title"

    ontbo.delete_profile(profile.id)

# Scene.source_type
def test_scene_source_type():
    ontbo = Ontbo(API_KEY, ONTBO_SERVER_ROOT)

    profile = ontbo.create_profile()

    scene = profile.create_scene(source_type="chatgpt")

    assert scene.source_type == "chatgpt"

    scene.set_properties(source_type="claude")

    updated_scene = profile.scene(scene.id)

    assert updated_scene.source_type == "claude"

    ontbo.delete_profile(profile.id)

# Scene.source_url

# Scene.set_properties

# Scene.add_messages

# Scene.clear_messages

# Scene.messages