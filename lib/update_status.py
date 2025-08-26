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
                    - "progress" (int | float): The progress value, typically
                      a percentage (0-100).
        """
        self._dict = json_dict

    @property
    def status(self) -> str:
        """
        str: The current status of the update (e.g., 'IDLE', 'WORKING').
        """
        return self._dict["status"]

    @property
    def progress(self) -> int | float:
        """
        int | float: The progress of the update, usually represented as a percentage.
        """
        return self._dict["progress"]
