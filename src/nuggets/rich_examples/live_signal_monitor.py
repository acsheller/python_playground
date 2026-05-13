from rich.live import Live
from rich.table import Table
import random
import time


def build_table():

    table = Table(title="Live Signal Monitor")

    table.add_column("Channel")
    table.add_column("Power")
    table.add_column("Noise")
    table.add_column("Status")

    for i in range(8):

        power = random.randint(-90, -20)
        noise = random.randint(1, 10)

        status = "[green]GOOD[/green]"

        if power > -35:
            status = "[red]HOT[/red]"

        if noise > 8:
            status = "[yellow]NOISY[/yellow]"

        if random.random() > 0.97:
            status = "[bold red]FAULT[/bold red]"

        table.add_row(
            f"CH-{i}",
            f"{power} dBm",
            f"{noise} dB",
            status
        )

    return table


with Live(build_table(), refresh_per_second=4) as live:

    while True:
        time.sleep(1)
        live.update(build_table())