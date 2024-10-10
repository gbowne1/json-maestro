import pytest
from unittest import mock

from jsonmaestro import load_jsonc, load_json


@pytest.mark.parametrize("file_name", ["jsonc.json", "json.json"])
def test_load_jsonc(file_name):
	# we are mocking sys.exit to check if it has been called
	with mock.patch("sys.exit") as mock_exit:
		result = load_jsonc(f"data/{file_name}")
		if file_name == "jsonc.json":
			assert result == {"key1": "value1", "key2": 42, "key3": True}
			mock_exit.assert_not_called()
		elif file_name == "json.json":
			assert result == {
			    "editor.fontSize": 14,
			    "files.autoSave": "onFocusChange"
			}
			mock_exit.assert_not_called()


@pytest.mark.parametrize("file_name", ["jsonc.json", "json.json"])
def test_load_json(file_name):
	# we are mocking sys.exit to check if it has been called
	with mock.patch("sys.exit") as mock_exit:
		result = load_json(f"data/{file_name}")
		if file_name == "jsonc.json":
			mock_exit.assert_called_once_with(1)
		elif file_name == "json.json":
			assert result == {
			    "editor.fontSize": 14,
			    "files.autoSave": "onFocusChange"
			}
			mock_exit.assert_not_called()
