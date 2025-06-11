from agents.travel_agent import generate_baby_travel_checklist

age = 3  # months
destination = "Finland"
weather = "cold"
duration = 5  # days

checklist = generate_baby_travel_checklist(age, destination, weather, duration)

print(f"🧳 Packing Checklist for {duration}-day trip to {destination} with a {age}-month-old:\n")
for item in checklist:
    print("✅", item)
