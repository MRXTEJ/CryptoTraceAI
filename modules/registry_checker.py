import sqlite3


def check_registry(address):

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
        (address,)
    )

    row = cursor.fetchone()

    conn.close()

    return row
