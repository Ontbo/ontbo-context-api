from enum import Enum


class QueryType(Enum):
    """
    Enumeration of query types used for different retrieval and reasoning strategies.
    """

    FULL_DATA = "FULL_DATA"
    """Retrieve and process the entire dataset without filtering."""

    MULTI_HOP = "MULTI_HOP"
    """Perform reasoning across multiple documents or facts, combining information step by step."""

    SINGLE_HOP = "SINGLE_HOP"
    """Answer a query using a direct lookup or reasoning from a single document or fact."""

    VECTOR_SEARCH = "VECTOR_SEARCH"
    """Retrieve relevant documents based on semantic similarity using vector embeddings."""
