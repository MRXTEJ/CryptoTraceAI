import os
import sqlite3
from rich.console import Console

console = Console()

def generate_report():
    case_id = input("\nEnter Case ID : ")

    conn = sqlite3.connect("database/cases.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM cases WHERE case_id=?",
        (case_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if not row:
        console.print("\n[bold red]Case Not Found[/bold red]")
        input("\nPress Enter...")
        return

    os.makedirs("reports", exist_ok=True)
    filename = f"reports/{case_id}.txt"

    with open(filename, "w") as report:
        report.write(f"""
==================================================
CRYPTOTRACE AI
INVESTIGATION REPORT
====================
Case ID       : {row[1]}
Wallet        : {row[2]}
Wallet Type   : {row[3]}
Risk Score    : {row[4]}
Status        : {row[5]}

## Notes

{row[6]}

==================================================
Agency        : Gurugram Police
Program       : GPCSSI 2026
===========================
""")

    console.print(
        f"\n[bold green]Report Generated[/bold green]\n{filename}"
    )
    input("\nPress Enter...")

def view_reports():
    os.makedirs("reports", exist_ok=True)
    files = os.listdir("reports")

    if not files:
        console.print("\n[bold red]No Reports Found[/bold red]")
    else:
        console.print("\n[bold green]AVAILABLE REPORTS[/bold green]\n")
        for index, file in enumerate(files, start=1):
            console.print(f"[{index}] {file}")

    input("\nPress Enter...")

def delete_report():
    os.makedirs("reports", exist_ok=True)
    files = os.listdir("reports")

    if not files:
        console.print("\n[bold red]No Reports Found[/bold red]")
        input("\nPress Enter...")
        return

    for index, file in enumerate(files, start=1):
        console.print(f"[{index}] {file}")

    try:
        choice = int(input("\nSelect Report Number : "))
        filename = files[choice - 1]
        os.remove(f"reports/{filename}")
        console.print("\n[bold green]Report Deleted[/bold green]")
    except Exception:
        console.print("\n[bold red]Invalid Selection[/bold red]")

    input("\nPress Enter...")

def export_all_cases():
    conn = sqlite3.connect("database/cases.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cases")
    rows = cursor.fetchall()
    conn.close()

    os.makedirs("reports", exist_ok=True)
    filename = "reports/ALL_CASES_REPORT.txt"

    with open(filename, "w") as report:
        report.write("========== ALL CASES ==========\n\n")
        for row in rows:
            report.write(f"""
Case ID : {row[1]}
Wallet  : {row[2]}
Type    : {row[3]}
Risk    : {row[4]}
Status  : {row[5]}

""")

    console.print(
        f"\n[bold green]Export Complete[/bold green]\n{filename}"
    )
    input("\nPress Enter...")
