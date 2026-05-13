event = {
    "type": "gain_update",
    "value": 20
}

match event:
    case {"type": "gain_update", "value": value}:
        print(f"Gain set to {value}")

    case _:
        print("Unknown event")