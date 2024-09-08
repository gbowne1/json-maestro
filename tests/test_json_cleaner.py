import pytest
import json
import os
import tempfile
from jsonmaestro import load_jsonc, load_vscode_settings, remove_comments, remove_duplicate_keys, add_schema_keys, sort_json_keys

# Helper function to create temporary JSON files for testing
def create_temp_json(tmp_path, content):
    file_path = tmp_path / "test_file.json"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return str(file_path)

def test_load_jsonc(tmp_path):
    content = '''
    {
        // This is a comment
        "key1": "value1",
        "key2": 42
    }
    '''
    file_path = create_temp_json(tmp_path, content)
    result = load_jsonc(file_path)
    assert result == {"key1": "value1", "key2": 42}

def test_load_vscode_settings(tmp_path):
    content = '''
    {
        // VSCode setting
        "editor.fontSize": 14,
        "files.autoSave": "onFocusChange"
    }
    '''
    file_path = create_temp_json(tmp_path, content)
    result = load_vscode_settings(file_path)
    assert result == {"editor.fontSize": 14, "files.autoSave": "onFocusChange"}

def test_remove_comments():
    input_data = {
        "key1": "value1",
        "key2": [1, 2, 3],
        "key3": {"nested": "value"}
    }
    result = remove_comments(input_data)
    assert result == input_data  # No comments to remove, should be identical

def test_remove_duplicate_keys():
    input_data = {
        "key1": "value1",
        "key2": "value2",
        "key1": "value3"  # Duplicate key
    }
    result = remove_duplicate_keys(input_data)
    assert result == {"key1": "value3", "key2": "value2"}

def test_add_schema_keys():
    input_data = {
        "someKey": "someValue"
    }
    result = add_schema_keys(input_data)
    assert "json.schemas" in result
    assert isinstance(result["json.schemas"], list)

def test_sort_json_keys():
    input_data = {
        "c": 3,
        "a": 1,
        "b": 2
    }
    result = sort_json_keys(input_data)
    assert list(result.keys()) == ["a", "b", "c"]

    result_reverse = sort_json_keys(input_data, reverse=True)
    assert list(result_reverse.keys()) == ["c", "b", "a"]