from enum import Enum


class QueryType(Enum):
    """
    QueryTypes are used as a parameter query methods to select the algorithm 
    to use to retrieve the relevant information in the user profile.
    """

    FULL_DATA = "FULL_DATA"
    """
    With FULL_DATA query, the algorithm makes a review of ALL items present in 
    the user profile. This method yields the best performance in terms of 
    recall rate, but with a higher token cost. 
    """

    MULTI_HOP = "MULTI_HOP"
    """
    When the query type is set to MULTI_HOP, the agent autonomously tries 
    different strategies and queries to find the relevant information in the 
    profile. This method is fit when the information to find about the user
    is not obvous to find, with a high latency as a counterpart.
    """

    SINGLE_HOP = "SINGLE_HOP"
    """
    Uses a low-latency vector search to find relvant information about the
    profile, then formats the search result using a LLM. Offers good recall
    rate and low latency.
    """

    VECTOR_SEARCH = "VECTOR_SEARCH"
    """
    Directly returns the result of a vector (embeddings) search in the user
    profile database. The best-matching results of the vector quezry are
    returned, but some irrelvant results might also be returned, requiring
    a post-processing by the host application.
    Offers very low letency results.
    """
