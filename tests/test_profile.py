import os
import time
from ontbo import Ontbo, SceneMessage, ProfileNotFoundError, SceneNotFoundError, UpdateStatus

API_KEY=os.getenv("API_KEY")
ONTBO_SERVER_ROOT=os.getenv("ONTBO_SERVER_ROOT")

ontbo = Ontbo(API_KEY, base_url=ONTBO_SERVER_ROOT)

PROFILE_UPDATE_MAX_SECONDS_WAIT = 30

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

def test_delete_scene_non_existing():
    exception_raised = False
    try:
        ontbo.profile("Non_existing_profile").delete_scene("some_scene")

    except ProfileNotFoundError:
        exception_raised = True
    
    assert exception_raised

    exception_raised = False

    profile = ontbo.create_profile()
    try:
        profile.delete_scene("some_scene")

    except SceneNotFoundError:
        exception_raised = True
    
    assert exception_raised

    ontbo.delete_profile(profile.id)    


# Profile.update

def test_profile_update():
    profile = ontbo.create_profile()

    scene = profile.create_scene()

    scene.add_messages(
        [SceneMessage("Hi, my name is Mike !")]
        )
    
    status = profile.update()
    assert status.pending == 1

    ontbo.delete_profile(profile.id)


def test_profile_update_on_non_existing_profile():
    profile = ontbo.profile("this_profile_does_not_exist")

    assert not profile.exists

    exception_raised = False

    try:
        profile.update()
    except ProfileNotFoundError:
        exception_raised = True

    assert exception_raised

# Profile.update_status

def test_update_status():
    profile = ontbo.create_profile()

    # This profile has just been created, so the pending sount should be zero.
    assert profile.update_status().pending == 0

    scene = profile.create_scene()

    scene.add_messages(
        [SceneMessage("Hi, my name is Mike !")]
        )
    
    status = profile.update()
    assert status.pending == profile.update_status().pending
    
    ontbo.delete_profile(profile.id)
    
def test_update_status_on_non_existing():
    profile = ontbo.profile("non_existing_profile")

    exception_raised = False

    try:
        profile.update_status()
    except ProfileNotFoundError:
        exception_raised = True

    assert exception_raised

# Profile.query_facts
# Profile.build_context


def test_profile_query_facts():

    profile = ontbo.create_profile()

    # This profile has just been created, so the pending sount should be zero.
    assert profile.update_status().pending == 0

    scene = profile.create_scene()

    scene.add_messages(
        [SceneMessage("Hi, my name is Mike and I am a software engineer !")]
        )
    
    status = profile.update()
    assert status.pending == profile.update_status().pending

    retry_count = PROFILE_UPDATE_MAX_SECONDS_WAIT

    while profile.update_status().pending != 0 and retry_count > 0:
        time.sleep(1)

    assert retry_count > 0

    assert profile.query_facts("What is the user's name?").find("Mike")
    assert profile.query_facts("What is the user's job?").find("engineer")

    assert profile.build_context("White me an introduction letter for a job").find("engineer")

    ontbo.delete_profile(profile.id)    



# Profile.append_facts

def test_profile_append_facts():


    profile = ontbo.create_profile()

    # This profile has just been created, so the pending sount should be zero.
    assert profile.update_status().pending == 0

    profile.append_facts("I like bananas")

    profile.update()

    retry_count = PROFILE_UPDATE_MAX_SECONDS_WAIT

    while profile.update_status().pending != 0 and retry_count > 0:
        time.sleep(1)

    assert retry_count > 0

    assert profile.query_facts("What fruit does the user like?").find("Banana")

    ontbo.delete_profile(profile.id)    


# Profile.list_facts
# Profile.get_fact_details
# Profile.delete_fact


def test_profile_list_facts():

    profile = ontbo.create_profile()

    assert profile.list_facts() == []

    profile.append_facts("I like bananas")

    profile.update()

    while profile.update_status().pending != 0 and retry_count > 0:
        time.sleep(1)

    retry_count = PROFILE_UPDATE_MAX_SECONDS_WAIT

    assert retry_count > 0

    facts = profile.list_facts(fields=["id", "data", "timestamp"])

    assert facts != []

    assert "id" in facts[0].keys()
    assert "data" in facts[0].keys()
    assert "timestamp" in facts[0].keys()

    fact_id = facts[0]["id"]


    profile.delete_fact(fact_id)

    facts = profile.list_facts(fields=["id", "data", "timestamp"])

    assert fact_id not in [fact["id"] for fact in facts]


    ontbo.delete_profile(profile.id)    




# TODO when implemented
# Profile.find_in_scenes


