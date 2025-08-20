from datetime import datetime
import os

events_dates = {
    "summer_break": "2025-06-09 15:00",
    "lia_start": "2025-09-25 08:00",
    "christmas": "2025-12-24 00:00",
    "bellas_birthday": "2025-12-07 00:00",
    "new_year": "2026-01-01 00:00",
    "graduation_party": "2026-06-09 16:30"
}

log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(log_dir, exist_ok=True)

# File to write output
log_file = os.path.join(log_dir, "countdown.log")


with open(log_file, "a") as f:
    now = datetime.now()
    counted_from = f"\nCountdown from: {now.strftime("%x %X")}\n----------------------------------------\n"
    f.write(counted_from)

    for event, date_str in events_dates.items():
    # Parse the datetime string (support both with and without time)
        if len(date_str) == 10:
            events_dates = datetime.strptime(date_str, "%Y-%m-%d")
        else:
            events_dates = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

        delta = events_dates - now

        if delta.total_seconds() > 0:
            days = delta.days
            hours, remainder = divmod(delta.seconds, 3600)
            minutes, _ = divmod(remainder, 60)
            line = f"{event:16} | {days} days, {hours:02} hours, {minutes:02} minutes left\n"
        else:
            line = f"{event:16} | Passed already!\n"

        # Write to file
        f.write(line)

print(f"Countdown written to {log_file}")