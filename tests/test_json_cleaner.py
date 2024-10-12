import pytest
import json
import os
import tempfile
from pathlib import Path
from jsonmaestro import load_jsonc, load_json, remove_comments, add_schema_keys, sort_json_keys


def create_temp_json(tmp_path, content):
	file_path = tmp_path / "test_file.json"
	try:
		with open(file_path, 'w', encoding='utf-8') as f:
			json.dump(content, f)
		return file_path
	except IOError as e:
		raise AssertionError(f"Failed to create temporary file: {e}")


def test_add_schema_keys():
	input_data = {}
	result = add_schema_keys(input_data)
	assert "json.schemas" in result
	assert isinstance(result["json.schemas"], list)
	assert len(result["json.schemas"]) > 0


def test_sort_json_keys():
	input_data = {"c": 3, "a": 1, "b": 2}
	result = sort_json_keys(input_data)
	assert list(result.keys()) == ["a", "b", "c"]

	result_reverse = sort_json_keys(input_data, reverse=True)
	assert list(result_reverse.keys()) == ["c", "b", "a"]


@pytest.fixture(scope='function')
def cleanup_temp_files(tmp_path_factory):
	yield
	for file in tmp_path_factory.mktemp("cleanup").iterdir():
		os.remove(file)


def test_cleanup_temp_files(cleanup_temp_files):
	content = '''
    {
        "test_key": "test_value"
    }
    '''
	file_path = create_temp_json(tmp_path_factory.mktemp("test_dir"), content)
	assert file_path.exists()
	cleanup_temp_files
	assert not file_path.exists()


def test_create_multiple_files(tmp_path_factory):
	content1 = '{"key1": "value1"}'
	content2 = '{"key2": "value2"}'

	file1 = create_temp_json(tmp_path_factory.mktemp("test_dir_1"), content1)
	file2 = create_temp_json(tmp_path_factory.mktemp("test_dir_2"), content2)

	assert file1.exists()
	assert file2.exists()
	assert file1 != file2

	cleanup_temp_files()
	assert not file1.exists()
	assert not file2.exists()


def test_parse_json_content(tmp_path):
	content = '''
    {
        "key1": "value1",
        "key2": 42
    }
    '''
	file_path = create_temp_json(tmp_path, content)
	with open(file_path, 'r') as f:
		parsed_content = json.load(f)
	assert parsed_content == {"key1": "value1", "key2": 42}


def test_tempfile_usage():
	with tempfile.TemporaryDirectory() as temp_dir:
		file_path = Path(temp_dir) / "test_file.txt"
		with file_path.open(mode="w") as f:
			f.write("Hello, pytest!")

		assert file_path.exists()
		assert file_path.read_text() == "Hello, pytest!"

		# Cleanup happens automatically when exiting the context manager
