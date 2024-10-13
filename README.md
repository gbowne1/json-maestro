# JSONMaestro

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python)
![Pylance](https://img.shields.io/badge/Pylance-Enabled-brightgreen?style=for-the-badge&logo=visual-studio-code)
![Pytest](https://img.shields.io/badge/Pytest-Passing-success?style=for-the-badge&logo=pytest)
![License](https://img.shields.io/github/license/gbowne1/JSONMaestro?style=for-the-badge)

JSONMaestro is a powerful Python tool designed to clean, process, and optimize JSON-like files. It handles various operations such as removing comments, eliminating duplicates, adding schema keys, and sorting keys. This utility is particularly useful for developers working with configuration files, API responses, or any JSON-structured data that needs refinement.

Key features:

- Supports JSON, JSONC, and VSCode settings.json files
- Removes duplicate keys and comments
- Adds schema keys for improved structure
- Offers flexible key sorting options
- Preserves data integrity while cleaning

JSONMaestro streamlines the process of preparing JSON data for further analysis or integration, making it an essential tool for data preprocessing and configuration management tasks.

## Getting Started

### From Source

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
```

4. install json maestro using your prefered method (NOTE: both are shown here, either one should work)

```bash
pip install . # for installing using pip
python setup.py install # for using setup.py script

```
## Contributing

See <CONTRIBUTING.md>

If you would like to work on issues and new features, we welcome your issues and Pull Requests.

## License

MIT
