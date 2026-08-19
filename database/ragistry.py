import sqlite3

conn = sqlite3.connect("database/registry.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS registry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    wallet_address TEXT,
    network TEXT,
    threat_level TEXT,
    case_id TEXT,
    reason TEXT
)
""")

conn.commit()
conn.close()

print("Registry Table Created Successfully")
