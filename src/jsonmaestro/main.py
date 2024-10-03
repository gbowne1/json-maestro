from jsonmaestro.jsonmaestro import load_vscode_settings, load_jsonc,remove_comments,remove_duplicate_keys,add_schema_keys, sort_json_keys,save_json
import sys
import os

def main():
    input_file = input("Enter the path to your JSON, JSONC, or VSCode settings.json file: ")

    # Check if it's a VSCode settings.json file
    if input_file.endswith('.json'):
        load_function = load_vscode_settings
    else:
        load_function = load_jsonc

    # Load the input file
    try:
        original_data = load_function(input_file)
    except Exception as e:
        print(f"Failed to load input file. Error: {str(e)}")
        sys.exit(1)

    # Process the data
    try:
        cleaned_data = remove_duplicate_keys(original_data)
        cleaned_data = add_schema_keys(cleaned_data)

        # Remove comments if requested
        remove_comments_option = input("Do you want to remove comments? (y/n): ").lower()
        if remove_comments_option == 'y':
            cleaned_data = remove_comments(cleaned_data)

        # Sort the keys
        sort_order = input("Do you want to sort keys? (y/n): ").lower()
        if sort_order == 'y':
            sort_method = input("Do you want to sort in ascending (a) or descending (d)? ").lower()
            if sort_method == 'a':
                cleaned_data = sort_json_keys(cleaned_data, reverse=False)
            elif sort_method == 'd':
                cleaned_data = sort_json_keys(cleaned_data, reverse=True)
            else:
                print("Invalid choice. Defaulting to ascending order.")
                cleaned_data = sort_json_keys(cleaned_data, reverse=False)
    except Exception as e:
        print(f"Failed to process data. Error: {str(e)}")
        sys.exit(1)

    # Save the cleaned data to the output file
    output_file = f"{os.path.splitext(input_file)[0]}_clean{os.path.splitext(input_file)[1]}"
    try:
        save_json(cleaned_data, output_file)
    except Exception as e:
        print(f"Failed to save cleaned data. Error: {str(e)}")
        sys.exit(1)

    print(f"Successfully processed {input_file}")
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
	main()