import json
import csv

from typing import Any, Dict, List, Union

from jsonmaestro import remove_comments


class LoaderFormatError(Exception):
	pass


class LoaderValueError(Exception):
	pass


class Loader():
	"""
	A Loader class for loading loading files in various formats.
	"""

	def __init__(self, file_path: str):
		self.file_path = file_path

	def load_as(
	    self, format: str
	) -> Union[Dict[str, Any], List[Dict[Union[str, Any], Union[str, Any]]]]:
		"""
		Load a file in a specific format.

		Args:
		format: The format of the file to load. Can be either "jsonc" or "json".

		Returns:
		The loaded file as a dictionary.

		Raises:
		LoaderFormatError: If the file format is not supported.
		LoaderValueError: If the file is not a valid JSON or JSONC file.
		"""

		with open(self.file_path, 'r', encoding='utf-8') as file:
			content = file.read()

			if format == "jsonc":
				content = remove_comments(content)

			if format == "jsonc" or format == "json":
				try:
					return json.loads(content)
				except json.JSONDecodeError:
					raise LoaderFormatError()
				except ValueError:
					raise LoaderValueError()

			if format == "csv":
				csvFile = csv.DictReader(file)

				rcontent: List[Dict[Union[str, Any], Union[str, Any]]] = []

				for row in csvFile:
					rcontent.append(row)

				return rcontent

			else:
				raise LoaderFormatError(f"Unsupported format: {format}")
