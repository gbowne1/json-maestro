import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../src")

import pytest
from jsonmaestro.logger import (
    log,
    logf,
    debug,
    debugf,
    info,
    infof,
    warn,
    warnf,
    error,
    errorf,
    fatal,
    fatalf,
)

from jsonmaestro.contantants import DEBUG_COLOR as _DEBUG_COLOR, RESET_COLOR as _RESET_COLOR, INFO_COLOR as _INFO_COLOR, WARN_COLOR as _WARN_COLOR, ERROR_COLOR as _ERROR_COLOR, FATAL_COLOR as _FATAL_COLOR

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
	assert f"{_DEBUG_COLOR}[ DEBUG ]{_RESET_COLOR}: Debug message" in captured.out


def test_debug_with_kwargs(capsys):
	debug("Debug message with kwargs", key="value")
	captured = capsys.readouterr()
	assert f"{_DEBUG_COLOR}[ DEBUG ]{_RESET_COLOR}: Debug message with kwargs" in captured.out
	assert "\tkey=value" in captured.out


def test_info_no_kwargs(capsys):
	info("Info message")
	captured = capsys.readouterr()
	assert f"{_INFO_COLOR}[ INFO ]{_RESET_COLOR}: Info message" in captured.out


def test_info_with_kwargs(capsys):
	info("Info message with kwargs", key="value")
	captured = capsys.readouterr()
	assert f"{_INFO_COLOR}[ INFO ]{_RESET_COLOR}: Info message with kwargs" in captured.out
	assert "\tkey=value" in captured.out


def test_warn_no_kwargs(capsys):
	warn("Warn message")
	captured = capsys.readouterr()
	assert f"{_WARN_COLOR}[ WARN ]{_RESET_COLOR}: Warn message" in captured.out


def test_warn_with_kwargs(capsys):
	warn("Warn message with kwargs", key="value")
	captured = capsys.readouterr()
	assert f"{_WARN_COLOR}[ WARN ]{_RESET_COLOR}: Warn message with kwargs" in captured.out
	assert "\tkey=value" in captured.out


def test_error_no_kwargs(capsys):
	error("Error message")
	captured = capsys.readouterr()
	assert f"{_ERROR_COLOR}[ ERROR ]{_RESET_COLOR}: Error message" in captured.out


def test_error_with_kwargs(capsys):
	error("Error message with kwargs", key="value")
	captured = capsys.readouterr()
	assert f"{_ERROR_COLOR}[ ERROR ]{_RESET_COLOR}: Error message with kwargs" in captured.out
	assert "\tkey=value" in captured.out


def test_fatal_no_kwargs(capsys):
	with pytest.raises(
	    SystemExit):  # expect SystemExit due to exit(1) in fatal
		fatal("Fatal message")
	captured = capsys.readouterr()
	assert f"{_FATAL_COLOR}[ FATAL ]{_RESET_COLOR}: Fatal message" in captured.out


def test_fatal_with_kwargs(capsys):
	with pytest.raises(
	    SystemExit):  # expect SystemExit due to exit(1) in fatal
		fatal("Fatal message with kwargs", key="value")
	captured = capsys.readouterr()
	assert f"{_FATAL_COLOR}[ FATAL ]{_RESET_COLOR}: Fatal message with kwargs" in captured.out
	assert "\tkey=value" in captured.out


def test_logf(capsys):
	logf("Test {} with {}", "formatting", "args")
	captured = capsys.readouterr()
	assert "Test formatting with args" in captured.out


def test_debugf_no_kwargs(capsys):
	debugf("Debug {} with {}", "formatted", "message")
	captured = capsys.readouterr()
	assert f"{_DEBUG_COLOR}[ DEBUG ]{_RESET_COLOR}: Debug formatted with message" in captured.out


def test_infof_no_kwargs(capsys):
	infof("Info {} with {}", "formatted", "message")
	captured = capsys.readouterr()
	assert f"{_INFO_COLOR}[ INFO ]{_RESET_COLOR}: Info formatted with message" in captured.out


def test_warnf_no_kwargs(capsys):
	warnf("Warn {} with {}", "formatted", "message")
	captured = capsys.readouterr()
	assert f"{_WARN_COLOR}[ WARN ]{_RESET_COLOR}: Warn formatted with message" in captured.out


def test_errorf_no_kwargs(capsys):
	errorf("Error {} with {}", "formatted", "message")
	captured = capsys.readouterr()
	assert f"{_ERROR_COLOR}[ ERROR ]{_RESET_COLOR}: Error formatted with message" in captured.out


def test_fatalf_no_kwargs(capsys):
	with pytest.raises(
	    SystemExit):  # Expect SystemExit due to exit(1) in fatalf
		fatalf("Fatal {} with {}", "formatted", "message")
	captured = capsys.readouterr()
	assert f"{_FATAL_COLOR}[ FATAL ]{_RESET_COLOR}: Fatal formatted with message" in captured.out


def test_debugf_with_args(capsys):
	debugf("Debug value: {}, another: {}", 42, "test")
	captured = capsys.readouterr()
	assert f"{_DEBUG_COLOR}[ DEBUG ]{_RESET_COLOR}: Debug value: 42, another: test" in captured.out


def test_infof_with_args(capsys):
	infof("User {} logged in at {}", "Alice", "10:00 AM")
	captured = capsys.readouterr()
	assert f"{_INFO_COLOR}[ INFO ]{_RESET_COLOR}: User Alice logged in at 10:00 AM" in captured.out


def test_warnf_with_args(capsys):
	warnf("Disk space is {}% full", 85)
	captured = capsys.readouterr()
	assert f"{_WARN_COLOR}[ WARN ]{_RESET_COLOR}: Disk space is 85% full" in captured.out


def test_errorf_with_args(capsys):
	errorf("Error {} occurred at {}", "500", "/path/to/resource")
	captured = capsys.readouterr()
	assert f"{_ERROR_COLOR}[ ERROR ]{_RESET_COLOR}: Error 500 occurred at /path/to/resource" in captured.out


def test_fatalf_with_args(capsys):
	with pytest.raises(
	    SystemExit):  # Expect SystemExit due to exit(1) in fatalf
		fatalf("Critical {}: code {}", "error", 500)
	captured = capsys.readouterr()
	assert f"{_FATAL_COLOR}[ FATAL ]{_RESET_COLOR}: Critical error: code 500" in captured.out
