from activity.activity import typing_time
import pytest

def test_latin_ordering_same_letters_returns_0():
    typed_time = typing_time("abcdefghijklmnopqrstuvwxyz", "aaaaa")
    assert typed_time == 0

def test_latin_ordering_cat_returns_time():
    typed_time = typing_time("abcdefghijklmnopqrstuvwxyz", "cat")
    assert typed_time == 23

def test_reverse_latin_ordering_cat_returns_time():
    typed_time = typing_time("zyxwvutsrqponmlkjihgfedcba", "cat")
    assert typed_time == 44
