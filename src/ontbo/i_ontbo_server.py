class IOntboServer:
    """
    Interface-like base class for an Ontbo server connection.

    This class defines the basic structure for storing server
    connection details such as the server URL and request headers.
    """

    def __init__(self):
        """
        Initialize the server connection with default values.

        Attributes:
            _url (str | None): The base URL of the server.
            _headers (dict | None): HTTP headers used for requests.
        """
        self._url = None
        self._headers = None

    @property
    def url(self):
        """
        str | None: The base URL of the Ontbo server.
        """
        return self._url
    
    @property
    def headers(self):
        """
        dict | None: The HTTP headers used for server requests.
        """
        return self._headers
