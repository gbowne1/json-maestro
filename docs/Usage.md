# Usage

This page will cover the usage of the command line tool, for library usage please refer to the [API](./API.md) page.

## Interactive Mode

The interactive mode allows you to run the tool in a command line interface, without the need to specify any arguments.

To run the tool in interactive mode, simply run the following command:

```bash
jsonmaestro
```

This will prompt you to enter the path to the JSON, JSONC, or VSCode settings.json file you want to clean.

Once you have entered the path, the tool will start cleaning the file and displaying the cleaned data.

## Command Line Arguments

The command line tool accepts the following arguments:

- `-f`, `--files`: A list of files to clean. You can specify multiple files by separating them with spaces.
- `-s`, `--sort`: The sorting method to use. You can choose between `a` for ascending order or `d` for descending order.
- `-i`, `--interactive`: Run the tool in interactive mode.
- `-d`, `--debug`: Enable debug mode. This will print additional information during the cleaning process.

### Examples

To clean a JSON file and sort the keys in ascending order, you can run the following command:

```bash
jsonmaestro -f path/to/file.json -s a
```

To clean a JSON file and sort the keys in descending order, you can run the following command:

```bash
jsonmaestro -f path/to/file.json -s d
```

To clean a JSON file in interactive mode, you can run the following command:

```bash
jsonmaestro -f path/to/file.json -i
```

To clean a JSON file in debug mode, you can run the following command:

```bash
jsonmaestro -f path/to/file.json -d
```