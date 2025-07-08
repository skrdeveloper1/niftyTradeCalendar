import datetime
from niftyTradeCalendar import is_holiday, get_trading_days, get_weekly_expiry_dates

def test_is_holiday():
    assert is_holiday(datetime.date(2024, 1, 26)) == True
    assert is_holiday(datetime.date(2024, 1, 27)) == False

def test_trading_days():
    days = get_trading_days(2024)
    assert all(d.weekday() < 5 for d in days)
    assert datetime.date(2024, 1, 26) not in days

def test_expiry():
    expiry = get_weekly_expiry_dates(2024)
    assert isinstance(expiry[0], datetime.date)
