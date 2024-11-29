from io import TextIOWrapper
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

	def _open_file(self) -> TextIOWrapper:
		"""
		Open the file.
		"""
		return open(self.file_path, 'r', encoding='utf-8')

	def _read_to_string(self) -> str:
		"""
		Read the file to a string.
		"""
		with open(self.file_path, 'r', encoding='utf-8') as file:
			return file.read()

	def _load_json(self, type: str) -> str:
		"""
		Load the file as JSON or JSONC.

		Args:
		type: The type of file to load. Can be either "jsonc" or "json".
		"""
		content = self._read_to_string()

		if type == "jsonc":
			content = remove_comments(content)

		return content

	def _load_csv(self) -> List[Dict[Union[str, Any], Union[str, Any]]]:
		"""
		Load the file as CSV.
		"""
		_file = self._open_file()
		csv_file = csv.DictReader(_file)

		content: List[Dict[Union[str, Any], Union[str, Any]]] = []

		for row in csv_file:
			content.append(row)

		_file.close()
		return content

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

		if format == "jsonc" or format == "json":
			try:
				return json.loads(self._load_json(format))
			except json.JSONDecodeError:
				raise LoaderFormatError()
			except ValueError:
				raise LoaderValueError()

		if format == "csv":
			return self._load_csv()

		else:
			raise LoaderFormatError(f"Unsupported format: {format}")