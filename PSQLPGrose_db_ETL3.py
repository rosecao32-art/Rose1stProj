import psycopg2
import pandas as pd

conn = psycopg2.connect(
    dbname="pgrose_db",
    user="pgrose",
    password="Xcfcyq32",
    host="localhost",
    port="5432"
)

print("Connected to PostgreSQL!")

# -----------------------------
# EXTRACT
# -----------------------------
df_sales = pd.read_sql("SELECT * FROM fact_sales;", conn)
print(df_sales)

# -----------------------------
# TRANSFORM
# -----------------------------
df_sales["avg_price"] = df_sales["total_amount"] / df_sales["quantity"]

# -----------------------------
# LOAD (example: write to a new analytics table)
# -----------------------------
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS fact_sales_summary (
        sales_key INT PRIMARY KEY,
        quantity INT,
        total_amount NUMERIC(10,2),
        avg_price NUMERIC(10,2)
    );
""")

for _, row in df_sales.iterrows():
    cursor.execute(
        """
        INSERT INTO fact_sales_summary (sales_key, quantity, total_amount, avg_price)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (sales_key) DO NOTHING;
        """,
        (int(row["sales_key"]), int(row["quantity"]),
         float(row["total_amount"]), float(row["avg_price"]))
    )

conn.commit()
cursor.close()
conn.close()

print("ETL complete!")
