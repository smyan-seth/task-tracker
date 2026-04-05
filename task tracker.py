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

def menu():
    print("\n1. Log activity\n2. View activities\n3. Quit")
    choice = input("Enter: ").strip()
    if choice == '1':
        write()
    elif choice == '2':
        read()
    elif choice == '3':
        print("Thank you for using Task Tracker!")
        return False
    else:
        print("Invalid choice.")
        menu()

run=True        
while(menu()):
    pass