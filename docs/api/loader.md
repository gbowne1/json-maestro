# Loader

## Description

The Loader class is responsible for loading files in various formats. It provides a unified interface for loading files, regardless of the format.

## Constructor

### __init__

Signature:

```python
def __init__(self, file_path: str) -> None:
```

Description:
Initializes the Loader class with a file path.

Parameters:

- `file_path`: The path to the file to load.

## Methods

### load_as

Signature:

```python
def load_as(self, format: str) -> Union[Dict[str, Any], List[Dict[Union[str, Any], Union[str, Any]]]]:
```

Description:
Loads a file in a specific format.

Parameters:

- `format`: The format of the file to load.

Returns:
The loaded file as a dictionary in case of JSON or JSONC format, or a list of dictionaries in case of CSV format.

## Usage

```python
from jsonmaestro.loader import Loader

loader = Loader("path/to/file.json")
data = loader.load_as("json")
```