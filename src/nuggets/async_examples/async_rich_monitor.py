import asyncio
import random
from datetime import datetime

from rich.live import Live
from rich.table import Table


channels = {
    f"CH-{i}": {
        "power": random.randint(-90, -40),
        "noise": random.randint(1, 5),
        "faults": 0,
        "last_event": "initialized",
    }
    for i in range(8)
}


async def telemetry_worker():
    while True:
        for name, channel in channels.items():
            channel["power"] += random.randint(-2, 2)
            channel["power"] = max(-100, min(-20, channel["power"]))

            channel["noise"] += random.randint(-1, 1)
            channel["noise"] = max(1, min(10, channel["noise"]))

            channel["last_event"] = "telemetry update"

            if random.random() > 0.97:
                channel["faults"] += 1
                channel["last_event"] = "fault detected"

        await asyncio.sleep(1)


def build_table():
    table = Table(title="Async Rich Signal Monitor")

    table.add_column("Channel")
    table.add_column("Power")
    table.add_column("Noise")
    table.add_column("Faults")
    table.add_column("Status")
    table.add_column("Last Event")

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
            f"{noise} dB",
            str(faults),
            status,
            channel["last_event"],
        )

    table.caption = f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    return table


async def ui_worker():
    with Live(build_table(), refresh_per_second=8) as live:
        while True:
            live.update(build_table())
            await asyncio.sleep(0.25)


async def heartbeat_worker():
    while True:
        print("heartbeat: async system alive")
        await asyncio.sleep(5)


async def main():
    await asyncio.gather(
        telemetry_worker(),
        ui_worker(),
        heartbeat_worker(),
    )


if __name__ == "__main__":
    asyncio.run(main())