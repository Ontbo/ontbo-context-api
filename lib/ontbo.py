from urllib.parse import urljoin
from typing import List

from lib.i_ontbo_server import IOntboServer
from lib.profile import Profile

import requests


class Ontbo(IOntboServer):
    """
    Main client class for interacting with the Ontbo server.

    This class manages profiles on the server and provides authentication
    via a bearer token.
    """

    def __init__(self, token: str, base_url: str = "https://api.ontbo.com/api/tests/"):
        """
        Initialize the Ontbo client.

        Args:
            token (str): API authentication token.
            base_url (str): Base URL of the Ontbo API.
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
        Create a Profile object for an existing profile on the server.

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
            requested_id (str): The desired ID for the new profile.
                                (Uniqueness is enforced server-side.)

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
        Delete a profile from lib.the server (along with its scenes).

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
