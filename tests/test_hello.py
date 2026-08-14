#!/usr/bin/env python
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from hello import hello  # noqa: E402


def test_hello_prints_world(capsys: pytest.CaptureFixture) -> None:
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"


def test_hello_prints_to_stdout(capsys: pytest.CaptureFixture) -> None:
    hello()
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out
    assert captured.err == ""
