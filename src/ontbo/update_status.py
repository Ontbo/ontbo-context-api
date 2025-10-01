class UpdateStatus:
    """
    Represents the status of an update process.

    This class is initialized from a JSON-like dictionary and provides
    convenient property access to the update status and its progress.
    """

    def __init__(self, json_dict: dict):
        """
        Initialize an UpdateStatus instance.

        Args:
            json_dict (dict): A dictionary containing update status data.
                Expected keys:
                    - "status" (str): The current status of the update.
        """
        self._dict = json_dict

    @property
    def pending(self) -> str:
        """
        str: the number of pending scenes to process in queue.
        """
        return self._dict["pending"]
