import pytest

from src.masks import mask_card, mask_check


def test_mask_card():
    assert mask_card("7000792289606361") == "7000 79** **** 6361"


@pytest.mark.parametrize("check_user, expected", [("73654108430135874305", "**4305")])
def test_mask_check(check_user, expected):
    assert mask_check(check_user) == expected

