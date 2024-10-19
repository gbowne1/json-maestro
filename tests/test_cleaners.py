import pytest

from jsonmaestro import remove_comments


@pytest.mark.parametrize("file_name", [
    "jsonc.json", "commented.json", "commented_with_duplicate.json",
    "bc_symbols.json", "ds_symbols.json", "mixed_comment_symbols.json",
    "package-lock-data.json"
])
def test_remove_comments(file_name):
	with open(f"data/{file_name}", "r") as file:
		data = remove_comments(file.read())

		if not file_name in [
		    "bc_symbols.json", "ds_symbols.json", "mixed_comment_symbols.json",
		    "package-lock-data.json"
		]:
			assert "//" not in data
			assert "/*" not in data
			assert "*/" not in data
		else:
			if file_name == "ds_symbols.json" or file_name == "package-lock-data.json":
				assert "//" in data
			elif file_name == "bc_symbols.json":
				assert "/*" in data
				assert "*/" in data
			else:
				assert "//" in data
				assert "/*" in data
				assert "*/" in data
