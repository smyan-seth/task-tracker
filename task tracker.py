import csv
import os
from datetime import date

TODAY = date.today().strftime("%B %d, %Y")
FILE = 'activity.csv'

def write():
    if not os.path.exists(FILE):
        with open(FILE, 'w', newline='') as f:
            csv.writer(f).writerow(['date', 'task_name', 'category', 'time_spent'])
    name = input('Task name: ')
    category = input('Category: ')
    duration = input('Time spent (HH:MM): ')
    with open(FILE, 'a', newline='') as f:
        csv.writer(f).writerow([TODAY, name, category, duration])
    print(f"✅ Logged: {name} under {category} for {duration}")

def read():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        if not rows:
            print("No activities logged yet.")
            return
        print(f"\n{'DATE':<20} {'TASK':<20} {'CATEGORY':<15} {'TIME'}")
        print("-" * 65)
        for row in rows:
            print(f"{row['date']:<20} {row['task_name']:<20} {row['category']:<15} {row['time_spent']}")
    else:
        print("No existing enteries")

def edit():
    if os.path.exists(FILE):

        with open(FILE, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        name = input('Task name to edit: ').strip()
        matches = [i for i, r in enumerate(rows) if r['task_name'].lower() == name.lower()]

        if not matches:
            print(f"No entry found with task name '{name}'.")
            return

        if len(matches) > 1:
            print(f"Found {len(matches)} entries with that name:")
            for i in matches:
                print(f"  {rows[i]['date']} — {rows[i]['task_name']} [{rows[i]['category']}] {rows[i]['time_spent']}")
            date_input = input('Enter the date of the entry to edit (e.g. April 07, 2026): ').strip()
            matches = [i for i in matches if rows[i]['date'].lower() == date_input.lower()]
            if not matches:
                print(f"No entry found for '{name}' on '{date_input}'.")
                return
            if len(matches) > 1:
                print("Multiple entries match that date. Editing the first one.")

        idx = matches[0]
        row = rows[idx]
        print(f"\nEditing: {row['date']} — {row['task_name']} [{row['category']}] {row['time_spent']}")
        print("Press Enter to keep the current value.")

        new_name = input(f"Task name [{row['task_name']}]: ").strip()
        new_category = input(f"Category [{row['category']}]: ").strip()
        new_duration = input(f"Time spent [{row['time_spent']}]: ").strip()

        rows[idx] = {
            'date': row['date'],
            'task_name': new_name or row['task_name'],
            'category': new_category or row['category'],
            'time_spent': new_duration or row['time_spent'],
        }

        with open(FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['date', 'task_name', 'category', 'time_spent'])
            writer.writeheader()
            writer.writerows(rows)

        print(f"✅ Updated: {rows[idx]['task_name']} on {rows[idx]['date']}")
    else:
        print("No existing enteries")

def menu():
    print("\n1. Log activity\n2. View activities\n3. Edit activity\n4. Quit")
    choice = input("Enter: ").strip()
    if choice == '1':
        write()
    elif choice == '2':
        read()
    elif choice == '3':
        edit()
    elif choice == '4':
        print("Thank you for using Task Tracker!")
        return False
    else:
        print("Invalid choice.")
    return True

while menu():
    pass
