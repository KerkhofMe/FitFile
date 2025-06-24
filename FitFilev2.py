from fitparse import FitFile
import csv
import os
import sys
from datetime import datetime

download_dir = os.path.expanduser("~/Downloads")
fit_files = [f for f in os.listdir(download_dir) if f.lower().endswith(".fit")]

if not fit_files:
    print("❌ No .fit files found in ~/Downloads")
    exit(1)

# ➤ Unieke kolomnamen verzamelen
def get_all_fieldnames(rows):
    fieldnames = set()
    for row in rows:
        fieldnames.update(row.keys())
    return list(fieldnames)

# ➤ CSV schrijven
def write_csv(filename, rows):
    if not rows:
        return
    fieldnames = get_all_fieldnames(rows)
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

for filename in fit_files:
    fit_path = os.path.join(download_dir, filename)
    fit_name = os.path.splitext(os.path.basename(fit_path))[0]
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

    try:
        fitfile = FitFile(fit_path)
    except Exception as e:
        print(f"❌ Error opening {filename}: {e}")
        continue

    record_rows = []
    lap_rows = []

    for msg in fitfile.get_messages():
        if msg.name == "record":
            record_rows.append({d.name: d.value for d in msg})
        elif msg.name == "lap":
            lap_rows.append({d.name: d.value for d in msg})

    record_filename = os.path.join(download_dir, f"record_{fit_name}_{timestamp}.csv")
    lap_filename = os.path.join(download_dir, f"lap_{fit_name}_{timestamp}.csv")

    if record_rows:
        write_csv(record_filename, record_rows)
        print(f"✅ Created: {record_filename}")
    else:
        print(f"⚠️ No record data in {filename}")
    if lap_rows:
        write_csv(lap_filename, lap_rows)
        print(f"✅ Created: {lap_filename}")
    else:
        print(f"⚠️ No lap data in {filename}")
