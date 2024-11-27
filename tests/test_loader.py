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
