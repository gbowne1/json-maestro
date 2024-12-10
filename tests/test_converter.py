import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../src")
from jsonmaestro.converter import Converter


def test_convert_csv_to_json():
	converter = Converter(
	    file_path="data/example.csv",
	    source_format="csv",
	    target_format="json",
	)
	output = converter.convert()

	assert output == {
	    "John": {
	        "age": "30",
	        "text_editor": "Sublime Text"
	    },
	    "Jane": {
	        "age": "25",
	        "text_editor": "Visual Studio Code"
	    },
	    "Michael": {
	        "age": "35",
	        "text_editor": "Neovim"
	    },
	    "Noah": {
	        "age": "40",
	        "text_editor": "Atom"
	    }
	}


def test_convert_json_to_csv():
	converter = Converter(file_path="data/example.json",
	                      source_format="json",
	                      target_format="csv")

	is_covertable = converter.convertable()
	assert is_covertable is True

	output = converter.convert()

	assert output == [{
	    'key': 'John',
	    'age': '30',
	    'text_editor': 'Sublime Text'
	}, {
	    'key': 'Jane',
	    'age': '25',
	    'text_editor': 'Visual Studio Code'
	}, {
	    'key': 'Michael',
	    'age': '35',
	    'text_editor': 'Neovim'
	}, {
	    'key': 'Noah',
	    'age': '40',
	    'text_editor': 'Atom'
	}]

	converter = Converter(
	    file_path="data/example_invalid_for_csv_conversion.json",
	    source_format="json",
	    target_format="csv")

	is_covertable = converter.convertable()
	assert is_covertable is False


def test_convertable_csv_to_json():
	converter = Converter(file_path=None,
	                      str_data=None,
	                      data=None,
	                      source_format="csv",
	                      target_format="json")

	assert converter.convertable() is True


def test_convertable_json_to_csv():
	converter = Converter(file_path=None,
	                      str_data=None,
	                      data=None,
	                      source_format="json",
	                      target_format="csv")

	is_covertable = converter.convertable()
	assert is_covertable is False


def test_is_json_covertible_valid():
	converter = Converter(file_path="data/example.json",
	                      source_format="json",
	                      target_format="csv")

	is_covertable = converter.convertable()
	assert is_covertable is True


def test_is_json_covertible_invalid():
	converter = Converter(
	    file_path="data/example_invalid_for_csv_conversion.json",
	    source_format="json",
	    target_format="csv")
	is_covertable = converter.convertable()
	assert is_covertable is False
