import tkinter as tk
from datetime import datetime
import pandas as pd
import threading

# Name of the output file
output_file = "productivity_log.xlsx"

def create_log_entry(status):
    """Create a log entry with timestamp and status."""
    df = pd.DataFrame({'timestamp': [datetime.now()], 'status': [status]})
    if not pd.io.excel.ExcelFile(output_file).sheet_names:
        df.to_excel(output_file)
    else:
        df_existing = pd.read_excel(output_file)
        df_new = pd.concat([df_existing, df])
        df_new.to_excel(output_file, index=False)

def on_productive_click():
    """Handler for 'Being Productive' button click."""
    create_log_entry("Being Productive")
    window.quit()

def on_distracted_click():
    """Handler for 'Was Being Distracted' button click."""
    create_log_entry("Was Being Distracted")
    window.quit()

def on_away_click():
    """Handler for 'Away' button click."""
    create_log_entry("Away")
    window.quit()

def show_popup():
    """Show a popup with the three status options."""
    global window
    window = tk.Tk()
    window.title('Productivity Tracker')

    button_productive = tk.Button(window, text="Being Productive", command=on_productive_click)
    button_productive.pack()

    button_distracted = tk.Button(window, text="Was Being Distracted", command=on_distracted_click)
    button_distracted.pack()

    button_away = tk.Button(window, text="Away", command=on_away_click)
    button_away.pack()

    # Automatically mark as "Away" if no response in 10 seconds
    window.after(10000, on_away_click)

    window.mainloop()

def start_scheduler():
    """Starts the popup scheduler, popping up every hour."""
    threading.Timer(60 * 60, start_scheduler).start()  # repeat every hour
    show_popup()

start_scheduler()
