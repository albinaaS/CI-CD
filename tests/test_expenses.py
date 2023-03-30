from main import total_by_population, total_by_area

def test_total_by_population(prepare_text_file):
    expected = {"Usa": 331000000.0,
                "France": 68000000.0,
                "Britain": 67000000.0,
                }
    result = total_by_population(prepare_text_file)
    assert set(expected.keys()) == set(result.keys())
    assert all([result[key] == expected[key] for key in result.keys()])

def test_total_by_area(prepare_text_file):
    expected = {"Usa": 9834000.0,
                "France": 551695.0,
                "Britain": 243610.0,
                }
    result = total_by_area(prepare_text_file)
    assert set(expected.keys()) == set(result.keys())
    assert all([result[key] == expected[key] for key in result.keys()])

