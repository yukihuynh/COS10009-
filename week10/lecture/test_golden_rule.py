
from test_harnesses import GemRecord, display_gems

# shared test data
gem1 = GemRecord(1, "Emerald", 4.0, 580.99)
gem2 = GemRecord(2, "Ruby", 3.2, 430.00)
gem3 = GemRecord(3, "Diamond", 5.1, 1200.00)

# 0 element
def test_display_gems_empty(capsys):
    display_gems([])
    captured = capsys.readouterr()
    assert captured.out == ""   # nothing should be printed

# 1 element
def test_display_gems_one(capsys):
    display_gems([gem1])
    captured = capsys.readouterr()
    assert "Emerald" in captured.out
    assert "Ruby"    not in captured.out   # only gem1 should print

# 3 elements
def test_display_gems_three(capsys):
    display_gems([gem1, gem2, gem3])
    captured = capsys.readouterr()
    assert "Emerald" in captured.out
    assert "Ruby"    in captured.out
    assert "Diamond" in captured.out