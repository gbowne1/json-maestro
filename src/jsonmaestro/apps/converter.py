import sys
import json
import csv

from typing import Dict, List

from jsonmaestro.logger import infof, errorf
from jsonmaestro.loader import Loader
from jsonmaestro.converter import Converter


def read_input() -> List[Dict[str, str]]:
	"""
	Reads input from stdin and returns a list of dictionaries.
	Each dictionary represents a line in the input file.
	The dictionary has three keys: "file", "format_in", and "format_out".
	"file_in" is the path to the file to be converted.
	"format_in" is the format of the file to be converted.
	"format_out" is the format to convert the file to.
	"file_out" is the path to the output file.
	"""
	input_data: List[Dict[str, str]] = []

	for line in sys.stdin:
		line = line.strip()
		l: Dict[str, str] = {}
		parts = line.split(" ")
		l["file_in"] = parts[0]
		l["format_in"] = parts[1]
		l["format_out"] = parts[2]
		l["file_out"] = parts[3]
		input_data.append(l)

	return input_data


def main() -> None:
	input_data: List[Dict[str, str]] = read_input()

	for conversion in input_data:
		infof("Converting {} from {} to {}", conversion['file_in'],
		      conversion['format_in'], conversion['format_out'])

		converter = Converter(file_path=None,
		                      str_data=None,
		                      data=Loader(conversion['file_in']).load_as(
		                          conversion['format_in']),
		                      source_format=conversion['format_in'],
		                      target_format=conversion['format_out'])

		if not converter.convertable():
			errorf("Conversion from {} to {} is not supported",
			       conversion['format_in'], conversion['format_out'])
			continue

		with open(conversion['file_out'], "w") as file:
			if converter.target_format == "csv":
				data = converter.convert()
				if data is not None and isinstance(data, list):
					fieldnames = list(data[0].keys())

					writer = csv.DictWriter(file, fieldnames=fieldnames)

					writer.writeheader()
					writer.writerows(data)

			elif converter.target_format == "json":
				json.dump(converter.convert(), file)


if __name__ == "__main__":
	main()
