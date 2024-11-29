from typing import Any, Dict, List, Union


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

	def __init__(
	    self,
	    source_format: str,
	    target_format: str,
	    file_path: Union[str, None] = None,
	    str_data: Union[str, None] = None,
	    data: Union[None, Union[Dict[str, Any],
	                            List[Dict[Union[str, Any],
	                                      Union[str, Any]]]]] = None,
	) -> None:
		...

	def convert(self) -> Union[None, Dict[str, Any], List[Dict[str, Any]]]:
		...
