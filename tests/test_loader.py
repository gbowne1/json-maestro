import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../src")
import json
from jsonmaestro.loader import Loader
from jsonmaestro import remove_comments


def test_load_json():
    loader = Loader("data/json.json")

    with open("data/json.json", "r", encoding="utf-8") as file:
        content = file.read()

        assert json.loads(content) == loader.load_as("json")


def test_load_jsonc():
    loader = Loader("data/jsonc.json")

    with open("data/jsonc.json", "r", encoding="utf-8") as file:
        content = file.read()

        assert json.loads(remove_comments(content)) == loader.load_as("jsonc")


def test_load_csv():
    loader = Loader("data/example.csv")
    content = loader.load_as("csv")
    assert content == [
        {
            "name": "John",
            "age": "30",
            "text_editor": "Sublime Text"
        },
        {
            "name": "Jane",
            "age": "25",
            "text_editor": "Visual Studio Code"
        },
        {
            "name": "Michael",
            "age": "35",
            "text_editor": "Neovim"
        },
        {
            "name": "Noah",
            "age": "40",
            "text_editor": "Atom"
        },
    ]
