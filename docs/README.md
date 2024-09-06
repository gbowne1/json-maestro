# JSONMaestro

This script takes a JSON, JSONC, or VSCode settings.json file as input, cleans it, and saves the cleaned data to a new file.

**Features:**

* Loads JSON, JSONC, and VSCode settings.json formats.
* Removes duplicate keys.
* Optionally removes comments.
* Optionally sorts keys alphabetically (ascending or descending).

### Usage

The script will prompt you for the path to the input file and ask if you want to remove comments and sort keys.

### Functions

#### `load_jsonc(file_path: str) -> Dict[str, Any]:`

* Loads JSONC data from a file, skipping comments starting with `//` and handling control characters.
* Raises `FileNotFoundError` if the file is not found.
* Raises `json.JSONDecodeError` if the JSON format is invalid.
* Raises `ValueError` for unexpected content in the file.

#### `load_vscode_settings(file_path: str) -> Dict[str, Any]:`

* Loads data from a VSCode settings.json file.
* Raises the same exceptions as `load_jsonc`.

#### `remove_comments(obj: Union[Dict[str, Any], List[Any], Any]) -> Union[Dict[str, Any], List[Any], Any]:`

* Recursively removes comments from a dictionary or list.
* Preserves other data types.

#### `remove_duplicate_keys(obj: Union[Dict[str, Any], List[Any], Any]) -> Union[Dict[str, Any], List[Any], Any]:`

* Recursively removes duplicate keys from a nested object.

#### `add_schema_keys(obj: T) -> T:`

* Adds schema-related keys to the object (if applicable).

#### `sort_json_keys(obj: T, reverse: bool = False) -> T:`

* Sorts dictionary keys recursively in ascending or descending order.

#### `save_json(data: Union[dict, list, str, int, float, bool], file_path: str):`

* Saves JSON data to a file.
* Raises `ValueError` for invalid JSON data.
* Raises `IOError` for issues writing to the file.

#### `main()`

* The main entry point of the script.
* Prompts the user for input and output file paths.
* Loads the data using the appropriate function.
* Processes the data by removing duplicates, adding schema keys (if applicable), optionally removing comments, and optionally sorting keys.
* Saves the cleaned data to a new file.