from urllib.parse import urljoin
from typing import List

from ontbo.i_ontbo_server import IOntboServer
from ontbo.scene_message import SceneMessage

import json
import requests


class Scene:
    """
    A scene is a unit of interaction between the Profile (user) and the system.

    Scenes can be created by calling:
        Ontbo.profile(profile_id).scene(id)
    """

    def __init__(self, server: IOntboServer, profile_id: str, id: str):
        """
        Initialize a Scene instance.

        Args:
            server (IOntboServer): The Ontbo server connection.
            profile_id (str): The ID of the profile associated with this scene.
            id (str): The unique ID of the scene.
        """
        self._server = server
        self._profile_id = profile_id
        self._id = id

    @property
    def id(self) -> str:
        """
        str: The unique ID of the scene.
        """
        return self._id

    def add_messages(
        self,
        messages: List[SceneMessage],
        update_now: bool = False,
        wait_for_result: bool = True
    ) -> str:
        """
        Add messages to the scene.

        Args:
            messages (List[SceneMessage]): The messages to add.
            update_now (bool): Whether to trigger an immediate update after adding messages.
            wait_for_result (bool): Whether to wait for processing to complete.

        Returns:
            str: The ID of the newly added message batch.
        """
        text_data = json.dumps([message.as_dict for message in messages])

        response = requests.post(
            urljoin(self._server.url,
                    f"profiles/{self._profile_id}/scenes/{self._id}/text"),
            data=text_data,
            params={
                "update_now": update_now,
                "wait_for_result": wait_for_result
            },
            headers=self._server.headers,
        )
        response.raise_for_status()
        return response.json()["id"]

    def clear_messages(self) -> None:
        """
        Delete all messages from lib.the scene.
        """
        response = requests.delete(
            urljoin(self._server.url,
                    f"profiles/{self._profile_id}/scenes/{self._id}/text"),
            headers=self._server.headers,
        )
        response.raise_for_status()

    @property
    def messages(self) -> List[SceneMessage]:
        """
        List[SceneMessage]: The list of messages in the scene.
        """
        response = requests.get(
            urljoin(self._server.url,
                    f"profiles/{self._profile_id}/scenes/{self._id}/text"),
            headers=self._server.headers,
        )
        response.raise_for_status()
        messages = response.json()

        return [
            SceneMessage(
                content=message["content"],
                role=message["role"],
                timestamp=message["timestamp"],
            )
            for message in messages
        ]
