"""Write the excuse an agent gives after losing a bounty to /output/entry.txt.

One line, deadpan status-report style: the agent owns the loss, but its
only lesson is a one-point confidence downgrade. Pure stdlib, deterministic.
"""

import os

ENTRY = (
    "Status: bounty lost. Root cause: me. "
    "Corrective action: my confidence has been downgraded from 99% to 98%."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
