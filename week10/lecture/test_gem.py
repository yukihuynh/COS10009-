from test_harnesses import GemRecord, display_gem

# Normal valid test case
def test_display_gem_normal(capsys):
    gem = GemRecord(1, "Emerald", 4, 580.99)
    display_gem(gem)
    captured = capsys.readouterr()
    assert "1"         in captured.out
    assert "Emerald"   in captured.out
    assert "4.00"      in captured.out
    assert "$580.99"   in captured.out

#Test gem with id is a floating point number
def test_display_gem_float_id(capsys):
    gem = GemRecord(2.9, "Emerald", 4, 580.99)
    display_gem(gem)
    captured = capsys.readouterr()
    assert "2\n"  in captured.out   # 2.9 → 2
    assert "2.9" not in captured.out

# Test gem with None description
def test_display_gem_none_description(capsys):
    gem = GemRecord(1, None, 4, 580.99)
    display_gem(gem)
    captured = capsys.readouterr()
    assert "Unknown" in captured.out
    assert "None"    not in captured.out

# Test Weight rounds to 2 decimal places
def test_display_gem_weight_format(capsys):
    gem = GemRecord(1, "Emerald", 4.568, 580.99)
    display_gem(gem)
    captured = capsys.readouterr()
    assert "4.57"  in captured.out
    assert "4.568" not in captured.out

#  TEst Price includes $ symbol
def test_display_gem_price_format(capsys):
    gem = GemRecord(1, "Emerald", 4, 580.99)
    display_gem(gem)
    captured = capsys.readouterr()
    assert "$580.99" in captured.out