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
