from urllib.parse import urljoin
from typing import List

from ontbo.i_ontbo_server import IOntboServer
from ontbo.profile import Profile

import requests


class Ontbo(IOntboServer):
    """
    Main client class for interacting with the Ontbo server.

    This class manages profiles on the server and provides authentication
    via a bearer token.
    """

    def __init__(self, token: str, base_url: str = "https://api.ontbo.com/api/v1.3/"):
        """
        Initialize the Ontbo client.

        Args:
            token (str): API authentication token.
            base_url (str): Optional, base URL of the Ontbo API. Use this if
            you need to connect to third-party instances of the Ontbo API.
        """
        self._url = base_url
        self._headers = {"Authorization": f"Bearer {token}"}

    @property
    def profile_ids(self) -> List[str]:
        """
        Retrieve the list of profile IDs already present on the server.

        Returns:
            List[str]: A list of profile UIDs.
        """
        response = requests.get(
            urljoin(self._url, "profiles"),
            headers=self._headers,
        )
        response.raise_for_status()
        return response.json()

    def profile(self, id: str) -> Profile:
        """
        Returns the existing profile with the selected ID. Warning: does not 
        check is the cprofile actually exists on the server. 
        Use Ontbo.profile_ids to check if the profile exists. 

        Args:
            id (str): The profile UID.

        Returns:
            Profile: The corresponding Profile object.
        """
        return Profile(self, id)

    def create_profile(self, requested_id: str) -> Profile:
        """
        Create a new profile on the server.

        Args:
            requested_id (str): The desired ID for the new profile. Uniqueness 
            is enforced server-side. If a profile with the requested ID exists, 
            the new profile IDs is created by adding a suffix to the profile ID.

        Returns:
            Profile: The newly created Profile object.
        """
        response = requests.post(
            urljoin(self._url, "profiles"),
            params={"requested_id": requested_id},
            headers=self._headers,
        )
        response.raise_for_status()
        return Profile(self, response.json()["id"])

    def delete_profile(self, id: str) -> bool:
        """
        Delete a profile from the server (along with its scenes).

        Args:
            id (str): The profile UID.

        Returns:
            bool: True if deletion was successful, False otherwise.
        """
        response = requests.delete(
            urljoin(self._url, f"profiles/{id}"),
            params={"delete_scenes": True},
            headers=self._headers,
        )
        response.raise_for_status()
        return response.json().get("result") == "OK"
