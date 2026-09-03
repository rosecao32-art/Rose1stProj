import csv
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

import csv
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

import numpy as np
import pandas as pd

def analyze_csv(file_path, numeric_column):
    try:
        # 1. Read the CSV file
        df = pd.read_csv(file_path)

        # 2. Print column names
        print("Column Names:")
        print(list(df.columns))
        print("-" * 40)

        # 3. Count rows
        total_rows = len(df)
        print(f"Total Rows in File: {total_rows}")
        print("-" * 40)

        # 4. Convert numeric strings to floats safely
        # errors='coerce' turns non-numeric strings (like 'abc' or 'N/A') into NaN
        df[numeric_column] = pd.to_numeric(df[numeric_column], errors="coerce")

        # 5. Number of missing values
        missing_count = df[numeric_column].isna().sum()
        print(f"Missing Values in '{numeric_column}': {missing_count}")
        print("-" * 40)

        # 6. Compute min, max, average (automatically ignores NaN values)
        if missing_count < total_rows:
            col_min = df[numeric_column].min()
            col_max = df[numeric_column].max()
            col_avg = df[numeric_column].mean()

            print(f"Analysis for '{numeric_column}':")
            print(f"  Minimum: {col_min}")
            print(f"  Maximum: {col_max}")
            print(f"  Average: {col_avg:.2f}")
        else:
            print(f"Error: Column '{numeric_column}' contains no valid numeric data.")

    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
    except KeyError:
        print(f"Error: The column '{numeric_column}' does not exist in this CSV.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

analyze_csv('data1.csv', 'Age')
analyze_csv('data1.csv', 'Height')
analyze_csv('data1.csv', 'Weight')