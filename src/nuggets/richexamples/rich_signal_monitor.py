from rich.console import Console
from rich.table import Table
import random

console = Console()


def run():
    table = Table(title="Signal Monitor")

    table.add_column("Channel")
    table.add_column("Power")
    table.add_column("Status")

    for i in range(8):
        power = random.randint(-90, -20)

        status = "GOOD"
        if power > -30:
            status = "HOT"

        table.add_row(
            f"CH-{i}",
            f"{power} dBm",
            status,
        )

    console.print(table)


if __name__ == "__main__":
    run()