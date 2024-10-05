import json

_JSON_FORMAT:str = "json"
_JSONC_FORMAT:str = "jsonc"

def is_json(file_path: str)-> bool:
	try:
		with open(file=file_path,mode='r') as file:
			json.load(file)
		return True
	except (json.JSONDecodeError, ValueError):
		return False

def get_format(file_path:str)->str:
	if is_json(file_path=file_path):
		return _JSON_FORMAT
	return _JSONC_FORMAT