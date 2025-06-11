import os
import sys

# Set parent folder (parent-life-agent) as root for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# DEBUG: Print sys.path (optional)
# print(sys.path)

from agents.pump_agent import get_free_blocks, suggest_pump_times
from utils import gcal

events = gcal.get_todays_events()
free_blocks = get_free_blocks(events)
suggestions = suggest_pump_times(free_blocks)

print("🍼 Suggested Pump Times for Today:\n")
if suggestions:
    for s in suggestions:
        print("✅", s)
else:
    print("⚠️ No suitable time found between 9 AM – 6 PM.")
