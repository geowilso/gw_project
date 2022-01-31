from gw_project.lib import curent_time


def test_string():
    assert type(curent_time()) == str
