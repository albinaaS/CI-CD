import pytest
from main import parse_line
from decimal import Decimal

@pytest.mark.parametrize("line, result",[("1 Ukraine 200km^2 40000000", ("Ukraine", Decimal("200"), Decimal("40000000"))),
                                        ("1 Ukraine 200 40000000", ("Ukraine", Decimal("200"), Decimal("40000000"))),
                                        ("1 UKRAINE 200km^2 40000000", ("Ukraine", Decimal("200"), Decimal("40000000"))),
                                        ])
def test_parse_line_only_name(line, result):
    assert parse_line(line) == result