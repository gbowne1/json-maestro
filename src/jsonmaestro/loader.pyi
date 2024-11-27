from typing import Any, Dict, List, Union


class LoaderFormatError(Exception):
	pass


class LoaderValueError(Exception):
	pass


class Loader():

	def __init__(self, file_path: str) -> None:
		...

	def load_as(
	    self, format: str
	) -> Union[Dict[str, Any], List[Dict[Union[str, Any], Union[str, Any]]]]:
		...
