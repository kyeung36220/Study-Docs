from seasons import get_total
from datetime import date

def test_count():
    assert get_total("2023-11-28") == "Five hundred twenty-seven thousand forty minutes"
