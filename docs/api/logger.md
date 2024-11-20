# Logger

log and logf are the same as print, but have preconstructed message.

debug, debugf print with `[ DEBUG ]` prefix in bright blue color.

info, infof print with `[ INFO ]` prefix in bright green color.

warn, warnf print with `[ WARN ]` prefix in bright yellow color.

error, errorf print with `[ ERROR ]` prefix in bright red color.

fatal, fatalf print with `[ FATAL ]` prefix in bright magenta color and exit with code 1.

## functions

### log

Signature:

```python
def log(message: str, **kwargs: Any) -> None:
```

Description:

Log a message to the logger.

Arguments:

- `message`: The message to log.
- `**kwargs`: Additional keyword arguments to pass to the logger.

### logf

Signature:

```python
def logf(format_str: str, *args: Any) -> None:
```

Description:

Log a formatted message to the logger.

Arguments:

- `format_str`: The format string to use.
- `*args`: The arguments to pass to the format string.

### debug

Signature:

```python
def debug(message: str, **kwargs: Any) -> None:
```

Description:

Log a debug message to the logger.

Arguments:

- `message`: The message to log.
- `**kwargs`: Additional keyword arguments to pass to the logger.

### debugf

Signature:

```python
def debugf(format_str: str, *args: Any) -> None:
```

Description:

Log a debug formatted message to the logger.

Arguments:

- `format_str`: The format string to use.
- `*args`: The arguments to pass to the format string.

### info

Signature:

```python
def info(message: str, **kwargs: Any) -> None:
```

Description:

Log an info message to the logger.

Arguments:

- `message`: The message to log.
- `**kwargs`: Additional keyword arguments to pass to the logger.

### infof

Signature:

```python
def infof(format_str: str, *args: Any) -> None:
```

Description:

Log an info formatted message to the logger.

Arguments:

- `format_str`: The format string to use.
- `*args`: The arguments to pass to the format string.

### warn

Signature:

```python
def warn(message: str, **kwargs: Any) -> None:
```

Description:

Log a warning message to the logger.

Arguments:

- `message`: The message to log.
- `**kwargs`: Additional keyword arguments to pass to the logger.

### warnf

Signature:

```python
def warnf(format_str: str, *args: Any) -> None:
```

Description:

Log a warning formatted message to the logger.

Arguments:

- `format_str`: The format string to use.
- `*args`: The arguments to pass to the format string.

### error

Signature:

```python
def error(message: str, **kwargs: Any) -> None:
```

Description:

Log an error message to the logger.

Arguments:

- `message`: The message to log.
- `**kwargs`: Additional keyword arguments to pass to the logger.

### errorf

Signature:

```python
def errorf(format_str: str, *args: Any) -> None:
```

Description:

Log an error formatted message to the logger.

Arguments:

- `format_str`: The format string to use.
- `*args`: The arguments to pass to the format string.

### fatal

Signature:

```python
def fatal(message: str, **kwargs: Any) -> NoReturn:
```

Description:

Log a fatal message to the logger and exit the program.

Arguments:

- `message`: The message to log.
- `**kwargs`: Additional keyword arguments to pass to the logger.

### fatalf

Signature:

```python
def fatalf(format_str: str, *args: Any) -> NoReturn:
```

Description:

Log a fatal formatted message to the logger and exit the program.

Arguments:

- `format_str`: The format string to use.
- `*args`: The arguments to pass to the format string.
