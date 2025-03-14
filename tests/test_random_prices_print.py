import sys

import numpy as np
import pytest
import typer

from cli import random_prices


def test_random_prices_with_invalid_arg(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["prog", "abc"])
    with pytest.raises(SystemExit) as exc_info:
        typer.run(random_prices)
    assert exc_info.value.code == 2
    captured = capsys.readouterr()
    assert "Invalid value for 'NUM': 'abc' is not a valid integer." in captured.err


def test_random_prices_with_invalid_negative_arg(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["prog", "-1"])
    with pytest.raises(SystemExit) as exc_info:
        typer.run(random_prices)
    assert exc_info.value.code == 2
    captured = capsys.readouterr()
    assert "No such option: -1" in captured.err


def test_random_prices_with_invalid_missing_arg(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["prog"])
    with pytest.raises(SystemExit) as exc_info:
        typer.run(random_prices)
    assert exc_info.value.code == 2
    captured = capsys.readouterr()
    assert "Missing argument 'NUM'. " in captured.err


def test_random_prices_with_valid_arg(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["prog", "3"])
    with pytest.raises(SystemExit) as exc_info:
        typer.run(random_prices)
    # success
    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    output = captured.out.strip()
    # reverse engineer printed string to array
    array = np.fromstring(output[1:-1], sep=" ")  # Remove [] and convert
    assert len(array) == 3
    assert all(0 <= x <= 100 for x in array)  # Check range if that's your requirement


def test_random_prices_with_valid_zero_arg(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["prog", "0"])
    with pytest.raises(SystemExit) as exc_info:
        typer.run(random_prices)
    # success
    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    output = captured.out.strip()
    # reverse engineer printed string to array
    array = np.fromstring(output[1:-1], sep=" ")  # Remove [] and convert
    assert len(array) == 0
