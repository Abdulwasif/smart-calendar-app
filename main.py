import calendar
import json
from datetime import datetime

year = 2026

# ---------- LOAD EVENTS ----------
try:
    with open("events.json", "r") as f:
        events = json.load(f)
except:
    events = {}

# ---------- ADD THIS FUNCTION HERE ----------
def show_month_with_events(year, month, events):
    month_cal = calendar.monthcalendar(year, month)
    print(f"\n{calendar.month_name[month]} {year}")
    print("Mo Tu We Th Fr Sa Su")

    for week in month_cal:
        for day in week:
            if day == 0:
                print("   ", end=" ")
            else:
                date_key = f"{str(day).zfill(2)}-{str(month).zfill(2)}-{year}"
                if date_key in events:
                    print(f"{str(day)+'*':<3}", end=" ")
                else:
                    print(f"{day:<3}", end=" ")
        print()

# ---------- PROGRAM START ----------
print("📅 SMART CALENDAR 2026")

while True:

    print("\n1. Show Month")
    print("2. Add Event")
    print("3. View All Events")
    print("0. Exit")

    choice = input("Choose option: ")

    # ---------- SHOW MONTH ----------
    if choice == "1":
        month = int(input("Enter month (1-12): "))
        show_month_with_events(year, month, events)


    # ---------- ADD EVENT ----------
    elif choice == "2":
        day = input("Enter day (DD): ")
        month = input("Enter month (MM): ")
        event_text = input("Enter event description: ")

        date_key = f"{day}-{month}-{year}"
        events[date_key] = event_text
        print("✅ Event added!")

    # ---------- VIEW EVENTS ----------
    elif choice == "3":
        print("\n📌 Your Events:")
        if not events:
            print("No events yet.")
        else:
            for date, event in events.items():
                print(date, ":", event)

    # ---------- EXIT ----------
    elif choice == "0":
        with open("events.json", "w") as f:
            json.dump(events, f)
        print("💾 Events saved. Goodbye 👋")
        break

    else:
        print("Invalid option ❌")
