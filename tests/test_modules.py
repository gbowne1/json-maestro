def test_import_helpers():
	"""
	Test if the helpers module can be imported and is not None.
	"""
	try:
		# Attempt to import the module
		import jsonmaestro.helpers as helpers

		# Assert that the module is imported correctly (not None)
		assert helpers is not None, "Failed to import helpers"

	except ModuleNotFoundError as e:
		# If the module cannot be found, fail the test
		assert False, f"ModuleNotFoundError: {e}"


def test_import_core():
	"""
		Test if the module containing core functionality can be imported and is not None.
	"""
	try:
		import jsonmaestro.jsonmaestro as core

		assert core is not None, "Failed to import core"

	except ModuleNotFoundError as e:
		assert False, f"ModuleNotFoundError: {e}"


def test_import_jsonmaestro():
	"""
		Test if the jsonmaestro itself is importable
	"""
	try:
		import jsonmaestro as jm

		assert jm is not None, "Failed to import jsonmaestro"

	except ModuleNotFoundError as e:
		assert False, f"ModuleNotFoundError: {e}"