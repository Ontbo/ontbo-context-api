from typing import List

import time
import json


class SceneMessage:
    """
    A single message in a chat conversation.

    Each message is associated with a role (either "user" or "assistant"),
    a content string, and a timestamp (in seconds since epoch).
    """

    def __init__(self, content: str, role: str = "user", timestamp: float = 0.0):
        """
        Initialize a SceneMessage.

        Args:
            content (str): The text content of the message.
            role (str): The role of the message sender. 
                        Typically "user" or "assistant".
            timestamp (float): The time the message was created (Unix epoch).
                               If 0.0 (default), the current time will be used.
        """
        self._content = content
        self._role = role
        self._timestamp = time.time() if timestamp == 0.0 else timestamp

    @property
    def content(self) -> str:
        """
        str: The text content of the message.
        """
        return self._content
    
    @property
    def role(self) -> str:
        """
        str: The role of the message sender (e.g., "user" or "assistant").
        """
        return self._role
    
    @property
    def timestamp(self) -> float:
        """
        float: The timestamp of the message (seconds since Unix epoch).
        """
        return self._timestamp
    
    @property
    def as_dict(self) -> dict:
        """
        dict: A dictionary representation of the message.

        Example:
            {
                "role": "user",
                "content": "Hello!",
                "timestamp": 1693249384.23
            }
        """
        return {
            "role": self.role,
            "content": self.content,
            "timestamp": self.timestamp
        }
    
    @staticmethod
    def from_string(input_str: str) -> List["SceneMessage"]:
        """
        Deserialize a JSON string into a list of SceneMessage objects.

        Args:
            input_str (str): JSON string representing a list of messages.
                             Each element should have "role", "content",
                             and "timestamp" fields.

        Returns:
            List[SceneMessage]: A list of deserialized messages.

        Example:
            input_str = '[{"role": "user", "content": "Hi", "timestamp": 1693249384.23}]'
            messages = SceneMessage.from_string(input_str)
        """
        data = json.loads(input_str)
        return [
            SceneMessage(
                content=message["content"],
                role=message["role"],
                timestamp=message["timestamp"]
            )
            for message in data
        ]
