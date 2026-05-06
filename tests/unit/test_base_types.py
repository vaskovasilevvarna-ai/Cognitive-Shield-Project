"""Unit tests for shared base type aliases."""

from typing import get_args, get_origin

from cognitive_shield.shared.types.base_types import JsonDict, StringList


def test_json_dict_alias_points_to_dict() -> None:
    """JsonDict is a dict alias with string keys."""
    assert get_origin(JsonDict) is dict
    assert get_args(JsonDict)[0] is str


def test_string_list_alias_points_to_list_of_strings() -> None:
    """StringList is a list alias with string items."""
    assert get_origin(StringList) is list
    assert get_args(StringList)[0] is str
