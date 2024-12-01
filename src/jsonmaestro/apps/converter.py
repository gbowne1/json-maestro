import sys
import json
import csv
import os
import datetime

from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Union

import click

from jsonmaestro.logger import infof, errorf
from jsonmaestro.loader import Loader
from jsonmaestro.converter import Converter


def read_file_input(lines: List[str]) -> List[Dict[str, str]]:
	"""
	Reads input from a file and returns a list of dictionaries.
	Each dictionary represents a line in the input file.
	The dictionary has three keys: "file", "format_in", and "format_out".
	"file_in" is the path to the file to be converted.
	"format_in" is the format of the file to be converted.
	"format_out" is the format to convert the file to.
	"file_out" is the path to the output file.
	"""
	input_data: List[Dict[str, str]] = []

	for line in lines:
		line = line.strip()
		l: Dict[str, str] = {}
		parts = line.split(" ")
		l["file_in"] = parts[0]
		l["format_in"] = parts[1]
		l["format_out"] = parts[2]
		l["file_out"] = parts[3]

		if len(parts) == 5:
			l["write"] = parts[4]
		else:
			l["write"] = "stdout"

		input_data.append(l)

	return input_data


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

		if len(parts) == 5:
			l["write"] = parts[4]
		else:
			l["write"] = "stdout"

		input_data.append(l)

	return input_data


def convert(input_data: Dict[str, str]) -> None:
	"""
	Handles the conversion of a single input line.
	"""

	time_now = datetime.datetime.now()

	infof("Converting {} from {} to {}", input_data['file_in'],
	      input_data['format_in'], input_data['format_out'])

	converter = Converter(file_path=None,
	                      str_data=None,
	                      data=Loader(input_data['file_in']).load_as(
	                          input_data['format_in']),
	                      source_format=input_data['format_in'],
	                      target_format=input_data['format_out'])

	if not converter.convertable():
		errorf("Conversion from {} to {} is not supported",
		       input_data['format_in'], input_data['format_out'])
		return

	if input_data['write'] == "stdout":
		infof("Writing to stdout not implemented yet")

	if input_data['write'] == "w":
		with open(input_data['file_out'], "w", encoding="utf-8") as file:
			if converter.target_format == "csv":
				data = converter.convert()
				if data is not None and isinstance(data, list):
					fieldnames = list(data[0].keys())

					writer = csv.DictWriter(file, fieldnames=fieldnames)

					writer.writeheader()
					writer.writerows(data)

			elif converter.target_format == "json":
				json.dump(converter.convert(), file)

	infof("Conversion from {} to {} for {} completed in {}",
	      input_data['format_in'], input_data['format_out'],
	      input_data['file_in'],
	      datetime.datetime.now() - time_now)


@click.command()
@click.option("-i",
              "--input",
              "--input-file",
              required=False,
              default=None,
              type=str)
def main(input_file: Union[str, None]) -> None:
	time_now = datetime.datetime.now()
	input_data: List[Dict[str, str]] = []

	if input_file is not None:
		infof("Reading input from file {}", input_file)
		with open(input_file, "r", encoding="utf-8") as file:
			file_data = file.readlines()
			input_data = read_file_input(file_data)
	else:
		input_data = read_input()

	core_count = os.cpu_count()
	if core_count is not None and core_count - 2 > 2:
		infof("Using {} threads", core_count - 2)
		with ThreadPoolExecutor(max_workers=(core_count - 2)) as executor:
			executor.map(convert, input_data)
	else:
		infof("Using 1 thread")
		for input_item in input_data:
			convert(input_item)

	infof("Conversion completed in {}", datetime.datetime.now() - time_now)


if __name__ == "__main__":
	main()
