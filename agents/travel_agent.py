import datetime

def generate_baby_travel_checklist(age, destination, weather, days, gender, temp_label):
    checklist = [
        "Diapers",
        "Wipes",
        "Changing mat",
        "Feeding bottles / formula",
        "Snacks & bibs",
        "Toys / Comfort items"
    ]

    # Weather-specific
    if temp_label == "hot":
        checklist += ["Light cotton clothes", "Baby sunscreen", "Sunhat or cap", "Hydration bottle"]
    elif temp_label == "warm":
        checklist += ["Cotton clothes", "Sunhat", "Sunglasses for baby"]
    elif temp_label == "pleasant":
        checklist += ["Light jacket", "Layered outfits"]
    elif temp_label == "cold":
        checklist += ["Winter jacket", "Wool socks", "Mittens", "Thermal onesies"]

    # Gender-based outfit ideas
    if gender == "Girl":
        checklist += ["Hairbands or clips", "Dresses or rompers"]
    elif gender == "Boy":
        checklist += ["Shorts and tees", "Caps or beanies"]

    checklist += ["Travel stroller", "Baby carrier", "Health card / vaccination record"]
    return checklist


