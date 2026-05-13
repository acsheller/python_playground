from datetime import datetime
import random
import time

from rich.live import Live
from rich.table import Table


channels = {
    f"CH-{i}": {
        "power": random.randint(-90, -40),
        "previous_power": None,
        "noise": random.randint(1, 5),
        "faults": 0,
    }
    for i in range(8)
}


def update_channels():
    for channel in channels.values():
        channel["previous_power"] = channel["power"]

        channel["power"] += random.randint(-2, 2)
        channel["power"] = max(-100, min(-20, channel["power"]))

        channel["noise"] += random.randint(-1, 1)
        channel["noise"] = max(1, min(10, channel["noise"]))

        if random.random() > 0.97:
            channel["faults"] += 1


def power_trend(channel):
    previous = channel["previous_power"]
    current = channel["power"]

    if previous is None:
        return "-"

    if current > previous:
        return "[red]▲[/red]"

    if current < previous:
        return "[green]▼[/green]"

    return "[dim]-[/dim]"


def build_table():
    table = Table(title="Persistent Signal Monitor")

    table.add_column("Channel")
    table.add_column("Power")
    table.add_column("Trend")
    table.add_column("Noise")
    table.add_column("Faults")
    table.add_column("Status")

    for name, channel in channels.items():
        power = channel["power"]
        noise = channel["noise"]
        faults = channel["faults"]

        status = "[green]GOOD[/green]"

        if power > -35:
            status = "[red]HOT[/red]"

        if noise > 8:
            status = "[yellow]NOISY[/yellow]"

        if faults > 0:
            status = "[bold red]FAULT[/bold red]"

        table.add_row(
            name,
            f"{power} dBm",
            power_trend(channel),
            f"{noise} dB",
            str(faults),
            status,
        )

    table.caption = f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    return table


def run():
    with Live(build_table(), refresh_per_second=4) as live:
        while True:
            update_channels()
            live.update(build_table())
            time.sleep(1)


if __name__ == "__main__":
    run()