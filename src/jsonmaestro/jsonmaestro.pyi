from typing import Any, Dict, List, TypeVar, Union

T = TypeVar('T', bound=Union[Dict[str, Any], List[Any], Any])


def load_jsonc(file_path: str) -> Dict[str, Any]:
	...


def load_json(file_path: str) -> Dict[str, Any]:
	...


def remove_comments(jsonc_content: str) -> str:
	...


def add_schema_keys(obj: T) -> T:
	...


def sort_json_keys(obj: T, reverse: bool = False) -> T:
	...


def save_json(data: Union[Dict[str, Any], List[Any], str, int, float, bool],
              file_path: str) -> None:
	...
