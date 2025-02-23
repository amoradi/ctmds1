import numpy as np
import pytest

from ctmds1.main import main


def test_main_with_invalid_arg():
    with pytest.raises(Exception):
        main("abc")  # type: ignore


def test_main_with_invalid_negative_arg():
    with pytest.raises(Exception):
        main(-1)


def test_main_with_invalid_missing_arg():
    with pytest.raises(Exception):
        main()


def test_main_with_valid_arg():
    result = main(3)
    assert isinstance(result, np.ndarray)
    assert len(result) == 3


def test_main_with_valid_zero_arg():
    result = main(0)
    assert isinstance(result, np.ndarray)
    assert len(result) == 0
