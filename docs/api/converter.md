# Converter

## Description

The Converter class is responsible for converting files between different formats. It provides a unified interface for converting files, regardless of the source and target formats.

## Constructor

### __init__

Signature:

```python
def __init__(self, file_path: str, str_data: str, data: Union[Dict[str, Any], List[Dict[Union[str, Any], Union[str, Any]]]], source_format: str, target_format: str) -> None:
```

Description:
Initializes the Converter class with the necessary parameters.

Parameters:

- `file_path [OPTIONAL]`: The path to the file to convert.
- `str_data [OPTIONAL]`: The string data to convert.
- `data [OPTIONAL]`: The data to convert.
- `source_format`: The format of the source data.
- `target_format`: The format to convert the data to.

## Methods

### convert

Signature:

```python
def convert(self) -> Union[Dict[str, Any], List[Dict[Union[str, Any], Union[str, Any]]]]:
```

Description:
Converts the data from the source format to the target format.

Returns:
The converted data in the target format.

### convertable

Signature:

```python
def convertable(self) -> bool:
```

Description:
Checks if the conversion is possible.

Returns:
`True` if the conversion is possible, `False` otherwise.

## Usage

### With file_path constructor

```python
from jsonmaestro.converter import Converter

converter = Converter(file_path="path/to/file.json", source_format="json", target_format="csv")
if not converter.convertable():
    print("Conversion not possible")
else:
    data = converter.convert()
```

### With str_data constructor

```python
from jsonmaestro.converter import Converter

converter = Converter(str_data='{"key": "value"}', source_format="json", target_format="csv")
if not converter.convertable():
    print("Conversion not possible")
else:
    data = converter.convert()
```

### With data constructor

```python
from jsonmaestro.converter import Converter

data = {"key": "value"}
converter = Converter(data=data, source_format="json", target_format="csv")
if not converter.convertable():
    print("Conversion not possible")
else:
    data = converter.convert()
```
