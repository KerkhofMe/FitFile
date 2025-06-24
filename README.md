# FitFilev2.py

This script automatically searches for all `.fit` files in your `~/Downloads` folder, reads them using the `fitparse` library, and exports the data to CSV files. Both record and lap data are exported to separate CSV files with unique column names.

## Features
- Searches for all `.fit` files in the Downloads folder
- Reads the files using `fitparse`
- Exports record and lap data to CSV files
- CSV files are named with a timestamp
- Provides clear error messages and status updates

## Requirements
- Python 3.7+
- The Python package `fitparse`

Install the required package with:

```bash
pip install fitparse
```

## Usage
1. Place one or more `.fit` files in your `~/Downloads` folder.
2. Run the script:

```bash
python FitFilev2.py
```

3. The exported CSV files will appear in the same folder (`~/Downloads`).

## Output
- `record_<filename>_<timestamp>.csv`: Contains all record data
- `lap_<filename>_<timestamp>.csv`: Contains all lap data

## Error Handling
- If no `.fit` files are found, you will see a message.
- If a file cannot be opened, the error will be shown.
- If there is no record or lap data, you will get a warning.

## Author
Joey Kerkhof

---

*This script is intended for personal use and quick conversion of Garmin FIT files to CSV.*
