def day_of_programmer(year):
    if year < 1919:
        # Julian calendar
        is_leap = True if year % 4 == 0 else False
    else:
        # Gregorian calendar
        is_leap = True if year % 4 == 0 and year % 100 != 0 else False
    # 256th day on leap year: 12 September
    if is_leap:
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"
