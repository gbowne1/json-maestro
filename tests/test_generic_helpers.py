import sys

from jsonmaestro.helpers import can_use_match


def test_can_use_match():
	can = can_use_match()
	if sys.version_info >= (3, 10):
		assert can is True
		return
	assert can is False
