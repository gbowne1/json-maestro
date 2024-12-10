
# JsonMaestro

## types

### T

Signature:

```python
T = TypeVar('T', bound=Union[Dict[str, Any], List[Any], Any])
```

Description:
Type variable representing a dictionary, list, or any other type.

## functions

### load_jsonc

Signature:

```python
def load_jsonc(file_path: str) -> Dict[str, Any]:
```

Description:
Loads a JSONC file.

Parameters:

- `file_path`: The path to the JSONC file to load.

Returns:
A dictionary containing the data from the JSONC file.

#### Example

```python
from jsonmaestro import load_jsonc

data = load_jsonc("path/to/file.jsonc")

print(data)
```

### load_json

Signature:

```python
def load_json(file_path: str) -> Dict[str, Any]:
```

Description:
Loads a JSON file.

Parameters:

- `file_path`: The path to the JSON file to load.

Returns:
A dictionary containing the data from the JSON file.

#### Example

```python
from jsonmaestro import load_json

data = load_json("path/to/file.json")

print(data)
```

### remove_comments

Signature:

```python
def remove_comments(jsonc_content: str) -> str:
```

Description:
Removes comments from a JSONC file.

Parameters:

- `jsonc_content`: The content of the JSONC file to remove comments from.

Returns:
A string containing the content of the JSONC file without comments.

#### Example

```python
from jsonmaestro import remove_comments

with open("path/to/file.jsonc", "r") as file:
    content = file.read()

    cleaned_content = remove_comments(content)

    print(cleaned_content)
```

### add_schema_keys

Signature:

```python
def add_schema_keys(obj: T) -> T:
```

Description:
Adds schema keys to a dictionary.

Parameters:

- `obj`: The dictionary to add schema keys to.

Returns:
The dictionary with schema keys added.

>NOTE:
>This example will be added in the future.

### sort_json_keys

Signature:

```python
def sort_json_keys(obj: T, reverse: bool = False) -> T:
```

Description:
Sorts the keys in a dictionary.

Parameters:

- `obj`: The dictionary to sort the keys of.
- `reverse`: Whether to sort the keys in descending order.

Returns:
The sorted dictionary.

#### Example

```python
from jsonmaestro import sort_json_keys

data = {"key1": "value1", "key2": 123, "key3": [1, 2, 3]}

sorted_data = sort_json_keys(data)

print(sorted_data)
```

### save_json

Signature:

```python
def save_json(data: Union[Dict[str, Any], List[Any], str, int, float, bool],
              file_path: str) -> None:
```

Description:
Saves JSON data to a file.

Parameters:

- `data`: The data to save.
- `file_path`: The path to the file to save the data to.

Returns:
None

#### Example

```python
from jsonmaestro import save_json

data = {"key1": "value1", "key2": 123, "key3": [1, 2, 3]}

save_json(data, "path/to/file.json")
```