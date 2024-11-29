import sys
from io import StringIO
from typing import Dict, List
from jsonmaestro.apps.converter import read_input, main


def test_read_input():
	original_stdin = sys.stdin
	test_input = "example.csv csv json example.json\n"
	sys.stdin = StringIO(test_input)

	data_out = read_input()

	assert len(data_out) == 1
	assert data_out[0]["file_in"] == "example.csv"
	assert data_out[0]["format_in"] == "csv"
	assert data_out[0]["format_out"] == "json"
	assert data_out[0]["file_out"] == "example.json"

	sys.stdin = original_stdin


def test_read_input_from_file():
	original_stdin = sys.stdin
	with open("data/test_stdin.txt", "r") as file:
		test_input = file.read()

	sys.stdin = StringIO(test_input)
	data_out = read_input()

	assert True

	with open("data/test_stdin.txt", "r") as file:
		input = file.readlines()

	assert len(data_out) == len(input)

	in_data: List[Dict[str, str]] = []

	for line in input:
		line = line.strip()
		l: Dict[str, str] = {}
		parts = line.split(" ")
		l["file_in"] = parts[0]
		l["format_in"] = parts[1]
		l["format_out"] = parts[2]
		l["file_out"] = parts[3]
		in_data.append(l)

	for i in range(len(data_out)):
		assert data_out[i]["file_in"] == in_data[i]["file_in"]
		assert data_out[i]["format_in"] == in_data[i]["format_in"]
		assert data_out[i]["format_out"] == in_data[i]["format_out"]
		assert data_out[i]["file_out"] == in_data[i]["file_out"]

	sys.stdin = original_stdin


def test_main():
	original_stdin = sys.stdin
	test_input = "data/example.csv csv json data/example.json\n"
	sys.stdin = StringIO(test_input)

	main()

	assert True

	sys.stdin = original_stdin
