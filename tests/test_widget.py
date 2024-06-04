import pytest


from src.widget import mask_type_card_check, date_conversion


def test_mask_type_card_check(card_str):
    assert mask_type_card_check("Visa Platinum 7000792289606361") == card_str

def test_mask_type_card_check_second():
    assert mask_type_card_check("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"

def test_mask_type_card_check_third(check_str):
    assert mask_type_card_check("Счет 35383033474447895560") == check_str