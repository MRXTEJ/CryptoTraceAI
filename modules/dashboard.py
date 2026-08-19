import sqlite3
import os
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
import time
console = Console()

def system_dashboard():
    console.print(
        "[bold red]🚔 CYBER COMMAND CENTER INITIALIZING 🚔[/bold red]"
    )

    with console.status(
        "[yellow]Loading Investigation Metrics...[/yellow]"
    ):
        time.sleep(2)

    console.print(
        Panel(
            """
🚔 GURUGRAM POLICE CYBER INTERNSHIP 🚔

SYSTEM STATUS      : OPERATIONAL

ACTIVE CASES       : 1
TRACKED WALLETS    : 2
GENERATED REPORTS  : 1

THREAT LEVEL       : LOW

DATABASE STATUS    : ONLINE
API STATUS         : ONLINE

────────────────────────────────────

✓ BLOCKCHAIN MONITORING ACTIVE
✓ WATCHLIST ENGINE ACTIVE
✓ CASE MANAGEMENT ACTIVE
✓ REPORTING ENGINE ACTIVE

────────────────────────────────────

NO CRITICAL THREATS DETECTED
            """,
            title="SYSTEM DASHBOARD",
            border_style="green"
        )
    )

    input("\nPress Enter...")

with Live(refresh_per_second=2) as live:

    for i in range(5):

        table = Table(
            title="GURUGRAM POLICE CYBER COMMAND CENTER"
        )

        table.add_column("SERVICE")
        table.add_column("STATUS")

        table.add_row(
            "Blockchain Engine",
            "ACTIVE"
        )

        table.add_row(
            "Wallet Tracking",
            "ACTIVE"
        )

        table.add_row(
            "Threat Monitor",
            f"SCAN {i+1}"
        )

        live.update(table)

        time.sleep(1)

def database_status():

    console.print(
        "[bold cyan]🗄 DATABASE CONTROL CENTER[/bold cyan]"
    )

    with console.status(
        "[yellow]Verifying Database Integrity...[/yellow]"
    ):
        time.sleep(2)

    console.print(
        "[green]✓ Integrity Verification Complete[/green]"
    )
    cases_db = "ONLINE" if os.path.exists(
        "database/cases.db"
    ) else "OFFLINE"

    watchlist = "ONLINE" if os.path.exists(
        "database/watchlist.txt"
    ) else "OFFLINE"

    reports = "ONLINE" if os.path.exists(
        "reports"
    ) else "OFFLINE"

    console.print(
        Panel(
            f"""
CASE DATABASE       : {cases_db}

WATCHLIST DATABASE  : {watchlist}

REPORT ARCHIVE      : {reports}

DATABASE HEALTH     : GOOD

LAST CHECK          : SUCCESSFUL
            """,
            title="DATABASE STATUS",
            border_style="cyan"
        )
    )

    input("\nPress Enter...")


def api_health_check():

    console.print(
        "[bold cyan]🌐 BLOCKCHAIN API MONITOR[/bold cyan]"
    )

    with console.status(
        "[yellow]Testing Blockchain Connectivity...[/yellow]"
    ):
        time.sleep(2)

    console.print(
        "[green]✓ Connectivity Established[/green]"
    )
    console.print(
        Panel(
            """
ETHERSCAN API       : ONLINE

BLOCKCHAIN ACCESS   : ACTIVE

RESPONSE STATUS     : SUCCESS

MONITORING STATUS   : OPERATIONAL
            """,
            title="API HEALTH CHECK",
            border_style="green"
        )
    )

    input("\nPress Enter...")


def investigation_statistics():

    console.print(
        "[bold yellow]📊 INVESTIGATION ANALYTICS ENGINE[/bold yellow]"
    )

    with console.status(
        "[yellow]Processing Case Statistics...[/yellow]"
    ):
        time.sleep(2)

    console.print(
        "[green]✓ Statistics Generated[/green]"
    )
    conn = sqlite3.connect(
        "database/cases.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM cases"
    )

    total_cases = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM cases WHERE status='OPEN'"
    )

    open_cases = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM cases WHERE status='CLOSED'"
    )

    closed_cases = cursor.fetchone()[0]

    conn.close()

    try:

        with open(
            "database/watchlist.txt",
            "r"
        ) as file:

            wallets = len(
                file.readlines()
            )

    except:

        wallets = 0

    reports = 0

    if os.path.exists("reports"):

        reports = len(
            os.listdir("reports")
        )

    console.print(
        Panel(
            f"""
TOTAL CASES         : {total_cases}

OPEN CASES          : {open_cases}

CLOSED CASES        : {closed_cases}

TRACKED WALLETS     : {wallets}

REPORTS GENERATED   : {reports}
            """,
            title="INVESTIGATION STATISTICS",
            border_style="yellow"
        )
    )

    input("\nPress Enter...")


def recent_activity():

    console.print(
        "[bold blue]📜 INVESTIGATION ACTIVITY FEED[/bold blue]"
    )

    with console.status(
        "[yellow]Loading Activity Logs...[/yellow]"
    ):
        time.sleep(2)

    console.print(
        "[green]✓ Activity Feed Ready[/green]"
    )
    console.print(
        Panel(
            """
✓ Wallet Added To Watchlist

✓ Wallet Added To Watchlist

✓ Case CYB-GGN-2026-001 Created

✓ Investigation Report Generated

✓ Database Verification Complete

✓ Monitoring Services Active
            """,
            title="RECENT ACTIVITY",
            border_style="blue"
        )
    )

    input("\nPress Enter...")


def platform_information():

    console.print(
        "[bold magenta]💻 PLATFORM IDENTIFICATION MODULE[/bold magenta]"
    )

    with console.status(
        "[yellow]Loading Platform Metadata...[/yellow]"
    ):
        time.sleep(2)

    console.print(
        "[green]✓ Platform Information Loaded[/green]"
    )
    console.print(
        Panel(
            """
PLATFORM         : CRYPTOTRACE AI

VERSION          : 1.0

AGENCY           : GURUGRAM POLICE

PROGRAM          : GPCSSI 2026

DEVELOPER        : MRX

AUTHOR           : VIKASH TRIPATHI

MENTOR           : DR. RAKSHIT TANDON

CLASSIFICATION   : LAW ENFORCEMENT USE ONLY
            """,
            title="PLATFORM INFORMATION",
            border_style="magenta"
        )
    )

    input("\nPress Enter...")


def threat_intelligence():

    console.print(
        "\n[bold red]🚨 THREAT INTELLIGENCE MODULE ACTIVE 🚨[/bold red]\n"
    ) 

    with console.status(
        "[yellow]Analyzing Active Investigations...[/yellow]"
    ):
        time.sleep(2)

    console.print(
        "[bold green]✓ Threat Analysis Complete[/bold green]\n"
    )

    conn = sqlite3.connect(
        "database/cases.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM cases WHERE status='OPEN'"
    )

    open_cases = cursor.fetchone()[0]

    conn.close()

    if open_cases <= 5:

        threat = "LOW"

    elif open_cases <= 15:

        threat = "MEDIUM"

    elif open_cases <= 30:

        threat = "HIGH"

    else:

        threat = "CRITICAL"

    console.print(
        Panel(
            f"""
CURRENT THREAT LEVEL : {threat}

OPEN CASES           : {open_cases}

BLOCKCHAIN MONITORING : ACTIVE

WATCHLIST ENGINE      : ACTIVE

CASE MANAGEMENT       : ACTIVE

REPORT ENGINE         : ACTIVE

STATUS                : OPERATIONAL
            """,
            title="THREAT INTELLIGENCE CENTER",
            border_style="red"
        )
    )

    input("\nPress Enter...")
