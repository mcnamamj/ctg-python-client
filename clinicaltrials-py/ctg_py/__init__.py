"""A client library for accessing ClinicalTrials.gov REST API"""

from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
)
