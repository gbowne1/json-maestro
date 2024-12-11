import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../src")

from jsonmaestro.helpers import can_use_match


def test_can_use_match():
	can = can_use_match()
	if sys.version_info >= (3, 10):
		assert can is True
		return
	assert can is False
