"""
This module provides sample functions for using pytest-mock.
"""

import requests


def connect_to_server(url):
    """
    This function calls 'connect()' function.
    """
    return connect(url)


def connect(url):
    """
    Attempts to connect to the url and returns a status code.
    """
    try:
        response = requests.get(url)
        return response.status_code
    except Exception:
        return 0


class ConnectServerClass:
    """
    Sample class of 'ConnectServer'.
    """

    def __init__(self):
        """
        Initialization.(Like Constructor.)
        """
        self._req = requests

    def get(self, url):
        """
        Connect to host with url.
        """
        try:
            response = self._req.get(url)
            return response.status_code
        except Exception:
            return 0
