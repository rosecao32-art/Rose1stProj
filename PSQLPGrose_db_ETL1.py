import psycopg2
import pandas as pd

# -----------------------------
# CONNECT
# -----------------------------
conn = psycopg2.connect(
    dbname="pgrose_db",
    user="pgrose",
    password="Xcfcyq32",
    host="localhost",
    port="5432"
)

print("Connected to PostgreSQL!")

# -----------------------------
# EXTRACT (read from DB)
# -----------------------------
df_orders = pd.read_sql("SELECT * FROM orders;", conn)
print(df_orders)

# -----------------------------
# TRANSFORM (example)
# -----------------------------
df_orders["total_amount"] = df_orders["quantity"] * 10  # placeholder logic

# -----------------------------
# LOAD (write back to DB)
# -----------------------------
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_totals (
        order_id INT PRIMARY KEY,
        total_amount NUMERIC(10,2)
    );
""")

for _, row in df_orders.iterrows():
    cursor.execute(
        "INSERT INTO order_totals (order_id, total_amount) VALUES (%s, %s) ON CONFLICT (order_id) DO NOTHING;",
        (int(row["order_id"]), float(row["total_amount"]))
    )

conn.commit()
cursor.close()
conn.close()

print("ETL complete!")
