"""
This test module tests the 'interaction' module,using pytest-mock.
"""

import requests
from exercise_python.interaction import connect_to_server, connect
from exercise_python.interaction import ConnectServerClass


def test_connect_to_server_200(mocker):
    """
    Cause the 'connect' function to return status code '200'.
    """
    status_code = 200
    url = "http://127.0.0.1"
    mocker.patch("exercise_python.interaction.connect", return_value=status_code)

    assert connect_to_server(url) == status_code


def test_connect_to_server_404(mocker):
    """
    Cause the 'connect' function to return status code '404'.
    """
    status_code = 404
    url = "http://137.0.0.1"
    mocker.patch("exercise_python.interaction.connect", return_value=status_code)

    assert connect_to_server(url) == status_code


def test_connect_to_server_variable(mocker):
    """
    Dynamically change the return value of a function.
    """

    def return_status_code(url):
        """
        A function that returns eigher 200, 404, 0 depending on the url.
        """
        if url == "http://127.0.0.1":
            return 200
        elif url == "http://137.0.0.1":
            return 404
        else:
            return 0

    mocker.patch("exercise_python.interaction.connect", side_effect=return_status_code)
    assert connect_to_server("http://127.0.0.1") == 200
    assert connect_to_server("http://137.0.0.1") == 404
    assert connect_to_server("htt://127.0.0.1") == 0


def test_connect_exception(mocker):
    """
    Raise an Exception when 'requests.get' is called in the 'connect()' function.
    """
    status_code = 0
    url = "http://127.0.0.1"
    mocker.patch.object(requests, "get", side_effect=Exception)
    assert connect(url) == status_code


class TestConnectServerClass:
    """
    Specfies the return of a function called within a 'ConnectServerClass'.
    """

    def test_get_200(self, mocker):
        """
        Replace '_req.get()' called by get mothod of 'ConnectServerClass'.
        """
        status_code = 200
        url = "http://127.0.0.1"
        connect_server = ConnectServerClass()
        response_mock = mocker.Mock()
        response_mock.status_code = status_code
        req_mock = mocker.MagicMock()
        req_mock.get = mocker.Mock(return_value=response_mock)
        mocker.patch.object(connect_server, "_req", req_mock)
        assert connect_server.get(url) == status_code

    def test_get_exception(self, mocker):
        """
        Raise an Exception when '_req.get' is called by the get method of 'ConnectServerClass'.
        """
        status_code = 0
        url = "http://127.0.0.1"
        connect_server = ConnectServerClass()
        req_mock = mocker.MagicMock()
        req_mock.get = mocker.Mock(side_effect=Exception)
        mocker.patch.object(connect_server, "_req", req_mock)
        assert connect_server.get(url) == status_code
