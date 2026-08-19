from rich.console import Console
from rich.panel import Panel

from modules.wallet_detector import detect_wallet
from modules.balance_checker import get_eth_balance

console = Console()


def track_wallet():

    address = input("\nEnter Wallet Address To Track : ").strip()

    network = detect_wallet(address)

    if network == "Unknown":

        console.print(
            "[bold red]Invalid Wallet Address[/bold red]"
        )

        input("\nPress Enter...")
        return

    balance = "N/A"

    if network == "Ethereum":

        eth_balance = get_eth_balance(address)

        if eth_balance is not None:

            balance = f"{eth_balance} ETH"

    console.print(
        Panel(
            f"""
Tracking ID:
TRK-001

Wallet Address:
{address}

Network:
{network}

Balance:
{balance}

Status:
Monitoring
            """,
            title="WALLET TRACKING",
            border_style="yellow"
        )
    )
    save = input("\nSave To Watchlist? (Y/N) : ").lower()

    if save == "y":
        with open(
            "database/watchlist.txt",
            "a"
        ) as file:
            file.write(
                f"{address}|{network}|{balance}\n"
            )

        console.print(
            "\n[bold green][SUCCESS][/bold green] Wallet Added To Watchlist"
        )
    else:
        console.print(
            "\n[bold yellow][INFO][/bold yellow] Wallet Not Saved"
        )

    input("\nPress Enter...")

def view_watchlist():

    try:

        with open("database/watchlist.txt", "r") as file:

            data = file.readlines()

        if not data:

            console.print(
                "\n[bold red]No Wallets Found In Watchlist[/bold red]"
            )

        else:

            console.print(
                "\n[bold green]TRACKED WALLETS[/bold green]\n"
            )

            for index, wallet in enumerate(data, start=1):

                address, network, balance = wallet.strip().split("|")

                console.print(
                    f"[{index}] {address} | {network} | {balance}"
                )

    except FileNotFoundError:

        console.print(
            "\n[bold red]Watchlist File Not Found[/bold red]"
        )

    input("\nPress Enter...")

def remove_wallet():

    try:

        with open("database/watchlist.txt", "r") as file:

            wallets = file.readlines()

        if not wallets:

            console.print(
                "\n[bold red]Watchlist Empty[/bold red]"
            )

            input("\nPress Enter...")
            return

        console.print(
            "\n[bold yellow]TRACKED WALLETS[/bold yellow]\n"
        )

        for index, wallet in enumerate(wallets, start=1):

            console.print(
                f"[{index}] {wallet.strip()}"
            )

        choice = int(
            input(
                "\nEnter Wallet Number To Remove : "
            )
        )

        if 1 <= choice <= len(wallets):

            removed = wallets.pop(choice - 1)

            with open(
                "database/watchlist.txt",
                "w"
            ) as file:

                file.writelines(wallets)

            console.print(
                f"\n[bold green]Removed:[/bold green] {removed}"
            )

        else:

            console.print(
                "\n[bold red]Invalid Selection[/bold red]"
            )

    except Exception as e:

        console.print(
            f"\n[bold red]Error:[/bold red] {e}"
        )

    input("\nPress Enter...")
