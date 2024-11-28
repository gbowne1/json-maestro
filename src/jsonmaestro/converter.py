from typing import Any, Dict, List, Union

from jsonmaestro.logger import fatal

from jsonmaestro.loader import Loader, LoaderFormatError, LoaderValueError

_ALLOWED_FORMATS = ["jsonc", "json", "csv"]

# Table of allowed conversions
# in fromat {source format: target format}
_ALLOWED_CONVERTIONS = {"csv": "json"}


class ConverterUnknownError(Exception):
	pass


class ConverterFormatError(Exception):
	pass


class ConverterNoSourceDataError(Exception):
	pass


class ConverterIncorrectSourceDataError(Exception):
	pass


class ConverterIvalidConversionError(Exception):
	pass


class Converter:
	"""
	A Converter class for converting between different formats.
	"""

	file_path: Union[str, None]
	str_data: Union[str, None]
	data: Union[None, Union[Dict[str, Any], List[Dict[Union[str, Any],
	                                                  Union[str, Any]]]]]

	source_format: str
	target_format: str

	def __init__(
	    self,
	    source_format: str,
	    target_format: str,
	    file_path: Union[str, None] = None,
	    str_data: Union[str, None] = None,
	    data: Union[None, Union[Dict[str, Any],
	                            List[Dict[Union[str, Any],
	                                      Union[str, Any]]]]] = None,
	):
		if file_path is not None:
			self.file_path = file_path
		else:
			self.file_path = None

		if str_data is not None:
			self.str_data = str_data
		else:
			self.str_data = None

		if data is not None:
			self.data = data
		else:
			self.data = None

		if source_format not in _ALLOWED_FORMATS:
			raise ConverterFormatError(
			    f"Source format {source_format} is not supported. Use one of {_ALLOWED_FORMATS}"
			)

		self.source_format = source_format

		if target_format not in _ALLOWED_FORMATS:
			raise ConverterFormatError(
			    f"Target format {target_format} is not supported. Use one of {_ALLOWED_FORMATS}"
			)

		self.target_format = target_format

	def convert(self) -> Union[None, Dict[str, Any], List[Dict[str, Any]]]:
		"""
		Converts the data from the source format to the target format.
		"""
		if self.source_format not in _ALLOWED_CONVERTIONS or _ALLOWED_CONVERTIONS[
		    self.source_format] != self.target_format:
			raise ConverterIvalidConversionError(
			    f"Conversion from {self.source_format} to {self.target_format} is not supported"
			)

		if self.data is None:
			if self.str_data:
				raise NotImplementedError(
				    "String data conversion is not implemented")
			elif self.file_path:
				loader = Loader(self.file_path)
				try:
					self.data = loader.load_as(self.source_format)
				except LoaderFormatError as e:
					fatal(
					    f"Failed to load file {self.file_path} because {str(e)}"
					)
				except LoaderValueError as e:
					fatal(
					    f"Failed to load file {self.file_path} because {str(e)}"
					)

			else:
				raise ConverterNoSourceDataError("No source data provided")

		if self.source_format == "csv" and self.target_format == "json":
			return self._convert_csv_to_json()
		else:
			raise ConverterUnknownError("Unsupported conversion logic")

	def _convert_csv_to_json(self) -> Dict[str, Any]:
		"""
		Converts CSV data to JSON.
		Uses the first value in each row as the key and the rest of the values as the value.
		"""
		if self.data is None:
			raise ConverterNoSourceDataError("No source data provided")
		if isinstance(self.data, dict):
			raise ConverterIncorrectSourceDataError(
			    "Source data is a dictionary, expected a list of dictionaries")

		data: Dict[str, Any] = {}

		for row in self.data:
			item: Dict[str, Any] = {}
			idx = 0
			json_key = list(row.values())[0]
			for key, value in row.items():
				if idx == 0:
					idx += 1
					continue

				item[key] = value
				idx += 1

			data[json_key] = item

		return data
