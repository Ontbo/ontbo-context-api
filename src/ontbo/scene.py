from urllib.parse import urljoin
from typing import List

from ontbo.i_ontbo_server import IOntboServer
from ontbo.scene_message import SceneMessage

import json
import requests


class Scene:
    """
    A scene is a unit of interaction between the Profile (user) and the system.

    You can get an existing scene by calling the method:
        Ontbo(api_key).profile(profile_id).scene(id)

    Or, you can also create a new scene for a profile by calling the method:
        Ontbo(api_key).profile(profile_id).create_scene(id)
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
        Get the scene unique id.

        Returns:
            (str)The unique ID of the scene.
        """
        return self._id

    def add_messages(
        self,
        messages: List[SceneMessage],
        update_now: bool = False
    ) -> str:
        """
        Add messages to the scene.

        Args:
            messages (List[SceneMessage]): a list of SceneMessage objects to
            add to the scene.
            update_now (bool): If set to true, the profile update is initiated 
            now. If set to false, profile might be updated later with
            other calls to Scene.add_messages(), or with a call to 
            Profile.update()

        Returns:
            str: The ID of the newly added message batch.
        """
        text_data = json.dumps([message.as_dict for message in messages])

        response = requests.post(
            urljoin(self._server.url,
                    f"profiles/{self._profile_id}/scenes/{self._id}/text"),
            data=text_data,
            params={
                "update_now": update_now
            },
            headers=self._server.headers,
            )
        response.raise_for_status()
        return response.json()["id"]

    def clear_messages(self) -> None:
        """
        Clears all messages in the scene. 
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
        Returns:
            List[SCeneMessage]: the conversational data of the scene.
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
