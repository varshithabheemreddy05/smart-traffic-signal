import time

def get_traffic():
    print("\nEnter traffic at each side:")
    traffic = {
        "North": int(input("North: ")),
        "South": int(input("South: ")),
        "East": int(input("East: ")),
        "West": int(input("West: "))
    }
    return traffic


def rotate_green(max_sides, cycles=6):
    """
    Rotates GREEN among tied highest traffic sides
    """
    print("\n🔄 Starting Rotation Mode (Tie Handling)\n")

    all_sides = ["North", "South", "East", "West"]

    for i in range(cycles):
        signals = {side: "RED" for side in all_sides}

        green_side = max_sides[i % len(max_sides)]
        signals[green_side] = "GREEN"

        print(f"Cycle {i+1}")
        for side in all_sides:
            print(f"{side}: {signals[side]}")
        print("-" * 30)

        time.sleep(1)


def signal_decision(traffic):
    max_value = max(traffic.values())

    # all sides having max traffic
    max_sides = [side for side, value in traffic.items() if value == max_value]

    # CASE 1: Single highest traffic
    if len(max_sides) == 1:
        print("\n✅ Single highest traffic detected")

        signals = {}
        for side in traffic:
            signals[side] = "GREEN" if side == max_sides[0] else "RED"

        return signals

    # CASE 2: Tie situation → rotation
    else:
        rotate_green(max_sides)
        return None


def display(signals):
    if signals:
        print("\n🚦 Traffic Signal Status:")
        for side, signal in signals.items():
            print(f"{side}: {signal}")


# ---------------- MAIN ----------------
traffic = get_traffic()
signals = signal_decision(traffic)
display(signals)
