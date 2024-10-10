import os
import pytest

from jsonmaestro import helpers, load_json, load_jsonc, save_json


@pytest.mark.parametrize(
    "file_name",
    ["jsonc.json", "commented.json", "commented_with_duplicate.json"])
def test_remove_comments(file_name):
	if helpers.is_json(f"data/{file_name}"):
		loader = load_json
	else:
		loader = load_jsonc

	data = loader(f"data/{file_name}")
	save_json(data=data, file_path=f"data/{file_name}.cleaned.json")

	with open(f"data/{file_name}.cleaned.json", "r") as file:
		data = file.read()
		assert "//" not in data
		assert "/*" not in data
		assert "*/" not in data

	os.remove(f"data/{file_name}.cleaned.json")
