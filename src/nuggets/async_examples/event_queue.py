import asyncio
import random
from datetime import datetime

from rich.console import Console


console = Console()

event_queue = asyncio.Queue()


async def telemetry_producer():

    channels = [f"CH-{i}" for i in range(8)]

    while True:

        await asyncio.sleep(random.uniform(0.5, 2.0))

        event = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "channel": random.choice(channels),
            "power": random.randint(-90, -20),
        }

        await event_queue.put(event)


async def fault_producer():

    channels = [f"CH-{i}" for i in range(8)]

    while True:

        await asyncio.sleep(random.uniform(3.0, 6.0))

        event = {
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "channel": random.choice(channels),
            "fault": "OVERLOAD",
        }

        await event_queue.put(event)


async def event_consumer():

    while True:

        event = await event_queue.get()

        if "fault" in event:

            console.print(
                f"[bold red]FAULT[/bold red] "
                f"{event['channel']} "
                f"{event['fault']} "
                f"@ {event['timestamp']}"
            )

        else:

            console.print(
                f"[green]TELEMETRY[/green] "
                f"{event['channel']} "
                f"{event['power']} dBm "
                f"@ {event['timestamp']}"
            )

        event_queue.task_done()


async def main():

    await asyncio.gather(
        telemetry_producer(),
        fault_producer(),
        event_consumer(),
    )


if __name__ == "__main__":
    asyncio.run(main())