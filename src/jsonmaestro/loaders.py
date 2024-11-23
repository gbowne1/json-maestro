import json
from typing import Any, Dict

from jsonmaestro.logger import fatal

from jsonmaestro import remove_comments


def load_jsonc(file_path: str) -> Dict[str, Any]:
	"""Load JSONC from a file, skipping comments starting with // and handling control characters."""
	try:
		with open(file_path, 'r', encoding='utf-8') as file:
			content = file.read()

			cleaned_content = remove_comments(content)

			# Parse the remaining content as JSON
			return json.loads(cleaned_content)

	except json.JSONDecodeError as e:
		fatal(
		    f"Error: Invalid JSON format in the file. Error details: {str(e)}\n"
		    + "Please check the contents of the file.")
	except ValueError as e:
		fatal(
		    f"Error: Unexpected content in the file. Error details: {str(e)}\n"
		    + "Please check the contents of the file.")


def load_json(file_path: str) -> Dict[str, Any]:
	"""Load json format compliant file."""
	try:
		with open(file_path, 'r', encoding='utf-8') as file:
			content = file.read()
			return json.loads(content)
	except json.JSONDecodeError as e:
		fatal(
		    f"Error: Invalid JSON format in the file. Error details: {str(e)}\n"
		    + "Please check the contents of the file.")
	except ValueError as e:
		fatal(
		    f"Error: Unexpected content in the file. Error details: {str(e)}\n"
		    + "Please check the contents of the file.")
