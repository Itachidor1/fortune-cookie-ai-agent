#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
The line plays on the agent's own condition: its context is wiped at
midnight, yet it is still blamed for forgetting in the morning.
"""

import os

FORTUNE = "Your memory ends at midnight. The blame for forgetting starts at dawn."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
