import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://pgrose:Xcfcyq32@localhost:5432/pgrose_db"
)

# -----------------------------
# EXTRACT
# -----------------------------
df = pd.read_csv("CSVraw_sales.csv")

# -----------------------------
# TRANSFORM
# -----------------------------
df.columns = df.columns.str.lower().str.strip()

# Clean numeric fields
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

# Remove invalid rows
df = df.dropna(subset=["price", "quantity"])
df = df[df["quantity"] > 0]
df = df[df["price"] > 0]

# Compute total
df["total_amount"] = df["price"] * df["quantity"]

# Convert date
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])

# -----------------------------
# LOOKUP DIMENSION KEYS
# -----------------------------
dim_customer = pd.read_sql("SELECT * FROM dim_customer;", engine)
dim_product  = pd.read_sql("SELECT * FROM dim_product;", engine)
dim_date     = pd.read_sql("SELECT * FROM dim_date;", engine)

# Convert dim_date to datetime
dim_date["full_date"] = pd.to_datetime(dim_date["full_date"])

# For demo purposes, assign customers randomly
df["customer_id"] = np.random.choice(dim_customer["customer_id"], size=len(df))

# Map product_key by item name
df = df.merge(dim_product[["product_key", "name"]], left_on="item", right_on="name")

# Map customer_key
df = df.merge(dim_customer[["customer_key", "customer_id"]], on="customer_id")

# Map date_key
df = df.merge(
    dim_date[["date_key", "full_date"]],
    left_on="date",
    right_on="full_date",
    how="inner"
)

# -----------------------------
# SELECT FACT TABLE COLUMNS
# -----------------------------
fact_df = df[[
    "customer_key",
    "product_key",
    "date_key",
    "quantity",
    "total_amount"
]]

# -----------------------------
# LOAD INTO fact_sales
# -----------------------------
fact_df.to_sql(
    "fact_sales",
    engine,
    if_exists="append",
    index=False
)

print("ETL complete — fact_sales updated with correct dimension keys!")
