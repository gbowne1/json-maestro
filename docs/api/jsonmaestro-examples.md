# Examples

This example show general use for the specific functions.

> NOTE:
> The fully functional examples that could be used as snippets will be added in the future.

## load_jsonc

```python
from jsonmaestro import load_jsonc

data = load_jsonc("path/to/file.jsonc")

print(data)
```

## load_json

```python
from jsonmaestro import load_json

data = load_json("path/to/file.json")

print(data)
```

## remove_comments

```python
from jsonmaestro import remove_comments

with open("path/to/file.jsonc", "r") as file:
    content = file.read()

    cleaned_content = remove_comments(content)

    print(cleaned_content)
```