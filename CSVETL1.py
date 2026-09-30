import pandas as pd
from datetime import datetime

# -----------------------------
# EXTRACT
# -----------------------------
def extract_data(input_path: str) -> pd.DataFrame:
    df = pd.read_csv(input_path)
    return df

# -----------------------------
# TRANSFORM
# -----------------------------
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Standardize column names
    df.columns = df.columns.str.lower().str.strip()

    # Convert date column
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Remove rows with invalid dates
    df = df.dropna(subset=["date"])

    # Convert price and quantity to numeric
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    # Drop rows with missing numeric values
    df = df.dropna(subset=["price", "quantity"])

    # Compute total sale amount
    df["total"] = df["price"] * df["quantity"]

    # Filter out negative or zero totals
    df = df[df["total"] > 0]

    # Aggregate: total sales per day
    daily_summary = (
        df.groupby(df["date"].dt.date)["total"]
        .sum()
        .reset_index()
        .rename(columns={"total": "daily_total"})
    )

    return daily_summary

# -----------------------------
# LOAD
# -----------------------------
def load_data(df: pd.DataFrame, output_path: str):
    # Save final dataset
    df.to_csv(output_path, index=False)

# -----------------------------
# MAIN PIPELINE
# -----------------------------
def run_etl(input_path: str, output_path: str):
    raw = extract_data(input_path)
    transformed = transform_data(raw)
    load_data(transformed, output_path)
    print(f"ETL complete. Output saved to {output_path}")

# Example usage
if __name__ == "__main__":
    run_etl("CSVraw_sales.csv", "CSVdaily_sales_summary.csv")
