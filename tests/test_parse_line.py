import pytest
from main import parse_line

def test_parse_line_only_name():
    country_name, _, _ = parse_line("1 Ukraine 200km^2 40000000")
    assert country_name == "Ukraine"

def test_parse_line_category():
    _, area, _, = parse_line("1 Ukraine 200km^2 40000000")
    assert area == 200

def test_parse_line_money() :
    _, _, population = parse_line("1 Ukraine 200km^2 40000000")
    assert population == 40000000

def test_line_items_number():
    with pytest.raises(ValueError):
        parse_line("1 Ukraine")

def test_line_items_number():
    with pytest.raises (ValueError) :
        parse_line("1 Ukraine -200km^2 40000000")