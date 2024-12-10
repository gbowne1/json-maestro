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

#### Example

```python
from jsonmaestro.helpers import is_json

if is_json("path/to/the/file"):
    print("Loading data as json")
else:
    print("Loading data as jsonc")
```

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

#### Example

```python
from jsonmaestor.helpers import get_format

format = get_format("path/to/the/file")

if format == "json":
    print("Loading data as json")
elif format == "jsonc":
    print("Loading data as jsonc")
else:
    raise Exeption("Unknown format")
```
