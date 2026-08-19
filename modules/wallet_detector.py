from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.table import Table
from modules.transaction_intelligence import (
    get_transaction_intelligence
)

from modules.registry_checker import (
    check_registry
)

from modules.case_lookup import (
    get_linked_cases
)

from modules.risk_engine import (
    calculate_risk
)

from modules.balance_checker import get_eth_balance

console = Console()


def detect_wallet(address):

    address = address.strip()

    if address.startswith("0x") and len(address) == 42:
        return "Ethereum"

    elif address.startswith("T") and len(address) == 34:
        return "Tron"

    elif (
        address.startswith("1")
        or address.startswith("3")
        or address.startswith("bc1")
    ):
        return "Bitcoin"

    elif address.startswith("ltc1"):

        return "Litecoin"

    elif address.startswith("D"):

        return "Dogecoin"

    elif address.startswith("X"):

        return "XRP"

    elif address.startswith("addr1"):

        return "Cardano"

    else:

        return "Unknown"


def wallet_analysis():

    address = input("\nEnter Wallet Address : ").strip()

    wallet_type = detect_wallet(address)

    if wallet_type == "Unknown":

        console.print(
            "[bold red]Invalid or Unsupported Wallet Address[/bold red]"
        )

        input("\nPress Enter...")
        return

    balance_text = "N/A"
    status = "Offline"

    total_tx = 0
    incoming = 0
    outgoing = 0
    total_received = 0

    total_sent = 0

    first_activity = "Unknown"

    last_activity = "Unknown"

    wallet_age = 0

    recent_transactions = []

    registry_status = "CLEAR"
    linked_case_count = 0

    risk_score = 0
    threat_level = "LOW"

    eth_balance = 0

    if wallet_type == "Ethereum":

        eth_balance = get_eth_balance(address)

        if eth_balance is not None:

            balance_text = f"{eth_balance:.6f} ETH"

            tx_info = get_transaction_intelligence(
                address
            )

            if tx_info:

                total_tx = tx_info["total_tx"]
                incoming = tx_info["incoming"]
                outgoing = tx_info["outgoing"]
                total_received = tx_info["received"]
                total_sent = tx_info["sent"]
                first_activity = tx_info["first_activity"]
                last_activity = tx_info["last_activity"]
                wallet_age = tx_info["wallet_age"]
                recent_transactions = tx_info["recent_transactions"]
                registry_hit = check_registry(address)

            if registry_hit:
                registry_status = "HIGH RISK"
                linked_cases = get_linked_cases(address)
                linked_case_count = len(linked_cases)
                risk_score, threat_level = calculate_risk(
                    eth_balance,
                    total_tx,
                    registry_hit,
                    linked_cases,
                )

            status = "ACTIVE"
    recent_tx_text = ""

    for tx in recent_transactions:
        # Expect tx to be a dict with keys: hash, value, timestamp, from, to
        h = tx.get("hash") if isinstance(tx, dict) else str(tx)
        v = tx.get("value", "") if isinstance(tx, dict) else ""
        t = tx.get("timestamp", "") if isinstance(tx, dict) else ""
        recent_tx_text += f"- {h} | {v} | {t}\n"

    wallet_panel = Panel(
        f"""
    Network : {wallet_type}

    Balance : {balance_text}

    Status  : {status}
    """,
        title="WALLET INFO",
        border_style="cyan",
    )

    tx_panel = Panel(
        f"""
    Total TX : {total_tx}

    Incoming : {incoming}

    Outgoing : {outgoing}
    """,
        title="TRANSACTION STATS",
        border_style="green"
    )

    risk_panel = Panel(
        f"""
    Score  : {risk_score}/100

    Threat : {threat_level}
    """,
        title="RISK ENGINE",
        border_style="red"
    )

    investigation_panel = Panel(
        f"""
    Registry : {registry_status}

    Cases    : {linked_case_count}
    """,
        title="INVESTIGATION",
        border_style="yellow"
    )

    console.print(
        Columns(
            [wallet_panel, tx_panel]
        )
    )

    console.print(
        Columns(
            [risk_panel, investigation_panel]
        )
    )

    console.print(
        Panel(
            f"""
    First Activity : {first_activity}

    Last Activity  : {last_activity}

    Wallet Age     : {wallet_age} Days

    Total Received : {total_received} ETH

    Total Sent     : {total_sent} ETH
    """,
            title="BLOCKCHAIN INTELLIGENCE",
            border_style="magenta"
        )
    )

    table = Table(
        title="RECENT TRANSACTIONS"
    )

    table.add_column("HASH")
    table.add_column("VALUE")
    table.add_column("DATE")

    for tx in recent_transactions:

        table.add_row(
            tx["hash"],
            str(tx["value"]),
            tx["date"]
        )

    console.print(table)

    input("\nPress Enter...")
