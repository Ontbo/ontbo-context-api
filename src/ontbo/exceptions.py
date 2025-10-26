class ProfileNotFoundError(LookupError):
    def __init__(self, profile_id, details=None):
        self._profile_id = profile_id
        self._details = details

    def __str__(self):
        details_str = f"({self._details})" if self._details is not None else ""
        return f"Profile {self._profile_id} not found {details_str}."


