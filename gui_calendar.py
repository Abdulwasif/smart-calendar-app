import sqlite3
import tkinter as tk
from tkinter import messagebox
import calendar

year = 2026

# ---------- DATABASE SETUP ----------
conn = sqlite3.connect("events.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    date TEXT PRIMARY KEY,
    description TEXT
)
""")
conn.commit()


# ---------- FUNCTIONS ----------
def show_calendar():
    month = month_var.get()
    cal_text = calendar.month(year, month)
    calendar_label.config(text=cal_text)


def add_event():
    day = day_entry.get()
    month = month_var.get()
    event_text = event_entry.get()

    if not day.isdigit() or not event_text:
        messagebox.showwarning("Error", "Enter valid day and event")
        return

    date_key = f"{str(day).zfill(2)}-{str(month).zfill(2)}-{year}"

    try:
        cursor.execute("INSERT OR REPLACE INTO events VALUES (?, ?)", (date_key, event_text))
        conn.commit()
        messagebox.showinfo("Success", "Event saved!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

    day_entry.delete(0, tk.END)
    event_entry.delete(0, tk.END)


# ---------- GUI WINDOW ----------
root = tk.Tk()
root.title("Smart Calendar 2026")
root.geometry("500x500")

month_var = tk.IntVar(value=1)

# Month dropdown
tk.Label(root, text="Select Month").pack()
tk.OptionMenu(root, month_var, *range(1, 13)).pack()

# Show calendar button
tk.Button(root, text="Show Calendar", command=show_calendar).pack()

calendar_label = tk.Label(root, text="", font=("Courier", 10), justify="left")
calendar_label.pack()

# Add event section
tk.Label(root, text="Add Event").pack()

day_entry = tk.Entry(root)
day_entry.pack()
day_entry.insert(0, "Day (DD)")

event_entry = tk.Entry(root)
event_entry.pack()
event_entry.insert(0, "Event Description")

tk.Button(root, text="Add Event", command=add_event).pack()

root.mainloop()
