from jsonmaestro import remove_duplicate_keys, add_schema_keys, sort_json_keys


def test_remove_duplicate_keys():
	input_data = {
	    "key1": "value1",
	    "key2": "value2",
	    "key1": "value3"  # Duplicate key
	}
	result = remove_duplicate_keys(input_data)
	expected_result = {"key1": "value3", "key2": "value2"}
	assert result == expected_result


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
