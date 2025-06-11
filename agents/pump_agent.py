import datetime
from utils.gcal import get_todays_events

WORK_START = 9  # 9 AM
WORK_END = 18   # 6 PM

def get_free_blocks(events, working_hours=(9, 18)):
    import datetime
    free_blocks = []
    today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    start_of_day = today.replace(hour=working_hours[0])
    end_of_day = today.replace(hour=working_hours[1])

    events = sorted(events, key=lambda x: x['start'])
    current = start_of_day

    for event in events:
        event_start = event['start']
        event_end = event['end']
        if current < event_start:
            free_blocks.append((current, event_start))
        current = max(current, event_end)

    if current < end_of_day:
        free_blocks.append((current, end_of_day))

    return free_blocks


def is_block_in_time_window(start_time, windows):
    for start, end in windows:
        if start <= start_time.time() <= end:
            return True
    return False


def suggest_pump_times(free_blocks, preferred_windows, num_sessions, min_minutes=20, max_minutes=30):
    import datetime
    suggestions = []
    last_suggestion_time = None

    for start, end in free_blocks:
        if len(suggestions) >= num_sessions:
            break

        duration = (end - start).total_seconds() / 60
        if duration < min_minutes:
            continue

        if not is_block_in_time_window(start, preferred_windows):
            continue

        if last_suggestion_time:
            gap = (start - last_suggestion_time).total_seconds() / 3600
            if gap < 2:
                continue  # Avoid sessions too close together

        block_start = start.strftime("%I:%M %p")
        block_end = (start + datetime.timedelta(minutes=min(max_minutes, duration))).strftime("%I:%M %p")
        suggestions.append(f"{block_start} – {block_end}")
        last_suggestion_time = start

    return suggestions

    

