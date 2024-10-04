from jsonmaestro.jsonmaestro import load_json, load_jsonc,remove_comments,remove_duplicate_keys,add_schema_keys, sort_json_keys,save_json
import jsonmaestro.helpers as helpers
import sys
import os
import click

def interactive_mode(debug: bool):
	input_file = input("Enter the path to your JSON, JSONC, or VSCode settings.json file: ")

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

		sort_method = input("Do you want to sort in ascending (a) or descending (d)? ").lower()
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
@click.option("-f","--files", required=False)
@click.option(
	"-c",
    "--clean",
    is_flag=True,
    required=False,
    default=None,
    type=bool,
    help="Remove comments from json file"
)
@click.option(
	"-s",
    "--sort",
    required=False,
    default="a",
    type=str,
    help="sort json keys in order ascending / descending"
)
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
@click.option(
	"-d",
    "--debug",
    is_flag=True,
    required=False,
    default=False,
    help="Run jsonmaestro in debug mode, enable debug printing"
)
def main(files: list[str], clean: bool, sort: str,interactive: bool, debug: bool):
	if debug:
		print(f"[DEBUG] files: {files}")
		print(f"[DEBUG] clean: {clean}")
		print(f"[DEBUG] sort: {sort}")
		print(f"[DEBUG] interactive: {interactive}")

	if not files:
		interactive=True

	if interactive:
		interactive_mode(debug=debug)

if __name__ == "__main__":
	main()
