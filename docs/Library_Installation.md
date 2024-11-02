# Library Installation

To install the Python library, you can use pip:

```bash
pip install json-maestro
```

This will install the latest version of the library.

Or you can put it in your requirements.txt file and install it with pip.

```diff
  dependency1
  dependency2
+ json-maestro
```

```bash
pip install -r requirements.txt
```

Or you can build the library from source.

1. Clone the repository

```bash
git clone https://github.com/gbowne1/json-maestro.git # via https
git clone git@github.com:gbowne1/json-maestro.git # via ssh
```

2. navigate to the cloned repository

```bash
cd /path/to/cloned/json-maestro
```

3. install requirements

```bash
pip install -r requirements.txt
pip install --upgrade build
```

4. build json maestro

```bash
python3 -m build
```

5. install json maestro using pip.
```bash
pip install .
```