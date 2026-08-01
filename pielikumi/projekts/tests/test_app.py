import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import add


def test_add():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(0, 5) == 5


def test_add_negative():
    assert add(-2, -3) == -5