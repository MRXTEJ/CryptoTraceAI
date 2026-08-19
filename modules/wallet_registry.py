import sqlite3
from rich.console import Console
from rich.table import Table

console = Console()


def init_registry():

    conn = sqlite3.connect(
        "database/registry.db"
    )

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


def add_wallet():

    wallet = input(
        "\nWallet Address : "
    )

    network = input(
        "Network : "
    )

    threat = input(
        "Threat Level : "
    )

    case_id = input(
        "Case ID : "
    )

    reason = input(
        "Reason : "
    )

    conn = sqlite3.connect(
        "database/registry.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO registry
        (
            wallet_address,
            network,
            threat_level,
            case_id,
            reason
        )

        VALUES (?, ?, ?, ?, ?)
        """,
        (
            wallet,
            network,
            threat,
            case_id,
            reason
        )
    )

    conn.commit()
    conn.close()

    console.print(
        "\n[green]Wallet Added Successfully[/green]"
    )

    input("\nPress Enter...")


def view_registry():

    conn = sqlite3.connect(
        "database/registry.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM registry"
    )

    rows = cursor.fetchall()

    conn.close()

    table = Table(
        title="HIGH RISK WALLET REGISTRY"
    )

    table.add_column("ID")
    table.add_column("Wallet")
    table.add_column("Network")
    table.add_column("Threat")
    table.add_column("Case ID")

    for row in rows:

        table.add_row(
            str(row[0]),
            row[1],
            row[2],
            row[3],
            row[4]
        )

    console.print(table)

    input("\nPress Enter...")


def search_wallet():

    wallet = input(
        "\nWallet Address : "
    )

    conn = sqlite3.connect(
        "database/registry.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM registry
        WHERE wallet_address=?
        """,
        (wallet,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:

        console.print(f"""

Wallet Address : {row[1]}

Network        : {row[2]}

Threat Level   : {row[3]}

Case ID        : {row[4]}

Reason         : {row[5]}

        """)

    else:

        console.print(
            "\n[red]Wallet Not Found[/red]"
        )

    input("\nPress Enter...")


def remove_wallet():

    wallet = input(
        "\nWallet Address : "
    )

    conn = sqlite3.connect(
        "database/registry.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM registry
        WHERE wallet_address=?
        """,
        (wallet,)
    )

    conn.commit()
    conn.close()

    console.print(
        "\n[green]Wallet Removed[/green]"
    )

    input("\nPress Enter...")


def wallet_registry_menu():

    init_registry()

    while True:

        console.print("""

[1] Add Wallet

[2] View Registry

[3] Search Wallet

[4] Remove Wallet

[0] Back

""")

        choice = input(
            "\nSelect Option > "
        )

        if choice == "1":

            add_wallet()

        elif choice == "2":

            view_registry()

        elif choice == "3":

            search_wallet()

        elif choice == "4":

            remove_wallet()

        elif choice == "0":

            break
