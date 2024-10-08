import json
import sys
import re
from typing import Union, List, Dict, Any, cast, TypeVar, Set

T = TypeVar('T', bound=Union[Dict[str, Any], List[Any], Any])

def load_jsonc(file_path: str) -> Dict[str, Any]:
	"""Load JSONC from a file, skipping comments starting with // and handling control characters."""
	try:
		with open(file_path, 'r', encoding='utf-8') as file:
			content = file.read()

			# Remove comments starting with //
			content = re.sub(r'//.*\n', '', content)

			# Handle control characters
			content = re.sub(r'[^\x20-\x7E]', '', content)

			# Parse the remaining content as JSON
			return json.loads(content)

	except json.JSONDecodeError as e:
		print(f"Error: Invalid JSON format in the file. Error details: {str(e)}")
		print("Please check the contents of the file.")
		sys.exit(1)
	except ValueError as e:
		print(f"Error: Unexpected content in the file. Error details: {str(e)}")
		print("Please check the contents of the file.")
		sys.exit(1)

def load_json(file_path: str)-> Dict[str, Any]:
	"""Load json format compliant file."""
	try:
		with open(file_path, 'r', encoding='utf-8') as file:
			content = file.read()
			return json.loads(content)
	except json.JSONDecodeError as e:
		print(f"Error: Invalid JSON format in the file. Error details: {str(e)}")
		print("Please check the contents of the file.")
		sys.exit(1)
	except ValueError as e:
		print(f"Error: Unexpected content in the file. Error details: {str(e)}")
		print("Please check the contents of the file.")
		sys.exit(1)

def remove_comments(obj: Union[Dict[str, Any], List[Any], Any]) -> Union[Dict[str, Any], List[Any], Any]:
	"""Remove comments from the object."""
	if isinstance(obj, dict):
		return {k: remove_comments(v) for k, v in obj.items()}
	elif isinstance(obj, list):
		return [remove_comments(item) for item in obj]
	else:
		return obj

def remove_duplicate_keys(obj: Union[Dict[str, Any], List[Any], Any]) -> Union[Dict[str, Any], List[Any], Any]:
	"""
	Recursively remove duplicate keys from a nested object.

	Args:
	obj: A dictionary, list, or any other object to process.

	Returns:
	A dictionary, list, or any other object with duplicate keys removed.
	"""
	if isinstance(obj, dict):
		new_obj: Dict[str, Any] = {}
		seen_keys: Set[str] = set()
		for key, value in obj.items():
			if key not in seen_keys:
				seen_keys.add(key)
				new_obj[key] = remove_duplicate_keys(value)
		return new_obj
	elif isinstance(obj, list):
		return [remove_duplicate_keys(item) for item in obj]
	else:
		return obj

def add_schema_keys(obj: T) -> T:
	"""
	Add schema-related keys to the object.

	Args:
	obj: An object (dictionary, list, or any other type) to process.

	Returns:
	The processed object with schema-related keys added.
	"""
	if isinstance(obj, dict):
		obj_dict: Dict[str, Any] = obj
		if "json.schemas" not in obj_dict:
			obj_dict["json.schemas"] = []
		for key, value in obj_dict.items():
			if isinstance(value, list) and key.startswith("json.schemas"):
				schema_list: List[Dict[str, Any]] = value
				for schema_item in schema_list:
						schema_item.setdefault("fileMatch", [])
						schema_item.setdefault("url", "")
	elif isinstance(obj, list):
		obj_list: List[Any] = obj
		for item in obj_list:
			add_schema_keys(item)
	return obj

def sort_json_keys(obj: T, reverse: bool = False) -> T:
	"""
	Sort dictionary keys recursively.

	Args:
	obj: An object (dictionary, list, or any other type) to process.
	reverse: Whether to sort in descending order (default is ascending).

	Returns:
	The processed object with sorted keys.
	"""
	if isinstance(obj, dict):
		sorted_dict = {k: sort_json_keys(v, reverse) for k, v in sorted(obj.items(), key=lambda x: x[0], reverse=reverse)}
		return cast(T, sorted_dict)
	elif isinstance(obj, list):
		sorted_list = [sort_json_keys(item, reverse) for item in obj]
		return cast(T, sorted_list)
	else:
		return obj

def save_json(data: Union[Dict[str, Any], List[Any], str, int, float, bool], file_path: str) -> None:
	"""
	Save JSON data to a file.

	Args:
	data: The JSON data to be saved. Can be a dictionary, list, string, integer, float, or boolean.
	file_path: The path to the file where the JSON data will be saved.

	Raises:
	ValueError: If the input data is not a valid JSON serializable object.
	IOError: If there's an issue writing to the file.
	"""
	try:
		with open(file_path, 'w', encoding='utf-8') as file:
			json.dump(data, file, indent=2)
	except IOError as e:
		print(f"Error: Unable to write to file '{file_path}'. Error: {str(e)}")
		sys.exit(1)
	except TypeError as e:
		raise ValueError(f"Invalid JSON data: {str(e)}")
