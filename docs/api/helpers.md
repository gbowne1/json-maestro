# Helpers

## functions

### is_json

Signature:
```python
def is_json(file_path: str) -> bool:
```

Description:
Checks if a file is a JSON file.

Parameters:
- `file_path`: The path to the file to check.

Returns:
`True` if the file is a JSON file, `False` otherwise.

### get_format

Signature:
```python
def get_format(file_path: str) -> str:
```

Description:
Gets the format of a JSON file.

Parameters:
- `file_path`: The path to the file to check.

Returns:
The format of the file as a string.

Possible values:
- `json`: The file is a JSON file.
- `jsonc`: The file is a JSONC file.