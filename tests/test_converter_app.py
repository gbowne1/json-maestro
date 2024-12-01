import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../src")
from io import StringIO
from typing import Dict, List

from click.testing import CliRunner

from jsonmaestro.apps.converter import read_input, read_file_input, main


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


def test_read_file_input():

	with open("data/test_file_input.txt", "r") as file:
		test_input = file.readlines()

	control_data: List[Dict[str, str]] = []

	for line in test_input:
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
		control_data.append(l)

	data_out = read_file_input(test_input)

	assert len(data_out) == len(control_data)

	for i in range(len(data_out)):
		assert data_out[i]["file_in"] == control_data[i]["file_in"]
		assert data_out[i]["format_in"] == control_data[i]["format_in"]
		assert data_out[i]["format_out"] == control_data[i]["format_out"]
		assert data_out[i]["file_out"] == control_data[i]["file_out"]
		assert data_out[i]["write"] == control_data[i]["write"]


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

		if len(parts) == 5:
			l["write"] = parts[4]
		else:
			l["write"] = "stdout"
		in_data.append(l)

	for i in range(len(data_out)):
		assert data_out[i]["file_in"] == in_data[i]["file_in"]
		assert data_out[i]["format_in"] == in_data[i]["format_in"]
		assert data_out[i]["format_out"] == in_data[i]["format_out"]
		assert data_out[i]["file_out"] == in_data[i]["file_out"]
		assert data_out[i]["write"] == in_data[i]["write"]

	sys.stdin = original_stdin


def test_main():
	original_stdin = sys.stdin
	if not os.path.exists("out"):
		os.mkdir("out")
	test_input = "data/example.csv csv json out/example.json w\n data/example.json json csv out/example.csv w\ndata/really_large.json jsonc csv out/really_large.csv w\ndata/really_large.csv csv json out/really_large.json w\n"
	sys.stdin = StringIO(test_input)

	runner = CliRunner()
	result = runner.invoke(main, input=test_input)

	assert result.exit_code == 0

	assert os.path.exists("out/example.json") is True
	assert os.path.exists("out/example.csv") is True
	assert os.path.exists("out/really_large.csv") is True
	assert os.path.exists("out/really_large.json") is True

	sys.stdin = original_stdin

	os.remove("out/example.json")
	os.remove("out/example.csv")
	os.remove("out/really_large.csv")
	os.remove("out/really_large.json")
	os.rmdir("out")
