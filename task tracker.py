import csv
import os
from datetime import date

today = date.today().strftime("%B %d, %Y")

if not os.path.exists('activity.csv'):
    with open('activity.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'task_name', 'category', 'time_spent'])

name = input('Task name: ')
category = input('Category: ')
time = input('Time spent (HH:MM): ')

with open('activity.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([today, name, category, time])

print(f"✅ Logged: {name} under {category} for {time}")