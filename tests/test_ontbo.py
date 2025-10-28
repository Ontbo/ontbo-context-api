import os
from ontbo import Ontbo, ProfileNotFoundError

API_KEY=os.getenv("API_KEY")
ONTBO_SERVER_ROOT=os.getenv("ONTBO_SERVER_ROOT")

ontbo = Ontbo(API_KEY, base_url=ONTBO_SERVER_ROOT)


###############################################################################
# Tests for the Ontbo class
###############################################################################


def test_incorrect_api_key():
    ontbo_wrong_key = Ontbo("a_very_suspiscious_api_key_f465fds645fdsqf645qsdc645cqcdsq", base_url=ONTBO_SERVER_ROOT)

    excepted = False
    try:
        ids = ontbo_wrong_key.profile_ids()
    except Exception as e:
        excepted = True

    assert excepted  

# Ontbo.profile_ids

def test_list_profiles():
    
    profiles = ontbo.profile_ids

    assert type(profiles) == list

    for profile_id in profiles:
        assert type(profile_id) == str

# Ontbo.profile

def test_profile():
    profile_id = "some_random_id"

    profile = ontbo.profile(profile_id)

    assert profile.id == profile_id

# Ontbo.create_profile

def test_create_profile():
    desired_id = "some_random_profile_id"
    old_profiles = ontbo.profile_ids
    profile = ontbo.create_profile(desired_id)

    assert profile.id not in old_profiles
    assert profile.id in ontbo.profile_ids

    # We delete the profile to keep everything clean

    ontbo.delete_profile(profile.id)

def test_create_profile_without_id():

    old_profiles = ontbo.profile_ids
    profile = ontbo.create_profile()

    assert profile.id not in old_profiles
    assert profile.id in ontbo.profile_ids

    ontbo.delete_profile(profile.id)

# Ontbo.delete_profile

def test_delete_profile():

    profiles_start = ontbo.profile_ids
    profile = ontbo.create_profile()

    assert profile.id not in profiles_start
    assert profile.id in ontbo.profile_ids

    ontbo.delete_profile(profile.id)

    assert profile.id not in ontbo.profile_ids


def test_delete_profile_nonexistent():
    profile_id = "this_profile_should_not_exist_"
    suffix_id = 0
    existing_ids = ontbo.profile_ids

    while f"{profile_id}{suffix_id}" in existing_ids:
        suffix_id += 1

    exception_raised = False

    try:
        ontbo.delete_profile(f"{profile_id}{suffix_id}")
    except ProfileNotFoundError as e:
        exception_raised = True

    assert exception_raised
        

