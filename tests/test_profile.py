import os
from ontbo import Ontbo, ProfileNotFoundError

API_KEY=os.getenv("API_KEY")
ONTBO_SERVER_ROOT=os.getenv("ONTBO_SERVER_ROOT")

ontbo = Ontbo(API_KEY, base_url=ONTBO_SERVER_ROOT)


###############################################################################
# Tests for the Profile class
###############################################################################


# Profile.exists

def test_exists():

    profile = ontbo.create_profile()
    assert profile.exists

    ontbo.delete_profile(profile.id)

    assert not profile.exists

# Profile.scene_ids

def test_scene_ids():
    SCENES_COUNT = 10

    profile = ontbo.create_profile()

    created_scenes_ids = []

    for i in range(SCENES_COUNT):
        created_scenes_ids.append(profile.create_scene().id)


    profile_scenes = profile.scene_ids

    for id in created_scenes_ids:
        assert id in profile_scenes

    for id in profile_scenes:
        assert id in created_scenes_ids

    ontbo.delete_profile(profile.id)

def test_scene_ids_on_non_existing_profile():
    
    profile_id = "this_profile_should_not_exist_"
    suffix_id = 0
    existing_ids = ontbo.profile_ids

    while f"{profile_id}{suffix_id}" in existing_ids:
        suffix_id += 1

    exception_raised = False

    try:
        ids = ontbo.profile(f"{profile_id}{suffix_id}").scene_ids
    except ProfileNotFoundError as e:
        exception_raised = True

    assert exception_raised

# Profile.scene

def test_scene_accessor():
    profile_id = "some_random_profile"
    scene_id = "some_random_scene"

    scene = ontbo.profile("some_random_profile").scene("some_random_scene")

    assert scene.id == scene_id
    assert scene._profile_id == profile_id

# Profile.create_scene


def test_create_scene():
    profile = ontbo.create_profile()

    assert profile.scene_ids == []

    new_scene = profile.create_scene()

    assert profile.scene_ids == [new_scene.id]

    ontbo.delete_profile(profile.id)

def test_create_scene_with_params():
    SCENE_TITLE = "This is some random scene title"
    SCENE_SOURCE_URL = "https://my-random-url.com/here"
    SCENE_SOURCE_TYPE = "somesource:yay"
    SCENE_PREFIX = "sceneprefix"

    profile = ontbo.create_profile()

    assert profile.scene_ids == []

    new_scene = profile.create_scene(
        title=SCENE_TITLE,
        source_url=SCENE_SOURCE_URL,
        source_type=SCENE_SOURCE_TYPE,
        prefix=SCENE_PREFIX
    )

    assert profile.scene_ids == [new_scene.id]
    assert new_scene.title == SCENE_TITLE
    assert new_scene.source_url == SCENE_SOURCE_URL
    assert new_scene.source_type == SCENE_SOURCE_TYPE
    print(new_scene.id)
    assert new_scene.id.startswith(SCENE_PREFIX)

    ontbo.delete_profile(profile.id)       

# Profile.delete_scene


def test_delete_scene():
    profile = ontbo.create_profile()

    assert profile.scene_ids == []

    existing_scenes = []
    for i in range(5):
        existing_scenes.append(profile.create_scene())

    scene_list_before = profile.scene_ids
    
    new_scene = profile.create_scene()

    assert new_scene.id in profile.scene_ids
    assert new_scene.id not in scene_list_before

    profile.delete_scene(new_scene.id)
    assert new_scene.id not in profile.scene_ids

    ontbo.delete_profile(profile.id)


# Profile.update

# Profile.update_status

# Profile.list_facts

# Profile.query_facts

# Profile.append_facts

# Profile.get_fact_details

# Profile.delete_fact

# Profile.build_context

# Profile.find_in_scenes