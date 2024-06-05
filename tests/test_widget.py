import pytest

from src.widget import date_conversion, mask_type_card_check


def test_mask_type_card_check(card_str):
    assert mask_type_card_check("Visa Platinum 7000792289606361") == card_str


def test_mask_type_card_check_second():
    assert mask_type_card_check("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"


def test_mask_type_card_check_third(check_str):
    assert mask_type_card_check("Счет 35383033474447895560") == check_str


def test_date_conversion():
    assert date_conversion("2018-07-11T02:26:18.671407") == "11.07.2018"