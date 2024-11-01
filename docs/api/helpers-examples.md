# Examples

## is_json

```python
from jsonmaestro.helpers import is_json

if is_json("path/to/the/file"):
    print("Loading data as json")
else:
    print("Loading data as jsonc")
```

## get_format

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