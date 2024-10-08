from typing import Any, Dict, List, Union
from jsonmaestro.jsonmaestro import load_json, load_jsonc, remove_comments, remove_duplicate_keys, add_schema_keys, sort_json_keys, save_json
import jsonmaestro.helpers as helpers
import sys
import os
import click


def interactive_mode(debug: bool):
	input_file = input(
	    "Enter the path to your JSON, JSONC, or VSCode settings.json file: ")

	if not os.path.exists(input_file):
		print(f"[ERROR] filepath {input_file} does not exists")
		sys.exit(1)

	# Check if it's a VSCode settings.json file
	if helpers.is_json(input_file):
		load_function = load_json
	else:
		load_function = load_jsonc

	original_data = load_function(input_file)

	# Process the data
	cleaned_data = remove_duplicate_keys(original_data)
	cleaned_data = add_schema_keys(cleaned_data)

	# Remove comments if requested
	if input("Do you want to remove comments? (y/n): ").lower() == 'y':
		if debug:
			print("[DEBUG]: remove_comments = y")
		cleaned_data = remove_comments(cleaned_data)
	else:
		if debug:
			print("[DEBUG]: remove_comments = n")

	# Sort the keys
	if input("Do you want to sort keys? (y/n): ").lower() == 'y':
		if debug:
			print("[DEBUG]: sort_keys = y")

		sort_method = input(
		    "Do you want to sort in ascending (a) or descending (d)? ").lower(
		    )
		if sort_method == 'a':
			if debug:
				print("[DEBUG]: order = a")

			cleaned_data = sort_json_keys(cleaned_data, reverse=False)
		elif sort_method == 'd':
			if debug:
				print("[DEBUG]: order = d")

			cleaned_data = sort_json_keys(cleaned_data, reverse=True)
		else:
			if debug:
				print("[DEBUG]: order = {sort_method}")
			print("Invalid choice. Defaulting to ascending order.")
			cleaned_data = sort_json_keys(cleaned_data, reverse=False)

	print(f"Successfully processed {input_file}")

	# Save the cleaned data to the output file
	output_file = f"{os.path.splitext(input_file)[0]}_clean{os.path.splitext(input_file)[1]}"
	try:
		save_json(cleaned_data, output_file)
	except Exception as e:
		print(f"[ERROR]: Failed to save cleaned data because {str(e)}")
		sys.exit(1)

	print(f"Cleaned data saved to {output_file}")


@click.command()
@click.option("-f", "--files", multiple=True, required=False, default=())
@click.option("-c",
              "--clean",
              is_flag=True,
              required=False,
              default=None,
              type=bool,
              help="Remove comments from json file")
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
    "Run jsonmaestro in inteactive, defults to this if no other arguments were provided"
)
@click.option("-d",
              "--debug",
              is_flag=True,
              required=False,
              default=False,
              help="Run jsonmaestro in debug mode, enable debug printing")
def main(files: tuple[str], clean: bool, sort: str, interactive: bool,
         debug: bool):
	empty_tuple = ()
	if empty_tuple:
		print("This won't be printed")  # This line won't execute.
	else:
		print("This will be printed")  # This will execute.
	if debug:
		print(f"[DEBUG] files: {files}")
		print(f"[DEBUG] clean: {clean}")
		print(f"[DEBUG] sort: {sort}")
		print(f"[DEBUG] interactive: {interactive}")

	if len(files) == 0:
		# pylance thinks this is unreachable, it is reachable hence we are checking the lenght of the tuple
		if debug:
			print(f"[DEBUG] lenght of files provided is 0")
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
			print(f"[ERROR] filepath {file} does not exists")
			sys.exit(1)

		content_map[file] = {}

		if helpers.is_json(file):
			content_map[file]["source"] = load_json(file)
		else:
			content_map[file]["source"] = load_jsonc(file)

		content_map[file]["clean"] = add_schema_keys(
		    remove_duplicate_keys(content_map[file]["source"]))

		if clean:
			content_map[file]["clean"] = remove_comments(
			    content_map[file]["clean"])

		if sort == "a":
			content_map[file]["clean"] = sort_json_keys(
			    content_map[file]["clean"], False)
		elif sort == "d":
			content_map[file]["clean"] = sort_json_keys(
			    content_map[file]["clean"], True)

		save_json(content_map[file]["clean"], output_file)


if __name__ == "__main__":
	main()
