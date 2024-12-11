from typing import Any, Dict, List, Union
from jsonmaestro.jsonmaestro import add_schema_keys, sort_json_keys, save_json
import jsonmaestro.helpers as helpers
import jsonmaestro.logger as logger
from jsonmaestro.loader import Loader
import sys
import os
import click


def interactive_mode(debug: bool):
	input_file = input(
	    "Enter the path to your JSON, JSONC, or VSCode settings.json file: ")

	if not os.path.exists(input_file):
		print(f"[ERROR] filepath {input_file} does not exists")
		sys.exit(1)

	loader = Loader(input_file)

	# Check if it's a VSCode settings.json file
	if helpers.is_json(input_file):
		original_data = loader.load_as("json")
	else:
		original_data = loader.load_as("jsonc")

	# Process the data
	cleaned_data = add_schema_keys(original_data)

	# Sort the keys
	if input("Do you want to sort keys? (y/n): ").lower() == 'y':
		if debug:
			logger.debug("sort_keys = y")

		sort_method = input(
		    "Do you want to sort in ascending (a) or descending (d)? ").lower(
		    )
		if sort_method == 'a':
			if debug:
				logger.debug("order = a")

			cleaned_data = sort_json_keys(cleaned_data, reverse=False)
		elif sort_method == 'd':
			if debug:
				logger.debug("order = d")

			cleaned_data = sort_json_keys(cleaned_data, reverse=True)
		else:
			if debug:
				logger.debug(f"order = {sort_method}")
			print("Invalid choice. Defaulting to ascending order.")
			cleaned_data = sort_json_keys(cleaned_data, reverse=False)

	print(f"Successfully processed {input_file}")

	# Save the cleaned data to the output file
	output_file = f"{os.path.splitext(input_file)[0]}_clean{os.path.splitext(input_file)[1]}"
	try:
		save_json(cleaned_data, output_file)
	except Exception as e:
		logger.fatal(f"Failed to save cleaned data because {str(e)}")

	print(f"Cleaned data saved to {output_file}")


@click.command()
@click.option("-f", "--files", multiple=True, required=False, default=())
@click.option("-s",
              "--sort",
              required=False,
              default="a",
              type=str,
              help="sort json keys in order ascending / descending")
@click.option(
    "-i",
    "--interactive",
    is_flag=True,
    required=False,
    default=None,
    type=bool,
    help=
    "Run jsonmaestro in interactive, defaults to this if no other arguments were provided"
)
@click.option("-d",
              "--debug",
              is_flag=True,
              required=False,
              default=False,
              help="Run jsonmaestro in debug mode, enable debug printing")
def main(files: tuple[str], sort: str, interactive: bool, debug: bool):
	empty_tuple = ()
	if empty_tuple:
		print("This won't be printed")  # This line won't execute.
	else:
		print("This will be printed")  # This will execute.
	if debug:
		logger.debug(f"files: {files}")
		logger.debug(f"sort: {sort}")
		logger.debug(f"interactive: {interactive}")

	if len(files) == 0:
		# pylance thinks this is unreachable, it is reachable hence we are checking the lenght of the tuple
		if debug:
			logger.debug(f"length of files provided is 0")
		interactive = True

	# short to interactive mode in no files are provided
	if interactive:
		interactive_mode(debug=debug)
		return

	content_map: Dict[str, Dict[str, Union[Dict[str, Any], List[Any],
	                                       Any]]] = {}
	for file in files:
		output_file = f"{os.path.splitext(file)[0]}_clean{os.path.splitext(file)[1]}"
		if not os.path.exists(file):
			logger.error(f"filepath {file} does not exists")
			sys.exit(1)

		content_map[file] = {}
		loader = Loader(file)

		if helpers.is_json(file):
			content_map[file]["source"] = loader.load_as("json")
		else:
			content_map[file]["source"] = loader.load_as("jsonc")

		content_map[file]["clean"] = add_schema_keys(
		    content_map[file]["source"])

		if sort == "a":
			content_map[file]["clean"] = sort_json_keys(
			    content_map[file]["clean"], False)
		elif sort == "d":
			content_map[file]["clean"] = sort_json_keys(
			    content_map[file]["clean"], True)

		save_json(content_map[file]["clean"], output_file)


if __name__ == "__main__":
	main()
