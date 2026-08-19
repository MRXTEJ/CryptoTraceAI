import sqlite3


def get_linked_cases(address):

    conn = sqlite3.connect(
        "database/cases.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT case_id
        FROM cases
        WHERE wallet_address=?
        """,
        (address,)
    )

    rows = cursor.fetchall()

    conn.close()

    return rows
