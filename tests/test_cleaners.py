import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../src")

import pytest

from jsonmaestro import helpers, save_json
from jsonmaestro.loader import Loader


@pytest.mark.parametrize(
    "file_name",
    ["jsonc.json", "commented.json", "commented_with_duplicate.json"])
def test_remove_comments(file_name):
    loader = Loader(file_path=f"data/{file_name}")
    if helpers.is_json(f"data/{file_name}"):
        data = loader.load_as("json")
    else:
        data = loader.load_as("jsonc")

    save_json(data=data, file_path=f"data/{file_name}.cleaned.json")

    with open(f"data/{file_name}.cleaned.json", "r") as file:
        data = file.read()
        assert "//" not in data
        assert "/*" not in data
        assert "*/" not in data

    os.remove(f"data/{file_name}.cleaned.json")
