import sqlite3
from rich.console import Console

console = Console()

def create_case():

    wallet = input("Wallet Address : ")
    wallet_type = input("Wallet Type : ")
    notes = input("Notes : ")

    conn = sqlite3.connect("database/cases.db")

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM cases")

    count = cursor.fetchone()[0] + 1

    case_id = f"CYB-GGN-2026-{count:03}"

    cursor.execute("""
        INSERT INTO cases
        (
            case_id,
            wallet_address,
            wallet_type,
            risk_score,
            status,
            notes
        )

        VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        case_id,
        wallet,
        wallet_type,
        0,
        "OPEN",
        notes
    ))

    conn.commit()
    conn.close()

    console.print(
        f"\n[green]Case Created Successfully[/green]\nCase ID : {case_id}"
    )

    input("\nPress Enter...")
def view_cases():

    conn = sqlite3.connect("database/cases.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cases")

    rows = cursor.fetchall()

    conn.close()

    print("\n========== CASES ==========\n")

    for row in rows:

        print(f"""
Case ID : {row[1]}
Wallet  : {row[2]}
Type    : {row[3]}
Risk    : {row[4]}
Status  : {row[5]}
        """)
def search_case():

    case_id = input("\nEnter Case ID : ")

    conn = sqlite3.connect("database/cases.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM cases WHERE case_id=?",
        (case_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:

        print(f"""
Case ID : {row[1]}
Wallet  : {row[2]}
Type    : {row[3]}
Risk    : {row[4]}
Status  : {row[5]}
Notes   : {row[6]}
""")

    else:

        print("\nCase Not Found")

    input("\nPress Enter...")
def close_case():

    case_id = input("\nEnter Case ID : ")

    conn = sqlite3.connect("database/cases.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE cases SET status='CLOSED' WHERE case_id=?",
        (case_id,)
    )

    conn.commit()
    conn.close()

    print("\nCase Closed Successfully")

    input("\nPress Enter...")
def delete_case():

    case_id = input("\nEnter Case ID : ")

    conn = sqlite3.connect("database/cases.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM cases WHERE case_id=?",
        (case_id,)
    )

    conn.commit()
    conn.close()

    print("\nCase Deleted Successfully")

    input("\nPress Enter...")

