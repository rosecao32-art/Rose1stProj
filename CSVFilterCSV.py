import pandas as pd
import sys
import os

def filter_experiments(input_file, output_file):
    """
    Reads a CSV of experimental runs, filters rows based on temperature and pH,
    adds a pass/fail column, and writes the result to a new CSV.
    """

    # Validate file existence
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    try:
        # Read CSV
        df = pd.read_csv(input_file)

        # Validate required columns
        required_cols = {"temperature", "pH"}
        if not required_cols.issubset(df.columns):
            print(f"Error: CSV must contain columns: {required_cols}")
            sys.exit(1)

        # Filter rows: temperature > 50 and 6 <= pH <= 8
        filtered_df = df[(df["temperature"] > 50) & (df["pH"].between(6, 8))]

        # Stretch: Add pass/fail column based on multiple criteria
        # Example: Pass if temperature > 50 and pH between 6–8
        filtered_df["pass/fail"] = filtered_df.apply(
            lambda row: "pass" if (50 < row["temperature"] and 6 <= row["pH"] <= 8) else "fail",
            axis=1
        )

        # Save to CSV
        filtered_df.to_csv(output_file, index=False)
        print(f"Filtered data saved to '{output_file}'.")

    except pd.errors.EmptyDataError:
        print("Error: The input CSV is empty.")
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

"""
if __name__ == "__main__":
    # Example usage: python script.py input.csv filtered.csv
    if len(sys.argv) != 3:
        print("Usage: python FilterCSV.py <data2.csv> <filtered.csv>")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
"""

filter_experiments('data2.csv', 'filtered.csv')
