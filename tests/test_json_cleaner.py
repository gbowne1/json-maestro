import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../src")
from jsonmaestro import add_schema_keys, sort_json_keys


def test_add_schema_keys():
    input_data = {}
    result = add_schema_keys(input_data)
    assert "json.schemas" in result


def test_sort_json_keys():
    input_data = {"c": 3, "a": 1, "b": 2}
    result = sort_json_keys(input_data)
    assert list(result.keys()) == ["a", "b", "c"]

    result_reverse = sort_json_keys(input_data, reverse=True)
    assert list(result_reverse.keys()) == ["c", "b", "a"]
