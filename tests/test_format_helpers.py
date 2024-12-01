import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../src")

import pytest
from unittest.mock import mock_open
from jsonmaestro.helpers import is_json, get_format

# Mock Data
valid_json_content = '{"name": "John", "age": 30}'  # Valid JSON content
invalid_json_content = '{"name": "John", "age": 30'  # Invalid JSON (missing closing bracket)
jsonc_content = '''// Comment
{
    "name": "John",
    "age": 30
	// this is comment inside of the data
}'''  # JSONC (JSON with comments, not valid JSON for is_json)


# Test for `is_json`
@pytest.mark.parametrize(
    "file_content, expected_result",
    [
        (valid_json_content, True),  # Valid JSON should return True
        (invalid_json_content, False),  # Invalid JSON should return False
        (jsonc_content, False),  # JSONC content should also return False
    ])
def test_is_json(mocker, file_content, expected_result):
	# Mock opening a file and returning the file_content
	mocker.patch("builtins.open", mock_open(read_data=file_content))

	# Call is_json function with a mock file path
	assert is_json("mock_file.json") == expected_result


# Test for `get_format`
@pytest.mark.parametrize(
    "file_content, expected_format",
    [
        (valid_json_content, "json"),  # Valid JSON should return "json"
        (invalid_json_content,
         "jsonc"),  # Invalid JSON should default to "jsonc"
        (jsonc_content, "jsonc"),  # JSONC content should return "jsonc"
    ])
def test_get_format(mocker, file_content, expected_format):
	# Mock opening a file and returning the file_content
	mocker.patch("builtins.open", mock_open(read_data=file_content))

	# Call get_format function with a mock file path
	assert get_format("mock_file.json") == expected_format
