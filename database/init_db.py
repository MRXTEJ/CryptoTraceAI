import sqlite3

conn = sqlite3.connect("database/cases.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cases (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    case_id TEXT,

    wallet_address TEXT,

    wallet_type TEXT,

    risk_score INTEGER,

    status TEXT,

    notes TEXT

)
""")

conn.commit()
conn.close()

print("Database Created Successfully")
