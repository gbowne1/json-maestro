import json
from typing import Union, List, Dict, Any, cast, TypeVar

try:
	from .logger import fatal
except ImportError:  # for debugging
	from logger import fatal

T = TypeVar('T', bound=Union[Dict[str, Any], List[Any], Any])


def remove_comments(jsonc_content: str) -> str:
	"""
		Removes the comments from source
	"""
	inside_string = False
	inside_block_comment = False
	inside_line_comment = False
	result: List[str] = []
	i = 0
	length = len(jsonc_content)

	while i < length:
		char = jsonc_content[i]
		next_char = jsonc_content[i + 1] if i + 1 < length else ''

		# Toggle the string state if encountering a double quote (and not escaping it)
		if char == '"' and not inside_block_comment and not inside_line_comment:
			if i == 0 or jsonc_content[i - 1] != '\\':
				inside_string = not inside_string

		# Start of block comment (/*)
		if not inside_string and not inside_block_comment and not inside_line_comment and char == '/' and next_char == '*':
			inside_block_comment = True
			i += 2  # Skip the /* characters
			continue

		# End of block comment (*/)
		if inside_block_comment and char == '*' and next_char == '/':
			inside_block_comment = False
			i += 2  # Skip the */ characters
			continue

		# Start of line comment (//)
		if not inside_string and not inside_block_comment and not inside_line_comment and char == '/' and next_char == '/':
			inside_line_comment = True
			i += 2  # Skip the // characters
			continue

		# End of line comment (at newline)
		if inside_line_comment and char == '\n':
			inside_line_comment = False
			result.append(char)  # Keep the newline
			i += 1
			continue

		# If not inside a comment, append the character to the result
		if not inside_block_comment and not inside_line_comment:
			result.append(char)

		i += 1

	return ''.join(result)


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
		sorted_dict = {
		    k: sort_json_keys(v, reverse)
		    for k, v in sorted(
		        obj.items(), key=lambda x: x[0], reverse=reverse)
		}
		return cast(T, sorted_dict)
	elif isinstance(obj, list):
		sorted_list = [sort_json_keys(item, reverse) for item in obj]
		return cast(T, sorted_list)
	else:
		return obj


def save_json(data: Union[Dict[str, Any], List[Any], str, int, float, bool],
              file_path: str) -> None:
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
		fatal(f"Error: Unable to write to file '{file_path}'. Error: {str(e)}")
	except TypeError as e:
		raise ValueError(f"Invalid JSON data: {str(e)}")
