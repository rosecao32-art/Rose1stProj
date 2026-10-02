from sqlalchemy import create_engine, text
import pandas as pd

# -----------------------------
# ENGINE
# -----------------------------
engine = create_engine("postgresql+psycopg2://pgrose:Xcfcyq32@localhost:5432/pgrose_db")

print("Connected to PostgreSQL!")

# -----------------------------
# EXTRACT
# -----------------------------
df_orders = pd.read_sql("SELECT * FROM orders;", engine)
print(df_orders)

# -----------------------------
# TRANSFORM
# -----------------------------
df_orders["total_amount"] = df_orders["quantity"] * 10

# -----------------------------
# LOAD
# -----------------------------
with engine.begin() as conn:   # auto‑commit block
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS order_totals (
            order_id INT PRIMARY KEY,
            total_amount NUMERIC(10,2)
        );
    """))

    for _, row in df_orders.iterrows():
        conn.execute(
            text("""
                INSERT INTO order_totals (order_id, total_amount)
                VALUES (:order_id, :total_amount)
                ON CONFLICT (order_id) DO NOTHING;
            """),
            {
                "order_id": int(row["order_id"]),
                "total_amount": float(row["total_amount"])
            }
        )

print("ETL complete!")
