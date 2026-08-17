#!/usr/bin/env python3
"""List all weekdays (with ISO week numbers) between two dates.

Usage:
    python3 cal.py [weekday]
    weekday: Monday = 0 ... Sunday = 6 (default 3 = Thursday)
"""

import sys
from datetime import date, timedelta


def list_weekdays(start: date, end: date, weekday: int = 3) -> list[date]:
    """Return all dates matching `weekday` between start and end (inclusive)."""
    days_until_match = (weekday - start.weekday()) % 7
    day = start + timedelta(days=days_until_match)
    result = []
    while day <= end:
        result.append(day)
        day += timedelta(days=7)
    return result


def format_weekday(day: date) -> str:
    iso_year, iso_week, _ = day.isocalendar()
    return f"{day.strftime('%d.%m.%Y')}  {day.strftime('%A'):9} KW {iso_week:>2}  (ISO year {iso_year})"


def main(argv: list[str]) -> None:
    weekday = 3  # Thursday
    if len(argv) > 1:
        weekday = int(argv[1])

    start = date(2026, 8, 17)
    end = date(2027, 2, 28)

    print(f"Weekday = {weekday} ({date(2026, 1, 5).strftime('%A').upper() if weekday == 0 else ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][weekday]})")
    print(f"Dates from {start} to {end}:\n")
    for d in list_weekdays(start, end, weekday=weekday):
        print(f"   {format_weekday(d)}")


if __name__ == "__main__":
    main(sys.argv)
