import pytest
from jsonmaestro.logger import (
    log,
    debug,
    info,
    warn,
    error,
    fatal,
    RESET_COLOR,
    DEBUG_COLOR,
    INFO_COLOR,
    WARN_COLOR,
    ERROR_COLOR,
    FATAL_COLOR,
)

# Test cases for each log level with and without additional kwargs


def test_log_no_level(capsys):
	log("Test message")
	captured = capsys.readouterr()
	assert "Test message" in captured.out


def test_log_with_kwargs(capsys):
	log("Test message with kwargs", key1="value1", key2="value2")
	captured = capsys.readouterr()
	assert "Test message with kwargs" in captured.out
	assert "key1=value1" in captured.out
	assert "key2=value2" in captured.out


def test_debug_no_kwargs(capsys):
	debug("Debug message")
	captured = capsys.readouterr()
	assert f"{DEBUG_COLOR}[ DEBUG ]{RESET_COLOR}: Debug message" in captured.out


def test_debug_with_kwargs(capsys):
	debug("Debug message with kwargs", key="value")
	captured = capsys.readouterr()
	assert f"{DEBUG_COLOR}[ DEBUG ]{RESET_COLOR}: Debug message with kwargs" in captured.out
	assert "\tkey=value" in captured.out


def test_info_no_kwargs(capsys):
	info("Info message")
	captured = capsys.readouterr()
	assert f"{INFO_COLOR}[ INFO ]{RESET_COLOR}: Info message" in captured.out


def test_info_with_kwargs(capsys):
	info("Info message with kwargs", key="value")
	captured = capsys.readouterr()
	assert f"{INFO_COLOR}[ INFO ]{RESET_COLOR}: Info message with kwargs" in captured.out
	assert "\tkey=value" in captured.out


def test_warn_no_kwargs(capsys):
	warn("Warn message")
	captured = capsys.readouterr()
	assert f"{WARN_COLOR}[ WARN ]{RESET_COLOR}: Warn message" in captured.out


def test_warn_with_kwargs(capsys):
	warn("Warn message with kwargs", key="value")
	captured = capsys.readouterr()
	assert f"{WARN_COLOR}[ WARN ]{RESET_COLOR}: Warn message with kwargs" in captured.out
	assert "\tkey=value" in captured.out


def test_error_no_kwargs(capsys):
	error("Error message")
	captured = capsys.readouterr()
	assert f"{ERROR_COLOR}[ ERROR ]{RESET_COLOR}: Error message" in captured.out


def test_error_with_kwargs(capsys):
	error("Error message with kwargs", key="value")
	captured = capsys.readouterr()
	assert f"{ERROR_COLOR}[ ERROR ]{RESET_COLOR}: Error message with kwargs" in captured.out
	assert "\tkey=value" in captured.out


def test_fatal_no_kwargs(capsys):
	with pytest.raises(
	    SystemExit):  # expect SystemExit due to exit(1) in fatal
		fatal("Fatal message")
	captured = capsys.readouterr()
	assert f"{FATAL_COLOR}[ FATAL ]{RESET_COLOR}: Fatal message" in captured.out


def test_fatal_with_kwargs(capsys):
	with pytest.raises(
	    SystemExit):  # expect SystemExit due to exit(1) in fatal
		fatal("Fatal message with kwargs", key="value")
	captured = capsys.readouterr()
	assert f"{FATAL_COLOR}[ FATAL ]{RESET_COLOR}: Fatal message with kwargs" in captured.out
	assert "\tkey=value" in captured.out
